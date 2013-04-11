import json
from cauliflower.domain.abstract import DataMapper, Entity
from .entity import Pattern

import xml.parsers.expat
from xml.dom.minidom import Node


class XMLMapper(DataMapper):

    def fromEntity(self, entity):
        xml = ""
        return xml

    def toEntity(self, node):
        pattern = Pattern()

        pattern.context = node.getAttributeNode('context').value
        pattern.name = self._text(node, 'name')
        pattern.problem = self._text(node, 'problem')
        pattern.solution = self._text(node, 'solution')
        pattern.consequences = self._text(node, 'consequences')
        pattern.image = self._text(node, 'diagram')
        return pattern

    # logic specific to get extract the textvalue from DOM element
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

    def iterator(self, doc):
        try:
            result = doc.getElementsByTagName('pattern')
        except xml.parsers.expat.ExpatError:
            result = []
        return result


class JSONMapper(DataMapper):

    def fromEntity(self, entity):
        data = {
            'name': entity.name,
            'problem': entity.problem,
            'solution': entity.solution,
            'diagram': entity.diagram
        }

        return json.dumps(data)

    def toEntity(self, data):
        data = json.loads(data)
        obj = Pattern()
        obj.name = data.get('name')
        obj.problem = data.get('problem')
        obj.solution = data.get('solution')
        obj.diagram = data.get('diagram')
        return obj

    def iterator(self, data=None):
        json.loads(data)
