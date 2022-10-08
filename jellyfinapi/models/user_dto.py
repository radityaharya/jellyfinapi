# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.user_configuration import UserConfiguration
from jellyfinapi.models.user_policy import UserPolicy
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class UserDto(object):

    """Implementation of the 'UserDto' model.

    Class UserDto.

    Attributes:
        name (string): Gets or sets the name.
        server_id (string): Gets or sets the server identifier.
        server_name (string): Gets or sets the name of the server.  This is
            not used by the server and is for client-side usage only.
        id (uuid|string): Gets or sets the id.
        primary_image_tag (string): Gets or sets the primary image tag.
        has_password (bool): Gets or sets a value indicating whether this
            instance has password.
        has_configured_password (bool): Gets or sets a value indicating
            whether this instance has configured password.
        has_configured_easy_password (bool): Gets or sets a value indicating
            whether this instance has configured easy password.
        enable_auto_login (bool): Gets or sets whether async login is enabled
            or not.
        last_login_date (datetime): Gets or sets the last login date.
        last_activity_date (datetime): Gets or sets the last activity date.
        configuration (UserConfiguration): Gets or sets the configuration.
        policy (UserPolicy): Gets or sets the policy.
        primary_image_aspect_ratio (float): Gets or sets the primary image
            aspect ratio.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "server_id": "ServerId",
        "server_name": "ServerName",
        "id": "Id",
        "primary_image_tag": "PrimaryImageTag",
        "has_password": "HasPassword",
        "has_configured_password": "HasConfiguredPassword",
        "has_configured_easy_password": "HasConfiguredEasyPassword",
        "enable_auto_login": "EnableAutoLogin",
        "last_login_date": "LastLoginDate",
        "last_activity_date": "LastActivityDate",
        "configuration": "Configuration",
        "policy": "Policy",
        "primary_image_aspect_ratio": "PrimaryImageAspectRatio",
    }

    _optionals = [
        "name",
        "server_id",
        "server_name",
        "id",
        "primary_image_tag",
        "has_password",
        "has_configured_password",
        "has_configured_easy_password",
        "enable_auto_login",
        "last_login_date",
        "last_activity_date",
        "configuration",
        "policy",
        "primary_image_aspect_ratio",
    ]

    _nullables = [
        "name",
        "server_id",
        "server_name",
        "primary_image_tag",
        "enable_auto_login",
        "last_login_date",
        "last_activity_date",
        "configuration",
        "policy",
        "primary_image_aspect_ratio",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        server_id=APIHelper.SKIP,
        server_name=APIHelper.SKIP,
        id=APIHelper.SKIP,
        primary_image_tag=APIHelper.SKIP,
        has_password=APIHelper.SKIP,
        has_configured_password=APIHelper.SKIP,
        has_configured_easy_password=APIHelper.SKIP,
        enable_auto_login=APIHelper.SKIP,
        last_login_date=APIHelper.SKIP,
        last_activity_date=APIHelper.SKIP,
        configuration=APIHelper.SKIP,
        policy=APIHelper.SKIP,
        primary_image_aspect_ratio=APIHelper.SKIP,
    ):
        """Constructor for the UserDto class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if server_id is not APIHelper.SKIP:
            self.server_id = server_id
        if server_name is not APIHelper.SKIP:
            self.server_name = server_name
        if id is not APIHelper.SKIP:
            self.id = id
        if primary_image_tag is not APIHelper.SKIP:
            self.primary_image_tag = primary_image_tag
        if has_password is not APIHelper.SKIP:
            self.has_password = has_password
        if has_configured_password is not APIHelper.SKIP:
            self.has_configured_password = has_configured_password
        if has_configured_easy_password is not APIHelper.SKIP:
            self.has_configured_easy_password = has_configured_easy_password
        if enable_auto_login is not APIHelper.SKIP:
            self.enable_auto_login = enable_auto_login
        if last_login_date is not APIHelper.SKIP:
            self.last_login_date = (
                APIHelper.RFC3339DateTime(last_login_date) if last_login_date else None
            )
        if last_activity_date is not APIHelper.SKIP:
            self.last_activity_date = (
                APIHelper.RFC3339DateTime(last_activity_date)
                if last_activity_date
                else None
            )
        if configuration is not APIHelper.SKIP:
            self.configuration = configuration
        if policy is not APIHelper.SKIP:
            self.policy = policy
        if primary_image_aspect_ratio is not APIHelper.SKIP:
            self.primary_image_aspect_ratio = primary_image_aspect_ratio

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
        server_id = (
            dictionary.get("ServerId")
            if "ServerId" in dictionary.keys()
            else APIHelper.SKIP
        )
        server_name = (
            dictionary.get("ServerName")
            if "ServerName" in dictionary.keys()
            else APIHelper.SKIP
        )
        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        primary_image_tag = (
            dictionary.get("PrimaryImageTag")
            if "PrimaryImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        has_password = (
            dictionary.get("HasPassword")
            if "HasPassword" in dictionary.keys()
            else APIHelper.SKIP
        )
        has_configured_password = (
            dictionary.get("HasConfiguredPassword")
            if "HasConfiguredPassword" in dictionary.keys()
            else APIHelper.SKIP
        )
        has_configured_easy_password = (
            dictionary.get("HasConfiguredEasyPassword")
            if "HasConfiguredEasyPassword" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_auto_login = (
            dictionary.get("EnableAutoLogin")
            if "EnableAutoLogin" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "LastLoginDate" in dictionary.keys():
            last_login_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("LastLoginDate")
                ).datetime
                if dictionary.get("LastLoginDate")
                else None
            )
        else:
            last_login_date = APIHelper.SKIP
        if "LastActivityDate" in dictionary.keys():
            last_activity_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("LastActivityDate")
                ).datetime
                if dictionary.get("LastActivityDate")
                else None
            )
        else:
            last_activity_date = APIHelper.SKIP
        if "Configuration" in dictionary.keys():
            configuration = (
                UserConfiguration.from_dictionary(dictionary.get("Configuration"))
                if dictionary.get("Configuration")
                else None
            )
        else:
            configuration = APIHelper.SKIP
        if "Policy" in dictionary.keys():
            policy = (
                UserPolicy.from_dictionary(dictionary.get("Policy"))
                if dictionary.get("Policy")
                else None
            )
        else:
            policy = APIHelper.SKIP
        primary_image_aspect_ratio = (
            dictionary.get("PrimaryImageAspectRatio")
            if "PrimaryImageAspectRatio" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            name,
            server_id,
            server_name,
            id,
            primary_image_tag,
            has_password,
            has_configured_password,
            has_configured_easy_password,
            enable_auto_login,
            last_login_date,
            last_activity_date,
            configuration,
            policy,
            primary_image_aspect_ratio,
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
        server_id = XmlUtilities.value_from_xml_element(root.find("ServerId"), str)
        server_name = XmlUtilities.value_from_xml_element(root.find("ServerName"), str)
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        primary_image_tag = XmlUtilities.value_from_xml_element(
            root.find("PrimaryImageTag"), str
        )
        has_password = XmlUtilities.value_from_xml_element(
            root.find("HasPassword"), bool
        )
        has_configured_password = XmlUtilities.value_from_xml_element(
            root.find("HasConfiguredPassword"), bool
        )
        has_configured_easy_password = XmlUtilities.value_from_xml_element(
            root.find("HasConfiguredEasyPassword"), bool
        )
        enable_auto_login = XmlUtilities.value_from_xml_element(
            root.find("EnableAutoLogin"), bool
        )
        last_login_date = XmlUtilities.value_from_xml_element(
            root.find("LastLoginDate"), APIHelper.RFC3339DateTime
        )
        last_activity_date = XmlUtilities.value_from_xml_element(
            root.find("LastActivityDate"), APIHelper.RFC3339DateTime
        )
        configuration = XmlUtilities.value_from_xml_element(
            root.find("UserConfiguration"), UserConfiguration
        )
        policy = XmlUtilities.value_from_xml_element(
            root.find("UserPolicy"), UserPolicy
        )
        primary_image_aspect_ratio = XmlUtilities.value_from_xml_element(
            root.find("PrimaryImageAspectRatio"), float
        )

        return cls(
            name,
            server_id,
            server_name,
            id,
            primary_image_tag,
            has_password,
            has_configured_password,
            has_configured_easy_password,
            enable_auto_login,
            last_login_date,
            last_activity_date,
            configuration,
            policy,
            primary_image_aspect_ratio,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.server_id, "ServerId")
        XmlUtilities.add_as_subelement(root, self.server_name, "ServerName")
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.primary_image_tag, "PrimaryImageTag")
        XmlUtilities.add_as_subelement(root, self.has_password, "HasPassword")
        XmlUtilities.add_as_subelement(
            root, self.has_configured_password, "HasConfiguredPassword"
        )
        XmlUtilities.add_as_subelement(
            root, self.has_configured_easy_password, "HasConfiguredEasyPassword"
        )
        XmlUtilities.add_as_subelement(root, self.enable_auto_login, "EnableAutoLogin")
        XmlUtilities.add_as_subelement(root, self.last_login_date, "LastLoginDate")
        XmlUtilities.add_as_subelement(
            root, self.last_activity_date, "LastActivityDate"
        )
        XmlUtilities.add_as_subelement(root, self.configuration, "UserConfiguration")
        XmlUtilities.add_as_subelement(root, self.policy, "UserPolicy")
        XmlUtilities.add_as_subelement(
            root, self.primary_image_aspect_ratio, "PrimaryImageAspectRatio"
        )
