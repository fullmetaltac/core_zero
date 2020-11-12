class DiskWin:

    def mount(self, *args, **kwargs):
        raise NotImplementedError()

    def unmount(self, *args, **kwargs):
        raise NotImplementedError()

    def eject(self, *args, **kwargs):
        raise NotImplementedError()

    def format(self, *args, **kwargs):
        raise NotImplementedError()

    def partition(self, *args, **kwargs):
        raise NotImplementedError()
