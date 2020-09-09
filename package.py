# -*- coding: utf-8 -*-

name = 'ninja'

version = '1.10.1+ta.1.0.0'

authors = [
    'philip.luk',
    'benjamin.skinner',
]

build_system = "cmake"

variants = [
    ['platform-windows', 'arch-x64', 'os-windows-10', 'visual_studio-2017.15.9'],
]

def commands():
    env.PATH.append('{root}/bin')