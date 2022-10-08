# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class PathSubstitution(object):

    """Implementation of the 'PathSubstitution' model.

    Defines the MediaBrowser.Model.Configuration.PathSubstitution.

    Attributes:
        mfrom (string): Gets or sets the value to substitute.
        to (string): Gets or sets the value to substitution with.

    """

    # Create a mapping from Model property names to API property names
    _names = {"mfrom": "From", "to": "To"}

    _optionals = [
        "mfrom",
        "to",
    ]

    def __init__(self, mfrom=APIHelper.SKIP, to=APIHelper.SKIP):
        """Constructor for the PathSubstitution class"""

        # Initialize members of the class
        if mfrom is not APIHelper.SKIP:
            self.mfrom = mfrom
        if to is not APIHelper.SKIP:
            self.to = to

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

        mfrom = dictionary.get("From") if dictionary.get("From") else APIHelper.SKIP
        to = dictionary.get("To") if dictionary.get("To") else APIHelper.SKIP
        # Return an object of this model
        return cls(mfrom, to)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        mfrom = XmlUtilities.value_from_xml_element(root.find("From"), str)
        to = XmlUtilities.value_from_xml_element(root.find("To"), str)

        return cls(mfrom, to)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.mfrom, "From")
        XmlUtilities.add_as_subelement(root, self.to, "To")
