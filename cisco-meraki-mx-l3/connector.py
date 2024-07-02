"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

  
from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import operations, check_health

logger = get_logger('cisco_meraki_mx_l3_firewall')


class CiscoMeraki(Connector):
    def execute(self, config, operation, params, **kwargs):
        logger.info('execute [{}]'.format(operation))
        try:
            operation = operations.get(operation)
            return operation(config, params)
        except Exception as err:
            logger.exception("An exception occurred [{}]".format(err))
            raise ConnectorError("An exception occurred [{}]".format(err))

    def check_health(self, config):
        logger.info('starting health check')
        return check_health(config)
