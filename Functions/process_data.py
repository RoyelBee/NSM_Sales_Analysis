
import pandas as pd
df = pd.read_csv('../Data/Master_data.csv')

data = df.loc[df['NSMNAME'] == 'Mr. Aniruddha Saha']
target_val = data.TarVal.sum()
sales_val = data.SalesValue.sum()
target_qty = data.TarQTY.sum()


# # Day wise target and Sales
day_wise_data = data.groupby('TRANSDATE').sum()

days = day_wise_data.index.tolist()
day_wise_target = day_wise_data['TarVal'].tolist()
day_wise_sales = day_wise_data['SalesValue'].tolist()