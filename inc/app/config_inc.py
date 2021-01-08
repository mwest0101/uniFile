from inc.commons.ReadJson import *
from inc.commons.StrNormalize import *
from inc.app.JsonParams import *
from inc.commons.Debug import *
from inc.app.lang import *

# ------------------------------------------------------
# Abro archivo json


JsonParams.loadFile("uniFile_conf.json")
StrNormalize.init(JsonParams.getSo())