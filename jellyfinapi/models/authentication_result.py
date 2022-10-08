# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.session_info import SessionInfo
from jellyfinapi.models.user_dto import UserDto
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class AuthenticationResult(object):

    """Implementation of the 'AuthenticationResult' model.

    TODO: type model description here.

    Attributes:
        user (UserDto): Class UserDto.
        session_info (SessionInfo): Class SessionInfo.
        access_token (string): TODO: type description here.
        server_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user": "User",
        "session_info": "SessionInfo",
        "access_token": "AccessToken",
        "server_id": "ServerId",
    }

    _optionals = [
        "user",
        "session_info",
        "access_token",
        "server_id",
    ]

    _nullables = [
        "user",
        "session_info",
        "access_token",
        "server_id",
    ]

    def __init__(
        self,
        user=APIHelper.SKIP,
        session_info=APIHelper.SKIP,
        access_token=APIHelper.SKIP,
        server_id=APIHelper.SKIP,
    ):
        """Constructor for the AuthenticationResult class"""

        # Initialize members of the class
        if user is not APIHelper.SKIP:
            self.user = user
        if session_info is not APIHelper.SKIP:
            self.session_info = session_info
        if access_token is not APIHelper.SKIP:
            self.access_token = access_token
        if server_id is not APIHelper.SKIP:
            self.server_id = server_id

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

        if "User" in dictionary.keys():
            user = (
                UserDto.from_dictionary(dictionary.get("User"))
                if dictionary.get("User")
                else None
            )
        else:
            user = APIHelper.SKIP
        if "SessionInfo" in dictionary.keys():
            session_info = (
                SessionInfo.from_dictionary(dictionary.get("SessionInfo"))
                if dictionary.get("SessionInfo")
                else None
            )
        else:
            session_info = APIHelper.SKIP
        access_token = (
            dictionary.get("AccessToken")
            if "AccessToken" in dictionary.keys()
            else APIHelper.SKIP
        )
        server_id = (
            dictionary.get("ServerId")
            if "ServerId" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(user, session_info, access_token, server_id)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        user = XmlUtilities.value_from_xml_element(root.find("UserDto"), UserDto)
        session_info = XmlUtilities.value_from_xml_element(
            root.find("SessionInfo"), SessionInfo
        )
        access_token = XmlUtilities.value_from_xml_element(
            root.find("AccessToken"), str
        )
        server_id = XmlUtilities.value_from_xml_element(root.find("ServerId"), str)

        return cls(user, session_info, access_token, server_id)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.user, "UserDto")
        XmlUtilities.add_as_subelement(root, self.session_info, "SessionInfo")
        XmlUtilities.add_as_subelement(root, self.access_token, "AccessToken")
        XmlUtilities.add_as_subelement(root, self.server_id, "ServerId")
