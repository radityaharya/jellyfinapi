# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class ConfigImageTypes(object):

    """Implementation of the 'ConfigImageTypes' model.

    TODO: type model description here.

    Attributes:
        backdrop_sizes (list of string): TODO: type description here.
        base_url (string): TODO: type description here.
        logo_sizes (list of string): TODO: type description here.
        poster_sizes (list of string): TODO: type description here.
        profile_sizes (list of string): TODO: type description here.
        secure_base_url (string): TODO: type description here.
        still_sizes (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backdrop_sizes": "BackdropSizes",
        "base_url": "BaseUrl",
        "logo_sizes": "LogoSizes",
        "poster_sizes": "PosterSizes",
        "profile_sizes": "ProfileSizes",
        "secure_base_url": "SecureBaseUrl",
        "still_sizes": "StillSizes",
    }

    _optionals = [
        "backdrop_sizes",
        "base_url",
        "logo_sizes",
        "poster_sizes",
        "profile_sizes",
        "secure_base_url",
        "still_sizes",
    ]

    _nullables = [
        "backdrop_sizes",
        "base_url",
        "logo_sizes",
        "poster_sizes",
        "profile_sizes",
        "secure_base_url",
        "still_sizes",
    ]

    def __init__(
        self,
        backdrop_sizes=APIHelper.SKIP,
        base_url=APIHelper.SKIP,
        logo_sizes=APIHelper.SKIP,
        poster_sizes=APIHelper.SKIP,
        profile_sizes=APIHelper.SKIP,
        secure_base_url=APIHelper.SKIP,
        still_sizes=APIHelper.SKIP,
    ):
        """Constructor for the ConfigImageTypes class"""

        # Initialize members of the class
        if backdrop_sizes is not APIHelper.SKIP:
            self.backdrop_sizes = backdrop_sizes
        if base_url is not APIHelper.SKIP:
            self.base_url = base_url
        if logo_sizes is not APIHelper.SKIP:
            self.logo_sizes = logo_sizes
        if poster_sizes is not APIHelper.SKIP:
            self.poster_sizes = poster_sizes
        if profile_sizes is not APIHelper.SKIP:
            self.profile_sizes = profile_sizes
        if secure_base_url is not APIHelper.SKIP:
            self.secure_base_url = secure_base_url
        if still_sizes is not APIHelper.SKIP:
            self.still_sizes = still_sizes

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

        backdrop_sizes = (
            dictionary.get("BackdropSizes")
            if "BackdropSizes" in dictionary.keys()
            else APIHelper.SKIP
        )
        base_url = (
            dictionary.get("BaseUrl")
            if "BaseUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        logo_sizes = (
            dictionary.get("LogoSizes")
            if "LogoSizes" in dictionary.keys()
            else APIHelper.SKIP
        )
        poster_sizes = (
            dictionary.get("PosterSizes")
            if "PosterSizes" in dictionary.keys()
            else APIHelper.SKIP
        )
        profile_sizes = (
            dictionary.get("ProfileSizes")
            if "ProfileSizes" in dictionary.keys()
            else APIHelper.SKIP
        )
        secure_base_url = (
            dictionary.get("SecureBaseUrl")
            if "SecureBaseUrl" in dictionary.keys()
            else APIHelper.SKIP
        )
        still_sizes = (
            dictionary.get("StillSizes")
            if "StillSizes" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            backdrop_sizes,
            base_url,
            logo_sizes,
            poster_sizes,
            profile_sizes,
            secure_base_url,
            still_sizes,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        backdrop_sizes = XmlUtilities.list_from_xml_element(root, "BackdropSizes", str)
        base_url = XmlUtilities.value_from_xml_element(root.find("BaseUrl"), str)
        logo_sizes = XmlUtilities.list_from_xml_element(root, "LogoSizes", str)
        poster_sizes = XmlUtilities.list_from_xml_element(root, "PosterSizes", str)
        profile_sizes = XmlUtilities.list_from_xml_element(root, "ProfileSizes", str)
        secure_base_url = XmlUtilities.value_from_xml_element(
            root.find("SecureBaseUrl"), str
        )
        still_sizes = XmlUtilities.list_from_xml_element(root, "StillSizes", str)

        return cls(
            backdrop_sizes,
            base_url,
            logo_sizes,
            poster_sizes,
            profile_sizes,
            secure_base_url,
            still_sizes,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.backdrop_sizes, "BackdropSizes")
        XmlUtilities.add_as_subelement(root, self.base_url, "BaseUrl")
        XmlUtilities.add_list_as_subelement(root, self.logo_sizes, "LogoSizes")
        XmlUtilities.add_list_as_subelement(root, self.poster_sizes, "PosterSizes")
        XmlUtilities.add_list_as_subelement(root, self.profile_sizes, "ProfileSizes")
        XmlUtilities.add_as_subelement(root, self.secure_base_url, "SecureBaseUrl")
        XmlUtilities.add_list_as_subelement(root, self.still_sizes, "StillSizes")
