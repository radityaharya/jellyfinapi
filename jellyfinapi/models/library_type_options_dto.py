# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.image_option import ImageOption
from jellyfinapi.models.library_option_info_dto import LibraryOptionInfoDto
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class LibraryTypeOptionsDto(object):

    """Implementation of the 'LibraryTypeOptionsDto' model.

    Library type options dto.

    Attributes:
        mtype (string): Gets or sets the type.
        metadata_fetchers (list of LibraryOptionInfoDto): Gets or sets the
            metadata fetchers.
        image_fetchers (list of LibraryOptionInfoDto): Gets or sets the image
            fetchers.
        supported_image_types (list of ImageTypeEnum): Gets or sets the
            supported image types.
        default_image_options (list of ImageOption): Gets or sets the default
            image options.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": "Type",
        "metadata_fetchers": "MetadataFetchers",
        "image_fetchers": "ImageFetchers",
        "supported_image_types": "SupportedImageTypes",
        "default_image_options": "DefaultImageOptions",
    }

    _optionals = [
        "mtype",
        "metadata_fetchers",
        "image_fetchers",
        "supported_image_types",
        "default_image_options",
    ]

    _nullables = [
        "mtype",
    ]

    def __init__(
        self,
        mtype=APIHelper.SKIP,
        metadata_fetchers=APIHelper.SKIP,
        image_fetchers=APIHelper.SKIP,
        supported_image_types=APIHelper.SKIP,
        default_image_options=APIHelper.SKIP,
    ):
        """Constructor for the LibraryTypeOptionsDto class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if metadata_fetchers is not APIHelper.SKIP:
            self.metadata_fetchers = metadata_fetchers
        if image_fetchers is not APIHelper.SKIP:
            self.image_fetchers = image_fetchers
        if supported_image_types is not APIHelper.SKIP:
            self.supported_image_types = supported_image_types
        if default_image_options is not APIHelper.SKIP:
            self.default_image_options = default_image_options

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

        mtype = (
            dictionary.get("Type") if "Type" in dictionary.keys() else APIHelper.SKIP
        )
        metadata_fetchers = None
        if dictionary.get("MetadataFetchers") is not None:
            metadata_fetchers = [
                LibraryOptionInfoDto.from_dictionary(x)
                for x in dictionary.get("MetadataFetchers")
            ]
        else:
            metadata_fetchers = APIHelper.SKIP
        image_fetchers = None
        if dictionary.get("ImageFetchers") is not None:
            image_fetchers = [
                LibraryOptionInfoDto.from_dictionary(x)
                for x in dictionary.get("ImageFetchers")
            ]
        else:
            image_fetchers = APIHelper.SKIP
        supported_image_types = (
            dictionary.get("SupportedImageTypes")
            if dictionary.get("SupportedImageTypes")
            else APIHelper.SKIP
        )
        default_image_options = None
        if dictionary.get("DefaultImageOptions") is not None:
            default_image_options = [
                ImageOption.from_dictionary(x)
                for x in dictionary.get("DefaultImageOptions")
            ]
        else:
            default_image_options = APIHelper.SKIP
        # Return an object of this model
        return cls(
            mtype,
            metadata_fetchers,
            image_fetchers,
            supported_image_types,
            default_image_options,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        metadata_fetchers = XmlUtilities.list_from_xml_element(
            root, "LibraryOptionInfoDto", LibraryOptionInfoDto
        )
        image_fetchers = XmlUtilities.list_from_xml_element(
            root, "LibraryOptionInfoDto", LibraryOptionInfoDto
        )
        supported_image_types = XmlUtilities.list_from_xml_element(
            root, "SupportedImageTypes", str
        )
        default_image_options = XmlUtilities.list_from_xml_element(
            root, "ImageOption", ImageOption
        )

        return cls(
            mtype,
            metadata_fetchers,
            image_fetchers,
            supported_image_types,
            default_image_options,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_list_as_subelement(
            root, self.metadata_fetchers, "LibraryOptionInfoDto"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.image_fetchers, "LibraryOptionInfoDto"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.supported_image_types, "SupportedImageTypes"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.default_image_options, "ImageOption"
        )
