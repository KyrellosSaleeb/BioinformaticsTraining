import pandas as pd

read_file = pd.read_excel (r'processed.cleveland.data.xlsx', sheet_name='Sheet1')
read_file.to_csv (r'heart.csv', index = None, header=True)