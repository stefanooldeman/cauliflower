from cauliflower.domain.mappers.abstract import DataMapper
from cauliflower.domain.models import Pattern
import json

class PatternXMLMapper(DataMapper):

    def fromEntity(self, entity):
        super(PatternXMLMapper, self).fromEntity(entity)
        xml = ""
        return xml

    def toEntity(self, data):
        super(PatternXMLMapper, self).toEntity(data)
        obj = Pattern()
        return obj


class PatternJSONMapper(DataMapper):


    def fromEntity(self, entity):
        super(PatternJSONMapper, self).fromEntity(entity)
        data = {
            'name': entity.name,
            'problem': entity.problem,
            'solution': entity.solution,
            'diagram': entity.diagram
        }

        return json.dumps(data)




    def toEntity(self, data):
        super(PatternJSONMapper, self).toEntity(data)
        data = json.loads('{"name": "mark", "problem": "foobar", "solution": "foobartwo", "diagram": "foobarthree"}')
        obj = Pattern()
        obj.name = data.get('name')
        obj.problem = data.get('problem')
        obj.solution = data.get('solution')
        obj.diagram = data.get('diagram')
        return obj

