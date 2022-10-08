# -*- coding: utf-8 -*-


import platform
from jellyfinapi.api_helper import APIHelper
from jellyfinapi.exceptions.api_exception import APIException


class BaseController(object):

    """All controllers inherit from this base class.

    Attributes:
        config (Configuration): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        auth_managers (dict): A dictionary which holds the instances of authentication managers.
        global_headers (dict): The global headers of the API which are sent with
            every request.

    """

    def global_headers(self):
        return {"user-agent": self.get_user_agent()}

    def __init__(self, config, auth_managers):
        self._config = config
        self._auth_managers = auth_managers
        self._http_call_back = config.http_call_back

    @property
    def config(self):
        return self._config

    @property
    def http_call_back(self):
        return self._http_call_back

    @property
    def auth_managers(self):
        return self._auth_managers

    def validate_parameters(self, **kwargs):
        """Validates required parameters of an endpoint.

        Args:
            kwargs (dict): A dictionary of the required parameters.

        """
        for name, value in kwargs.items():
            if value is None:
                raise ValueError("Required parameter {} cannot be None.".format(name))

    def execute_request(self, request, binary=False, name=None, to_retry=None):
        """Executes an HttpRequest.

        Args:
            request (HttpRequest): The HttpRequest to execute.
            binary (bool): A flag which should be set to True if
                a binary response is expected.
            to_retry (bool): whether to retry on a particular request

        Returns:
            HttpResponse: The HttpResponse received.

        """
        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back is not None:
            self.logger.info(
                "Calling the on_before_request method of http_call_back for {}.".format(
                    name
                )
            )
            self.http_call_back.on_before_request(request)

        # Add global headers to request
        self.logger.info(
            "Merging global headers with endpoint headers for {}.".format(name)
        )
        prepared_headers = {key: str(value) for key, value in request.headers.items()}
        request.headers = {**self.global_headers(), **prepared_headers}

        # Invoke the API call to fetch the response.
        self.logger.debug("Raw request for {} is: {}".format(name, vars(request)))
        func = (
            self.config.http_client.execute_as_binary
            if binary
            else self.config.http_client.execute_as_string
        )
        response = func(request, to_retry=to_retry)
        self.logger.debug("Raw response for {} is: {}".format(name, vars(response)))

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back is not None:
            self.logger.info(
                "Calling on_after_response method of http_call_back for {}.".format(
                    name
                )
            )
            self.http_call_back.on_after_response(response)

        return response

    def validate_response(self, response):
        """Validates an HTTP response by checking for global errors.

        Args:
            response (HttpResponse): The HttpResponse of the API call.

        """
        if (response.status_code < 200) or (
            response.status_code > 208
        ):  # [200,208] = HTTP OK
            raise APIException("HTTP response not OK.", response)

    def get_user_agent(self):
        user_agent = "APIMATIC 3.0"
        parameters = {}

        agent = APIHelper.append_url_with_template_parameters(user_agent, parameters)
        return agent.replace("  ", " ")

    def apply_auth_schemes(self, request, *auth_options):
        auth_error_message = []
        # traverse all options for OR auth
        for option in auth_options:
            # split the option for AND auths
            schemes = option.split()
            # check if all AND auth credentials exist in auth managers
            if all(
                scheme in self.auth_managers
                and self.auth_managers[scheme].validate_arguments()
                for scheme in schemes
            ):
                # apply each auth scheme in AND case to request then break
                for scheme in schemes:
                    self.auth_managers[scheme].apply(request)
                break
            else:
                for scheme in schemes:
                    if scheme in self.auth_managers:
                        auth_error_message.append(
                            self.auth_managers[scheme].error_message()
                        )
            # if the auth credentials for this auth option are missing then move to next
            ## or if this is the last/only option then throw exception with reasonable message
            if option is auth_options[-1]:
                raise PermissionError(
                    "Required authentication is missing for: "
                    + " and ".join(auth_error_message)
                )
