

class Entity(object):
    """
    used in MapperAbsrtact for strictness
    """

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

    def iterator(self):
        return iter([])
