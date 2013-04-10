import collections


class Pattern(Entity):

    @property
    def name(self):
        return self.v.get('name')

    @name.setter
    def name(self, value):
        self.v['name'] = value

    @property
    def context(self):
        return self.v.get('context')

    @context.setter
    def context(self, value):
        self.v['context'] = value

    @property
    def problem(self):
        return self.v.get('problem')

    @problem.setter
    def problem(self, value):
        self.v['problem'] = value

    @property
    def solution(self):
        return self.v.get('solution')

    @solution.setter
    def solution(self, value):
        self.v['solution'] = value

    @property
    def image(self):
        return self.v.get('image')

    @image.setter
    def image(self, value):
        self.v['image'] = value
