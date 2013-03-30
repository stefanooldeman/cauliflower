import argparse
from cauliflower.service.cargo import CargoService


c = CargoService('/Users/mark/Desktop/')
c.do_import('foobar.json')


