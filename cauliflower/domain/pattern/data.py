from cauliflower.domain.abstract import DataMapper, Entity
from .entity import Pattern

import xml.dom.minidom
import xml.parsers.expat
from xml.dom.minidom import Node


class XMLMapper(DataMapper):

    def fromEntity(self, entity):
        super(XMLMapper, self).fromEntity(entity)
        xml = ""
        return xml

    def toEntity(self, node):
        super(XMLMapper, self).toEntity(node)
        pattern = Pattern()

        pattern.context = node.getAttributeNode('context').value
        pattern.name = self._text(node, 'name')
        pattern.problem = self._text(node, 'problem')
        pattern.solution = self._text(node, 'solution')
        pattern.consequences = self._text(node, 'consequences')
        pattern.image = self._text(node, 'diagram')
        return pattern

    def _text(self, node, tagname=None):
        if tagname:
            try:
                node = node.getElementsByTagName(tagname)[0]
                nodelist = node.childNodes
            except IndexError:
                nodelist = []

        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return None if len(rc) == 0 else ''.join(rc)

    def iterator(self):
        try:
            doc = xml.dom.minidom.parse(self.filepath)
            result = doc.getElementsByTagName('pattern')
        except xml.parsers.expat.ExpatError:
            result = []
        return result


class JSONMapper(DataMapper):

    def fromEntity(self, entity):
        super(JSONMapper, self).fromEntity(entity)
        xml = ""
        return xml

    def toEntity(self, data):
        super(JSONMapper, self).toEntity(data)
        obj = Pattern()
        return obj
