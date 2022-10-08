# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class NetworkConfiguration(object):

    """Implementation of the 'NetworkConfiguration' model.

    Defines the Jellyfin.Networking.Configuration.NetworkConfiguration.

    Attributes:
        require_https (bool): Gets or sets a value indicating whether the
            server should force connections over HTTPS.
        certificate_path (string): Gets or sets the filesystem path of an
            X.509 certificate to use for SSL.
        certificate_password (string): Gets or sets the password required to
            access the X.509 certificate data in the file specified by
            Jellyfin.Networking.Configuration.NetworkConfiguration.CertificateP
            ath.
        base_url (string): Gets or sets a value used to specify the URL prefix
            that your Jellyfin instance can be accessed at.
        public_https_port (int): Gets or sets the public HTTPS port.
        http_server_port_number (int): Gets or sets the HTTP server port
            number.
        https_port_number (int): Gets or sets the HTTPS server port number.
        enable_https (bool): Gets or sets a value indicating whether to use
            HTTPS.
        public_port (int): Gets or sets the public mapped port.
        u_pn_p_create_http_port_map (bool): Gets or sets a value indicating
            whether the http port should be mapped as part of UPnP automatic
            port forwarding.
        udp_port_range (string): Gets or sets the UDPPortRange.
        enable_ipv_6 (bool): Gets or sets a value indicating whether gets or
            sets IPV6 capability.
        enable_ipv_4 (bool): Gets or sets a value indicating whether gets or
            sets IPV4 capability.
        enable_ssdp_tracing (bool): Gets or sets a value indicating whether
            detailed SSDP logs are sent to the console/log.  "Emby.Dlna":
            "Debug" must be set in logging.default.json for this property to
            have any effect.
        ssdp_tracing_filter (string): Gets or sets the SSDPTracingFilter  Gets
            or sets a value indicating whether an IP address is to be used to
            filter the detailed ssdp logs that are being sent to the
            console/log.  If the setting "Emby.Dlna": "Debug" msut be set in
            logging.default.json for this property to work.
        udp_send_count (int): Gets or sets the number of times SSDP UDP
            messages are sent.
        udp_send_delay (int): Gets or sets the delay between each groups of
            SSDP messages (in ms).
        ignore_virtual_interfaces (bool): Gets or sets a value indicating
            whether address names that match
            Jellyfin.Networking.Configuration.NetworkConfiguration.VirtualInter
            faceNames should be Ignore for the purposes of binding.
        virtual_interface_names (string): Gets or sets a value indicating the
            interfaces that should be ignored. The list can be comma
            separated. <seealso
            cref="P:Jellyfin.Networking.Configuration.NetworkConfiguration.Igno
            reVirtualInterfaces" />.
        gateway_monitor_period (int): Gets or sets the time (in seconds)
            between the pings of SSDP gateway monitor.
        enable_multi_socket_binding (bool): Gets a value indicating whether
            multi-socket binding is available.
        trust_all_ip_6_interfaces (bool): Gets or sets a value indicating
            whether all IPv6 interfaces should be treated as on the internal
            network.  Depending on the address range implemented ULA ranges
            might not be used.
        hd_homerun_port_range (string): Gets or sets the ports that HDHomerun
            uses.
        published_server_uri_by_subnet (list of string): Gets or sets the
            PublishedServerUriBySubnet  Gets or sets PublishedServerUri to
            advertise for specific subnets.
        auto_discovery_tracing (bool): Gets or sets a value indicating whether
            Autodiscovery tracing is enabled.
        auto_discovery (bool): Gets or sets a value indicating whether
            Autodiscovery is enabled.
        remote_ip_filter (list of string): Gets or sets the filter for remote
            IP connectivity. Used in conjuntion with <seealso
            cref="P:Jellyfin.Networking.Configuration.NetworkConfiguration.IsRe
            moteIPFilterBlacklist" />.
        is_remote_ip_filter_blacklist (bool): Gets or sets a value indicating
            whether <seealso
            cref="P:Jellyfin.Networking.Configuration.NetworkConfiguration.Remo
            teIPFilter" /> contains a blacklist or a whitelist. Default is a
            whitelist.
        enable_u_pn_p (bool): Gets or sets a value indicating whether to
            enable automatic port forwarding.
        enable_remote_access (bool): Gets or sets a value indicating whether
            access outside of the LAN is permitted.
        local_network_subnets (list of string): Gets or sets the subnets that
            are deemed to make up the LAN.
        local_network_addresses (list of string): Gets or sets the interface
            addresses which Jellyfin will bind to. If empty, all interfaces
            will be used.
        known_proxies (list of string): Gets or sets the known proxies. If the
            proxy is a network, it's added to the KnownNetworks.
        enable_published_server_uri_by_request (bool): Gets or sets a value
            indicating whether the published server uri is based on
            information in HTTP requests.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "require_https": "RequireHttps",
        "certificate_path": "CertificatePath",
        "certificate_password": "CertificatePassword",
        "base_url": "BaseUrl",
        "public_https_port": "PublicHttpsPort",
        "http_server_port_number": "HttpServerPortNumber",
        "https_port_number": "HttpsPortNumber",
        "enable_https": "EnableHttps",
        "public_port": "PublicPort",
        "u_pn_p_create_http_port_map": "UPnPCreateHttpPortMap",
        "udp_port_range": "UDPPortRange",
        "enable_ipv_6": "EnableIPV6",
        "enable_ipv_4": "EnableIPV4",
        "enable_ssdp_tracing": "EnableSSDPTracing",
        "ssdp_tracing_filter": "SSDPTracingFilter",
        "udp_send_count": "UDPSendCount",
        "udp_send_delay": "UDPSendDelay",
        "ignore_virtual_interfaces": "IgnoreVirtualInterfaces",
        "virtual_interface_names": "VirtualInterfaceNames",
        "gateway_monitor_period": "GatewayMonitorPeriod",
        "enable_multi_socket_binding": "EnableMultiSocketBinding",
        "trust_all_ip_6_interfaces": "TrustAllIP6Interfaces",
        "hd_homerun_port_range": "HDHomerunPortRange",
        "published_server_uri_by_subnet": "PublishedServerUriBySubnet",
        "auto_discovery_tracing": "AutoDiscoveryTracing",
        "auto_discovery": "AutoDiscovery",
        "remote_ip_filter": "RemoteIPFilter",
        "is_remote_ip_filter_blacklist": "IsRemoteIPFilterBlacklist",
        "enable_u_pn_p": "EnableUPnP",
        "enable_remote_access": "EnableRemoteAccess",
        "local_network_subnets": "LocalNetworkSubnets",
        "local_network_addresses": "LocalNetworkAddresses",
        "known_proxies": "KnownProxies",
        "enable_published_server_uri_by_request": "EnablePublishedServerUriByRequest",
    }

    _optionals = [
        "require_https",
        "certificate_path",
        "certificate_password",
        "base_url",
        "public_https_port",
        "http_server_port_number",
        "https_port_number",
        "enable_https",
        "public_port",
        "u_pn_p_create_http_port_map",
        "udp_port_range",
        "enable_ipv_6",
        "enable_ipv_4",
        "enable_ssdp_tracing",
        "ssdp_tracing_filter",
        "udp_send_count",
        "udp_send_delay",
        "ignore_virtual_interfaces",
        "virtual_interface_names",
        "gateway_monitor_period",
        "enable_multi_socket_binding",
        "trust_all_ip_6_interfaces",
        "hd_homerun_port_range",
        "published_server_uri_by_subnet",
        "auto_discovery_tracing",
        "auto_discovery",
        "remote_ip_filter",
        "is_remote_ip_filter_blacklist",
        "enable_u_pn_p",
        "enable_remote_access",
        "local_network_subnets",
        "local_network_addresses",
        "known_proxies",
        "enable_published_server_uri_by_request",
    ]

    def __init__(
        self,
        require_https=APIHelper.SKIP,
        certificate_path=APIHelper.SKIP,
        certificate_password=APIHelper.SKIP,
        base_url=APIHelper.SKIP,
        public_https_port=APIHelper.SKIP,
        http_server_port_number=APIHelper.SKIP,
        https_port_number=APIHelper.SKIP,
        enable_https=APIHelper.SKIP,
        public_port=APIHelper.SKIP,
        u_pn_p_create_http_port_map=APIHelper.SKIP,
        udp_port_range=APIHelper.SKIP,
        enable_ipv_6=APIHelper.SKIP,
        enable_ipv_4=APIHelper.SKIP,
        enable_ssdp_tracing=APIHelper.SKIP,
        ssdp_tracing_filter=APIHelper.SKIP,
        udp_send_count=APIHelper.SKIP,
        udp_send_delay=APIHelper.SKIP,
        ignore_virtual_interfaces=APIHelper.SKIP,
        virtual_interface_names=APIHelper.SKIP,
        gateway_monitor_period=APIHelper.SKIP,
        enable_multi_socket_binding=APIHelper.SKIP,
        trust_all_ip_6_interfaces=APIHelper.SKIP,
        hd_homerun_port_range=APIHelper.SKIP,
        published_server_uri_by_subnet=APIHelper.SKIP,
        auto_discovery_tracing=APIHelper.SKIP,
        auto_discovery=APIHelper.SKIP,
        remote_ip_filter=APIHelper.SKIP,
        is_remote_ip_filter_blacklist=APIHelper.SKIP,
        enable_u_pn_p=APIHelper.SKIP,
        enable_remote_access=APIHelper.SKIP,
        local_network_subnets=APIHelper.SKIP,
        local_network_addresses=APIHelper.SKIP,
        known_proxies=APIHelper.SKIP,
        enable_published_server_uri_by_request=APIHelper.SKIP,
    ):
        """Constructor for the NetworkConfiguration class"""

        # Initialize members of the class
        if require_https is not APIHelper.SKIP:
            self.require_https = require_https
        if certificate_path is not APIHelper.SKIP:
            self.certificate_path = certificate_path
        if certificate_password is not APIHelper.SKIP:
            self.certificate_password = certificate_password
        if base_url is not APIHelper.SKIP:
            self.base_url = base_url
        if public_https_port is not APIHelper.SKIP:
            self.public_https_port = public_https_port
        if http_server_port_number is not APIHelper.SKIP:
            self.http_server_port_number = http_server_port_number
        if https_port_number is not APIHelper.SKIP:
            self.https_port_number = https_port_number
        if enable_https is not APIHelper.SKIP:
            self.enable_https = enable_https
        if public_port is not APIHelper.SKIP:
            self.public_port = public_port
        if u_pn_p_create_http_port_map is not APIHelper.SKIP:
            self.u_pn_p_create_http_port_map = u_pn_p_create_http_port_map
        if udp_port_range is not APIHelper.SKIP:
            self.udp_port_range = udp_port_range
        if enable_ipv_6 is not APIHelper.SKIP:
            self.enable_ipv_6 = enable_ipv_6
        if enable_ipv_4 is not APIHelper.SKIP:
            self.enable_ipv_4 = enable_ipv_4
        if enable_ssdp_tracing is not APIHelper.SKIP:
            self.enable_ssdp_tracing = enable_ssdp_tracing
        if ssdp_tracing_filter is not APIHelper.SKIP:
            self.ssdp_tracing_filter = ssdp_tracing_filter
        if udp_send_count is not APIHelper.SKIP:
            self.udp_send_count = udp_send_count
        if udp_send_delay is not APIHelper.SKIP:
            self.udp_send_delay = udp_send_delay
        if ignore_virtual_interfaces is not APIHelper.SKIP:
            self.ignore_virtual_interfaces = ignore_virtual_interfaces
        if virtual_interface_names is not APIHelper.SKIP:
            self.virtual_interface_names = virtual_interface_names
        if gateway_monitor_period is not APIHelper.SKIP:
            self.gateway_monitor_period = gateway_monitor_period
        if enable_multi_socket_binding is not APIHelper.SKIP:
            self.enable_multi_socket_binding = enable_multi_socket_binding
        if trust_all_ip_6_interfaces is not APIHelper.SKIP:
            self.trust_all_ip_6_interfaces = trust_all_ip_6_interfaces
        if hd_homerun_port_range is not APIHelper.SKIP:
            self.hd_homerun_port_range = hd_homerun_port_range
        if published_server_uri_by_subnet is not APIHelper.SKIP:
            self.published_server_uri_by_subnet = published_server_uri_by_subnet
        if auto_discovery_tracing is not APIHelper.SKIP:
            self.auto_discovery_tracing = auto_discovery_tracing
        if auto_discovery is not APIHelper.SKIP:
            self.auto_discovery = auto_discovery
        if remote_ip_filter is not APIHelper.SKIP:
            self.remote_ip_filter = remote_ip_filter
        if is_remote_ip_filter_blacklist is not APIHelper.SKIP:
            self.is_remote_ip_filter_blacklist = is_remote_ip_filter_blacklist
        if enable_u_pn_p is not APIHelper.SKIP:
            self.enable_u_pn_p = enable_u_pn_p
        if enable_remote_access is not APIHelper.SKIP:
            self.enable_remote_access = enable_remote_access
        if local_network_subnets is not APIHelper.SKIP:
            self.local_network_subnets = local_network_subnets
        if local_network_addresses is not APIHelper.SKIP:
            self.local_network_addresses = local_network_addresses
        if known_proxies is not APIHelper.SKIP:
            self.known_proxies = known_proxies
        if enable_published_server_uri_by_request is not APIHelper.SKIP:
            self.enable_published_server_uri_by_request = (
                enable_published_server_uri_by_request
            )

    @classmethod
    def from_dictionary(cls, dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        require_https = (
            dictionary.get("RequireHttps")
            if "RequireHttps" in dictionary.keys()
            else APIHelper.SKIP
        )
        certificate_path = (
            dictionary.get("CertificatePath")
            if dictionary.get("CertificatePath")
            else APIHelper.SKIP
        )
        certificate_password = (
            dictionary.get("CertificatePassword")
            if dictionary.get("CertificatePassword")
            else APIHelper.SKIP
        )
        base_url = (
            dictionary.get("BaseUrl") if dictionary.get("BaseUrl") else APIHelper.SKIP
        )
        public_https_port = (
            dictionary.get("PublicHttpsPort")
            if dictionary.get("PublicHttpsPort")
            else APIHelper.SKIP
        )
        http_server_port_number = (
            dictionary.get("HttpServerPortNumber")
            if dictionary.get("HttpServerPortNumber")
            else APIHelper.SKIP
        )
        https_port_number = (
            dictionary.get("HttpsPortNumber")
            if dictionary.get("HttpsPortNumber")
            else APIHelper.SKIP
        )
        enable_https = (
            dictionary.get("EnableHttps")
            if "EnableHttps" in dictionary.keys()
            else APIHelper.SKIP
        )
        public_port = (
            dictionary.get("PublicPort")
            if dictionary.get("PublicPort")
            else APIHelper.SKIP
        )
        u_pn_p_create_http_port_map = (
            dictionary.get("UPnPCreateHttpPortMap")
            if "UPnPCreateHttpPortMap" in dictionary.keys()
            else APIHelper.SKIP
        )
        udp_port_range = (
            dictionary.get("UDPPortRange")
            if dictionary.get("UDPPortRange")
            else APIHelper.SKIP
        )
        enable_ipv_6 = (
            dictionary.get("EnableIPV6")
            if "EnableIPV6" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_ipv_4 = (
            dictionary.get("EnableIPV4")
            if "EnableIPV4" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_ssdp_tracing = (
            dictionary.get("EnableSSDPTracing")
            if "EnableSSDPTracing" in dictionary.keys()
            else APIHelper.SKIP
        )
        ssdp_tracing_filter = (
            dictionary.get("SSDPTracingFilter")
            if dictionary.get("SSDPTracingFilter")
            else APIHelper.SKIP
        )
        udp_send_count = (
            dictionary.get("UDPSendCount")
            if dictionary.get("UDPSendCount")
            else APIHelper.SKIP
        )
        udp_send_delay = (
            dictionary.get("UDPSendDelay")
            if dictionary.get("UDPSendDelay")
            else APIHelper.SKIP
        )
        ignore_virtual_interfaces = (
            dictionary.get("IgnoreVirtualInterfaces")
            if "IgnoreVirtualInterfaces" in dictionary.keys()
            else APIHelper.SKIP
        )
        virtual_interface_names = (
            dictionary.get("VirtualInterfaceNames")
            if dictionary.get("VirtualInterfaceNames")
            else APIHelper.SKIP
        )
        gateway_monitor_period = (
            dictionary.get("GatewayMonitorPeriod")
            if dictionary.get("GatewayMonitorPeriod")
            else APIHelper.SKIP
        )
        enable_multi_socket_binding = (
            dictionary.get("EnableMultiSocketBinding")
            if "EnableMultiSocketBinding" in dictionary.keys()
            else APIHelper.SKIP
        )
        trust_all_ip_6_interfaces = (
            dictionary.get("TrustAllIP6Interfaces")
            if "TrustAllIP6Interfaces" in dictionary.keys()
            else APIHelper.SKIP
        )
        hd_homerun_port_range = (
            dictionary.get("HDHomerunPortRange")
            if dictionary.get("HDHomerunPortRange")
            else APIHelper.SKIP
        )
        published_server_uri_by_subnet = (
            dictionary.get("PublishedServerUriBySubnet")
            if dictionary.get("PublishedServerUriBySubnet")
            else APIHelper.SKIP
        )
        auto_discovery_tracing = (
            dictionary.get("AutoDiscoveryTracing")
            if "AutoDiscoveryTracing" in dictionary.keys()
            else APIHelper.SKIP
        )
        auto_discovery = (
            dictionary.get("AutoDiscovery")
            if "AutoDiscovery" in dictionary.keys()
            else APIHelper.SKIP
        )
        remote_ip_filter = (
            dictionary.get("RemoteIPFilter")
            if dictionary.get("RemoteIPFilter")
            else APIHelper.SKIP
        )
        is_remote_ip_filter_blacklist = (
            dictionary.get("IsRemoteIPFilterBlacklist")
            if "IsRemoteIPFilterBlacklist" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_u_pn_p = (
            dictionary.get("EnableUPnP")
            if "EnableUPnP" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_remote_access = (
            dictionary.get("EnableRemoteAccess")
            if "EnableRemoteAccess" in dictionary.keys()
            else APIHelper.SKIP
        )
        local_network_subnets = (
            dictionary.get("LocalNetworkSubnets")
            if dictionary.get("LocalNetworkSubnets")
            else APIHelper.SKIP
        )
        local_network_addresses = (
            dictionary.get("LocalNetworkAddresses")
            if dictionary.get("LocalNetworkAddresses")
            else APIHelper.SKIP
        )
        known_proxies = (
            dictionary.get("KnownProxies")
            if dictionary.get("KnownProxies")
            else APIHelper.SKIP
        )
        enable_published_server_uri_by_request = (
            dictionary.get("EnablePublishedServerUriByRequest")
            if "EnablePublishedServerUriByRequest" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            require_https,
            certificate_path,
            certificate_password,
            base_url,
            public_https_port,
            http_server_port_number,
            https_port_number,
            enable_https,
            public_port,
            u_pn_p_create_http_port_map,
            udp_port_range,
            enable_ipv_6,
            enable_ipv_4,
            enable_ssdp_tracing,
            ssdp_tracing_filter,
            udp_send_count,
            udp_send_delay,
            ignore_virtual_interfaces,
            virtual_interface_names,
            gateway_monitor_period,
            enable_multi_socket_binding,
            trust_all_ip_6_interfaces,
            hd_homerun_port_range,
            published_server_uri_by_subnet,
            auto_discovery_tracing,
            auto_discovery,
            remote_ip_filter,
            is_remote_ip_filter_blacklist,
            enable_u_pn_p,
            enable_remote_access,
            local_network_subnets,
            local_network_addresses,
            known_proxies,
            enable_published_server_uri_by_request,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        require_https = XmlUtilities.value_from_xml_element(
            root.find("RequireHttps"), bool
        )
        certificate_path = XmlUtilities.value_from_xml_element(
            root.find("CertificatePath"), str
        )
        certificate_password = XmlUtilities.value_from_xml_element(
            root.find("CertificatePassword"), str
        )
        base_url = XmlUtilities.value_from_xml_element(root.find("BaseUrl"), str)
        public_https_port = XmlUtilities.value_from_xml_element(
            root.find("PublicHttpsPort"), int
        )
        http_server_port_number = XmlUtilities.value_from_xml_element(
            root.find("HttpServerPortNumber"), int
        )
        https_port_number = XmlUtilities.value_from_xml_element(
            root.find("HttpsPortNumber"), int
        )
        enable_https = XmlUtilities.value_from_xml_element(
            root.find("EnableHttps"), bool
        )
        public_port = XmlUtilities.value_from_xml_element(root.find("PublicPort"), int)
        u_pn_p_create_http_port_map = XmlUtilities.value_from_xml_element(
            root.find("UPnPCreateHttpPortMap"), bool
        )
        udp_port_range = XmlUtilities.value_from_xml_element(
            root.find("UDPPortRange"), str
        )
        enable_ipv_6 = XmlUtilities.value_from_xml_element(
            root.find("EnableIPV6"), bool
        )
        enable_ipv_4 = XmlUtilities.value_from_xml_element(
            root.find("EnableIPV4"), bool
        )
        enable_ssdp_tracing = XmlUtilities.value_from_xml_element(
            root.find("EnableSSDPTracing"), bool
        )
        ssdp_tracing_filter = XmlUtilities.value_from_xml_element(
            root.find("SSDPTracingFilter"), str
        )
        udp_send_count = XmlUtilities.value_from_xml_element(
            root.find("UDPSendCount"), int
        )
        udp_send_delay = XmlUtilities.value_from_xml_element(
            root.find("UDPSendDelay"), int
        )
        ignore_virtual_interfaces = XmlUtilities.value_from_xml_element(
            root.find("IgnoreVirtualInterfaces"), bool
        )
        virtual_interface_names = XmlUtilities.value_from_xml_element(
            root.find("VirtualInterfaceNames"), str
        )
        gateway_monitor_period = XmlUtilities.value_from_xml_element(
            root.find("GatewayMonitorPeriod"), int
        )
        enable_multi_socket_binding = XmlUtilities.value_from_xml_element(
            root.find("EnableMultiSocketBinding"), bool
        )
        trust_all_ip_6_interfaces = XmlUtilities.value_from_xml_element(
            root.find("TrustAllIP6Interfaces"), bool
        )
        hd_homerun_port_range = XmlUtilities.value_from_xml_element(
            root.find("HDHomerunPortRange"), str
        )
        published_server_uri_by_subnet = XmlUtilities.list_from_xml_element(
            root, "PublishedServerUriBySubnet", str
        )
        auto_discovery_tracing = XmlUtilities.value_from_xml_element(
            root.find("AutoDiscoveryTracing"), bool
        )
        auto_discovery = XmlUtilities.value_from_xml_element(
            root.find("AutoDiscovery"), bool
        )
        remote_ip_filter = XmlUtilities.list_from_xml_element(
            root, "RemoteIPFilter", str
        )
        is_remote_ip_filter_blacklist = XmlUtilities.value_from_xml_element(
            root.find("IsRemoteIPFilterBlacklist"), bool
        )
        enable_u_pn_p = XmlUtilities.value_from_xml_element(
            root.find("EnableUPnP"), bool
        )
        enable_remote_access = XmlUtilities.value_from_xml_element(
            root.find("EnableRemoteAccess"), bool
        )
        local_network_subnets = XmlUtilities.list_from_xml_element(
            root, "LocalNetworkSubnets", str
        )
        local_network_addresses = XmlUtilities.list_from_xml_element(
            root, "LocalNetworkAddresses", str
        )
        known_proxies = XmlUtilities.list_from_xml_element(root, "KnownProxies", str)
        enable_published_server_uri_by_request = XmlUtilities.value_from_xml_element(
            root.find("EnablePublishedServerUriByRequest"), bool
        )

        return cls(
            require_https,
            certificate_path,
            certificate_password,
            base_url,
            public_https_port,
            http_server_port_number,
            https_port_number,
            enable_https,
            public_port,
            u_pn_p_create_http_port_map,
            udp_port_range,
            enable_ipv_6,
            enable_ipv_4,
            enable_ssdp_tracing,
            ssdp_tracing_filter,
            udp_send_count,
            udp_send_delay,
            ignore_virtual_interfaces,
            virtual_interface_names,
            gateway_monitor_period,
            enable_multi_socket_binding,
            trust_all_ip_6_interfaces,
            hd_homerun_port_range,
            published_server_uri_by_subnet,
            auto_discovery_tracing,
            auto_discovery,
            remote_ip_filter,
            is_remote_ip_filter_blacklist,
            enable_u_pn_p,
            enable_remote_access,
            local_network_subnets,
            local_network_addresses,
            known_proxies,
            enable_published_server_uri_by_request,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.require_https, "RequireHttps")
        XmlUtilities.add_as_subelement(root, self.certificate_path, "CertificatePath")
        XmlUtilities.add_as_subelement(
            root, self.certificate_password, "CertificatePassword"
        )
        XmlUtilities.add_as_subelement(root, self.base_url, "BaseUrl")
        XmlUtilities.add_as_subelement(root, self.public_https_port, "PublicHttpsPort")
        XmlUtilities.add_as_subelement(
            root, self.http_server_port_number, "HttpServerPortNumber"
        )
        XmlUtilities.add_as_subelement(root, self.https_port_number, "HttpsPortNumber")
        XmlUtilities.add_as_subelement(root, self.enable_https, "EnableHttps")
        XmlUtilities.add_as_subelement(root, self.public_port, "PublicPort")
        XmlUtilities.add_as_subelement(
            root, self.u_pn_p_create_http_port_map, "UPnPCreateHttpPortMap"
        )
        XmlUtilities.add_as_subelement(root, self.udp_port_range, "UDPPortRange")
        XmlUtilities.add_as_subelement(root, self.enable_ipv_6, "EnableIPV6")
        XmlUtilities.add_as_subelement(root, self.enable_ipv_4, "EnableIPV4")
        XmlUtilities.add_as_subelement(
            root, self.enable_ssdp_tracing, "EnableSSDPTracing"
        )
        XmlUtilities.add_as_subelement(
            root, self.ssdp_tracing_filter, "SSDPTracingFilter"
        )
        XmlUtilities.add_as_subelement(root, self.udp_send_count, "UDPSendCount")
        XmlUtilities.add_as_subelement(root, self.udp_send_delay, "UDPSendDelay")
        XmlUtilities.add_as_subelement(
            root, self.ignore_virtual_interfaces, "IgnoreVirtualInterfaces"
        )
        XmlUtilities.add_as_subelement(
            root, self.virtual_interface_names, "VirtualInterfaceNames"
        )
        XmlUtilities.add_as_subelement(
            root, self.gateway_monitor_period, "GatewayMonitorPeriod"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_multi_socket_binding, "EnableMultiSocketBinding"
        )
        XmlUtilities.add_as_subelement(
            root, self.trust_all_ip_6_interfaces, "TrustAllIP6Interfaces"
        )
        XmlUtilities.add_as_subelement(
            root, self.hd_homerun_port_range, "HDHomerunPortRange"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.published_server_uri_by_subnet, "PublishedServerUriBySubnet"
        )
        XmlUtilities.add_as_subelement(
            root, self.auto_discovery_tracing, "AutoDiscoveryTracing"
        )
        XmlUtilities.add_as_subelement(root, self.auto_discovery, "AutoDiscovery")
        XmlUtilities.add_list_as_subelement(
            root, self.remote_ip_filter, "RemoteIPFilter"
        )
        XmlUtilities.add_as_subelement(
            root, self.is_remote_ip_filter_blacklist, "IsRemoteIPFilterBlacklist"
        )
        XmlUtilities.add_as_subelement(root, self.enable_u_pn_p, "EnableUPnP")
        XmlUtilities.add_as_subelement(
            root, self.enable_remote_access, "EnableRemoteAccess"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.local_network_subnets, "LocalNetworkSubnets"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.local_network_addresses, "LocalNetworkAddresses"
        )
        XmlUtilities.add_list_as_subelement(root, self.known_proxies, "KnownProxies")
        XmlUtilities.add_as_subelement(
            root,
            self.enable_published_server_uri_by_request,
            "EnablePublishedServerUriByRequest",
        )
