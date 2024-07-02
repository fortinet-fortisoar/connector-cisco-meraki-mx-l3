""" Copyright start
  Copyright (C) 2008 - 2024 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """


from requests import request, exceptions as req_exceptions
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('cisco_meraki_mx_l3_firewall')


def get_curr_oper_info(info_json, action):
    try:
        operations = info_json.get('operations')
        exec_action = [action_info for action_info in operations if action_info['operation'] == action]
        return exec_action[0]

    except Exception as err:
        logger.error("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def api_request(config, params, action):
    try:
        data = None
        server_url = config.get('server_url')
        if not server_url.startswith('https://'):
            server_url = 'https://' + server_url
        if not server_url.endswith('/'):
            server_url = '{0}/api/v1/'.format(server_url)

        headers = {'Authorization': "Bearer " + config.get('api_key'),
                   'Accept':  'application/json'}

        if action['endpoint'] == "":
            endpoint = server_url
        else:
            url = action['endpoint']
            endpoint = server_url + url.format(networkId=params.get("networkId"))

        if action["http_method"] == "PUT":
            data = params.get("rules")

        try:
            response = request(action["http_method"], endpoint, headers=headers, data=data,
                               verify=config.get('verify_ssl'))

            if response.status_code != 200 and response.status_code != 201:
                err_msg = "Status Code: {0} Details: {1}".format(response.status_code, response.reason)
                raise ConnectorError(err_msg)

            try:
                return response.json()
            except Exception as e:
                logger.error(e)
                raise ConnectorError(e)

        except req_exceptions.SSLError:
            logger.error('An SSL error occurred')
            raise ConnectorError('An SSL error occurred')
        except req_exceptions.ConnectionError:
            logger.error('A connection error occurred')
            raise ConnectorError('A connection error occurred')
        except req_exceptions.Timeout:
            logger.error('The request timed out')
            raise ConnectorError('The request timed out')
        except req_exceptions.RequestException:
            logger.error('There was an error while handling the request')
            raise ConnectorError('There was an error while handling the request')
        except Exception as e:
            logger.error(e)
            raise ConnectorError(e)

    except Exception as err:
        raise ConnectorError(str(err))


def check_health(config):
    try:
        action = dict()
        action["http_method"] ="GET"
        action["endpoint"] = ""
        resp= api_request(config, params={}, action=action)
        if resp:
            return True

    except Exception as e:
        logger.error(e)
        raise ConnectorError(e)

