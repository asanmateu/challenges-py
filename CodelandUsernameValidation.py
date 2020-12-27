def CodelandUsernameValidation(str):
  if len(str) not in range(4, 26):
    return 'false'
  elif not str[0].isalpha():
    return 'false'
  elif str[-1] == '_':
    return 'false'
  elif [i for i in str if str.isalnum or i == '_'] == []:
    return 'false'
  else:
    return 'true'


print(CodelandUsernameValidation(input()))