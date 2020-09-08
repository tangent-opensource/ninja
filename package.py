# -*- coding: utf-8 -*-

name = 'ninja'

version = '1.10.1'

authors = [
    'philip.luk',
    'benjamin.skinner',
]

requires = [
]

build_requires = [
]

variants = [
    ['platform-windows', 'visual_studio-2017.15.9'],
    ['platform-linux'],
]

def commands():
    env.PATH.append('{root}/bin')