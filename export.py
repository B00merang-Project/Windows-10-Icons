#!/bin/python3

import os
import subprocess


INKSCAPE_EXE = 'inkscape'
SRC_DIR = os.path.join(
    os.path.dirname(__file__),
    'scalable', 'mimetypes'
)
TARGET_DIRS = [
    22, 24, 32, 48, 128, 256, 512
]
OUT_DIRS = [
    os.path.join(os.path.dirname(__file__), f'{folder}x{folder}', 'mimetypes')
    for folder in TARGET_DIRS
]
SVG_FILES = [
    'text-css',
    'text-richtext',
    'text-rust',
    'text-tcl',
    'text-turtle',
    'text-vbscript',
    'text-x-c++hdr',
    'text-x-chdr',
    'text-x-cmake',
    'text-x-csharp',
    'text-x-c++src',
    'text-x-csrc',
    'text-x-dsrc',
    'text-x-erlang',
    'text-x-generic',
    'text-x-go',
    'text-x-java',
    'text-x-kotlin',
    'text-x-lua',
    'text-x-matlab',
    'text-x-python',
    'text-x-qml',
    'text-x-sass',
    'text-x-scss',
    'text-x-vala',
]

if __name__ == "__main__":
    for svgFile in SVG_FILES:
        print(f'Exporting {svgFile}...')
        srcPath = os.path.join(
            SRC_DIR, f'{svgFile}.svg'
        )
        for index in range(len(TARGET_DIRS)):
            outputPath = os.path.join(
                OUT_DIRS[index], f'{svgFile}.png'
            )
            outputWidth = TARGET_DIRS[index]
            proc = subprocess.run([
                INKSCAPE_EXE,
                '--export-type', 'png',
                '--export-width', f'{outputWidth}',
                '--export-filename', outputPath,
                srcPath
            ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if proc.returncode != 0:
                print(proc.stderr)
                exit(-1)
