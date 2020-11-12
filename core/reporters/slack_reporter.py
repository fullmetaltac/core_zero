from requests import post

from core import ParamError


class SlackReporter:
    def __init__(self):
        self.web_hook = None

    def set_web_hook(self, url: str):
        self.web_hook = url
        return self

    def __check_required_parameters(self):
        if self.web_hook is not None:
            return True
        else:
            raise ParamError('set_web_hook')

    def print_to_slack(self, message):
        self.__check_required_parameters()
        post(self.web_hook, json={"text": message})
