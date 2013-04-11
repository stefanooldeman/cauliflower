from cauliflower.domain.abstract import Mapper
import cauliflower.domain.storage as storage


class PickleMapper(Mapper):

    def __init__(self):
        self.storage = storage.PickleStorage()

    def save(self, entity):
        print("saved " + entity.pkid)
        #TODO fix PickleStorage
        #data = self.storage.load(entity.pkid)
        #if data is False:
        #    self.storage.create(entity.pkid)
        #self.save(entity)
