import sys,os
sys.path.append(os.path.join(sys.path[0],'..'))
from pprint import pprint
from pychinavo.astrodict import astrodict

dict = astrodict()
pprint(dict.termdetails(1))
pprint(dict.fuzzy('vega'))
pprint(dict.precise('vega'))