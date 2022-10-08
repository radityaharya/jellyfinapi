# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class GetProgramsDto(object):

    """Implementation of the 'GetProgramsDto' model.

    Get programs dto.

    Attributes:
        channel_ids (list of uuid|string): Gets or sets the channels to return
            guide information for.
        user_id (uuid|string): Gets or sets optional. Filter by user id.
        min_start_date (datetime): Gets or sets the minimum premiere start
            date.  Optional.
        has_aired (bool): Gets or sets filter by programs that have completed
            airing, or not.  Optional.
        is_airing (bool): Gets or sets filter by programs that are currently
            airing, or not.  Optional.
        max_start_date (datetime): Gets or sets the maximum premiere start
            date.  Optional.
        min_end_date (datetime): Gets or sets the minimum premiere end date.
            Optional.
        max_end_date (datetime): Gets or sets the maximum premiere end date.
            Optional.
        is_movie (bool): Gets or sets filter for movies.  Optional.
        is_series (bool): Gets or sets filter for series.  Optional.
        is_news (bool): Gets or sets filter for news.  Optional.
        is_kids (bool): Gets or sets filter for kids.  Optional.
        is_sports (bool): Gets or sets filter for sports.  Optional.
        start_index (int): Gets or sets the record index to start at. All
            items with a lower index will be dropped from the results.
            Optional.
        limit (int): Gets or sets the maximum number of records to return.
            Optional.
        sort_by (list of string): Gets or sets specify one or more sort
            orders, comma delimited. Options: Name, StartDate.  Optional.
        sort_order (list of SortOrderEnum): Gets or sets sort Order -
            Ascending,Descending.
        genres (list of string): Gets or sets the genres to return guide
            information for.
        genre_ids (list of uuid|string): Gets or sets the genre ids to return
            guide information for.
        enable_images (bool): Gets or sets include image information in
            output.  Optional.
        enable_total_record_count (bool): Gets or sets a value indicating
            whether retrieve total record count.
        image_type_limit (int): Gets or sets the max number of images to
            return, per image type.  Optional.
        enable_image_types (list of ImageTypeEnum): Gets or sets the image
            types to include in the output.  Optional.
        enable_user_data (bool): Gets or sets include user data.  Optional.
        series_timer_id (string): Gets or sets filter by series timer id.
            Optional.
        library_series_id (uuid|string): Gets or sets filter by library series
            id.  Optional.
        fields (list of ItemFieldsEnum): Gets or sets specify additional
            fields of information to return in the output. This allows
            multiple, comma delimited. Options: Budget, Chapters, DateCreated,
            Genres, HomePageUrl, IndexOptions, MediaStreams, Overview,
            ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio,
            Revenue, SortName, Studios, Taglines.  Optional.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "channel_ids": "ChannelIds",
        "user_id": "UserId",
        "min_start_date": "MinStartDate",
        "has_aired": "HasAired",
        "is_airing": "IsAiring",
        "max_start_date": "MaxStartDate",
        "min_end_date": "MinEndDate",
        "max_end_date": "MaxEndDate",
        "is_movie": "IsMovie",
        "is_series": "IsSeries",
        "is_news": "IsNews",
        "is_kids": "IsKids",
        "is_sports": "IsSports",
        "start_index": "StartIndex",
        "limit": "Limit",
        "sort_by": "SortBy",
        "sort_order": "SortOrder",
        "genres": "Genres",
        "genre_ids": "GenreIds",
        "enable_images": "EnableImages",
        "enable_total_record_count": "EnableTotalRecordCount",
        "image_type_limit": "ImageTypeLimit",
        "enable_image_types": "EnableImageTypes",
        "enable_user_data": "EnableUserData",
        "series_timer_id": "SeriesTimerId",
        "library_series_id": "LibrarySeriesId",
        "fields": "Fields",
    }

    _optionals = [
        "channel_ids",
        "user_id",
        "min_start_date",
        "has_aired",
        "is_airing",
        "max_start_date",
        "min_end_date",
        "max_end_date",
        "is_movie",
        "is_series",
        "is_news",
        "is_kids",
        "is_sports",
        "start_index",
        "limit",
        "sort_by",
        "sort_order",
        "genres",
        "genre_ids",
        "enable_images",
        "enable_total_record_count",
        "image_type_limit",
        "enable_image_types",
        "enable_user_data",
        "series_timer_id",
        "library_series_id",
        "fields",
    ]

    _nullables = [
        "min_start_date",
        "has_aired",
        "is_airing",
        "max_start_date",
        "min_end_date",
        "max_end_date",
        "is_movie",
        "is_series",
        "is_news",
        "is_kids",
        "is_sports",
        "start_index",
        "limit",
        "enable_images",
        "image_type_limit",
        "enable_user_data",
        "series_timer_id",
    ]

    def __init__(
        self,
        channel_ids=APIHelper.SKIP,
        user_id=APIHelper.SKIP,
        min_start_date=APIHelper.SKIP,
        has_aired=APIHelper.SKIP,
        is_airing=APIHelper.SKIP,
        max_start_date=APIHelper.SKIP,
        min_end_date=APIHelper.SKIP,
        max_end_date=APIHelper.SKIP,
        is_movie=APIHelper.SKIP,
        is_series=APIHelper.SKIP,
        is_news=APIHelper.SKIP,
        is_kids=APIHelper.SKIP,
        is_sports=APIHelper.SKIP,
        start_index=APIHelper.SKIP,
        limit=APIHelper.SKIP,
        sort_by=APIHelper.SKIP,
        sort_order=APIHelper.SKIP,
        genres=APIHelper.SKIP,
        genre_ids=APIHelper.SKIP,
        enable_images=APIHelper.SKIP,
        enable_total_record_count=APIHelper.SKIP,
        image_type_limit=APIHelper.SKIP,
        enable_image_types=APIHelper.SKIP,
        enable_user_data=APIHelper.SKIP,
        series_timer_id=APIHelper.SKIP,
        library_series_id=APIHelper.SKIP,
        fields=APIHelper.SKIP,
    ):
        """Constructor for the GetProgramsDto class"""

        # Initialize members of the class
        if channel_ids is not APIHelper.SKIP:
            self.channel_ids = channel_ids
        if user_id is not APIHelper.SKIP:
            self.user_id = user_id
        if min_start_date is not APIHelper.SKIP:
            self.min_start_date = (
                APIHelper.RFC3339DateTime(min_start_date) if min_start_date else None
            )
        if has_aired is not APIHelper.SKIP:
            self.has_aired = has_aired
        if is_airing is not APIHelper.SKIP:
            self.is_airing = is_airing
        if max_start_date is not APIHelper.SKIP:
            self.max_start_date = (
                APIHelper.RFC3339DateTime(max_start_date) if max_start_date else None
            )
        if min_end_date is not APIHelper.SKIP:
            self.min_end_date = (
                APIHelper.RFC3339DateTime(min_end_date) if min_end_date else None
            )
        if max_end_date is not APIHelper.SKIP:
            self.max_end_date = (
                APIHelper.RFC3339DateTime(max_end_date) if max_end_date else None
            )
        if is_movie is not APIHelper.SKIP:
            self.is_movie = is_movie
        if is_series is not APIHelper.SKIP:
            self.is_series = is_series
        if is_news is not APIHelper.SKIP:
            self.is_news = is_news
        if is_kids is not APIHelper.SKIP:
            self.is_kids = is_kids
        if is_sports is not APIHelper.SKIP:
            self.is_sports = is_sports
        if start_index is not APIHelper.SKIP:
            self.start_index = start_index
        if limit is not APIHelper.SKIP:
            self.limit = limit
        if sort_by is not APIHelper.SKIP:
            self.sort_by = sort_by
        if sort_order is not APIHelper.SKIP:
            self.sort_order = sort_order
        if genres is not APIHelper.SKIP:
            self.genres = genres
        if genre_ids is not APIHelper.SKIP:
            self.genre_ids = genre_ids
        if enable_images is not APIHelper.SKIP:
            self.enable_images = enable_images
        if enable_total_record_count is not APIHelper.SKIP:
            self.enable_total_record_count = enable_total_record_count
        if image_type_limit is not APIHelper.SKIP:
            self.image_type_limit = image_type_limit
        if enable_image_types is not APIHelper.SKIP:
            self.enable_image_types = enable_image_types
        if enable_user_data is not APIHelper.SKIP:
            self.enable_user_data = enable_user_data
        if series_timer_id is not APIHelper.SKIP:
            self.series_timer_id = series_timer_id
        if library_series_id is not APIHelper.SKIP:
            self.library_series_id = library_series_id
        if fields is not APIHelper.SKIP:
            self.fields = fields

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

        channel_ids = (
            dictionary.get("ChannelIds")
            if dictionary.get("ChannelIds")
            else APIHelper.SKIP
        )
        user_id = (
            dictionary.get("UserId") if dictionary.get("UserId") else APIHelper.SKIP
        )
        if "MinStartDate" in dictionary.keys():
            min_start_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("MinStartDate")
                ).datetime
                if dictionary.get("MinStartDate")
                else None
            )
        else:
            min_start_date = APIHelper.SKIP
        has_aired = (
            dictionary.get("HasAired")
            if "HasAired" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_airing = (
            dictionary.get("IsAiring")
            if "IsAiring" in dictionary.keys()
            else APIHelper.SKIP
        )
        if "MaxStartDate" in dictionary.keys():
            max_start_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("MaxStartDate")
                ).datetime
                if dictionary.get("MaxStartDate")
                else None
            )
        else:
            max_start_date = APIHelper.SKIP
        if "MinEndDate" in dictionary.keys():
            min_end_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("MinEndDate")
                ).datetime
                if dictionary.get("MinEndDate")
                else None
            )
        else:
            min_end_date = APIHelper.SKIP
        if "MaxEndDate" in dictionary.keys():
            max_end_date = (
                APIHelper.RFC3339DateTime.from_value(
                    dictionary.get("MaxEndDate")
                ).datetime
                if dictionary.get("MaxEndDate")
                else None
            )
        else:
            max_end_date = APIHelper.SKIP
        is_movie = (
            dictionary.get("IsMovie")
            if "IsMovie" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_series = (
            dictionary.get("IsSeries")
            if "IsSeries" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_news = (
            dictionary.get("IsNews")
            if "IsNews" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_kids = (
            dictionary.get("IsKids")
            if "IsKids" in dictionary.keys()
            else APIHelper.SKIP
        )
        is_sports = (
            dictionary.get("IsSports")
            if "IsSports" in dictionary.keys()
            else APIHelper.SKIP
        )
        start_index = (
            dictionary.get("StartIndex")
            if "StartIndex" in dictionary.keys()
            else APIHelper.SKIP
        )
        limit = (
            dictionary.get("Limit") if "Limit" in dictionary.keys() else APIHelper.SKIP
        )
        sort_by = (
            dictionary.get("SortBy") if dictionary.get("SortBy") else APIHelper.SKIP
        )
        sort_order = (
            dictionary.get("SortOrder")
            if dictionary.get("SortOrder")
            else APIHelper.SKIP
        )
        genres = (
            dictionary.get("Genres") if dictionary.get("Genres") else APIHelper.SKIP
        )
        genre_ids = (
            dictionary.get("GenreIds") if dictionary.get("GenreIds") else APIHelper.SKIP
        )
        enable_images = (
            dictionary.get("EnableImages")
            if "EnableImages" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_total_record_count = (
            dictionary.get("EnableTotalRecordCount")
            if "EnableTotalRecordCount" in dictionary.keys()
            else APIHelper.SKIP
        )
        image_type_limit = (
            dictionary.get("ImageTypeLimit")
            if "ImageTypeLimit" in dictionary.keys()
            else APIHelper.SKIP
        )
        enable_image_types = (
            dictionary.get("EnableImageTypes")
            if dictionary.get("EnableImageTypes")
            else APIHelper.SKIP
        )
        enable_user_data = (
            dictionary.get("EnableUserData")
            if "EnableUserData" in dictionary.keys()
            else APIHelper.SKIP
        )
        series_timer_id = (
            dictionary.get("SeriesTimerId")
            if "SeriesTimerId" in dictionary.keys()
            else APIHelper.SKIP
        )
        library_series_id = (
            dictionary.get("LibrarySeriesId")
            if dictionary.get("LibrarySeriesId")
            else APIHelper.SKIP
        )
        fields = (
            dictionary.get("Fields") if dictionary.get("Fields") else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(
            channel_ids,
            user_id,
            min_start_date,
            has_aired,
            is_airing,
            max_start_date,
            min_end_date,
            max_end_date,
            is_movie,
            is_series,
            is_news,
            is_kids,
            is_sports,
            start_index,
            limit,
            sort_by,
            sort_order,
            genres,
            genre_ids,
            enable_images,
            enable_total_record_count,
            image_type_limit,
            enable_image_types,
            enable_user_data,
            series_timer_id,
            library_series_id,
            fields,
        )

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        channel_ids = XmlUtilities.list_from_xml_element(root, "ChannelIds", str)
        user_id = XmlUtilities.value_from_xml_element(root.find("UserId"), str)
        min_start_date = XmlUtilities.value_from_xml_element(
            root.find("MinStartDate"), APIHelper.RFC3339DateTime
        )
        has_aired = XmlUtilities.value_from_xml_element(root.find("HasAired"), bool)
        is_airing = XmlUtilities.value_from_xml_element(root.find("IsAiring"), bool)
        max_start_date = XmlUtilities.value_from_xml_element(
            root.find("MaxStartDate"), APIHelper.RFC3339DateTime
        )
        min_end_date = XmlUtilities.value_from_xml_element(
            root.find("MinEndDate"), APIHelper.RFC3339DateTime
        )
        max_end_date = XmlUtilities.value_from_xml_element(
            root.find("MaxEndDate"), APIHelper.RFC3339DateTime
        )
        is_movie = XmlUtilities.value_from_xml_element(root.find("IsMovie"), bool)
        is_series = XmlUtilities.value_from_xml_element(root.find("IsSeries"), bool)
        is_news = XmlUtilities.value_from_xml_element(root.find("IsNews"), bool)
        is_kids = XmlUtilities.value_from_xml_element(root.find("IsKids"), bool)
        is_sports = XmlUtilities.value_from_xml_element(root.find("IsSports"), bool)
        start_index = XmlUtilities.value_from_xml_element(root.find("StartIndex"), int)
        limit = XmlUtilities.value_from_xml_element(root.find("Limit"), int)
        sort_by = XmlUtilities.list_from_xml_element(root, "SortBy", str)
        sort_order = XmlUtilities.list_from_xml_element(root, "SortOrder", str)
        genres = XmlUtilities.list_from_xml_element(root, "Genres", str)
        genre_ids = XmlUtilities.list_from_xml_element(root, "GenreIds", str)
        enable_images = XmlUtilities.value_from_xml_element(
            root.find("EnableImages"), bool
        )
        enable_total_record_count = XmlUtilities.value_from_xml_element(
            root.find("EnableTotalRecordCount"), bool
        )
        image_type_limit = XmlUtilities.value_from_xml_element(
            root.find("ImageTypeLimit"), int
        )
        enable_image_types = XmlUtilities.list_from_xml_element(
            root, "EnableImageTypes", str
        )
        enable_user_data = XmlUtilities.value_from_xml_element(
            root.find("EnableUserData"), bool
        )
        series_timer_id = XmlUtilities.value_from_xml_element(
            root.find("SeriesTimerId"), str
        )
        library_series_id = XmlUtilities.value_from_xml_element(
            root.find("LibrarySeriesId"), str
        )
        fields = XmlUtilities.list_from_xml_element(root, "Fields", str)

        return cls(
            channel_ids,
            user_id,
            min_start_date,
            has_aired,
            is_airing,
            max_start_date,
            min_end_date,
            max_end_date,
            is_movie,
            is_series,
            is_news,
            is_kids,
            is_sports,
            start_index,
            limit,
            sort_by,
            sort_order,
            genres,
            genre_ids,
            enable_images,
            enable_total_record_count,
            image_type_limit,
            enable_image_types,
            enable_user_data,
            series_timer_id,
            library_series_id,
            fields,
        )

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_list_as_subelement(root, self.channel_ids, "ChannelIds")
        XmlUtilities.add_as_subelement(root, self.user_id, "UserId")
        XmlUtilities.add_as_subelement(root, self.min_start_date, "MinStartDate")
        XmlUtilities.add_as_subelement(root, self.has_aired, "HasAired")
        XmlUtilities.add_as_subelement(root, self.is_airing, "IsAiring")
        XmlUtilities.add_as_subelement(root, self.max_start_date, "MaxStartDate")
        XmlUtilities.add_as_subelement(root, self.min_end_date, "MinEndDate")
        XmlUtilities.add_as_subelement(root, self.max_end_date, "MaxEndDate")
        XmlUtilities.add_as_subelement(root, self.is_movie, "IsMovie")
        XmlUtilities.add_as_subelement(root, self.is_series, "IsSeries")
        XmlUtilities.add_as_subelement(root, self.is_news, "IsNews")
        XmlUtilities.add_as_subelement(root, self.is_kids, "IsKids")
        XmlUtilities.add_as_subelement(root, self.is_sports, "IsSports")
        XmlUtilities.add_as_subelement(root, self.start_index, "StartIndex")
        XmlUtilities.add_as_subelement(root, self.limit, "Limit")
        XmlUtilities.add_list_as_subelement(root, self.sort_by, "SortBy")
        XmlUtilities.add_list_as_subelement(root, self.sort_order, "SortOrder")
        XmlUtilities.add_list_as_subelement(root, self.genres, "Genres")
        XmlUtilities.add_list_as_subelement(root, self.genre_ids, "GenreIds")
        XmlUtilities.add_as_subelement(root, self.enable_images, "EnableImages")
        XmlUtilities.add_as_subelement(
            root, self.enable_total_record_count, "EnableTotalRecordCount"
        )
        XmlUtilities.add_as_subelement(root, self.image_type_limit, "ImageTypeLimit")
        XmlUtilities.add_list_as_subelement(
            root, self.enable_image_types, "EnableImageTypes"
        )
        XmlUtilities.add_as_subelement(root, self.enable_user_data, "EnableUserData")
        XmlUtilities.add_as_subelement(root, self.series_timer_id, "SeriesTimerId")
        XmlUtilities.add_as_subelement(root, self.library_series_id, "LibrarySeriesId")
        XmlUtilities.add_list_as_subelement(root, self.fields, "Fields")
