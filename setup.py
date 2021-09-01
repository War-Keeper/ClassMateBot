from setuptools import setup

setup(
  name='ClassMateBot',
  version='0.1',
  description='A Discord bot for classrom discord channels',
  long_description=""" A Discord bot  which provides utility commands for students and teachers in classrom discord channels """,
  author='Chaitanya Patel, Walter Evan Brown, Kunwar Vidhan, Sumedh Sanjay Salvi, Sunil Dattatraya Upare',
  author_emails='cpatel3@ncsu.edu, webrown2@ncsu.edu, kvidhan@ncsu.edu, ssalvi@ncsu.edu, supare@ncsu.edu',
  url='https://github.com/War-Keeper/ClassMateBot',
  liscense='MIT',
  install_requires=['pytest','discord.py'],
  classifiers=[ 'Development Status :: 1 - Planning', 
                  'License :: OSI Approved :: MIT License', 
                  'Programming Language :: Python :: 3.9' 
              ]
)
