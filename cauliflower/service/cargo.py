import os
import mimetypes

import cauliflower.domain.pattern as pattern
import cauliflower.errors as errors


class CargoService(object):

    def __init__(self, basepath):
        if basepath[-1] is not os.sep:
            # if last char (-1) is not a slash (/) append it
            basepath += os.sep

        self._mapper = None
        self.upload_dir = basepath
        self.patterns = []

    def do_import(self, filename):
        self.filepath = self.upload_dir + filename
        self._checkfile(self.filepath)

        if self.filetype == 'xml':
            import xml.dom.minidom
            data = xml.dom.minidom.parse(self.filepath)

        mapper = self.pattern_mapper
        for row in mapper.iterator(data):
            entity = mapper.toEntity(row)
            mapper.save(entity)
            self.patterns.append(entity)

        return True

    def do_export(self, desitnation):
        raise NotImplemented

    def _checkfile(self, filepath):
        try:
            open(filepath, 'r')
        except IOError:
            print('404, file {} not found').format(filepath)
            raise

        (mime, _) = mimetypes.guess_type(filepath)
        self.filetype = mime.split('/')[1]
        if self.filetype not in ['xml', 'json']:
            raise errors.ValidationError('filetype is not supported')

    @property
    def size(self):
        return len(self.patterns)

    @property
    def pattern_mapper(self):
        # lazy loading
        # gives posibility to overwrite (Dependency injection)
        if self._mapper is not None:
            return self._mapper

        mapper = pattern.PickleMapper()

        if self.filetype == 'xml':
            dataMapper = pattern.XMLMapper()

        if self.filetype == 'json':
            dataMapper = pattern.JSONMapper()

        #TODO maybe a Factory pattern would be nice..
        mapper.dataMapper = dataMapper
        self._mapper = mapper
        return self._mapper

    @pattern_mapper.setter
    def pattern_mapper(self, mapper):
        self._file_mapper = mapper
