import pandas as pd
import matplotlib.pyplot as plt

# citirea datelor din csv-uri
df_apple_revenue = pd.read_csv('Revenue/Apple_annual_revenue.csv')
print('Data Frame in care sunt prezentate veniturile Apple: \n', df_apple_revenue, '\n')

df_iphone_revenue = pd.read_csv('Revenue/iPhone_annual_revenue.csv')
print('Data Frame in care sunt prezentate veniturile iPhone:\n', df_iphone_revenue, '\n')

df_ipad_revenue = pd.read_csv('Revenue/iPad_annual_revenue.csv')
print('Data Frame in care sunt prezentate veniturile iPad:\n', df_ipad_revenue, '\n')

df_mac_revenue = pd.read_csv('Revenue/Mac_annual_revenue.csv')
print('Data Frame in care sunt prezentate veniturile Mac:\n', df_mac_revenue, '\n')

df_accessories_revenue = pd.read_csv('Revenue/Wearable_home_and_accessories_annual_revenue.csv')
print('Data Frame in care sunt prezentate veniturile aduse din accesorii:\n', df_accessories_revenue, '\n')

df_services_revenue = pd.read_csv('Revenue/Apple_services_annual_revenue.csv')
print('Data Frame in care sunt prezentate veniturile aduse din serviciile Apple:\n', df_services_revenue, '\n')

# plot pentru reprezentarea grafica a ascensiunii firmei
plt.plot(df_apple_revenue['Year'], df_apple_revenue['Revenue ($bn)'])
plt.scatter(df_apple_revenue['Year'], df_apple_revenue['Revenue ($bn)'], color='red')

plt.title("Grafic de linie privind veniturile Apple")
plt.xlabel("Anul")
plt.ylabel("Venit ($bn)")

plt.show()