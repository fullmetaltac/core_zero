from dataclasses import dataclass
from enum import Enum


# macOS
class Mac:
    class Scheme(Enum):
        GPT = 'GPT'
        MBR = 'MBR'
        NONE = ''

    class FsType(Enum):
        FREE = 'free'
        EXFAT = 'ExFAT'
        FAT32 = 'FAT32'
        HFS_PLUS = 'HFS+'
        JHFS_PLUS = 'JHFS+'


class SystemProfilerDataType(Enum):
    USB = "SPUSBDataType"
    NVM = "SPNVMeDataType"


class SystemProfilerKey(Enum):
    BSD_NAME = "bsd_name"
    SERIAL_NUM = "serial_num"
    MOUNT_POINT = "mount_point"
    DEVICE_SERIAL = "device_serial"


@dataclass
class PartitionData:
    id: str
    size: str
    fs_type: Mac.FsType


# Windows
class Win:
    class Scheme(Enum):
        pass

    class FsType(Enum):
        pass


# Linux
class Linux:
    class Scheme(Enum):
        pass

    class FsType(Enum):
        pass
