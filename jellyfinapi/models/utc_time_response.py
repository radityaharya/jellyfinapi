# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
from jellyfinapi.utilities.xml_utilities import XmlUtilities


class UtcTimeResponse(object):

    """Implementation of the 'UtcTimeResponse' model.

    Class UtcTimeResponse.

    Attributes:
        request_reception_time (datetime): Gets the UTC time when request has
            been received.
        response_transmission_time (datetime): Gets the UTC time when response
            has been sent.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_reception_time": "RequestReceptionTime",
        "response_transmission_time": "ResponseTransmissionTime",
    }

    _optionals = [
        "request_reception_time",
        "response_transmission_time",
    ]

    def __init__(
        self,
        request_reception_time=APIHelper.SKIP,
        response_transmission_time=APIHelper.SKIP,
    ):
        """Constructor for the UtcTimeResponse class"""

        # Initialize members of the class
        if request_reception_time is not APIHelper.SKIP:
            self.request_reception_time = (
                APIHelper.RFC3339DateTime(request_reception_time)
                if request_reception_time
                else None
            )
        if response_transmission_time is not APIHelper.SKIP:
            self.response_transmission_time = (
                APIHelper.RFC3339DateTime(response_transmission_time)
                if response_transmission_time
                else None
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

        request_reception_time = (
            APIHelper.RFC3339DateTime.from_value(
                dictionary.get("RequestReceptionTime")
            ).datetime
            if dictionary.get("RequestReceptionTime")
            else APIHelper.SKIP
        )
        response_transmission_time = (
            APIHelper.RFC3339DateTime.from_value(
                dictionary.get("ResponseTransmissionTime")
            ).datetime
            if dictionary.get("ResponseTransmissionTime")
            else APIHelper.SKIP
        )
        # Return an object of this model
        return cls(request_reception_time, response_transmission_time)

    @classmethod
    def from_element(cls, root):
        """Initialize an instance of this class using an xml.etree.Element.

        Args:
            root (string): The root xml element.

        Returns:
            object: An instance of this class.

        """
        request_reception_time = XmlUtilities.value_from_xml_element(
            root.find("RequestReceptionTime"), APIHelper.RFC3339DateTime
        )
        response_transmission_time = XmlUtilities.value_from_xml_element(
            root.find("ResponseTransmissionTime"), APIHelper.RFC3339DateTime
        )

        return cls(request_reception_time, response_transmission_time)

    def to_xml_sub_element(self, root):
        """Convert this object to an instance of xml.etree.Element.

        Args:
            root (xml.etree.Element): The parent of this xml element.
        """
        XmlUtilities.add_as_subelement(
            root, self.request_reception_time, "RequestReceptionTime"
        )
        XmlUtilities.add_as_subelement(
            root, self.response_transmission_time, "ResponseTransmissionTime"
        )
