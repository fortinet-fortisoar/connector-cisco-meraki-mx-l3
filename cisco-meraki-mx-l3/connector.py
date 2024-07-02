"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

  
from .operations import check_health , get_curr_oper_info, api_request
from connectors.core.connector import Connector, get_logger, ConnectorError

logger = get_logger('cisco_meraki_mx_l3_firewall')


class CiscoMeraki(Connector):
    def execute(self, config, operation, params, **kwargs):
        logger.info('execute [{}]'.format(operation))
        try:
            logger.info('execute [{}]'.format(operation))
            operation_info = get_curr_oper_info(self._info_json, operation)
            return api_request(config, params, operation_info)
        except Exception as err:
            logger.exception("An exception occurred [{}]".format(err))
            raise ConnectorError("An exception occurred [{}]".format(err))

    def check_health(self, config):
        logger.info('starting health check')
        check_health(config)
        logger.info('completed health check no errors')
