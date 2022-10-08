
# Network Configuration

Defines the Jellyfin.Networking.Configuration.NetworkConfiguration.

## Structure

`NetworkConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `require_https` | `bool` | Optional | Gets or sets a value indicating whether the server should force connections over HTTPS. |
| `certificate_path` | `string` | Optional | Gets or sets the filesystem path of an X.509 certificate to use for SSL. |
| `certificate_password` | `string` | Optional | Gets or sets the password required to access the X.509 certificate data in the file specified by Jellyfin.Networking.Configuration.NetworkConfiguration.CertificatePath. |
| `base_url` | `string` | Optional | Gets or sets a value used to specify the URL prefix that your Jellyfin instance can be accessed at. |
| `public_https_port` | `int` | Optional | Gets or sets the public HTTPS port. |
| `http_server_port_number` | `int` | Optional | Gets or sets the HTTP server port number. |
| `https_port_number` | `int` | Optional | Gets or sets the HTTPS server port number. |
| `enable_https` | `bool` | Optional | Gets or sets a value indicating whether to use HTTPS. |
| `public_port` | `int` | Optional | Gets or sets the public mapped port. |
| `u_pn_p_create_http_port_map` | `bool` | Optional | Gets or sets a value indicating whether the http port should be mapped as part of UPnP automatic port forwarding. |
| `udp_port_range` | `string` | Optional | Gets or sets the UDPPortRange. |
| `enable_ipv_6` | `bool` | Optional | Gets or sets a value indicating whether gets or sets IPV6 capability. |
| `enable_ipv_4` | `bool` | Optional | Gets or sets a value indicating whether gets or sets IPV4 capability. |
| `enable_ssdp_tracing` | `bool` | Optional | Gets or sets a value indicating whether detailed SSDP logs are sent to the console/log.<br>"Emby.Dlna": "Debug" must be set in logging.default.json for this property to have any effect. |
| `ssdp_tracing_filter` | `string` | Optional | Gets or sets the SSDPTracingFilter<br>Gets or sets a value indicating whether an IP address is to be used to filter the detailed ssdp logs that are being sent to the console/log.<br>If the setting "Emby.Dlna": "Debug" msut be set in logging.default.json for this property to work. |
| `udp_send_count` | `int` | Optional | Gets or sets the number of times SSDP UDP messages are sent. |
| `udp_send_delay` | `int` | Optional | Gets or sets the delay between each groups of SSDP messages (in ms). |
| `ignore_virtual_interfaces` | `bool` | Optional | Gets or sets a value indicating whether address names that match Jellyfin.Networking.Configuration.NetworkConfiguration.VirtualInterfaceNames should be Ignore for the purposes of binding. |
| `virtual_interface_names` | `string` | Optional | Gets or sets a value indicating the interfaces that should be ignored. The list can be comma separated. <seealso cref="P:Jellyfin.Networking.Configuration.NetworkConfiguration.IgnoreVirtualInterfaces" />. |
| `gateway_monitor_period` | `int` | Optional | Gets or sets the time (in seconds) between the pings of SSDP gateway monitor. |
| `enable_multi_socket_binding` | `bool` | Optional | Gets a value indicating whether multi-socket binding is available. |
| `trust_all_ip_6_interfaces` | `bool` | Optional | Gets or sets a value indicating whether all IPv6 interfaces should be treated as on the internal network.<br>Depending on the address range implemented ULA ranges might not be used. |
| `hd_homerun_port_range` | `string` | Optional | Gets or sets the ports that HDHomerun uses. |
| `published_server_uri_by_subnet` | `List of string` | Optional | Gets or sets the PublishedServerUriBySubnet<br>Gets or sets PublishedServerUri to advertise for specific subnets. |
| `auto_discovery_tracing` | `bool` | Optional | Gets or sets a value indicating whether Autodiscovery tracing is enabled. |
| `auto_discovery` | `bool` | Optional | Gets or sets a value indicating whether Autodiscovery is enabled. |
| `remote_ip_filter` | `List of string` | Optional | Gets or sets the filter for remote IP connectivity. Used in conjuntion with <seealso cref="P:Jellyfin.Networking.Configuration.NetworkConfiguration.IsRemoteIPFilterBlacklist" />. |
| `is_remote_ip_filter_blacklist` | `bool` | Optional | Gets or sets a value indicating whether <seealso cref="P:Jellyfin.Networking.Configuration.NetworkConfiguration.RemoteIPFilter" /> contains a blacklist or a whitelist. Default is a whitelist. |
| `enable_u_pn_p` | `bool` | Optional | Gets or sets a value indicating whether to enable automatic port forwarding. |
| `enable_remote_access` | `bool` | Optional | Gets or sets a value indicating whether access outside of the LAN is permitted. |
| `local_network_subnets` | `List of string` | Optional | Gets or sets the subnets that are deemed to make up the LAN. |
| `local_network_addresses` | `List of string` | Optional | Gets or sets the interface addresses which Jellyfin will bind to. If empty, all interfaces will be used. |
| `known_proxies` | `List of string` | Optional | Gets or sets the known proxies. If the proxy is a network, it's added to the KnownNetworks. |
| `enable_published_server_uri_by_request` | `bool` | Optional | Gets or sets a value indicating whether the published server uri is based on information in HTTP requests. |

## Example (as JSON)

```json
{
  "RequireHttps": null,
  "CertificatePath": null,
  "CertificatePassword": null,
  "BaseUrl": null,
  "PublicHttpsPort": null,
  "HttpServerPortNumber": null,
  "HttpsPortNumber": null,
  "EnableHttps": null,
  "PublicPort": null,
  "UPnPCreateHttpPortMap": null,
  "UDPPortRange": null,
  "EnableIPV6": null,
  "EnableIPV4": null,
  "EnableSSDPTracing": null,
  "SSDPTracingFilter": null,
  "UDPSendCount": null,
  "UDPSendDelay": null,
  "IgnoreVirtualInterfaces": null,
  "VirtualInterfaceNames": null,
  "GatewayMonitorPeriod": null,
  "TrustAllIP6Interfaces": null,
  "HDHomerunPortRange": null,
  "PublishedServerUriBySubnet": null,
  "AutoDiscoveryTracing": null,
  "AutoDiscovery": null,
  "RemoteIPFilter": null,
  "IsRemoteIPFilterBlacklist": null,
  "EnableUPnP": null,
  "EnableRemoteAccess": null,
  "LocalNetworkSubnets": null,
  "LocalNetworkAddresses": null,
  "KnownProxies": null,
  "EnablePublishedServerUriByRequest": null
}
```

