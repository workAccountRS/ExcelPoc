import pandas as pd


a = pd.read_excel(open('testFile.xlsx', 'rb'),
              sheet_name='Relational DB')

print(a)