import collections
import cauliflower.errors as errors

"""
Pattern: `Layer Supertype` is a simple idea. All you need is
a superclass for all the objects in a layer-for example, a Domain
Object superclass for all the domain objects in a Domain Model. Common
features, such as the storage and handling of Identity Fields, can go here.
All Data Mappers in the mapping layer can have a superclass that
relies on the faxt that all domain objects have a common superclass.
"""


class Entity(object):

    def __init__(self):
        # to prevent getting non existing variabels
        self.v = collections.defaultdict()


class DataMapper(object):

    def fromEntity(self, entity):
        """
        translate a entity object into a data specific representation
        """

    def toEntity(self, data):
        """
        translate raw data (specific representation) into a entity object
        """

    def iterator(self, data):
        return iter([])


class Mapper(object):

    def __init__(self):
        self.data = None

    # abstract methods
    def create(self, entity):
        raise NotImplemented

    def update(self, entity):
        raise NotImplemented

    def delete(self, entity):
        raise NotImplemented

    # proxy methods for DataMappers
    def populate(self, data):
        self.toEntity(data)

    def iterator(self, data):
        return self.dataMapper.iterator(data)

    def toEntity(self, data):
        return self.dataMapper.toEntity(data)

    def fromEntity(self, entity):
        if isinstance(entity, DataMapper) is False:
            msg = 'param entity not instance of DataMapper'
            raise errors.ValidationError(msg)
        return self.dataMapper.fromEntity(entity)

    @property
    def dataMapper(self):
        return self._data_mapper

    @dataMapper.setter
    def dataMapper(self, dataMapper):
        self._data_mapper = dataMapper
