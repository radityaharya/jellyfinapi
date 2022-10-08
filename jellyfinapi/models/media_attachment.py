# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MediaAttachment(object):

    """Implementation of the 'MediaAttachment' model.

    Class MediaAttachment.

    Attributes:
        codec (string): Gets or sets the codec.
        codec_tag (string): Gets or sets the codec tag.
        comment (string): Gets or sets the comment.
        index (int): Gets or sets the index.
        file_name (string): Gets or sets the filename.
        mime_type (string): Gets or sets the MIME type.
        delivery_url (string): Gets or sets the delivery URL.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "codec": "Codec",
        "codec_tag": "CodecTag",
        "comment": "Comment",
        "index": "Index",
        "file_name": "FileName",
        "mime_type": "MimeType",
        "delivery_url": "DeliveryUrl",
    }

    _optionals = [
        "codec",
        "codec_tag",
        "comment",
        "index",
        "file_name",
        "mime_type",
        "delivery_url",
    ]

    _nullables = [
        "codec",
        "codec_tag",
        "comment",
        "file_name",
        "mime_type",
        "delivery_url",
    ]

    def __init__(
        self,
        codec=APIHelper.SKIP,
        codec_tag=APIHelper.SKIP,
        comment=APIHelper.SKIP,
        index=APIHelper.SKIP,
        file_name=APIHelper.SKIP,
        mime_type=APIHelper.SKIP,
        delivery_url=APIHelper.SKIP,
    ):
        """Constructor for the MediaAttachment class"""

        # Initialize members of the class
        if codec is not APIHelper.SKIP:
            self.codec = codec
        if codec_tag is not APIHelper.SKIP:
            self.codec_tag = codec_tag
        if comment is not APIHelper.SKIP:
            self.comment = comment
        if index is not APIHelper.SKIP:
            self.index = index
        if file_name is not APIHelper.SKIP:
            self.file_name = file_name
        if mime_type is not APIHelper.SKIP:
            self.mime_type = mime_type
        if delivery_url is not APIHelper.SKIP:
            self.delivery_url = delivery_url

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

        codec = (
            dictionary.get("Codec") if "Codec" in dictionary.keys() else APIHelper.SKIP
        )
        codec_tag = (
            dictionary.get("CodecTag")
            if "CodecTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        comment = (
            dictionary.get("Comment")
            if "Comment" in dictionary.keys()
            else APIHelper.SKIP
        )
        index = dictionary.get("Index") if dictionary.get("Index") else APIHelper.SKIP
        file_name = (
            dictionary.get("FileName")
            if "FileName" in dictionary.keys()
            else APIHelper.SKIP
        )
        mime_type = (
            dictionary.get("MimeType")
            if "MimeType" in dictionary.keys()
            else APIHelper.SKIP
        )
        delivery_url = (
            dictionary.get("DeliveryUrl")
            if "DeliveryUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(codec, codec_tag, comment, index, file_name, mime_type, delivery_url)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        codec = XmlUtilities.value_from_xml_element(root.find("Codec"), str)
        codec_tag = XmlUtilities.value_from_xml_element(root.find("CodecTag"), str)
        comment = XmlUtilities.value_from_xml_element(root.find("Comment"), str)
        index = XmlUtilities.value_from_xml_element(root.find("Index"), int)
        file_name = XmlUtilities.value_from_xml_element(root.find("FileName"), str)
        mime_type = XmlUtilities.value_from_xml_element(root.find("MimeType"), str)
        delivery_url = XmlUtilities.value_from_xml_element(
            root.find("DeliveryUrl"), str
        )

        return cls(codec, codec_tag, comment, index, file_name, mime_type, delivery_url)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.codec, "Codec")
        XmlUtilities.add_as_subelement(root, self.codec_tag, "CodecTag")
        XmlUtilities.add_as_subelement(root, self.comment, "Comment")
        XmlUtilities.add_as_subelement(root, self.index, "Index")
        XmlUtilities.add_as_subelement(root, self.file_name, "FileName")
        XmlUtilities.add_as_subelement(root, self.mime_type, "MimeType")
        XmlUtilities.add_as_subelement(root, self.delivery_url, "DeliveryUrl")
