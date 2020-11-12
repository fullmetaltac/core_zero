from serial import Serial

from core import ParamError


class ComManager:

    def __init__(self):
        self.com = None
        self.port = None
        self.baud_rate = None

    def set_port(self, port: str):
        self.port = port
        return self

    def set_baud_rate(self, baud_rate: int):
        self.port = baud_rate
        return self

    def build(self):
        self.com = Serial(port=self.port, baudrate=self.baud_rate)
        return self.com

    def reset(self):
        self.com = None

    def __check_required_parameters(self):
        if self.port is not None and self.baud_rate is not None:
            return True
        else:
            raise ParamError('set_port', 'set_baud_rate', 'build')

    def read(self):
        self.__check_required_parameters()
        return self.com.read(self.com.inWaiting()).decode()

    def write(self, msg: str):
        self.__check_required_parameters()
        self.com.write(f'{msg}\n'.encode())

    def close(self):
        self.__check_required_parameters()
        self.com.close()

    def execute(self, msg: str):
        self.__check_required_parameters()
        self.write(msg)
        return self.read()
