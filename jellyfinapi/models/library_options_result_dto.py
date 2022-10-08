# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.library_option_info_dto import LibraryOptionInfoDto
from jellyfinapi.models.library_type_options_dto import LibraryTypeOptionsDto
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class LibraryOptionsResultDto(object):

    """Implementation of the 'LibraryOptionsResultDto' model.

    Library options result dto.

    Attributes:
        metadata_savers (list of LibraryOptionInfoDto): Gets or sets the
            metadata savers.
        metadata_readers (list of LibraryOptionInfoDto): Gets or sets the
            metadata readers.
        subtitle_fetchers (list of LibraryOptionInfoDto): Gets or sets the
            subtitle fetchers.
        type_options (list of LibraryTypeOptionsDto): Gets or sets the type
            options.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "metadata_savers": "MetadataSavers",
        "metadata_readers": "MetadataReaders",
        "subtitle_fetchers": "SubtitleFetchers",
        "type_options": "TypeOptions",
    }

    _optionals = [
        "metadata_savers",
        "metadata_readers",
        "subtitle_fetchers",
        "type_options",
    ]

    def __init__(
        self,
        metadata_savers=APIHelper.SKIP,
        metadata_readers=APIHelper.SKIP,
        subtitle_fetchers=APIHelper.SKIP,
        type_options=APIHelper.SKIP,
    ):
        """Constructor for the LibraryOptionsResultDto class"""

        # Initialize members of the class
        if metadata_savers is not APIHelper.SKIP:
            self.metadata_savers = metadata_savers
        if metadata_readers is not APIHelper.SKIP:
            self.metadata_readers = metadata_readers
        if subtitle_fetchers is not APIHelper.SKIP:
            self.subtitle_fetchers = subtitle_fetchers
        if type_options is not APIHelper.SKIP:
            self.type_options = type_options

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

        metadata_savers = None
        if dictionary.get("MetadataSavers") is not None:
            metadata_savers = [
                LibraryOptionInfoDto.from_dictionary(x)
                for x in dictionary.get("MetadataSavers")
            ]
        else:
            metadata_savers = APIHelper.SKIP
        metadata_readers = None
        if dictionary.get("MetadataReaders") is not None:
            metadata_readers = [
                LibraryOptionInfoDto.from_dictionary(x)
                for x in dictionary.get("MetadataReaders")
            ]
        else:
            metadata_readers = APIHelper.SKIP
        subtitle_fetchers = None
        if dictionary.get("SubtitleFetchers") is not None:
            subtitle_fetchers = [
                LibraryOptionInfoDto.from_dictionary(x)
                for x in dictionary.get("SubtitleFetchers")
            ]
        else:
            subtitle_fetchers = APIHelper.SKIP
        type_options = None
        if dictionary.get("TypeOptions") is not None:
            type_options = [
                LibraryTypeOptionsDto.from_dictionary(x)
                for x in dictionary.get("TypeOptions")
            ]
        else:
            type_options = APIHelper.SKIP
        # Return an object of this model
        return cls(metadata_savers, metadata_readers, subtitle_fetchers, type_options)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        metadata_savers = XmlUtilities.list_from_xml_element(
            root, "LibraryOptionInfoDto", LibraryOptionInfoDto
        )
        metadata_readers = XmlUtilities.list_from_xml_element(
            root, "LibraryOptionInfoDto", LibraryOptionInfoDto
        )
        subtitle_fetchers = XmlUtilities.list_from_xml_element(
            root, "LibraryOptionInfoDto", LibraryOptionInfoDto
        )
        type_options = XmlUtilities.list_from_xml_element(
            root, "LibraryTypeOptionsDto", LibraryTypeOptionsDto
        )

        return cls(metadata_savers, metadata_readers, subtitle_fetchers, type_options)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(
            root, self.metadata_savers, "LibraryOptionInfoDto"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.metadata_readers, "LibraryOptionInfoDto"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.subtitle_fetchers, "LibraryOptionInfoDto"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.type_options, "LibraryTypeOptionsDto"
        )
