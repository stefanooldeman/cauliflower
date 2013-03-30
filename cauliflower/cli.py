import argparse

from cauliflower.service.cargo import CargoService

c = CargoService('/media/uploads/')
c.do_import('foobar.xml')
