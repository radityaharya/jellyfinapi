# -*- coding: utf-8 -*-


class CustomHeaderAuthentication:
    def __init__(self, x_emby_token):
        self._x_emby_token = x_emby_token

    def validate_arguments(self):
        if self._x_emby_token:
            return True
        return False

    def apply(self, http_request):
        """Add custom authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which
                authentication will be added.

        """
        http_request.add_header("X-Emby-Token", self._x_emby_token)

    def error_message(self):
        """Display error message on occurrence of authentication faliure
        in CustomHeaderAuthentication

        """
        return "CustomHeaderAuthentication: _x_emby_token is undefined."
