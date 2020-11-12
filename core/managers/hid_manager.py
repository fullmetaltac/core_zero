import hid

from core import ParamError


class HidManager:

    def __init__(self):
        self.device = None
        self.vendor_id = None
        self.product_id = None

    def set_vendor_id(self, vendor_id):
        self.vendor_id = vendor_id
        return self

    def set_product_id(self, product_id):
        self.product_id = product_id
        return self

    def build(self):
        self.device = hid.device()
        self.device.open(self.vendor_id, self.product_id)
        return self.device

    def reset(self):
        self.device = None

    def __check_required_parameters(self):
        if self.vendor_id is not None and self.product_id is not None:
            return True
        else:
            raise ParamError('set_vendor_id', 'set_product_id')

    def write(self, *args, **kwargs):
        self.device.write(*args, **kwargs)

    def read(self, *args, **kwargs):
        return self.read(*args, **kwargs)

    def close(self):
        self.device.close()
