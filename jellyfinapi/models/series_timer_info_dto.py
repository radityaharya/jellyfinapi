# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class SeriesTimerInfoDto(object):

    """Implementation of the 'SeriesTimerInfoDto' model.

    Class SeriesTimerInfoDto.

    Attributes:
        id (string): Gets or sets the Id of the recording.
        mtype (string): TODO: type description here.
        server_id (string): Gets or sets the server identifier.
        external_id (string): Gets or sets the external identifier.
        channel_id (uuid|string): Gets or sets the channel id of the
            recording.
        external_channel_id (string): Gets or sets the external channel
            identifier.
        channel_name (string): Gets or sets the channel name of the
            recording.
        channel_primary_image_tag (string): TODO: type description here.
        program_id (string): Gets or sets the program identifier.
        external_program_id (string): Gets or sets the external program
            identifier.
        name (string): Gets or sets the name of the recording.
        overview (string): Gets or sets the description of the recording.
        start_date (datetime): Gets or sets the start date of the recording,
            in UTC.
        end_date (datetime): Gets or sets the end date of the recording, in
            UTC.
        service_name (string): Gets or sets the name of the service.
        priority (int): Gets or sets the priority.
        pre_padding_seconds (int): Gets or sets the pre padding seconds.
        post_padding_seconds (int): Gets or sets the post padding seconds.
        is_pre_padding_required (bool): Gets or sets a value indicating
            whether this instance is pre padding required.
        parent_backdrop_item_id (string): Gets or sets the Id of the Parent
            that has a backdrop if the item does not have one.
        parent_backdrop_image_tags (list of string): Gets or sets the parent
            backdrop image tags.
        is_post_padding_required (bool): Gets or sets a value indicating
            whether this instance is post padding required.
        keep_until (KeepUntilEnum): TODO: type description here.
        record_any_time (bool): Gets or sets a value indicating whether
            [record any time].
        skip_episodes_in_library (bool): TODO: type description here.
        record_any_channel (bool): Gets or sets a value indicating whether
            [record any channel].
        keep_up_to (int): TODO: type description here.
        record_new_only (bool): Gets or sets a value indicating whether
            [record new only].
        days (list of DayOfWeekEnum): Gets or sets the days.
        day_pattern (DayPatternEnum): Gets or sets the day pattern.
        image_tags (dict): Gets or sets the image tags.
        parent_thumb_item_id (string): Gets or sets the parent thumb item id.
        parent_thumb_image_tag (string): Gets or sets the parent thumb image
            tag.
        parent_primary_image_item_id (string): Gets or sets the parent primary
            image item identifier.
        parent_primary_image_tag (string): Gets or sets the parent primary
            image tag.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "Id",
        "mtype": "Type",
        "server_id": "ServerId",
        "external_id": "ExternalId",
        "channel_id": "ChannelId",
        "external_channel_id": "ExternalChannelId",
        "channel_name": "ChannelName",
        "channel_primary_image_tag": "ChannelPrimaryImageTag",
        "program_id": "ProgramId",
        "external_program_id": "ExternalProgramId",
        "name": "Name",
        "overview": "Overview",
        "start_date": "StartDate",
        "end_date": "EndDate",
        "service_name": "ServiceName",
        "priority": "Priority",
        "pre_padding_seconds": "PrePaddingSeconds",
        "post_padding_seconds": "PostPaddingSeconds",
        "is_pre_padding_required": "IsPrePaddingRequired",
        "parent_backdrop_item_id": "ParentBackdropItemId",
        "parent_backdrop_image_tags": "ParentBackdropImageTags",
        "is_post_padding_required": "IsPostPaddingRequired",
        "keep_until": "KeepUntil",
        "record_any_time": "RecordAnyTime",
        "skip_episodes_in_library": "SkipEpisodesInLibrary",
        "record_any_channel": "RecordAnyChannel",
        "keep_up_to": "KeepUpTo",
        "record_new_only": "RecordNewOnly",
        "days": "Days",
        "day_pattern": "DayPattern",
        "image_tags": "ImageTags",
        "parent_thumb_item_id": "ParentThumbItemId",
        "parent_thumb_image_tag": "ParentThumbImageTag",
        "parent_primary_image_item_id": "ParentPrimaryImageItemId",
        "parent_primary_image_tag": "ParentPrimaryImageTag",
    }

    _optionals = [
        "id",
        "mtype",
        "server_id",
        "external_id",
        "channel_id",
        "external_channel_id",
        "channel_name",
        "channel_primary_image_tag",
        "program_id",
        "external_program_id",
        "name",
        "overview",
        "start_date",
        "end_date",
        "service_name",
        "priority",
        "pre_padding_seconds",
        "post_padding_seconds",
        "is_pre_padding_required",
        "parent_backdrop_item_id",
        "parent_backdrop_image_tags",
        "is_post_padding_required",
        "keep_until",
        "record_any_time",
        "skip_episodes_in_library",
        "record_any_channel",
        "keep_up_to",
        "record_new_only",
        "days",
        "day_pattern",
        "image_tags",
        "parent_thumb_item_id",
        "parent_thumb_image_tag",
        "parent_primary_image_item_id",
        "parent_primary_image_tag",
    ]

    _nullables = [
        "id",
        "mtype",
        "server_id",
        "external_id",
        "external_channel_id",
        "channel_name",
        "channel_primary_image_tag",
        "program_id",
        "external_program_id",
        "name",
        "overview",
        "service_name",
        "parent_backdrop_item_id",
        "parent_backdrop_image_tags",
        "days",
        "day_pattern",
        "parent_thumb_item_id",
        "parent_thumb_image_tag",
        "parent_primary_image_item_id",
        "parent_primary_image_tag",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        server_id=APIHelper.SKIP,
        external_id=APIHelper.SKIP,
        channel_id=APIHelper.SKIP,
        external_channel_id=APIHelper.SKIP,
        channel_name=APIHelper.SKIP,
        channel_primary_image_tag=APIHelper.SKIP,
        program_id=APIHelper.SKIP,
        external_program_id=APIHelper.SKIP,
        name=APIHelper.SKIP,
        overview=APIHelper.SKIP,
        start_date=APIHelper.SKIP,
        end_date=APIHelper.SKIP,
        service_name=APIHelper.SKIP,
        priority=APIHelper.SKIP,
        pre_padding_seconds=APIHelper.SKIP,
        post_padding_seconds=APIHelper.SKIP,
        is_pre_padding_required=APIHelper.SKIP,
        parent_backdrop_item_id=APIHelper.SKIP,
        parent_backdrop_image_tags=APIHelper.SKIP,
        is_post_padding_required=APIHelper.SKIP,
        keep_until=APIHelper.SKIP,
        record_any_time=APIHelper.SKIP,
        skip_episodes_in_library=APIHelper.SKIP,
        record_any_channel=APIHelper.SKIP,
        keep_up_to=APIHelper.SKIP,
        record_new_only=APIHelper.SKIP,
        days=APIHelper.SKIP,
        day_pattern=APIHelper.SKIP,
        image_tags=APIHelper.SKIP,
        parent_thumb_item_id=APIHelper.SKIP,
        parent_thumb_image_tag=APIHelper.SKIP,
        parent_primary_image_item_id=APIHelper.SKIP,
        parent_primary_image_tag=APIHelper.SKIP,
    ):
        """Constructor for the SeriesTimerInfoDto class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if server_id is not APIHelper.SKIP:
            self.server_id = server_id
        if external_id is not APIHelper.SKIP:
            self.external_id = external_id
        if channel_id is not APIHelper.SKIP:
            self.channel_id = channel_id
        if external_channel_id is not APIHelper.SKIP:
            self.external_channel_id = external_channel_id
        if channel_name is not APIHelper.SKIP:
            self.channel_name = channel_name
        if channel_primary_image_tag is not APIHelper.SKIP:
            self.channel_primary_image_tag = channel_primary_image_tag
        if program_id is not APIHelper.SKIP:
            self.program_id = program_id
        if external_program_id is not APIHelper.SKIP:
            self.external_program_id = external_program_id
        if name is not APIHelper.SKIP:
            self.name = name
        if overview is not APIHelper.SKIP:
            self.overview = overview
        if start_date is not APIHelper.SKIP:
            self.start_date = (
                APIHelper.RFC3339DateTime(start_date) if start_date else None
            )
        if end_date is not APIHelper.SKIP:
            self.end_date = APIHelper.RFC3339DateTime(end_date) if end_date else None
        if service_name is not APIHelper.SKIP:
            self.service_name = service_name
        if priority is not APIHelper.SKIP:
            self.priority = priority
        if pre_padding_seconds is not APIHelper.SKIP:
            self.pre_padding_seconds = pre_padding_seconds
        if post_padding_seconds is not APIHelper.SKIP:
            self.post_padding_seconds = post_padding_seconds
        if is_pre_padding_required is not APIHelper.SKIP:
            self.is_pre_padding_required = is_pre_padding_required
        if parent_backdrop_item_id is not APIHelper.SKIP:
            self.parent_backdrop_item_id = parent_backdrop_item_id
        if parent_backdrop_image_tags is not APIHelper.SKIP:
            self.parent_backdrop_image_tags = parent_backdrop_image_tags
        if is_post_padding_required is not APIHelper.SKIP:
            self.is_post_padding_required = is_post_padding_required
        if keep_until is not APIHelper.SKIP:
            self.keep_until = keep_until
        if record_any_time is not APIHelper.SKIP:
            self.record_any_time = record_any_time
        if skip_episodes_in_library is not APIHelper.SKIP:
            self.skip_episodes_in_library = skip_episodes_in_library
        if record_any_channel is not APIHelper.SKIP:
            self.record_any_channel = record_any_channel
        if keep_up_to is not APIHelper.SKIP:
            self.keep_up_to = keep_up_to
        if record_new_only is not APIHelper.SKIP:
            self.record_new_only = record_new_only
        if days is not APIHelper.SKIP:
            self.days = days
        if day_pattern is not APIHelper.SKIP:
            self.day_pattern = day_pattern
        if image_tags is not APIHelper.SKIP:
            self.image_tags = image_tags
        if parent_thumb_item_id is not APIHelper.SKIP:
            self.parent_thumb_item_id = parent_thumb_item_id
        if parent_thumb_image_tag is not APIHelper.SKIP:
            self.parent_thumb_image_tag = parent_thumb_image_tag
        if parent_primary_image_item_id is not APIHelper.SKIP:
            self.parent_primary_image_item_id = parent_primary_image_item_id
        if parent_primary_image_tag is not APIHelper.SKIP:
            self.parent_primary_image_tag = parent_primary_image_tag

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

        id = dictionary.get("Id") if "Id" in dictionary.keys() else APIHelper.SKIP
        mtype = (
            dictionary.get("Type") if "Type" in dictionary.keys() else APIHelper.SKIP
        )
        server_id = (
            dictionary.get("ServerId")
            if "ServerId" in dictionary.keys()
            else APIHelper.SKIP
        )
        external_id = (
            dictionary.get("ExternalId")
            if "ExternalId" in dictionary.keys()
            else APIHelper.SKIP
        )
        channel_id = (
            dictionary.get("ChannelId")
            if dictionary.get("ChannelId")
            else APIHelper.SKIP
        )
        external_channel_id = (
            dictionary.get("ExternalChannelId")
            if "ExternalChannelId" in dictionary.keys()
            else APIHelper.SKIP
        )
        channel_name = (
            dictionary.get("ChannelName")
            if "ChannelName" in dictionary.keys()
            else APIHelper.SKIP
        )
        channel_primary_image_tag = (
            dictionary.get("ChannelPrimaryImageTag")
            if "ChannelPrimaryImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        program_id = (
            dictionary.get("ProgramId")
            if "ProgramId" in dictionary.keys()
            else APIHelper.SKIP
        )
        external_program_id = (
            dictionary.get("ExternalProgramId")
            if "ExternalProgramId" in dictionary.keys()
            else APIHelper.SKIP
        )
        name = dictionary.get("Name") if "Name" in dictionary.keys() else APIHelper.SKIP
        overview = (
            dictionary.get("Overview")
            if "Overview" in dictionary.keys()
            else APIHelper.SKIP
        )
        start_date = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("StartDate")).datetime
            if dictionary.get("StartDate")
            else APIHelper.SKIP
        )
        end_date = (
            APIHelper.RFC3339DateTime.from_value(dictionary.get("EndDate")).datetime
            if dictionary.get("EndDate")
            else APIHelper.SKIP
        )
        service_name = (
            dictionary.get("ServiceName")
            if "ServiceName" in dictionary.keys()
            else APIHelper.SKIP
        )
        priority = (
            dictionary.get("Priority") if dictionary.get("Priority") else APIHelper.SKIP
        )
        pre_padding_seconds = (
            dictionary.get("PrePaddingSeconds")
            if dictionary.get("PrePaddingSeconds")
            else APIHelper.SKIP
        )
        post_padding_seconds = (
            dictionary.get("PostPaddingSeconds")
            if dictionary.get("PostPaddingSeconds")
            else APIHelper.SKIP
        )
        is_pre_padding_required = (
            dictionary.get("IsPrePaddingRequired")
            if "IsPrePaddingRequired" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_backdrop_item_id = (
            dictionary.get("ParentBackdropItemId")
            if "ParentBackdropItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_backdrop_image_tags = (
            dictionary.get("ParentBackdropImageTags")
            if "ParentBackdropImageTags" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_post_padding_required = (
            dictionary.get("IsPostPaddingRequired")
            if "IsPostPaddingRequired" in dictionary.keys()
            else APIHelper.SKIP
        )
        keep_until = (
            dictionary.get("KeepUntil")
            if dictionary.get("KeepUntil")
            else APIHelper.SKIP
        )
        record_any_time = (
            dictionary.get("RecordAnyTime")
            if "RecordAnyTime" in dictionary.keys()
            else APIHelper.SKIP
        )
        skip_episodes_in_library = (
            dictionary.get("SkipEpisodesInLibrary")
            if "SkipEpisodesInLibrary" in dictionary.keys()
            else APIHelper.SKIP
        )
        record_any_channel = (
            dictionary.get("RecordAnyChannel")
            if "RecordAnyChannel" in dictionary.keys()
            else APIHelper.SKIP
        )
        keep_up_to = (
            dictionary.get("KeepUpTo") if dictionary.get("KeepUpTo") else APIHelper.SKIP
        )
        record_new_only = (
            dictionary.get("RecordNewOnly")
            if "RecordNewOnly" in dictionary.keys()
            else APIHelper.SKIP
        )
        days = dictionary.get("Days") if "Days" in dictionary.keys() else APIHelper.SKIP
        day_pattern = (
            dictionary.get("DayPattern")
            if "DayPattern" in dictionary.keys()
            else APIHelper.SKIP
        )
        image_tags = (
            dictionary.get("ImageTags")
            if dictionary.get("ImageTags")
            else APIHelper.SKIP
        )
        parent_thumb_item_id = (
            dictionary.get("ParentThumbItemId")
            if "ParentThumbItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_thumb_image_tag = (
            dictionary.get("ParentThumbImageTag")
            if "ParentThumbImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_primary_image_item_id = (
            dictionary.get("ParentPrimaryImageItemId")
            if "ParentPrimaryImageItemId" in dictionary.keys()
            else APIHelper.SKIP
        )
        parent_primary_image_tag = (
            dictionary.get("ParentPrimaryImageTag")
            if "ParentPrimaryImageTag" in dictionary.keys()
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            id,
            mtype,
            server_id,
            external_id,
            channel_id,
            external_channel_id,
            channel_name,
            channel_primary_image_tag,
            program_id,
            external_program_id,
            name,
            overview,
            start_date,
            end_date,
            service_name,
            priority,
            pre_padding_seconds,
            post_padding_seconds,
            is_pre_padding_required,
            parent_backdrop_item_id,
            parent_backdrop_image_tags,
            is_post_padding_required,
            keep_until,
            record_any_time,
            skip_episodes_in_library,
            record_any_channel,
            keep_up_to,
            record_new_only,
            days,
            day_pattern,
            image_tags,
            parent_thumb_item_id,
            parent_thumb_image_tag,
            parent_primary_image_item_id,
            parent_primary_image_tag,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        id = XmlUtilities.value_from_xml_element(root.find("Id"), str)
        mtype = XmlUtilities.value_from_xml_element(root.find("Type"), str)
        server_id = XmlUtilities.value_from_xml_element(root.find("ServerId"), str)
        external_id = XmlUtilities.value_from_xml_element(root.find("ExternalId"), str)
        channel_id = XmlUtilities.value_from_xml_element(root.find("ChannelId"), str)
        external_channel_id = XmlUtilities.value_from_xml_element(
            root.find("ExternalChannelId"), str
        )
        channel_name = XmlUtilities.value_from_xml_element(
            root.find("ChannelName"), str
        )
        channel_primary_image_tag = XmlUtilities.value_from_xml_element(
            root.find("ChannelPrimaryImageTag"), str
        )
        program_id = XmlUtilities.value_from_xml_element(root.find("ProgramId"), str)
        external_program_id = XmlUtilities.value_from_xml_element(
            root.find("ExternalProgramId"), str
        )
        name = XmlUtilities.value_from_xml_element(root.find("Name"), str)
        overview = XmlUtilities.value_from_xml_element(root.find("Overview"), str)
        start_date = XmlUtilities.value_from_xml_element(
            root.find("StartDate"), APIHelper.RFC3339DateTime
        )
        end_date = XmlUtilities.value_from_xml_element(
            root.find("EndDate"), APIHelper.RFC3339DateTime
        )
        service_name = XmlUtilities.value_from_xml_element(
            root.find("ServiceName"), str
        )
        priority = XmlUtilities.value_from_xml_element(root.find("Priority"), int)
        pre_padding_seconds = XmlUtilities.value_from_xml_element(
            root.find("PrePaddingSeconds"), int
        )
        post_padding_seconds = XmlUtilities.value_from_xml_element(
            root.find("PostPaddingSeconds"), int
        )
        is_pre_padding_required = XmlUtilities.value_from_xml_element(
            root.find("IsPrePaddingRequired"), bool
        )
        parent_backdrop_item_id = XmlUtilities.value_from_xml_element(
            root.find("ParentBackdropItemId"), str
        )
        parent_backdrop_image_tags = XmlUtilities.list_from_xml_element(
            root, "ParentBackdropImageTags", str
        )
        is_post_padding_required = XmlUtilities.value_from_xml_element(
            root.find("IsPostPaddingRequired"), bool
        )
        keep_until = XmlUtilities.value_from_xml_element(root.find("KeepUntil"), str)
        record_any_time = XmlUtilities.value_from_xml_element(
            root.find("RecordAnyTime"), bool
        )
        skip_episodes_in_library = XmlUtilities.value_from_xml_element(
            root.find("SkipEpisodesInLibrary"), bool
        )
        record_any_channel = XmlUtilities.value_from_xml_element(
            root.find("RecordAnyChannel"), bool
        )
        keep_up_to = XmlUtilities.value_from_xml_element(root.find("KeepUpTo"), int)
        record_new_only = XmlUtilities.value_from_xml_element(
            root.find("RecordNewOnly"), bool
        )
        days = XmlUtilities.list_from_xml_element(root, "Days", str)
        day_pattern = XmlUtilities.value_from_xml_element(root.find("DayPattern"), str)
        image_tags = XmlUtilities.dict_from_xml_element(root.find("ImageTags"), dict)

        parent_thumb_item_id = XmlUtilities.value_from_xml_element(
            root.find("ParentThumbItemId"), str
        )
        parent_thumb_image_tag = XmlUtilities.value_from_xml_element(
            root.find("ParentThumbImageTag"), str
        )
        parent_primary_image_item_id = XmlUtilities.value_from_xml_element(
            root.find("ParentPrimaryImageItemId"), str
        )
        parent_primary_image_tag = XmlUtilities.value_from_xml_element(
            root.find("ParentPrimaryImageTag"), str
        )

        return cls(
            id,
            mtype,
            server_id,
            external_id,
            channel_id,
            external_channel_id,
            channel_name,
            channel_primary_image_tag,
            program_id,
            external_program_id,
            name,
            overview,
            start_date,
            end_date,
            service_name,
            priority,
            pre_padding_seconds,
            post_padding_seconds,
            is_pre_padding_required,
            parent_backdrop_item_id,
            parent_backdrop_image_tags,
            is_post_padding_required,
            keep_until,
            record_any_time,
            skip_episodes_in_library,
            record_any_channel,
            keep_up_to,
            record_new_only,
            days,
            day_pattern,
            image_tags,
            parent_thumb_item_id,
            parent_thumb_image_tag,
            parent_primary_image_item_id,
            parent_primary_image_tag,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(root, self.id, "Id")
        XmlUtilities.add_as_subelement(root, self.mtype, "Type")
        XmlUtilities.add_as_subelement(root, self.server_id, "ServerId")
        XmlUtilities.add_as_subelement(root, self.external_id, "ExternalId")
        XmlUtilities.add_as_subelement(root, self.channel_id, "ChannelId")
        XmlUtilities.add_as_subelement(
            root, self.external_channel_id, "ExternalChannelId"
        )
        XmlUtilities.add_as_subelement(root, self.channel_name, "ChannelName")
        XmlUtilities.add_as_subelement(
            root, self.channel_primary_image_tag, "ChannelPrimaryImageTag"
        )
        XmlUtilities.add_as_subelement(root, self.program_id, "ProgramId")
        XmlUtilities.add_as_subelement(
            root, self.external_program_id, "ExternalProgramId"
        )
        XmlUtilities.add_as_subelement(root, self.name, "Name")
        XmlUtilities.add_as_subelement(root, self.overview, "Overview")
        XmlUtilities.add_as_subelement(root, self.start_date, "StartDate")
        XmlUtilities.add_as_subelement(root, self.end_date, "EndDate")
        XmlUtilities.add_as_subelement(root, self.service_name, "ServiceName")
        XmlUtilities.add_as_subelement(root, self.priority, "Priority")
        XmlUtilities.add_as_subelement(
            root, self.pre_padding_seconds, "PrePaddingSeconds"
        )
        XmlUtilities.add_as_subelement(
            root, self.post_padding_seconds, "PostPaddingSeconds"
        )
        XmlUtilities.add_as_subelement(
            root, self.is_pre_padding_required, "IsPrePaddingRequired"
        )
        XmlUtilities.add_as_subelement(
            root, self.parent_backdrop_item_id, "ParentBackdropItemId"
        )
        XmlUtilities.add_list_as_subelement(
            root, self.parent_backdrop_image_tags, "ParentBackdropImageTags"
        )
        XmlUtilities.add_as_subelement(
            root, self.is_post_padding_required, "IsPostPaddingRequired"
        )
        XmlUtilities.add_as_subelement(root, self.keep_until, "KeepUntil")
        XmlUtilities.add_as_subelement(root, self.record_any_time, "RecordAnyTime")
        XmlUtilities.add_as_subelement(
            root, self.skip_episodes_in_library, "SkipEpisodesInLibrary"
        )
        XmlUtilities.add_as_subelement(
            root, self.record_any_channel, "RecordAnyChannel"
        )
        XmlUtilities.add_as_subelement(root, self.keep_up_to, "KeepUpTo")
        XmlUtilities.add_as_subelement(root, self.record_new_only, "RecordNewOnly")
        XmlUtilities.add_list_as_subelement(root, self.days, "Days")
        XmlUtilities.add_as_subelement(root, self.day_pattern, "DayPattern")
        XmlUtilities.add_dict_as_subelement(
            root, self.image_tags, dictionary_name="ImageTags"
        )
        XmlUtilities.add_as_subelement(
            root, self.parent_thumb_item_id, "ParentThumbItemId"
        )
        XmlUtilities.add_as_subelement(
            root, self.parent_thumb_image_tag, "ParentThumbImageTag"
        )
        XmlUtilities.add_as_subelement(
            root, self.parent_primary_image_item_id, "ParentPrimaryImageItemId"
        )
        XmlUtilities.add_as_subelement(
            root, self.parent_primary_image_tag, "ParentPrimaryImageTag"
        )
