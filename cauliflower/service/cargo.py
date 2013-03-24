import xml.sax
import json
import os

from cauliflower.domain.mappers.pattern import PatternXMLMapper
import cauliflower.errors as errors


class CargoService(object):

    def __init__(self, basepath):
        self.upload_dir = basepath

    def do_import(self, filepath):
        if self._checkfile(filepath):
            raise errors.ValidationError('file not supported')
        mapper = PatternXMLMapper()
        mapper.toEntity(row)

    def do_export(self, desitnation):
        raise NotImplemented

    def _checkfile(self, filepath):
        supported = ['xml', 'json']
        return True
