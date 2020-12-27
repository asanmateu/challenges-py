def FindIntersection(strArr):
  a = map(int, strArr[0].split(','))
  b = map(int, strArr[1].split(','))
  c = list(set(a) & set(b))
  c.sort()

  if c == []:
    return 'false'
  else:
    return ','.join(map(str, c))


print(FindIntersection(input()))
