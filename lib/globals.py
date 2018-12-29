"""
Global configuration of the project.
All hardcoded pathes and other data should be
(theoretically) here.
"""
from __future__ import print_function

import logging
import os
import yaml
from pygments.styles import get_all_styles

USE_OS_PACKAGES = False  # set to False if you pull cheat sheets repositories from GitHub
DOCKERIZED = True      # set to True if the service is running in a Docker container

SERVER_ADDRESS = '0.0.0.0'
SERVER_PORT = 8002

MYDIR = os.path.abspath(os.path.join(__file__, '..', '..'))
_CONF_FILE = os.path.join(MYDIR, 'etc/config.yaml')

if DOCKERIZED:
    REDISHOST = 'redis'
else:
    REDISHOST = 'localhost'

ANSI2HTML = os.path.join(MYDIR, "share/ansi2html.sh")

LOG_FILE = os.path.join(MYDIR, 'log/main.log')
FILE_QUERIES_LOG = os.path.join(MYDIR, 'log/queries.log')
TEMPLATES = os.path.join(MYDIR, 'share/templates')
STATIC = os.path.join(MYDIR, 'share/static')
PATH_VIM_ENVIRONMENT = os.path.join(MYDIR, 'share/vim')


    PATH_TLDR_PAGES = os.path.join(MYDIR, "cheatsheets/tldr/*/*.md")
    PATH_CHEAT_PAGES = os.path.join(MYDIR, "cheatsheets/cheat/*")
    PATH_CHEAT_SHEETS = os.path.join(MYDIR, "cheatsheets/sheets/")
    PATH_CHEAT_SHEETS_SPOOL = os.path.join(MYDIR, "cheatsheets/spool/")
    PATH_LEARNXINY = os.path.join(MYDIR, "cheatsheets/learnxinyminutes-docs")
    PATH_LATENZ = os.path.join(MYDIR, "late.nz/bin")

GITHUB_REPOSITORY = {
    "late.nz"           :   'mechanicalAI/late.nz',
    "cheat.sheets"      :   'mechanicalAI/cheat.sheets',
    "cheat.sheets dir"  :   'mechanicalAI/cheat.sheets',
    "tldr"              :   'mechanicalAI/tldr',
    "cheat"             :   'mechanicalAI/cheat',
    "learnxiny"         :   'mechanicalAI/learnxinyminutes-docs',
    "internal"          :   '',
    "search"            :   '',
    "unknown"           :   '',
}


#
# Reading configuration from etc/config.yaml
# config overrides default settings
#
if os.path.exists(_CONF_FILE):
    _CONFIG = yaml.load(_CONF_FILE)
    if 'server' in _CONFIG:
        _SERVER_CONFIG = _CONFIG['server']
        if 'address' in _SERVER_CONFIG:
            SERVER_ADDRESS = _SERVER_CONFIG['address']
        if 'port' in _SERVER_CONFIG:
            SERVER_ADDRESS = _SERVER_CONFIG['port']


COLOR_STYLES = sorted(list(get_all_styles()))

MALFORMED_RESPONSE_HTML_PAGE = open(os.path.join(STATIC, 'malformed-response.html')).read()

def error(text):
    """
    Log error `text` and produce a RuntimeError exception
    """
    if not text.startswith('Too many queries'):
        print(text)
    logging.error("ERROR %s", text)
    raise RuntimeError(text)

def log(text):
    """
    Log error `text` (if it does not start with 'Too many queries')
    """
    if not text.startswith('Too many queries'):
        print(text)
        logging.info(text)
