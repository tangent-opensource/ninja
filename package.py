# -*- coding: utf-8 -*-

name = 'ninja'

version = '1.10.1+ta.1.0.1'

authors = [
    'philip.luk',
    'benjamin.skinner',
]

build_system = "cmake"

@early()
def private_build_requires():
    import sys
    if 'win' in str(sys.platform):
        return ['visual_studio']
    else:
        return ['gcc-7']

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10'],
]

def commands():
    env.PATH.append('{root}/bin')