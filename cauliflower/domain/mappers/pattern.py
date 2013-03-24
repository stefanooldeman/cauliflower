from cauliflower.domain.mappers.abstract import DataMapper
from cauliflower.domain.models import Pattern


class PatternXMLMapper(DataMapper):

    def fromEntity(self, entity):
        super(PatternXMLMapper, self).fromEntity(entity)
        xml = ""
        return xml

    def toEntity(self, data):
        super(PatternXMLMapper, self).toEntity(data)
        obj = Pattern()
        return obj