

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
