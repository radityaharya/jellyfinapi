# -*- coding: utf-8 -*-


from jellyfinapi.utilities.xml_utilities import XmlUtilities


class QuickConnectDto(object):

    """Implementation of the 'QuickConnectDto' model.

    The quick connect request body.

    Attributes:
        secret (string): Gets or sets the quick connect secret.

    """

    # Create a mapping from Model property names to API property names
    _names = {"secret": "Secret"}

    def __init__(self, secret=None):
        """Constructor for the QuickConnectDto class"""

        # Initialize members of the class
        self.secret = secret

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

        secret = dictionary.get("Secret") if dictionary.get("Secret") else None
        # Return an object of this model
        return cls(secret)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        secret = XmlUtilities.value_from_xml_element(root.find("Secret"), str)

        return cls(secret)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.secret, "Secret")
