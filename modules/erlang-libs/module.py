import os
from osv.modules.api import *
from osv.modules.filemap import FileMap
from osv.modules import api

_module = '${OSV_BASE}/modules/erlang-libs'

api.require("openssl")
api.require("libz")
api.require("ncurses")

default = ""
