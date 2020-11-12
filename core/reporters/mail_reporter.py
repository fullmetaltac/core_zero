import smtplib
import ssl
from typing import List

from core import ParamError


class MailReporter:

    def __init__(self):
        self.service_port = None
        self.service_host = None
        self.service_user = None
        self.service_password = None

    def set_service_user(self, service_user: str):
        self.service_user = service_user
        return self

    def set_service_password(self, service_password: str):
        self.service_password = service_password
        return self

    def set_service_port(self, service_port: str):
        self.service_port = service_port
        return self

    def set_service_host(self, service_host: str):
        self.service_host = service_host
        return self

    def __check_required_parameters(self):
        condition = self.service_user is not None and self.service_password is not None \
                    and self.service_host is not None and self.service_port is not None
        if condition:
            return True
        else:
            raise ParamError('set_service_user', 'set_service_password', 'set_service_host', 'set_service_port')

    def send_email(self, recipients: List[str], content: str):
        self.__check_required_parameters()
        server = smtplib.SMTP(self.service_host, self.service_port)
        server.starttls(context=ssl.create_default_context())
        server.login(self.service_user, self.service_password)
        server.sendmail(self.service_user, recipients, content)
