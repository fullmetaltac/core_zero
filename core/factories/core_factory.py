from core.factories.disk_factory import DiskFactory as df
from core.managers.cmd_manager import CmdManager
from core.managers.com_manager import ComManager
from core.managers.file_manager import FileManager
from core.managers.networking.ftp_manager import FtpManager
from core.managers.networking.nfs_manager import NfsManager
from core.managers.networking.smb_manager import SmbManager
from core.managers.networking.ssh_manager import SshManager
from core.managers.perf_manager import PerfManager
from core.managers.string_manager import StringManager
from core.reporters.mail_reporter import MailReporter
from core.reporters.slack_reporter import SlackReporter
from core.reporters.xray_reporter import XRayReporter


class CoreFactory:

    def __init__(self):
        # managers
        self.com = ComManager()
        self.cmd = CmdManager()
        self.disk = df.disk_manager()
        self.hid = None  # requires additional installation in system

        # networking
        self.smb = SmbManager()
        self.nfs = NfsManager()
        self.ftp = FtpManager()
        self.ssh = SshManager()

        # reporters
        self.mail = MailReporter()
        self.xray = XRayReporter()
        self.slack = SlackReporter()

        # util
        self.file = FileManager()
        self.perf = PerfManager()
        self.string = StringManager()

    def set_hid_manager(self, manager):
        self.hid = manager
