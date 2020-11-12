class ParamError(Exception):

    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return repr(f'Some of the required parameter is missing. Use {",".join(self.args)} for proper usage.')
