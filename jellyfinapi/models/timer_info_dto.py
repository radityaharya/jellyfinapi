# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.models.base_item_dto import BaseItemDto
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class TimerInfoDto(object):

    """Implementation of the 'TimerInfoDto' model.

    TODO: type model description here.

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
        status (RecordingStatusEnum): Gets or sets the status.
        series_timer_id (string): Gets or sets the series timer identifier.
        external_series_timer_id (string): Gets or sets the external series
            timer identifier.
        run_time_ticks (long|int): Gets or sets the run time ticks.
        program_info (BaseItemDto): Gets or sets the program information.

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
        "status": "Status",
        "series_timer_id": "SeriesTimerId",
        "external_series_timer_id": "ExternalSeriesTimerId",
        "run_time_ticks": "RunTimeTicks",
        "program_info": "ProgramInfo",
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
        "status",
        "series_timer_id",
        "external_series_timer_id",
        "run_time_ticks",
        "program_info",
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
        "series_timer_id",
        "external_series_timer_id",
        "run_time_ticks",
        "program_info",
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
        status=APIHelper.SKIP,
        series_timer_id=APIHelper.SKIP,
        external_series_timer_id=APIHelper.SKIP,
        run_time_ticks=APIHelper.SKIP,
        program_info=APIHelper.SKIP,
    ):
        """Constructor for the TimerInfoDto class"""

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
        if status is not APIHelper.SKIP:
            self.status = status
        if series_timer_id is not APIHelper.SKIP:
            self.series_timer_id = series_timer_id
        if external_series_timer_id is not APIHelper.SKIP:
            self.external_series_timer_id = external_series_timer_id
        if run_time_ticks is not APIHelper.SKIP:
            self.run_time_ticks = run_time_ticks
        if program_info is not APIHelper.SKIP:
            self.program_info = program_info

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
        status = (
            dictionary.get("Status") if dictionary.get("Status") else APIHelper.SKIP
        )
        series_timer_id = (
            dictionary.get("SeriesTimerId")
            if "SeriesTimerId" in dictionary.keys()
            else APIHelper.SKIP
        )
        external_series_timer_id = (
            dictionary.get("ExternalSeriesTimerId")
            if "ExternalSeriesTimerId" in dictionary.keys()
            else APIHelper.SKIP
        )
        run_time_ticks = (
            dictionary.get("RunTimeTicks")
            if "RunTimeTicks" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "ProgramInfo" in dictionary.keys():
            program_info = (
                BaseItemDto.from_dictionary(dictionary.get("ProgramInfo"))
                if dictionary.get("ProgramInfo")
                else None
            )
        else:
            program_info = APIHelper.SKIP
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
            status,
            series_timer_id,
            external_series_timer_id,
            run_time_ticks,
            program_info,
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
        status = XmlUtilities.value_from_xml_element(root.find("Status"), str)
        series_timer_id = XmlUtilities.value_from_xml_element(
            root.find("SeriesTimerId"), str
        )
        external_series_timer_id = XmlUtilities.value_from_xml_element(
            root.find("ExternalSeriesTimerId"), str
        )
        run_time_ticks = XmlUtilities.value_from_xml_element(
            root.find("RunTimeTicks"), int
        )
        program_info = XmlUtilities.value_from_xml_element(
            root.find("BaseItemDto"), BaseItemDto
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
            status,
            series_timer_id,
            external_series_timer_id,
            run_time_ticks,
            program_info,
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
        XmlUtilities.add_as_subelement(root, self.status, "Status")
        XmlUtilities.add_as_subelement(root, self.series_timer_id, "SeriesTimerId")
        XmlUtilities.add_as_subelement(
            root, self.external_series_timer_id, "ExternalSeriesTimerId"
        )
        XmlUtilities.add_as_subelement(root, self.run_time_ticks, "RunTimeTicks")
        XmlUtilities.add_as_subelement(root, self.program_info, "BaseItemDto")
