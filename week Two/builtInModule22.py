
import sys
import textwrap
from logger import Logger
"""
@author:Ranjit
Created_date : 23/2/2021
updated_date : 23/2/2021
Title :  builtIn Module.
"""

module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))