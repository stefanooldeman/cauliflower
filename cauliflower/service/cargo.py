import os
import mimetypes

from cauliflower.domain.mappers.pattern import PatternXMLMapper
import cauliflower.errors as errors


class CargoService(object):

    def __init__(self, basepath):
        if basepath[-1] is not os.sep:
            # if last char (-1) is not a slash (/) append it
            basepath += os.sep

        self._file_mapper = None
        self.upload_dir = basepath
        self.patterns = []

    def do_import(self, filepath):
        filepath = self.upload_dir + filepath
        if self._checkfile(filepath) is False:
            raise errors.ValidationError('filetype is not supported')

        # set the filepath to the mapper, and it will take care
        mapper = self.file_mapper
        mapper.filepath = filepath  # Hacky?
        for row in mapper.iterator():
            self.patterns.append(mapper.toEntity(row))

        return True

    def do_export(self, desitnation):
        raise NotImplemented

    def _checkfile(self, filepath):
        open(filepath, 'r')
        (filetype, _) = mimetypes.guess_type(filepath)
        return bool(filetype.split('/')[1] in ['xml', 'json'])

    @property
    def size(self):
        return len(self.patterns)

    @property
    def file_mapper(self):
        # lazy loading
        # gives posibility to overwrite (Dependency injection)
        if self._file_mapper is None:
            self._file_mapper = PatternXMLMapper()
        return self._file_mapper

    @file_mapper.setter
    def file_mapper(self, mapper):
        self._file_mapper = mapper
