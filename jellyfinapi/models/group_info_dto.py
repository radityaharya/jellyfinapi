# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class GroupInfoDto(object):

    """Implementation of the 'GroupInfoDto' model.

    Class GroupInfoDto.

    Attributes:
        group_id (uuid|string): Gets the group identifier.
        group_name (string): Gets the group name.
        state (GroupStateTypeEnum): Gets the group state.
        participants (list of string): Gets the participants.
        last_updated_at (datetime): Gets the date when this DTO has been
            created.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_id": "GroupId",
        "group_name": "GroupName",
        "state": "State",
        "participants": "Participants",
        "last_updated_at": "LastUpdatedAt",
    }

    _optionals = [
        "group_id",
        "group_name",
        "state",
        "participants",
        "last_updated_at",
    ]

    def __init__(
        self,
        group_id=APIHelper.SKIP,
        group_name=APIHelper.SKIP,
        state=APIHelper.SKIP,
        participants=APIHelper.SKIP,
        last_updated_at=APIHelper.SKIP,
    ):
        """Constructor for the GroupInfoDto class"""

        # Initialize members of the class
        if group_id is not APIHelper.SKIP:
            self.group_id = group_id
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name
        if state is not APIHelper.SKIP:
            self.state = state
        if participants is not APIHelper.SKIP:
            self.participants = participants
        if last_updated_at is not APIHelper.SKIP:
            self.last_updated_at = (
                APIHelper.RFC3339DateTime(last_updated_at) if last_updated_at else None
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

        group_id = (
            dictionary.get("GroupId") if dictionary.get("GroupId") else APIHelper.SKIP
        )
        group_name = (
            dictionary.get("GroupName")
            if dictionary.get("GroupName")
            else APIHelper.SKIP
        )
        state = dictionary.get("State") if dictionary.get("State") else APIHelper.SKIP
        participants = (
            dictionary.get("Participants")
            if dictionary.get("Participants")
            else APIHelper.SKIP
        )
        last_updated_at = (
            APIHelper.RFC3339DateTime.from_value(
                dictionary.get("LastUpdatedAt")
            ).datetime
            if dictionary.get("LastUpdatedAt")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(group_id, group_name, state, participants, last_updated_at)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        group_id = XmlUtilities.value_from_xml_element(root.find("GroupId"), str)
        group_name = XmlUtilities.value_from_xml_element(root.find("GroupName"), str)
        state = XmlUtilities.value_from_xml_element(root.find("State"), str)
        participants = XmlUtilities.list_from_xml_element(root, "Participants", str)
        last_updated_at = XmlUtilities.value_from_xml_element(
            root.find("LastUpdatedAt"), APIHelper.RFC3339DateTime
        )

        return cls(group_id, group_name, state, participants, last_updated_at)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.group_id, "GroupId")
        XmlUtilities.add_as_subelement(root, self.group_name, "GroupName")
        XmlUtilities.add_as_subelement(root, self.state, "State")
        XmlUtilities.add_list_as_subelement(root, self.participants, "Participants")
        XmlUtilities.add_as_subelement(root, self.last_updated_at, "LastUpdatedAt")
