import cauliflower.domain.storage as storage


class Mapper(object):

    def __init__(self):
        self.storage = storage.PickleStorage()

    def save(self):
        pass
