from setuptools import setup

APP_NAME = "Binary-Decimal Converter"
APP = ['main.py']

OPTIONS = {
    'iconfile': 'media/bash.icns',
    'argv_emulation': True,
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': 'Desktop Founds Control',
        'CFBundleVersion':'0.1.0 stable',
        'CFBundleShortVersionString':'0.1.0',
        'NSHumanReadableCopyright':'Copyright (c) 2021, Andrey_SVJ, All'
    }

}
setup(
    app=APP,
    name=APP_NAME,
    options = {'py2app':OPTIONS},
    set_requires = ['py2app'],
)