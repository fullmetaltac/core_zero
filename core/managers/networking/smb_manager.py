from smb.SMBConnection import SMBConnection

from core import ParamError


class SmbManager:
    def __init__(self):
        self.port = 445

        self.conn = None
        self.host = None
        self.user = None
        self.password = None
        self.service_name = None

    def set_port(self, port: int):
        self.port = port
        return self

    def set_host(self, host: str):
        self.host = host
        return self

    def set_user(self, user: str):
        self.user = user
        return self

    def set_pass(self, password: str):
        self.password = password
        return self

    def set_service_name(self, service_name: str):
        self.service_name = service_name
        return self

    def connect(self):
        self.conn = SMBConnection(self.user, self.password, "", "", use_ntlm_v2=True)
        return self.conn.connect(self.host, self.port)

    def __check_required_parameters(self):
        condition = self.conn is not None and self.host is not None \
                    and self.user is not None and self.password is not None and self.service_name is not None
        if condition:
            return True
        else:
            raise ParamError('set_host', 'set_user', 'set_pass', 'set_service_name', 'connect')

    def reset(self):
        self.conn = None

    def download(self, smb_path: str, file_path: str):
        """
        :param service_name: the name of the shared folder for the *path*
        :param smb_path: Path of the file on the remote server.
        :param file_path: The path of file to upload.
        """
        self.__check_required_parameters()
        with open(file_path, 'wb') as file:
            self.conn.retrieveFile(self.service_name, smb_path, file)

    def upload(self, smb_path: str, file_path: str):
        """
        :param service_name: the name of the shared folder for the *path*
        :param smb_path: Path of the file on the remote server.
        :param file_path: The path of file to upload.
        """
        self.__check_required_parameters()
        with open(file_path, 'rb') as file:
            self.conn.storeFile(self.service_name, smb_path, file)
