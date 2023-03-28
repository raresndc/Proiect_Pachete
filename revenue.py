import pandas as pd
import matplotlib.pyplot as plt

# citirea datelor din csv-uri
# df_apple_revenue = pd.read_csv('Revenue/Apple_annual_revenue.csv')
# print('Data Frame in care sunt prezentate veniturile Apple: \n', df_apple_revenue, '\n')
#
# df_iphone_revenue = pd.read_csv('Revenue/iPhone_annual_revenue.csv')
# print('Data Frame in care sunt prezentate veniturile iPhone:\n', df_iphone_revenue, '\n')
#
# df_ipad_revenue = pd.read_csv('Revenue/iPad_annual_revenue.csv')
# print('Data Frame in care sunt prezentate veniturile iPad:\n', df_ipad_revenue, '\n')
#
# df_mac_revenue = pd.read_csv('Revenue/Mac_annual_revenue.csv')
# print('Data Frame in care sunt prezentate veniturile Mac:\n', df_mac_revenue, '\n')
#
# df_accessories_revenue = pd.read_csv('Revenue/Wearable_home_and_accessories_annual_revenue.csv')
# print('Data Frame in care sunt prezentate veniturile aduse din accesorii:\n', df_accessories_revenue, '\n')
#
# df_services_revenue = pd.read_csv('Revenue/Apple_services_annual_revenue.csv')
# print('Data Frame in care sunt prezentate veniturile aduse din serviciile Apple:\n', df_services_revenue, '\n')
#
# # plot pentru reprezentarea grafica a ascensiunii firmei
# plt.plot(df_apple_revenue['Year'], df_apple_revenue['Revenue ($bn)'])
# plt.scatter(df_apple_revenue['Year'], df_apple_revenue['Revenue ($bn)'], color='red')
#
# plt.title("Grafic de linie privind veniturile Apple")
# plt.xlabel("Anul")
# plt.ylabel("Venit ($bn)")
#
# plt.show()

'''wearable, home and accessories = AirPods + Watch + HomePod'''
'''iPhone revenue + sales'''
'''Mac revenue + sales'''
'''iPad revenue + sales'''

'''top 5 years most sales'''

df_headphones_sales = pd.read_csv("Sales/AirPod_annual_sales.csv")
df_headphones_sales = df_headphones_sales.rename(columns={'Sales (mm)' : 'Headphone Sales'})
df_smartwatch_sales = pd.read_csv("Sales/Apple_watch_sales.csv")
df_smartwatch_sales = df_smartwatch_sales.rename(columns={'Sales (mm)' : 'Smartwatch Sales'})
df_smartspeaker_sales = pd.read_csv("Sales/HomePod_annual_sales.csv")
df_smartspeaker_sales = df_smartspeaker_sales.rename(columns={'Sales (mm)' : 'Smartspeaker Sales'})
df_tablet_sales = pd.read_csv("Sales/iPad_annual_sales.csv")
df_tablet_sales = df_tablet_sales.rename(columns={'Sales (mm)' : 'Tablet Sales'})
df_phone_sales = pd.read_csv("Sales/iPhone_annual_sales.csv")
df_phone_sales = df_phone_sales.rename(columns={'Sales (mm)' : 'Phone Sales'})
df_pc_sales = pd.read_csv("Sales/Mac_annual_sales.csv")
df_pc_sales = df_pc_sales.rename(columns={'Sales (mm)' : 'Pc Sales'})

df_merged = pd.merge(df_headphones_sales, df_smartwatch_sales, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_smartspeaker_sales, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_tablet_sales, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_phone_sales, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_pc_sales, on='Year', how='outer')
variables = list(df_merged)[1:]
df_merged = df_merged.set_index('Year')
df_merged = df_merged.sort_values(by='Year',ascending=False)
df_merged.to_csv("Sales/Merged_Sales.csv")


