from ftplib import FTP

from core import ParamError


class FtpManager:
    def __init__(self):
        self.ftp_url = None
        self.ftp_user = None
        self.ftp_pass = None

    def set_ftp_url(self, ftp_url: str):
        self.ftp_url = ftp_url
        return self

    def set_ftp_user(self, ftp_user: str):
        self.ftp_user = ftp_user
        return self

    def set_ftp_pass(self, ftp_pass: str):
        self.ftp_pass = ftp_pass
        return self

    def __check_required_parameters(self):
        if self.ftp_url is not None and self.ftp_user is not None and self.ftp_pass is not None:
            return True
        else:
            raise ParamError('set_ftp_url', 'set_ftp_user', 'set_ftp_pass')

    def file_download(self, remote_file_url: str, local_file_path: str):
        '''
        :param remote_file_url: File location on the ftp server that will be downloaded
        :param local_file_path: Location on local filesystem where file will be stored
        :return: None
        '''
        self.__check_required_parameters()
        with FTP(self.ftp_url, self.ftp_user, self.ftp_pass) as ftp, open(local_file_path, "wb") as file:
            ftp.retrbinary(f"RETR {remote_file_url}", file.write)

    def file_send(self, local_file_path: str, destination_url: str):
        '''
        :param local_file_path: Location of the local file that will be downloaded to the ftp server
        :param destination_url: File location on the ftp where it will be uploaded
        :return: None
        '''
        self.__check_required_parameters()
        with FTP(self.ftp_url, self.ftp_user, self.ftp_pass) as ftp, open(local_file_path, 'rb') as file:
            ftp.storbinary(f'STOR {destination_url}', file)
