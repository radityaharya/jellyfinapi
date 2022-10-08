# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class GeneralCommand(object):

    """Implementation of the 'GeneralCommand' model.

    TODO: type model description here.

    Attributes:
        name (GeneralCommandTypeEnum): This exists simply to identify a set of
            known commands.
        controlling_user_id (uuid|string): TODO: type description here.
        arguments (dict): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "controlling_user_id": "ControllingUserId",
        "arguments": "Arguments",
    }

    _optionals = [
        "name",
        "controlling_user_id",
        "arguments",
    ]

    _nullables = [
        "arguments",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        controlling_user_id=APIHelper.SKIP,
        arguments=APIHelper.SKIP,
    ):
        """Constructor for the GeneralCommand class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if controlling_user_id is not APIHelper.SKIP:
            self.controlling_user_id = controlling_user_id
        if arguments is not APIHelper.SKIP:
            self.arguments = arguments

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

        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        controlling_user_id = (
            dictionary.get("ControllingUserId")
            if dictionary.get("ControllingUserId")
            else APIHelper.SKIP
        )
        arguments = (
            dictionary.get("Arguments")
            if "Arguments" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(name, controlling_user_id, arguments)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        controlling_user_id = XmlUtilities.value_from_xml_element(
            root.find("ControllingUserId"), str
        )
        arguments = XmlUtilities.dict_from_xml_element(root.find("Arguments"), dict)

        return cls(name, controlling_user_id, arguments)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(
            root, self.controlling_user_id, "ControllingUserId"
        )
        XmlUtilities.add_dict_as_subelement(
            root, self.arguments, dictionary_name="Arguments"
        )
