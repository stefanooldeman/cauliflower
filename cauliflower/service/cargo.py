import xml.sax
import json
import os


class CargoService:

    def do_import(self, filepath):
        supported = ['xml', 'json']
        if self._checkfile(filepath):
            print 'ok here we go'
        else:
            print 'not a supported file'

    def do_export(self, desitnation):
        raise NotImplemented

    def _checkfile(self, filepath):
        return True
