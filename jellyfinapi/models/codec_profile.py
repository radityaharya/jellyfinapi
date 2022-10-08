# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.profile_condition import ProfileCondition
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class CodecProfile(object):

    """Implementation of the 'CodecProfile' model.

    TODO: type model description here.

    Attributes:
        mtype (CodecTypeEnum): TODO: type description here.
        conditions (list of ProfileCondition): TODO: type description here.
        apply_conditions (list of ProfileCondition): TODO: type description
            here.
        codec (string): TODO: type description here.
        container (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": "Type",
        "conditions": "Conditions",
        "apply_conditions": "ApplyConditions",
        "codec": "Codec",
        "container": "Container",
    }

    _optionals = [
        "mtype",
        "conditions",
        "apply_conditions",
        "codec",
        "container",
    ]

    _nullables = [
        "conditions",
        "apply_conditions",
        "codec",
        "container",
    ]

    def __init__(
        self,
        mtype=APIHelper.SKIP,
        conditions=APIHelper.SKIP,
        apply_conditions=APIHelper.SKIP,
        codec=APIHelper.SKIP,
        container=APIHelper.SKIP,
    ):
        """Constructor for the CodecProfile class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if conditions is not APIHelper.SKIP:
            self.conditions = conditions
        if apply_conditions is not APIHelper.SKIP:
            self.apply_conditions = apply_conditions
        if codec is not APIHelper.SKIP:
            self.codec = codec
        if container is not APIHelper.SKIP:
            self.container = container

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

        mtype = dictionary.get("Type") if dictionary.get("Type") else APIHelper.SKIP
        if "Conditions" in dictionary.keys():
            conditions = (
                [
                    ProfileCondition.from_dictionary(x)
                    for x in dictionary.get("Conditions")
                ]
                if dictionary.get("Conditions")
                else None
            )
        else:
            conditions = APIHelper.SKIP
        if "ApplyConditions" in dictionary.keys():
            apply_conditions = (
                [
                    ProfileCondition.from_dictionary(x)
                    for x in dictionary.get("ApplyConditions")
                ]
                if dictionary.get("ApplyConditions")
                else None
            )
        else:
            apply_conditions = APIHelper.SKIP
        codec = (
            dictionary.get("Codec") if "Codec" in dictionary.keys() else APIHelper.SKIP
        )
        container = (
            dictionary.get("Container")
            if "Container" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(mtype, conditions, apply_conditions, codec, container)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        conditions = XmlUtilities.list_from_xml_element(
            root, "ProfileCondition", ProfileCondition
        )
        apply_conditions = XmlUtilities.list_from_xml_element(
            root, "ProfileCondition", ProfileCondition
        )
        codec = XmlUtilities.value_from_xml_element(root.find("Codec"), str)
        container = XmlUtilities.value_from_xml_element(root.find("Container"), str)

        return cls(mtype, conditions, apply_conditions, codec, container)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_list_as_subelement(root, self.conditions, "ProfileCondition")
        XmlUtilities.add_list_as_subelement(
            root, self.apply_conditions, "ProfileCondition"
        )
        XmlUtilities.add_as_subelement(root, self.codec, "Codec")
        XmlUtilities.add_as_subelement(root, self.container, "Container")
