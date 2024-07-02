"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""


from requests import request, exceptions as req_exceptions
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('cisco_meraki_mx_l3_firewall')


class CiscoMeraki:
    def __init__(self, config):
        self.base_url = config.get("server_url")
        if self.base_url.startswith('https://') or self.base_url.startswith('http://'):
            self.base_url = self.base_url.strip('/')
        else:
            self.base_url = 'https://{0}'.format(self.base_url.strip('/'))
        self.api_key = config.get("api_key")
        self.verify_ssl = config.get("verify_ssl")

    def make_request(self, endpoint, headers=None, params=None, data=None, method='GET'):
        try:
            headers = {'Authorization': "Bearer " + self.get('api_key'), 'Accept':  'application/json'}
            url = '{0}{1}{2}'.format(self.base_url, '/api/v1/', endpoint)
            logger.info('Request URL {0}'.format(url))
            response = requests.request(method, url, data=data, headers=headers, verify=self.verify_ssl, params=params)

            if response.status_code in [200, 201, 204, 206]:
                if response.text != "":
                    return response.json()
                else:
                    return True
            elif response.status_code == 404:
                return response
            else:
                if response.text != "":
                    err_resp = response.json()
                    failure_msg = err_resp['ERROR_DESCRIPTION']
                    error_msg = 'Response [{0}:{1} Details: {2}]'.format(response.status_code, response.reason,
                                                                         failure_msg if failure_msg else '')
                else:
                    error_msg = 'Response [{0}:{1}]'.format(response.status_code, response.reason)
                logger.error(error_msg)
                raise ConnectorError(error_msg)
        except requests.exceptions.SSLError as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(self.error_msg['ssl_error']))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(self.error_msg['time_out']))
        except Exception as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(e))

    def build_payload(self, params):
        result = {k: v for k, v in params.items() if v is not None and v != ''}
        return result


def get_network_appliance_firewall_rules(config, params):
    obj = CiscoMeraki(config)
    networkId = params.get("networkId")
    response = obj.make_request(endpoint='/networks/{networkId}/appliance/firewall/l3FirewallRules'.format(networkId=networkId))
    return response


def update_network_appliance_firewall_rules(config, params):
    obj = CiscoMeraki(config)
    networkId = params.get('networkId')
    params.pop('networkId')
    params = obj.build_payload(params)
    response = obj.make_request(endpoint='/networks/{networkId}/appliance/firewall/l3FirewallRules'.format(networkId=networkId), data=params)
    return response


def check_health(config):
    try:
        obj = CiscoMeraki(config)
        server_response = obj.make_request(endpoint='/organizations')
        if server_response:
            return True
    except Exception as err:
        logger.error("{0}".format(str(err)))
        raise ConnectorError(str(err))



operations = {
    "get_network_appliance_firewall_rules": get_network_appliance_firewall_rules,
    "update_network_appliance_firewall_rules": update_network_appliance_firewall_rules
}





