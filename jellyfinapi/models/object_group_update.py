# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ObjectGroupUpdate(object):

    """Implementation of the 'ObjectGroupUpdate' model.

    Class GroupUpdate.

    Attributes:
        group_id (uuid|string): Gets the group identifier.
        mtype (GroupUpdateTypeEnum): Gets the update type.
        data (object): Gets the update data.

    """

    # Create a mapping from Model property names to API property names
    _names = {"group_id": "GroupId", "mtype": "Type", "data": "Data"}

    _optionals = [
        "group_id",
        "mtype",
        "data",
    ]

    def __init__(
        self, group_id=APIHelper.SKIP, mtype=APIHelper.SKIP, data=APIHelper.SKIP
    ):
        """Constructor for the ObjectGroupUpdate class"""

        # Initialize members of the class
        if group_id is not APIHelper.SKIP:
            self.group_id = group_id
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if data is not APIHelper.SKIP:
            self.data = data

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

        group_id = (
            dictionary.get("GroupId") if dictionary.get("GroupId") else APIHelper.SKIP
        )
        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        data = dictionary.get("Data") if dictionary.get("Data") else APIHelper.SKIP
        # Return an object of this model
        return cls(group_id, mtype, data)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        group_id = XmlUtilities.value_from_xml_element(root.find("GroupId"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        data = XmlUtilities.value_from_xml_element(root.find("Data"), str)

        return cls(group_id, mtype, data)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.group_id, "GroupId")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.data, "Data")
