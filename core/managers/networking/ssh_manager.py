from paramiko import RSAKey, SSHClient, AutoAddPolicy

from core import ParamError


class SshManager:

    def __init__(self):
        self.pem = None
        self.ipv4 = None
        self.user = None
        self.password = None
        self.ssh = SSHClient()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())

    def set_pem(self, pem_path: str):
        self.pem = RSAKey.from_private_key_file(pem_path)

    def set_ipv4(self, ipv4: str):
        self.ipv4 = ipv4

    def set_user(self, user: str):
        self.user = user

    def set_pass(self, password: str):
        self.password = password

    def connect(self):
        self.ssh.get_host_keys().clear()
        self.ssh.connect(self.ipv4, username=self.user, password=self.password, pkey=self.pem)

    def __check_required_parameters(self):
        if self.ipv4 is not None and self.user is not None and self.password is not None:
            return True
        else:
            raise ParamError('set_ipv4', 'set_user', 'set_pass', 'connect')

    def execute(self, command, close=True):
        self.__check_required_parameters()
        stdin, stdout, stderr = self.ssh.exec_command(command)
        if close:
            self.ssh.close()
        return stdout.read().decode('utf-8')
