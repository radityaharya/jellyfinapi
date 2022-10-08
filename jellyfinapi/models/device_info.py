# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.client_capabilities import ClientCapabilities
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class DeviceInfo(object):

    """Implementation of the 'DeviceInfo' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        access_token (string): Gets or sets the access token.
        id (string): Gets or sets the identifier.
        last_user_name (string): Gets or sets the last name of the user.
        app_name (string): Gets or sets the name of the application.
        app_version (string): Gets or sets the application version.
        last_user_id (uuid|string): Gets or sets the last user identifier.
        date_last_activity (datetime): Gets or sets the date last modified.
        capabilities (ClientCapabilities): Gets or sets the capabilities.
        icon_url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "access_token": "AccessToken",
        "id": "Id",
        "last_user_name": "LastUserName",
        "app_name": "AppName",
        "app_version": "AppVersion",
        "last_user_id": "LastUserId",
        "date_last_activity": "DateLastActivity",
        "capabilities": "Capabilities",
        "icon_url": "IconUrl",
    }

    _optionals = [
        "name",
        "access_token",
        "id",
        "last_user_name",
        "app_name",
        "app_version",
        "last_user_id",
        "date_last_activity",
        "capabilities",
        "icon_url",
    ]

    _nullables = [
        "name",
        "access_token",
        "id",
        "last_user_name",
        "app_name",
        "app_version",
        "capabilities",
        "icon_url",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        access_token=APIHelper.SKIP,
        id=APIHelper.SKIP,
        last_user_name=APIHelper.SKIP,
        app_name=APIHelper.SKIP,
        app_version=APIHelper.SKIP,
        last_user_id=APIHelper.SKIP,
        date_last_activity=APIHelper.SKIP,
        capabilities=APIHelper.SKIP,
        icon_url=APIHelper.SKIP,
    ):
        """Constructor for the DeviceInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if access_token is not APIHelper.SKIP:
            self.access_token = access_token
        if id is not APIHelper.SKIP:
            self.id = id
        if last_user_name is not APIHelper.SKIP:
            self.last_user_name = last_user_name
        if app_name is not APIHelper.SKIP:
            self.app_name = app_name
        if app_version is not APIHelper.SKIP:
            self.app_version = app_version
        if last_user_id is not APIHelper.SKIP:
            self.last_user_id = last_user_id
        if date_last_activity is not APIHelper.SKIP:
            self.date_last_activity = (
                APIHelper.RFC3339DateTime(date_last_activity)
                if date_last_activity
                else None
            )
        if capabilities is not APIHelper.SKIP:
            self.capabilities = capabilities
        if icon_url is not APIHelper.SKIP:
            self.icon_url = icon_url

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

        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        access_token = (
            dictionary.get("AccessToken")
            if "AccessToken" in dictionary.keys()
            else APIHelper.SKIP
        )
        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        last_user_name = (
            dictionary.get("LastUserName")
            if "LastUserName" in dictionary.keys()
            else APIHelper.SKIP
        )
        app_name = (
            dictionary.get("AppName")
            if "AppName" in dictionary.keys()
            else APIHelper.SKIP
        )
        app_version = (
            dictionary.get("AppVersion")
            if "AppVersion" in dictionary.keys()
            else APIHelper.SKIP
        )
        last_user_id = (
            dictionary.get("LastUserId")
            if dictionary.get("LastUserId")
            else APIHelper.SKIP
        )
        date_last_activity = (
            APIHelper.RFC3339DateTime.from_value(
                dictionary.get("DateLastActivity")
            ).datetime
            if dictionary.get("DateLastActivity")
            else APIHelper.SKIP
        )
        if "Capabilities" in dictionary.keys():
            capabilities = (
                ClientCapabilities.from_dictionary(dictionary.get("Capabilities"))
                if dictionary.get("Capabilities")
                else None
            )
        else:
            capabilities = APIHelper.SKIP
        icon_url = (
            dictionary.get("IconUrl")
            if "IconUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            name,
            access_token,
            id,
            last_user_name,
            app_name,
            app_version,
            last_user_id,
            date_last_activity,
            capabilities,
            icon_url,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        access_token = XmlUtilities.value_from_xml_element(
            root.find("AccessToken"), str
        )
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        last_user_name = XmlUtilities.value_from_xml_element(
            root.find("LastUserName"), str
        )
        app_name = XmlUtilities.value_from_xml_element(root.find("AppName"), str)
        app_version = XmlUtilities.value_from_xml_element(root.find("AppVersion"), str)
        last_user_id = XmlUtilities.value_from_xml_element(root.find("LastUserId"), str)
        date_last_activity = XmlUtilities.value_from_xml_element(
            root.find("DateLastActivity"), APIHelper.RFC3339DateTime
        )
        capabilities = XmlUtilities.value_from_xml_element(
            root.find("ClientCapabilities"), ClientCapabilities
        )
        icon_url = XmlUtilities.value_from_xml_element(root.find("IconUrl"), str)

        return cls(
            name,
            access_token,
            id,
            last_user_name,
            app_name,
            app_version,
            last_user_id,
            date_last_activity,
            capabilities,
            icon_url,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.access_token, "AccessToken")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.last_user_name, "LastUserName")
        XmlUtilities.add_as_subelement(root, self.app_name, "AppName")
        XmlUtilities.add_as_subelement(root, self.app_version, "AppVersion")
        XmlUtilities.add_as_subelement(root, self.last_user_id, "LastUserId")
        XmlUtilities.add_as_subelement(
            root, self.date_last_activity, "DateLastActivity"
        )
        XmlUtilities.add_as_subelement(root, self.capabilities, "ClientCapabilities")
        XmlUtilities.add_as_subelement(root, self.icon_url, "IconUrl")
