# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class MetadataConfiguration(object):

    """Implementation of the 'MetadataConfiguration' model.

    TODO: type model description here.

    Attributes:
        use_file_creation_time_for_date_added (bool): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "use_file_creation_time_for_date_added": "UseFileCreationTimeForDateAdded"
    }

    _optionals = [
        "use_file_creation_time_for_date_added",
    ]

    def __init__(self, use_file_creation_time_for_date_added=APIHelper.SKIP):
        """Constructor for the MetadataConfiguration class"""

        # Initialize members of the class
        if use_file_creation_time_for_date_added is not APIHelper.SKIP:
            self.use_file_creation_time_for_date_added = (
                use_file_creation_time_for_date_added
            )

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

        use_file_creation_time_for_date_added = (
            dictionary.get("UseFileCreationTimeForDateAdded")
            if "UseFileCreationTimeForDateAdded" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(use_file_creation_time_for_date_added)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        use_file_creation_time_for_date_added = XmlUtilities.value_from_xml_element(
            root.find("UseFileCreationTimeForDateAdded"), bool
        )

        return cls(use_file_creation_time_for_date_added)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(
            root,
            self.use_file_creation_time_for_date_added,
            "UseFileCreationTimeForDateAdded",
        )
