## About the connector
Cisco Meraki MX L3 Firewall gives administrators complete control over the users, content, and applications on their network. This connector facilitates automated operations to fetch firewall rules, update the firewall rules etc.
<p>This document provides information about the Cisco Meraki MX L3 Firewall Connector, which facilitates automated interactions, with a Cisco Meraki MX L3 Firewall server using FortiSOAR&trade; playbooks. Add the Cisco Meraki MX L3 Firewall Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Cisco Meraki MX L3 Firewall.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-cisco-meraki-mx-l3</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Cisco Meraki MX L3 Firewall server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Cisco Meraki MX L3 Firewall server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Cisco Meraki MX L3 Firewall</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Service based URI to which you will connect and perform the automated operations.
</td>
</tr><tr><td>API Key</td><td>API key configured for your account for using the Cisco Meraki API.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Network Appliance Firewall L3 Firewall Rules</td><td>Retrieves a list of MX L3 firewall rules for a specific MX network based on the Network ID you have specified.</td><td>get_network_appliance_firewall_rules <br/>Investigation</td></tr>
<tr><td>Update Network Appliance Firewall L3 Firewall Rules</td><td>Updates the MX L3 firewall rules for a specific MX network based on the Network ID and rules you have specified.</td><td>update_network_appliance_firewall_rules <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Network Appliance Firewall L3 Firewall Rules
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Network ID</td><td>Specify the ID of the MX network for which to retrieve the list of MX L3 firewall rules.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "rules": [
        {
            "comment": "",
            "policy": "",
            "protocol": "",
            "destPort": "",
            "destCidr": "",
            "srcPort": "",
            "srcCidr": "",
            "syslogEnabled": ""
        }
    ]
}</pre>
### operation: Update Network Appliance Firewall L3 Firewall Rules
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Network ID</td><td>Specify the ID of the MX network whose L3 firewall rules are to be updated.
</td></tr><tr><td>Policy</td><td>Specify the 'allow' or 'deny' traffic specified by this rule.
</td></tr><tr><td>Protocol</td><td>Specify the The type of protocol. e.g. 'tcp', 'udp', 'icmp', 'icmp6' or 'any'.
</td></tr><tr><td>Source IP Address(es)</td><td>Specify the source IP address(es) (in IP or CIDR notation), fully-qualified domain names (FQDN) or 'any' whose L3 firewall rules are to be updated. (note: FQDN not supported for source addresses)
</td></tr><tr><td>Destination IP Address(es)</td><td>Specify the destination IP address(es) (in IP or CIDR notation), fully-qualified domain names (FQDN) or 'any' whose L3 firewall rules are to be updated.
</td></tr><tr><td>Source Port(s)</td><td>(Optional) Specify the source port(s) (integer in the range 1-65535), or 'any' whose L3 firewall rules are to be updated.
</td></tr><tr><td>Destination Port(s)</td><td>(Optional) Specify the destination port(s) (integer in the range 1-65535), or 'any' whose L3 firewall rules are to be updated.
</td></tr><tr><td>Comment</td><td>(Optional) Specify the description of the rule whose L3 firewall rules are to be updated.
</td></tr><tr><td>Syslog Enabled</td><td>(Optional) Specify to log this rule to syslog (true or false, boolean value) - only applicable if a syslog has been configured.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "rules": [
        {
            "comment": "",
            "policy": "",
            "protocol": "",
            "destPort": "",
            "destCidr": "",
            "srcPort": "",
            "srcCidr": "",
            "syslogEnabled": ""
        }
    ]
}</pre>
## Included playbooks
The `Sample - cisco-meraki-mx-l3 - 1.0.0` playbook collection comes bundled with the Cisco Meraki MX L3 Firewall connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Cisco Meraki MX L3 Firewall connector.

- Get Network Appliance Firewall L3 Firewall Rules
- Update Network Appliance Firewall L3 Firewall Rules

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
