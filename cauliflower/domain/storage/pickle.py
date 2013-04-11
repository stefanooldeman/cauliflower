import pickle

"""
Patterns that fit this type of class Gateway, Mapper or Adapter.
But a Gataway just wraps the exising interface provided by a third-party api
"""


class PickleStorage(object):

    def save(self, data):
        pickle.dump(data, self._file)

    def load(self, filename):
        data = pickle.load(self.basepath + filename)
        return data

    def delete(self, data):
        pass

    def create(self, filename):
        pass
        #self._file = self.basepath + filename
