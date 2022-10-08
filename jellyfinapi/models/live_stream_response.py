# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.media_source_info import MediaSourceInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class LiveStreamResponse(object):

    """Implementation of the 'LiveStreamResponse' model.

    TODO: type model description here.

    Attributes:
        media_source (MediaSourceInfo): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {"media_source": "MediaSource"}

    _optionals = [
        "media_source",
    ]

    def __init__(self, media_source=APIHelper.SKIP):
        """Constructor for the LiveStreamResponse class"""

        # Initialize members of the class
        if media_source is not APIHelper.SKIP:
            self.media_source = media_source

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

        media_source = (
            MediaSourceInfo.from_dictionary(dictionary.get("MediaSource"))
            if "MediaSource" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(media_source)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        media_source = XmlUtilities.value_from_xml_element(
            root.find("MediaSourceInfo"), MediaSourceInfo
        )

        return cls(media_source)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.media_source, "MediaSourceInfo")
