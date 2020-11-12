import json
from typing import List

from core.managers.cmd_manager import CmdManager as cmd
from core.managers.disk import Mac, PartitionData, SystemProfilerDataType, SystemProfilerKey
from core.util.json_util import json_search_by_key_val


class DiskMac:

    @staticmethod
    def disk_data(key: SystemProfilerKey, value: str, data_type: SystemProfilerDataType):
        """
        :param key: field for search e.g. serial_num
        :param value: value for search
        :param data_type: system profiler data type. For full list use 'system_profiler -listDataTypes'
        :return: disk data that stored in system_profiler
        """
        usb_data = cmd.execute(f'system_profiler {data_type.value} -json')
        return json_search_by_key_val(json.loads(usb_data), key.value, value)

    @staticmethod
    def format(bsd_name: str, name: str, fs_type: Mac.FsType, scheme: Mac.Scheme):
        cmd.execute(f'diskutil eraseDisk {fs_type.value} {name} {scheme.value} /dev/{bsd_name}')

    @staticmethod
    def partition(bsd_name: str, partition_data: List[PartitionData]):
        command = f'diskutil partitionDisk {bsd_name} '
        cmd.execute(command + ''.join([f'{p.fs_type.value} {p.id} {p.size} ' for p in partition_data]))

    @staticmethod
    def mount(bsd_name: str):
        cmd.execute(f'diskutil mountDisk /dev/{bsd_name}')

    @staticmethod
    def unmount(bsd_name: str):
        cmd.execute(f'diskutil unmountDisk /dev/{bsd_name}')

    @staticmethod
    def eject(bsd_name: str):
        cmd.execute(f'diskutil eject /dev/{bsd_name}')
