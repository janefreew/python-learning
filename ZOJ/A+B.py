
# while True:
#        try:
#               # line = raw_input()
#               line = input()
#               a = line.split()
#               print (int(a[0]) + int(a[1]))
#        except:
#               break

while True:
  try:
      # line = raw_input()
      line = input()
      a = line.split()
      print(int(a[0]) + int(a[1]))
  except:
      print('here')
      break