from sys import platform

from core.managers.disk.disk_linux import DiskLinux
from core.managers.disk.disk_mac import DiskMac
from core.managers.disk.disk_win import DiskWin


class DiskFactory:

    @staticmethod
    def disk_manager():
        if platform == 'win32':
            return DiskWin()
        elif platform == 'darwin':
            return DiskMac()
        elif platform == 'linux':
            return DiskLinux()
        else:
            raise ValueError(platform)
