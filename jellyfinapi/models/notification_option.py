# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class NotificationOption(object):

    """Implementation of the 'NotificationOption' model.

    TODO: type model description here.

    Attributes:
        mtype (string): TODO: type description here.
        disabled_monitor_users (list of string): Gets or sets user Ids to not
            monitor (it's opt out).
        send_to_users (list of string): Gets or sets user Ids to send to (if
            SendToUserMode == Custom).
        enabled (bool): Gets or sets a value indicating whether this
            MediaBrowser.Model.Notifications.NotificationOption is enabled.
        disabled_services (list of string): Gets or sets the disabled
            services.
        send_to_user_mode (SendToUserTypeEnum): Gets or sets the send to user
            mode.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": "Type",
        "disabled_monitor_users": "DisabledMonitorUsers",
        "send_to_users": "SendToUsers",
        "enabled": "Enabled",
        "disabled_services": "DisabledServices",
        "send_to_user_mode": "SendToUserMode",
    }

    _optionals = [
        "mtype",
        "disabled_monitor_users",
        "send_to_users",
        "enabled",
        "disabled_services",
        "send_to_user_mode",
    ]

    _nullables = [
        "mtype",
    ]

    def __init__(
        self,
        mtype=APIHelper.SKIP,
        disabled_monitor_users=APIHelper.SKIP,
        send_to_users=APIHelper.SKIP,
        enabled=APIHelper.SKIP,
        disabled_services=APIHelper.SKIP,
        send_to_user_mode=APIHelper.SKIP,
    ):
        """Constructor for the NotificationOption class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if disabled_monitor_users is not APIHelper.SKIP:
            self.disabled_monitor_users = disabled_monitor_users
        if send_to_users is not APIHelper.SKIP:
            self.send_to_users = send_to_users
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if disabled_services is not APIHelper.SKIP:
            self.disabled_services = disabled_services
        if send_to_user_mode is not APIHelper.SKIP:
            self.send_to_user_mode = send_to_user_mode

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

        mtype = (
            dictionary.get("Type") if "Type" in dictionary.keys() else APIHelper.SKIP
        )
        disabled_monitor_users = (
            dictionary.get("DisabledMonitorUsers")
            if dictionary.get("DisabledMonitorUsers")
            else APIHelper.SKIP
        )
        send_to_users = (
            dictionary.get("SendToUsers")
            if dictionary.get("SendToUsers")
            else APIHelper.SKIP
        )
        enabled = (
            dictionary.get("Enabled")
            if "Enabled" in dictionary.keys()
            else APIHelper.SKIP
        )
        disabled_services = (
            dictionary.get("DisabledServices")
            if dictionary.get("DisabledServices")
            else APIHelper.SKIP
        )
        send_to_user_mode = (
            dictionary.get("SendToUserMode")
            if dictionary.get("SendToUserMode")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            mtype,
            disabled_monitor_users,
            send_to_users,
            enabled,
            disabled_services,
            send_to_user_mode,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        disabled_monitor_users = XmlUtilities.list_from_xml_element(
            root, "DisabledMonitorUsers", str
        )
        send_to_users = XmlUtilities.list_from_xml_element(root, "SendToUsers", str)
        enabled = XmlUtilities.value_from_xml_element(root.find("Enabled"), bool)
        disabled_services = XmlUtilities.list_from_xml_element(
            root, "DisabledServices", str
        )
        send_to_user_mode = XmlUtilities.value_from_xml_element(
            root.find("SendToUserMode"), str
        )

        return cls(
            mtype,
            disabled_monitor_users,
            send_to_users,
            enabled,
            disabled_services,
            send_to_user_mode,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_list_as_subelement(
            root, self.disabled_monitor_users, "DisabledMonitorUsers"
        )
        XmlUtilities.add_list_as_subelement(root, self.send_to_users, "SendToUsers")
        XmlUtilities.add_as_subelement(root, self.enabled, "Enabled")
        XmlUtilities.add_list_as_subelement(
            root, self.disabled_services, "DisabledServices"
        )
        XmlUtilities.add_as_subelement(root, self.send_to_user_mode, "SendToUserMode")
