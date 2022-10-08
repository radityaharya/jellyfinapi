# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TaskTriggerInfo(object):

    """Implementation of the 'TaskTriggerInfo' model.

    Class TaskTriggerInfo.

    Attributes:
        mtype (string): Gets or sets the type.
        time_of_day_ticks (long|int): Gets or sets the time of day.
        interval_ticks (long|int): Gets or sets the interval.
        day_of_week (DayOfWeekEnum): Gets or sets the day of week.
        max_runtime_ticks (long|int): Gets or sets the maximum runtime ticks.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": "Type",
        "time_of_day_ticks": "TimeOfDayTicks",
        "interval_ticks": "IntervalTicks",
        "day_of_week": "DayOfWeek",
        "max_runtime_ticks": "MaxRuntimeTicks",
    }

    _optionals = [
        "mtype",
        "time_of_day_ticks",
        "interval_ticks",
        "day_of_week",
        "max_runtime_ticks",
    ]

    _nullables = [
        "mtype",
        "time_of_day_ticks",
        "interval_ticks",
        "day_of_week",
        "max_runtime_ticks",
    ]

    def __init__(
        self,
        mtype=APIHelper.SKIP,
        time_of_day_ticks=APIHelper.SKIP,
        interval_ticks=APIHelper.SKIP,
        day_of_week=APIHelper.SKIP,
        max_runtime_ticks=APIHelper.SKIP,
    ):
        """Constructor for the TaskTriggerInfo class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if time_of_day_ticks is not APIHelper.SKIP:
            self.time_of_day_ticks = time_of_day_ticks
        if interval_ticks is not APIHelper.SKIP:
            self.interval_ticks = interval_ticks
        if day_of_week is not APIHelper.SKIP:
            self.day_of_week = day_of_week
        if max_runtime_ticks is not APIHelper.SKIP:
            self.max_runtime_ticks = max_runtime_ticks

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

        mtype = (
            dictionary.get("Type") if "Type" in dictionary.keys() else APIHelper.SKIP
        )
        time_of_day_ticks = (
            dictionary.get("TimeOfDayTicks")
            if "TimeOfDayTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        interval_ticks = (
            dictionary.get("IntervalTicks")
            if "IntervalTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        day_of_week = (
            dictionary.get("DayOfWeek")
            if "DayOfWeek" in dictionary.keys()
            else APIHelper.SKIP
        )
        max_runtime_ticks = (
            dictionary.get("MaxRuntimeTicks")
            if "MaxRuntimeTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            mtype, time_of_day_ticks, interval_ticks, day_of_week, max_runtime_ticks
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        time_of_day_ticks = XmlUtilities.value_from_xml_element(
            root.find("TimeOfDayTicks"), int
        )
        interval_ticks = XmlUtilities.value_from_xml_element(
            root.find("IntervalTicks"), int
        )
        day_of_week = XmlUtilities.value_from_xml_element(root.find("DayOfWeek"), str)
        max_runtime_ticks = XmlUtilities.value_from_xml_element(
            root.find("MaxRuntimeTicks"), int
        )

        return cls(
            mtype, time_of_day_ticks, interval_ticks, day_of_week, max_runtime_ticks
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.time_of_day_ticks, "TimeOfDayTicks")
        XmlUtilities.add_as_subelement(root, self.interval_ticks, "IntervalTicks")
        XmlUtilities.add_as_subelement(root, self.day_of_week, "DayOfWeek")
        XmlUtilities.add_as_subelement(root, self.max_runtime_ticks, "MaxRuntimeTicks")
