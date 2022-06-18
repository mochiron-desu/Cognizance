import pandas as pd

ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai', 'campus'])
n = len(ser)
temp=""
for a in range(0, n):
    temp = temp+str(ser.get(key=a)).capitalize()+" "
    

print(temp)