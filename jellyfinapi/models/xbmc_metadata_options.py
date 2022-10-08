# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class XbmcMetadataOptions(object):

    """Implementation of the 'XbmcMetadataOptions' model.

    TODO: type model description here.

    Attributes:
        user_id (string): TODO: type description here.
        release_date_format (string): TODO: type description here.
        save_image_paths_in_nfo (bool): TODO: type description here.
        enable_path_substitution (bool): TODO: type description here.
        enable_extra_thumbs_duplication (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_id": "UserId",
        "release_date_format": "ReleaseDateFormat",
        "save_image_paths_in_nfo": "SaveImagePathsInNfo",
        "enable_path_substitution": "EnablePathSubstitution",
        "enable_extra_thumbs_duplication": "EnableExtraThumbsDuplication",
    }

    _optionals = [
        "user_id",
        "release_date_format",
        "save_image_paths_in_nfo",
        "enable_path_substitution",
        "enable_extra_thumbs_duplication",
    ]

    _nullables = [
        "user_id",
    ]

    def __init__(
        self,
        user_id=APIHelper.SKIP,
        release_date_format=APIHelper.SKIP,
        save_image_paths_in_nfo=APIHelper.SKIP,
        enable_path_substitution=APIHelper.SKIP,
        enable_extra_thumbs_duplication=APIHelper.SKIP,
    ):
        """Constructor for the XbmcMetadataOptions class"""

        # Initialize members of the class
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
        if release_date_format is not APIHelper.SKIP:
            self.release_date_format = release_date_format
        if save_image_paths_in_nfo is not APIHelper.SKIP:
            self.save_image_paths_in_nfo = save_image_paths_in_nfo
        if enable_path_substitution is not APIHelper.SKIP:
            self.enable_path_substitution = enable_path_substitution
        if enable_extra_thumbs_duplication is not APIHelper.SKIP:
            self.enable_extra_thumbs_duplication = enable_extra_thumbs_duplication

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

        user_id = (
            dictionary.get("UserId")
            if "UserId" in dictionary.keys()
            else APIHelper.SKIP
        )
        release_date_format = (
            dictionary.get("ReleaseDateFormat")
            if dictionary.get("ReleaseDateFormat")
            else APIHelper.SKIP
        )
        save_image_paths_in_nfo = (
            dictionary.get("SaveImagePathsInNfo")
            if "SaveImagePathsInNfo" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_path_substitution = (
            dictionary.get("EnablePathSubstitution")
            if "EnablePathSubstitution" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_extra_thumbs_duplication = (
            dictionary.get("EnableExtraThumbsDuplication")
            if "EnableExtraThumbsDuplication" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            user_id,
            release_date_format,
            save_image_paths_in_nfo,
            enable_path_substitution,
            enable_extra_thumbs_duplication,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
        release_date_format = XmlUtilities.value_from_xml_element(
            root.find("ReleaseDateFormat"), str
        )
        save_image_paths_in_nfo = XmlUtilities.value_from_xml_element(
            root.find("SaveImagePathsInNfo"), bool
        )
        enable_path_substitution = XmlUtilities.value_from_xml_element(
            root.find("EnablePathSubstitution"), bool
        )
        enable_extra_thumbs_duplication = XmlUtilities.value_from_xml_element(
            root.find("EnableExtraThumbsDuplication"), bool
        )

        return cls(
            user_id,
            release_date_format,
            save_image_paths_in_nfo,
            enable_path_substitution,
            enable_extra_thumbs_duplication,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
        XmlUtilities.add_as_subelement(
            root, self.release_date_format, "ReleaseDateFormat"
        )
        XmlUtilities.add_as_subelement(
            root, self.save_image_paths_in_nfo, "SaveImagePathsInNfo"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_path_substitution, "EnablePathSubstitution"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_extra_thumbs_duplication, "EnableExtraThumbsDuplication"
        )
