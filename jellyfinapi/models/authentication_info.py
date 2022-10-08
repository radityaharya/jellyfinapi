# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class AuthenticationInfo(object):

    """Implementation of the 'AuthenticationInfo' model.

    TODO: type model description here.

    Attributes:
        id (long|int): Gets or sets the identifier.
        access_token (string): Gets or sets the access token.
        device_id (string): Gets or sets the device identifier.
        app_name (string): Gets or sets the name of the application.
        app_version (string): Gets or sets the application version.
        device_name (string): Gets or sets the name of the device.
        user_id (uuid|string): Gets or sets the user identifier.
        is_active (bool): Gets or sets a value indicating whether this
            instance is active.
        date_created (datetime): Gets or sets the date created.
        date_revoked (datetime): Gets or sets the date revoked.
        date_last_activity (datetime): TODO: type description here.
        user_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "Id",
        "access_token": "AccessToken",
        "device_id": "DeviceId",
        "app_name": "AppName",
        "app_version": "AppVersion",
        "device_name": "DeviceName",
        "user_id": "UserId",
        "is_active": "IsActive",
        "date_created": "DateCreated",
        "date_revoked": "DateRevoked",
        "date_last_activity": "DateLastActivity",
        "user_name": "UserName",
    }

    _optionals = [
        "id",
        "access_token",
        "device_id",
        "app_name",
        "app_version",
        "device_name",
        "user_id",
        "is_active",
        "date_created",
        "date_revoked",
        "date_last_activity",
        "user_name",
    ]

    _nullables = [
        "access_token",
        "device_id",
        "app_name",
        "app_version",
        "device_name",
        "date_revoked",
        "user_name",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        access_token=APIHelper.SKIP,
        device_id=APIHelper.SKIP,
        app_name=APIHelper.SKIP,
        app_version=APIHelper.SKIP,
        device_name=APIHelper.SKIP,
        user_id=APIHelper.SKIP,
        is_active=APIHelper.SKIP,
        date_created=APIHelper.SKIP,
        date_revoked=APIHelper.SKIP,
        date_last_activity=APIHelper.SKIP,
        user_name=APIHelper.SKIP,
    ):
        """Constructor for the AuthenticationInfo class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if access_token is not APIHelper.SKIP:
            self.access_token = access_token
        if device_id is not APIHelper.SKIP:
            self.device_id = device_id
        if app_name is not APIHelper.SKIP:
            self.app_name = app_name
        if app_version is not APIHelper.SKIP:
            self.app_version = app_version
        if device_name is not APIHelper.SKIP:
            self.device_name = device_name
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
        if is_active is not APIHelper.SKIP:
            self.is_active = is_active
        if date_created is not APIHelper.SKIP:
            self.date_created = (
                APIHelper.RFC3339DateTime(date_created) if date_created else None
            )
        if date_revoked is not APIHelper.SKIP:
            self.date_revoked = (
                APIHelper.RFC3339DateTime(date_revoked) if date_revoked else None
            )
        if date_last_activity is not APIHelper.SKIP:
            self.date_last_activity = (
                APIHelper.RFC3339DateTime(date_last_activity)
                if date_last_activity
                else None
            )
        if user_name is not APIHelper.SKIP:
            self.user_name = user_name

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

        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        access_token = (
            dictionary.get("AccessToken")
            if "AccessToken" in dictionary.keys()
            else APIHelper.SKIP
        )
        device_id = (
            dictionary.get("DeviceId")
            if "DeviceId" in dictionary.keys()
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
        device_name = (
            dictionary.get("DeviceName")
            if "DeviceName" in dictionary.keys()
            else APIHelper.SKIP
        )
        user_id = (
            dictionary.get("UserId") if dictionary.get("UserId") else APIHelper.SKIP
        )
        is_active = (
            dictionary.get("IsActive")
            if "IsActive" in dictionary.keys()
            else APIHelper.SKIP
        )
        date_created = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("DateCreated")).datetime
            if dictionary.get("DateCreated")
            else APIHelper.SKIP
        )
        if "DateRevoked" in dictionary.keys():
            date_revoked = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("DateRevoked")
                ).datetime
                if dictionary.get("DateRevoked")
                else None
            )
        else:
            date_revoked = APIHelper.SKIP
        date_last_activity = (
            APIHelper.RFC3339DateTime.from_value(
                dictionary.get("DateLastActivity")
            ).datetime
            if dictionary.get("DateLastActivity")
            else APIHelper.SKIP
        )
        user_name = (
            dictionary.get("UserName")
            if "UserName" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            id,
            access_token,
            device_id,
            app_name,
            app_version,
            device_name,
            user_id,
            is_active,
            date_created,
            date_revoked,
            date_last_activity,
            user_name,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), int)
        access_token = XmlUtilities.value_from_xml_element(
            root.find("AccessToken"), str
        )
        device_id = XmlUtilities.value_from_xml_element(root.find("DeviceId"), str)
        app_name = XmlUtilities.value_from_xml_element(root.find("AppName"), str)
        app_version = XmlUtilities.value_from_xml_element(root.find("AppVersion"), str)
        device_name = XmlUtilities.value_from_xml_element(root.find("DeviceName"), str)
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
        is_active = XmlUtilities.value_from_xml_element(root.find("IsActive"), bool)
        date_created = XmlUtilities.value_from_xml_element(
            root.find("DateCreated"), APIHelper.RFC3339DateTime
        )
        date_revoked = XmlUtilities.value_from_xml_element(
            root.find("DateRevoked"), APIHelper.RFC3339DateTime
        )
        date_last_activity = XmlUtilities.value_from_xml_element(
            root.find("DateLastActivity"), APIHelper.RFC3339DateTime
        )
        user_name = XmlUtilities.value_from_xml_element(root.find("UserName"), str)

        return cls(
            id,
            access_token,
            device_id,
            app_name,
            app_version,
            device_name,
            user_id,
            is_active,
            date_created,
            date_revoked,
            date_last_activity,
            user_name,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.access_token, "AccessToken")
        XmlUtilities.add_as_subelement(root, self.device_id, "DeviceId")
        XmlUtilities.add_as_subelement(root, self.app_name, "AppName")
        XmlUtilities.add_as_subelement(root, self.app_version, "AppVersion")
        XmlUtilities.add_as_subelement(root, self.device_name, "DeviceName")
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
        XmlUtilities.add_as_subelement(root, self.is_active, "IsActive")
        XmlUtilities.add_as_subelement(root, self.date_created, "DateCreated")
        XmlUtilities.add_as_subelement(root, self.date_revoked, "DateRevoked")
        XmlUtilities.add_as_subelement(
            root, self.date_last_activity, "DateLastActivity"
        )
        XmlUtilities.add_as_subelement(root, self.user_name, "UserName")
