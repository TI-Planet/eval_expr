# eval_expr TI-Nspire CX II python library
# Latest version and documentation: https://github.com/TI-Planet/eval_expr
# Author: Adrien "Adriweb" Bertrand
# See tiplanet.org for more cool stuff :)
# License: Unlicense / Public Domain / Do whatever you want

# Useful for eval
from math import sqrt, pi, e

# Internal helper functions....
def _return_number_if_possible(s):
  try:
    f = float(s)
    return int(f) if int(f) == f else f
  except ValueError:
    return s

def _return_evaled_if_possible(thing):
  try:
    return eval("("+str(thing)+")")
  except:
    return thing

def _cleanstr(res):
  res = res[1:-1]  # to remove the quotes
  res = res.replace("*\uf02f", "j")  # complex i
  res = res.replace("\uf02f", "j")  # complex i
  res = res.replace("\u221a", "sqrt")
  res = res.replace("\u03c0", "pi")
  res = res.replace("\uf03f", "e")
  res = _return_number_if_possible(res)  # auto type...
  return res

# Public functions
def eval_expr(expr, trypyeval=False):
  from ti_system import writeST, readST
  writeST("tmppy_", 'strsub(string('+str(expr)+'),"/","$%$")')  # eval and store
  res = readST("tmppy_")  # retrieve stored value
  res = res.replace("$%$", "/")  # magic replacement
  res = _cleanstr(res)
  if trypyeval == True:
    res = _return_evaled_if_possible(res)
  return res

def call_func(funcname, *pyargs):
  fargs = ','.join(map(str, pyargs))
  expr = funcname + '(' + fargs + ')'
  res = eval_expr(expr)
  return res if res != expr else None

# Aliases for compat with other stuff
caseval = eval_expr
eval_native = eval_expr

