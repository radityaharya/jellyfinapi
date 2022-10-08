# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class QuickConnectResult(object):

    """Implementation of the 'QuickConnectResult' model.

    Stores the state of an quick connect request.

    Attributes:
        authenticated (bool): Gets or sets a value indicating whether this
            request is authorized.
        secret (string): Gets the secret value used to uniquely identify this
            request. Can be used to retrieve authentication information.
        code (string): Gets the user facing code used so the user can quickly
            differentiate this request from others.
        device_id (string): Gets the requesting device id.
        device_name (string): Gets the requesting device name.
        app_name (string): Gets the requesting app name.
        app_version (string): Gets the requesting app version.
        date_added (datetime): Gets or sets the DateTime that this request was
            created.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "authenticated": "Authenticated",
        "secret": "Secret",
        "code": "Code",
        "device_id": "DeviceId",
        "device_name": "DeviceName",
        "app_name": "AppName",
        "app_version": "AppVersion",
        "date_added": "DateAdded",
    }

    _optionals = [
        "authenticated",
        "secret",
        "code",
        "device_id",
        "device_name",
        "app_name",
        "app_version",
        "date_added",
    ]

    def __init__(
        self,
        authenticated=APIHelper.SKIP,
        secret=APIHelper.SKIP,
        code=APIHelper.SKIP,
        device_id=APIHelper.SKIP,
        device_name=APIHelper.SKIP,
        app_name=APIHelper.SKIP,
        app_version=APIHelper.SKIP,
        date_added=APIHelper.SKIP,
    ):
        """Constructor for the QuickConnectResult class"""

        # Initialize members of the class
        if authenticated is not APIHelper.SKIP:
            self.authenticated = authenticated
        if secret is not APIHelper.SKIP:
            self.secret = secret
        if code is not APIHelper.SKIP:
            self.code = code
        if device_id is not APIHelper.SKIP:
            self.device_id = device_id
        if device_name is not APIHelper.SKIP:
            self.device_name = device_name
        if app_name is not APIHelper.SKIP:
            self.app_name = app_name
        if app_version is not APIHelper.SKIP:
            self.app_version = app_version
        if date_added is not APIHelper.SKIP:
            self.date_added = (
                APIHelper.RFC3339DateTime(date_added) if date_added else None
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

        authenticated = (
            dictionary.get("Authenticated")
            if "Authenticated" in dictionary.keys()
            else APIHelper.SKIP
        )
        secret = (
            dictionary.get("Secret") if dictionary.get("Secret") else APIHelper.SKIP
        )
        code = dictionary.get("Code") if dictionary.get("Code") else APIHelper.SKIP
        device_id = (
            dictionary.get("DeviceId") if dictionary.get("DeviceId") else APIHelper.SKIP
        )
        device_name = (
            dictionary.get("DeviceName")
            if dictionary.get("DeviceName")
            else APIHelper.SKIP
        )
        app_name = (
            dictionary.get("AppName") if dictionary.get("AppName") else APIHelper.SKIP
        )
        app_version = (
            dictionary.get("AppVersion")
            if dictionary.get("AppVersion")
            else APIHelper.SKIP
        )
        date_added = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("DateAdded")).datetime
            if dictionary.get("DateAdded")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            authenticated,
            secret,
            code,
            device_id,
            device_name,
            app_name,
            app_version,
            date_added,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        authenticated = XmlUtilities.value_from_xml_element(
            root.find("Authenticated"), bool
        )
        secret = XmlUtilities.value_from_xml_element(root.find("Secret"), str)
        code = XmlUtilities.value_from_xml_element(root.find("Code"), str)
        device_id = XmlUtilities.value_from_xml_element(root.find("DeviceId"), str)
        device_name = XmlUtilities.value_from_xml_element(root.find("DeviceName"), str)
        app_name = XmlUtilities.value_from_xml_element(root.find("AppName"), str)
        app_version = XmlUtilities.value_from_xml_element(root.find("AppVersion"), str)
        date_added = XmlUtilities.value_from_xml_element(
            root.find("DateAdded"), APIHelper.RFC3339DateTime
        )

        return cls(
            authenticated,
            secret,
            code,
            device_id,
            device_name,
            app_name,
            app_version,
            date_added,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.authenticated, "Authenticated")
        XmlUtilities.add_as_subelement(root, self.secret, "Secret")
        XmlUtilities.add_as_subelement(root, self.code, "Code")
        XmlUtilities.add_as_subelement(root, self.device_id, "DeviceId")
        XmlUtilities.add_as_subelement(root, self.device_name, "DeviceName")
        XmlUtilities.add_as_subelement(root, self.app_name, "AppName")
        XmlUtilities.add_as_subelement(root, self.app_version, "AppVersion")
        XmlUtilities.add_as_subelement(root, self.date_added, "DateAdded")
