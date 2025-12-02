from setuptools import setup

setup(name='mygit',
      packages=['mygit'],
      entry_points={'console_scripts': [
          'mygit = mygit.cli:main',
      ]})
