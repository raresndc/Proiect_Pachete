import pandas as pd

df_headphones_sales = pd.read_csv("Sales/AirPod_annual_sales.csv")
df_headphones_sales = df_headphones_sales.rename(columns={'Sales (mm)' : 'Headphone-Sales'})
df_smartwatch_sales = pd.read_csv("Sales/Apple_watch_sales.csv")
df_smartwatch_sales = df_smartwatch_sales.rename(columns={'Sales (mm)' : 'Smartwatch-Sales'})
df_smartspeaker_sales = pd.read_csv("Sales/HomePod_annual_sales.csv")
df_smartspeaker_sales = df_smartspeaker_sales.rename(columns={'Sales (mm)' : 'Smartspeaker-Sales'})
df_tablet_sales = pd.read_csv("Sales/iPad_annual_sales.csv")
df_tablet_sales = df_tablet_sales.rename(columns={'Sales (mm)' : 'Tablet-Sales'})
df_phone_sales = pd.read_csv("Sales/iPhone_annual_sales.csv")
df_phone_sales = df_phone_sales.rename(columns={'Sales (mm)' : 'Phone-Sales'})
df_pc_sales = pd.read_csv("Sales/Mac_annual_sales.csv")
df_pc_sales = df_pc_sales.rename(columns={'Sales (mm)' : 'Pc-Sales'})

df_merged = pd.merge(df_headphones_sales, df_smartwatch_sales, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_smartspeaker_sales, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_tablet_sales, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_phone_sales, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_pc_sales, on='Year', how='outer')
variables = list(df_merged)[1:]
# print(variables)
df_merged = df_merged.sort_values(by='Year',ascending=False)
df_merged1 = df_merged.copy()
for var in variables:
    df_merged1.loc[(df_merged1[var]<10.0),[var]]=10.0

df_merged['Total'] = df_merged[variables].sum(axis=1)
print("Most important columms\n",df_merged1.drop(columns=df_merged1.columns[[1,2,3]],axis=1))

print("First five years\n", df_merged.iloc[:5,:])
df_merged.to_csv("Sales/Merged_Sales.csv")

