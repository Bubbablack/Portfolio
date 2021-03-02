import re

def add(string):
  string = _normalize_delimiters(string)
  if string:
    return _add_numbers_in_string(string)
  else:
    return 0

def _normalize_delimiters(string):
  string = _normalize_custom_delimiter(string)
  return string

def _normalize_custom_delimiter(string):

  if string.startswith('//['):
    stringer = re.match('//(\[(.*)\])', string)
    delim1 = stringer.group(2)
    win = list(map(lambda delim1: delim1, delim1.split('][')))
    delimiter_spec, string = string.split('\n', 1)
    for i in win:
      string = string.replace(i, ',')
  
    
  elif string.startswith('//'):
    delimiter_spec, string = string.split('\n', 1)
    delimiter = delimiter_spec[2:]
    string = string.replace(delimiter, ',')
  
  return string

def _add_numbers_in_string(string):
  string =string.replace('\n', ',')
  numbers = _validate_format(string)
  _validate_numbers(numbers)
   
  numbers =_check_thousand(numbers)
  return sum(numbers)
def _validate_format(string):
  try:
    numbers = list(map(int, string.split(',')))
  except:
    raise ValueError('ERROR: invalid input')
  return numbers
 
def _check_thousand(numbers):
  string = list(map(lambda x: x* 0 if x >= 1000 else x, numbers))
  return string

def _validate_numbers(numbers): 
  k = list(filter(lambda x: x < 0, numbers))
  
  if k:
    raise ValueError('ERROR: negatives not allowed '+','.join(str(x) for x in k))
    




