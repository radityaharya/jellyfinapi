# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.country_info import CountryInfo
from jellyfinapi.models.culture_dto import CultureDto
from jellyfinapi.models.external_id_info import ExternalIdInfo
from jellyfinapi.models.name_value_pair import NameValuePair
from jellyfinapi.models.parental_rating import ParentalRating
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MetadataEditorInfo(object):

    """Implementation of the 'MetadataEditorInfo' model.

    TODO: type model description here.

    Attributes:
        parental_rating_options (list of ParentalRating): TODO: type
            description here.
        countries (list of CountryInfo): TODO: type description here.
        cultures (list of CultureDto): TODO: type description here.
        external_id_infos (list of ExternalIdInfo): TODO: type description
            here.
        content_type (string): TODO: type description here.
        content_type_options (list of NameValuePair): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "parental_rating_options": "ParentalRatingOptions",
        "countries": "Countries",
        "cultures": "Cultures",
        "external_id_infos": "ExternalIdInfos",
        "content_type": "ContentType",
        "content_type_options": "ContentTypeOptions",
    }

    _optionals = [
        "parental_rating_options",
        "countries",
        "cultures",
        "external_id_infos",
        "content_type",
        "content_type_options",
    ]

    _nullables = [
        "content_type",
    ]

    def __init__(
        self,
        parental_rating_options=APIHelper.SKIP,
        countries=APIHelper.SKIP,
        cultures=APIHelper.SKIP,
        external_id_infos=APIHelper.SKIP,
        content_type=APIHelper.SKIP,
        content_type_options=APIHelper.SKIP,
    ):
        """Constructor for the MetadataEditorInfo class"""

        # Initialize members of the class
        if parental_rating_options is not APIHelper.SKIP:
            self.parental_rating_options = parental_rating_options
        if countries is not APIHelper.SKIP:
            self.countries = countries
        if cultures is not APIHelper.SKIP:
            self.cultures = cultures
        if external_id_infos is not APIHelper.SKIP:
            self.external_id_infos = external_id_infos
        if content_type is not APIHelper.SKIP:
            self.content_type = content_type
        if content_type_options is not APIHelper.SKIP:
            self.content_type_options = content_type_options

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

        parental_rating_options = None
        if dictionary.get("ParentalRatingOptions") is not None:
            parental_rating_options = [
                ParentalRating.from_dictionary(x)
                for x in dictionary.get("ParentalRatingOptions")
            ]
        else:
            parental_rating_options = APIHelper.SKIP
        countries = None
        if dictionary.get("Countries") is not None:
            countries = [
                CountryInfo.from_dictionary(x) for x in dictionary.get("Countries")
            ]
        else:
            countries = APIHelper.SKIP
        cultures = None
        if dictionary.get("Cultures") is not None:
            cultures = [
                CultureDto.from_dictionary(x) for x in dictionary.get("Cultures")
            ]
        else:
            cultures = APIHelper.SKIP
        external_id_infos = None
        if dictionary.get("ExternalIdInfos") is not None:
            external_id_infos = [
                ExternalIdInfo.from_dictionary(x)
                for x in dictionary.get("ExternalIdInfos")
            ]
        else:
            external_id_infos = APIHelper.SKIP
        content_type = (
            dictionary.get("ContentType")
            if "ContentType" in dictionary.keys()
            else APIHelper.SKIP
        )
        content_type_options = None
        if dictionary.get("ContentTypeOptions") is not None:
            content_type_options = [
                NameValuePair.from_dictionary(x)
                for x in dictionary.get("ContentTypeOptions")
            ]
        else:
            content_type_options = APIHelper.SKIP
        # Return an object of this model
        return cls(
            parental_rating_options,
            countries,
            cultures,
            external_id_infos,
            content_type,
            content_type_options,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        parental_rating_options = XmlUtilities.list_from_xml_element(
            root, "ParentalRating", ParentalRating
        )
        countries = XmlUtilities.list_from_xml_element(root, "CountryInfo", CountryInfo)
        cultures = XmlUtilities.list_from_xml_element(root, "CultureDto", CultureDto)
        external_id_infos = XmlUtilities.list_from_xml_element(
            root, "ExternalIdInfo", ExternalIdInfo
        )
        content_type = XmlUtilities.value_from_xml_element(
            root.find("ContentType"), str
        )
        content_type_options = XmlUtilities.list_from_xml_element(
            root, "NameValuePair", NameValuePair
        )

        return cls(
            parental_rating_options,
            countries,
            cultures,
            external_id_infos,
            content_type,
            content_type_options,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(
            root, self.parental_rating_options, "ParentalRating"
        )
        XmlUtilities.add_list_as_subelement(root, self.countries, "CountryInfo")
        XmlUtilities.add_list_as_subelement(root, self.cultures, "CultureDto")
        XmlUtilities.add_list_as_subelement(
            root, self.external_id_infos, "ExternalIdInfo"
        )
        XmlUtilities.add_as_subelement(root, self.content_type, "ContentType")
        XmlUtilities.add_list_as_subelement(
            root, self.content_type_options, "NameValuePair"
        )
