# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.task_result import TaskResult
from jellyfinapi.models.task_trigger_info import TaskTriggerInfo
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TaskInfo(object):

    """Implementation of the 'TaskInfo' model.

    Class TaskInfo.

    Attributes:
        name (string): Gets or sets the name.
        state (TaskStateEnum): Gets or sets the state of the task.
        current_progress_percentage (float): Gets or sets the progress.
        id (string): Gets or sets the id.
        last_execution_result (TaskResult): Gets or sets the last execution
            result.
        triggers (list of TaskTriggerInfo): Gets or sets the triggers.
        description (string): Gets or sets the description.
        category (string): Gets or sets the category.
        is_hidden (bool): Gets or sets a value indicating whether this
            instance is hidden.
        key (string): Gets or sets the key.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "Name",
        "state": "State",
        "current_progress_percentage": "CurrentProgressPercentage",
        "id": "Id",
        "last_execution_result": "LastExecutionResult",
        "triggers": "Triggers",
        "description": "Description",
        "category": "Category",
        "is_hidden": "IsHidden",
        "key": "Key",
    }

    _optionals = [
        "name",
        "state",
        "current_progress_percentage",
        "id",
        "last_execution_result",
        "triggers",
        "description",
        "category",
        "is_hidden",
        "key",
    ]

    _nullables = [
        "name",
        "current_progress_percentage",
        "id",
        "last_execution_result",
        "triggers",
        "description",
        "category",
        "key",
    ]

    def __init__(
        self,
        name=APIHelper.SKIP,
        state=APIHelper.SKIP,
        current_progress_percentage=APIHelper.SKIP,
        id=APIHelper.SKIP,
        last_execution_result=APIHelper.SKIP,
        triggers=APIHelper.SKIP,
        description=APIHelper.SKIP,
        category=APIHelper.SKIP,
        is_hidden=APIHelper.SKIP,
        key=APIHelper.SKIP,
    ):
        """Constructor for the TaskInfo class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if state is not APIHelper.SKIP:
            self.state = state
        if current_progress_percentage is not APIHelper.SKIP:
            self.current_progress_percentage = current_progress_percentage
        if id is not APIHelper.SKIP:
            self.id = id
        if last_execution_result is not APIHelper.SKIP:
            self.last_execution_result = last_execution_result
        if triggers is not APIHelper.SKIP:
            self.triggers = triggers
        if description is not APIHelper.SKIP:
            self.description = description
        if category is not APIHelper.SKIP:
            self.category = category
        if is_hidden is not APIHelper.SKIP:
            self.is_hidden = is_hidden
        if key is not APIHelper.SKIP:
            self.key = key

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

        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        state = dictionary.get("State") if dictionary.get("State") else APIHelper.SKIP
        current_progress_percentage = (
            dictionary.get("CurrentProgressPercentage")
            if "CurrentProgressPercentage" in dictionary.keys()
            else APIHelper.SKIP
        )
        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        if "LastExecutionResult" in dictionary.keys():
            last_execution_result = (
                TaskResult.from_dictionary(dictionary.get("LastExecutionResult"))
                if dictionary.get("LastExecutionResult")
                else None
            )
        else:
            last_execution_result = APIHelper.SKIP
        if "Triggers" in dictionary.keys():
            triggers = (
                [TaskTriggerInfo.from_dictionary(x) for x in dictionary.get("Triggers")]
                if dictionary.get("Triggers")
                else None
            )
        else:
            triggers = APIHelper.SKIP
        description = (
            dictionary.get("Description")
            if "Description" in dictionary.keys()
            else APIHelper.SKIP
        )
        category = (
            dictionary.get("Category")
            if "Category" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_hidden = (
            dictionary.get("IsHidden")
            if "IsHidden" in dictionary.keys()
            else APIHelper.SKIP
        )
        key = dictionary.get("Key") if "Key" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(
            name,
            state,
            current_progress_percentage,
            id,
            last_execution_result,
            triggers,
            description,
            category,
            is_hidden,
            key,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        state = XmlUtilities.value_from_xml_element(root.find("State"), str)
        current_progress_percentage = XmlUtilities.value_from_xml_element(
            root.find("CurrentProgressPercentage"), float
        )
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        last_execution_result = XmlUtilities.value_from_xml_element(
            root.find("TaskResult"), TaskResult
        )
        triggers = XmlUtilities.list_from_xml_element(
            root, "TaskTriggerInfo", TaskTriggerInfo
        )
        description = XmlUtilities.value_from_xml_element(root.find("Description"), str)
        category = XmlUtilities.value_from_xml_element(root.find("Category"), str)
        is_hidden = XmlUtilities.value_from_xml_element(root.find("IsHidden"), bool)
        key = XmlUtilities.value_from_xml_element(root.find("Key"), str)

        return cls(
            name,
            state,
            current_progress_percentage,
            id,
            last_execution_result,
            triggers,
            description,
            category,
            is_hidden,
            key,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.state, "State")
        XmlUtilities.add_as_subelement(
            root, self.current_progress_percentage, "CurrentProgressPercentage"
        )
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.last_execution_result, "TaskResult")
        XmlUtilities.add_list_as_subelement(root, self.triggers, "TaskTriggerInfo")
        XmlUtilities.add_as_subelement(root, self.description, "Description")
        XmlUtilities.add_as_subelement(root, self.category, "Category")
        XmlUtilities.add_as_subelement(root, self.is_hidden, "IsHidden")
        XmlUtilities.add_as_subelement(root, self.key, "Key")
