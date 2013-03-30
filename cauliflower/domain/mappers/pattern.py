from cauliflower.domain.mappers.abstract import DataMapper
from cauliflower.domain.models import Pattern

import xml.dom.minidom
import xml.parsers.expat
from xml.dom.minidom import Node


class PatternXMLMapper(DataMapper):

    def fromEntity(self, entity):
        super(PatternXMLMapper, self).fromEntity(entity)
        xml = ""
        return xml

    def toEntity(self, data):
        super(PatternXMLMapper, self).toEntity(data)
        obj = Pattern()
        return obj

    def iterator(self):
        try:
            doc = xml.dom.minidom.parse(self.filepath)
            result = doc.getElementsByTagName('pattern')
        except xml.parsers.expat.ExpatError:
            result = []
        return result


class PatternJSONMapper(DataMapper):

    def fromEntity(self, entity):
        super(PatternJSONMapper, self).fromEntity(entity)
        xml = ""
        return xml

    def toEntity(self, data):
        super(PatternJSONMapper, self).toEntity(data)
        obj = Pattern()
        return obj
