# -*- coding: utf-8 -*-


from jellyfinapi.api_helper import APIHelper
import jellyfinapi.exceptions.api_exception


class ProblemDetailsException(jellyfinapi.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the ProblemDetailsException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(ProblemDetailsException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.mtype = (
            dictionary.get("type") if "type" in dictionary.keys() else APIHelper.SKIP
        )
        self.title = (
            dictionary.get("title") if "title" in dictionary.keys() else APIHelper.SKIP
        )
        self.status = (
            dictionary.get("status")
            if "status" in dictionary.keys()
            else APIHelper.SKIP
        )
        self.detail = (
            dictionary.get("detail")
            if "detail" in dictionary.keys()
            else APIHelper.SKIP
        )
        self.instance = (
            dictionary.get("instance")
            if "instance" in dictionary.keys()
            else APIHelper.SKIP
        )
