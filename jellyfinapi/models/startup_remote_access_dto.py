# -*- coding: utf-8 -*-


from jellyfinapi.utilities.xml_utilities import XmlUtilities


class StartupRemoteAccessDto(object):

    """Implementation of the 'StartupRemoteAccessDto' model.

    Startup remote access dto.

    Attributes:
        enable_remote_access (bool): Gets or sets a value indicating whether
            enable remote access.
        enable_automatic_port_mapping (bool): Gets or sets a value indicating
            whether enable automatic port mapping.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enable_remote_access": "EnableRemoteAccess",
        "enable_automatic_port_mapping": "EnableAutomaticPortMapping",
    }

    def __init__(self, enable_remote_access=None, enable_automatic_port_mapping=None):
        """Constructor for the StartupRemoteAccessDto class"""

        # Initialize members of the class
        self.enable_remote_access = enable_remote_access
        self.enable_automatic_port_mapping = enable_automatic_port_mapping

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

        enable_remote_access = (
            dictionary.get("EnableRemoteAccess")
            if "EnableRemoteAccess" in dictionary.keys()
            else None
        )
        enable_automatic_port_mapping = (
            dictionary.get("EnableAutomaticPortMapping")
            if "EnableAutomaticPortMapping" in dictionary.keys()
            else None
        )
        # Return an object of this model
        return cls(enable_remote_access, enable_automatic_port_mapping)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        enable_remote_access = XmlUtilities.value_from_xml_element(
            root.find("EnableRemoteAccess"), bool
        )
        enable_automatic_port_mapping = XmlUtilities.value_from_xml_element(
            root.find("EnableAutomaticPortMapping"), bool
        )

        return cls(enable_remote_access, enable_automatic_port_mapping)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(
            root, self.enable_remote_access, "EnableRemoteAccess"
        )
        XmlUtilities.add_as_subelement(
            root, self.enable_automatic_port_mapping, "EnableAutomaticPortMapping"
        )
