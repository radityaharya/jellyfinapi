# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class DeviceProfileInfo(object):

    """Implementation of the 'DeviceProfileInfo' model.

    TODO: type model description here.

    Attributes:
        id (string): Gets or sets the identifier.
        name (string): Gets or sets the name.
        mtype (DeviceProfileTypeEnum): Gets or sets the type.

    """

    # Create a mapping from Model property names to API property names
    _names = {"id": "Id", "name": "Name", "mtype": "Type"}

    _optionals = [
        "id",
        "name",
        "mtype",
    ]

    _nullables = [
        "id",
        "name",
    ]

    def __init__(self, id=APIHelper.SKIP, name=APIHelper.SKIP, mtype=APIHelper.SKIP):
        """Constructor for the DeviceProfileInfo class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if name is not APIHelper.SKIP:
            self.name = name
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype

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

        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        # Return an object of this model
        return cls(id, name, mtype)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)

        return cls(id, name, mtype)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
