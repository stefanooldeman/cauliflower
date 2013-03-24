import os
import mimetypes

from cauliflower.domain.mappers.pattern import PatternXMLMapper
import cauliflower.errors as errors


class CargoService(object):

    def __init__(self, basepath):
        if basepath[-1] is not os.sep:
            # if last char (-1) is not a slash (/) append it
            basepath += os.sep

        self.upload_dir = basepath

    def do_import(self, filepath):
        if self._checkfile(self.upload_dir + filepath) is False:
            raise errors.ValidationError('filetype is not supported')

        mapper = PatternXMLMapper()
        mapper.toEntity('')
        self._size = 0
        return True

    def do_export(self, desitnation):
        raise NotImplemented

    def _checkfile(self, filepath):
        open(filepath, 'r')
        (filetype, _) = mimetypes.guess_type(filepath)
        return bool(filetype.split('/')[1] in ['xml', 'json'])

    @property
    def size(self):
        return self._size
