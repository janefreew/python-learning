import  os


from pathlib import  Path
# print(os.path.abspath('./'))
# print(os.path.exists('./'))

q = Path('.')
print(q.resolve())



p = Path('./tmp/a/b')
Path.mkdir(p,parents=True)