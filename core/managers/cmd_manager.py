from subprocess import PIPE, Popen


class CmdManager:
    @staticmethod
    def execute(cmd: str, wait=True):
        process = Popen(cmd, shell=True, stdout=PIPE)
        if wait:
            process.wait()
        return process.stdout.read().decode('utf-8')
