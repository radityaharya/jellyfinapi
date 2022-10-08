# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class BrandingOptions(object):

    """Implementation of the 'BrandingOptions' model.

    The branding options.

    Attributes:
        login_disclaimer (string): Gets or sets the login disclaimer.
        custom_css (string): Gets or sets the custom CSS.
        splashscreen_enabled (bool): Gets or sets a value indicating whether
            to enable the splashscreen.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "login_disclaimer": "LoginDisclaimer",
        "custom_css": "CustomCss",
        "splashscreen_enabled": "SplashscreenEnabled",
    }

    _optionals = [
        "login_disclaimer",
        "custom_css",
        "splashscreen_enabled",
    ]

    _nullables = [
        "login_disclaimer",
        "custom_css",
    ]

    def __init__(
        self,
        login_disclaimer=APIHelper.SKIP,
        custom_css=APIHelper.SKIP,
        splashscreen_enabled=APIHelper.SKIP,
    ):
        """Constructor for the BrandingOptions class"""

        # Initialize members of the class
        if login_disclaimer is not APIHelper.SKIP:
            self.login_disclaimer = login_disclaimer
        if custom_css is not APIHelper.SKIP:
            self.custom_css = custom_css
        if splashscreen_enabled is not APIHelper.SKIP:
            self.splashscreen_enabled = splashscreen_enabled

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

        login_disclaimer = (
            dictionary.get("LoginDisclaimer")
            if "LoginDisclaimer" in dictionary.keys()
            else APIHelper.SKIP
        )
        custom_css = (
            dictionary.get("CustomCss")
            if "CustomCss" in dictionary.keys()
            else APIHelper.SKIP
        )
        splashscreen_enabled = (
            dictionary.get("SplashscreenEnabled")
            if "SplashscreenEnabled" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(login_disclaimer, custom_css, splashscreen_enabled)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        login_disclaimer = XmlUtilities.value_from_xml_element(
            root.find("LoginDisclaimer"), str
        )
        custom_css = XmlUtilities.value_from_xml_element(root.find("CustomCss"), str)
        splashscreen_enabled = XmlUtilities.value_from_xml_element(
            root.find("SplashscreenEnabled"), bool
        )

        return cls(login_disclaimer, custom_css, splashscreen_enabled)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.login_disclaimer, "LoginDisclaimer")
        XmlUtilities.add_as_subelement(root, self.custom_css, "CustomCss")
        XmlUtilities.add_as_subelement(
            root, self.splashscreen_enabled, "SplashscreenEnabled"
        )
