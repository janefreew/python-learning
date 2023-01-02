from pandas import Series,DataFrame
import  pandas as pd
obj = Series([4,5,6,-7])
print(obj)
print(obj.index)
print(obj.values)

obj2 = Series([4,5,6,-7],index=['a','b','c','d'])
print(obj2)