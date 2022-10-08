# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ChapterInfo(object):

    """Implementation of the 'ChapterInfo' model.

    Class ChapterInfo.

    Attributes:
        start_position_ticks (long|int): Gets or sets the start position
            ticks.
        name (string): Gets or sets the name.
        image_path (string): Gets or sets the image path.
        image_date_modified (datetime): TODO: type description here.
        image_tag (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_position_ticks": "StartPositionTicks",
        "name": "Name",
        "image_path": "ImagePath",
        "image_date_modified": "ImageDateModified",
        "image_tag": "ImageTag",
    }

    _optionals = [
        "start_position_ticks",
        "name",
        "image_path",
        "image_date_modified",
        "image_tag",
    ]

    _nullables = [
        "name",
        "image_path",
        "image_tag",
    ]

    def __init__(
        self,
        start_position_ticks=APIHelper.SKIP,
        name=APIHelper.SKIP,
        image_path=APIHelper.SKIP,
        image_date_modified=APIHelper.SKIP,
        image_tag=APIHelper.SKIP,
    ):
        """Constructor for the ChapterInfo class"""

        # Initialize members of the class
        if start_position_ticks is not APIHelper.SKIP:
            self.start_position_ticks = start_position_ticks
        if name is not APIHelper.SKIP:
            self.name = name
        if image_path is not APIHelper.SKIP:
            self.image_path = image_path
        if image_date_modified is not APIHelper.SKIP:
            self.image_date_modified = (
                APIHelper.RFC3339DateTime(image_date_modified)
                if image_date_modified
                else None
            )
        if image_tag is not APIHelper.SKIP:
            self.image_tag = image_tag

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

        start_position_ticks = (
            dictionary.get("StartPositionTicks")
            if dictionary.get("StartPositionTicks")
            else APIHelper.SKIP
        )
        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        image_path = (
            dictionary.get("ImagePath")
            if "ImagePath" in dictionary.keys()
            else APIHelper.SKIP
        )
        image_date_modified = (
            APIHelper.RFC3339DateTime.from_value(
                dictionary.get("ImageDateModified")
            ).datetime
            if dictionary.get("ImageDateModified")
            else APIHelper.SKIP
        )
        image_tag = (
            dictionary.get("ImageTag")
            if "ImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            start_position_ticks, name, image_path, image_date_modified, image_tag
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        start_position_ticks = XmlUtilities.value_from_xml_element(
            root.find("StartPositionTicks"), int
        )
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        image_path = XmlUtilities.value_from_xml_element(root.find("ImagePath"), str)
        image_date_modified = XmlUtilities.value_from_xml_element(
            root.find("ImageDateModified"), APIHelper.RFC3339DateTime
        )
        image_tag = XmlUtilities.value_from_xml_element(root.find("ImageTag"), str)

        return cls(
            start_position_ticks, name, image_path, image_date_modified, image_tag
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(
            root, self.start_position_ticks, "StartPositionTicks"
        )
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.image_path, "ImagePath")
        XmlUtilities.add_as_subelement(
            root, self.image_date_modified, "ImageDateModified"
        )
        XmlUtilities.add_as_subelement(root, self.image_tag, "ImageTag")
