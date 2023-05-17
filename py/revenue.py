import pandas as pd
import matplotlib.pyplot as plt
from functii import *

# citirea datelor din csv-uri
df_apple_revenue = pd.read_csv('../Revenue/Apple_annual_revenue.csv')
df_apple_revenue = df_apple_revenue.rename(columns={'Revenue ($bn)' : 'Apple Revenue'})
print('Data Frame in care sunt prezentate veniturile Apple: \n', df_apple_revenue, '\n')

df_iphone_revenue = pd.read_csv('../Revenue/iPhone_annual_revenue.csv')
df_iphone_revenue = df_iphone_revenue.rename(columns={'Revenue ($bn)' : 'iPhone Revenue'})
print('Data Frame in care sunt prezentate veniturile iPhone:\n', df_iphone_revenue, '\n')

df_ipad_revenue = pd.read_csv('../Revenue/iPad_annual_revenue.csv')
df_ipad_revenue = df_ipad_revenue.rename(columns={'Revenue ($bn)' : 'iPad Revenue'})
print('Data Frame in care sunt prezentate veniturile iPad:\n', df_ipad_revenue, '\n')

df_mac_revenue = pd.read_csv('../Revenue/Mac_annual_revenue.csv')
df_mac_revenue = df_mac_revenue.rename(columns={'Revenue ($bn)' : 'Mac Revenue'})
print('Data Frame in care sunt prezentate veniturile Mac:\n', df_mac_revenue, '\n')

df_accessories_revenue = pd.read_csv('../Revenue/Wearable_home_and_accessories_annual_revenue.csv')
df_accessories_revenue = df_accessories_revenue.rename(columns={'Revenue ($bn)' : 'Accessories Revenue'})
print('Data Frame in care sunt prezentate veniturile aduse din accesorii:\n', df_accessories_revenue, '\n')

df_services_revenue = pd.read_csv('../Revenue/Apple_services_annual_revenue.csv')
df_services_revenue = df_services_revenue.rename(columns={'Revenue ($bn)' : 'Services Revenue'})
print('Data Frame in care sunt prezentate veniturile aduse din serviciile Apple:\n', df_services_revenue, '\n')

# merge
df_merged = pd.merge(df_apple_revenue, df_iphone_revenue, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_ipad_revenue, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_mac_revenue, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_accessories_revenue, on='Year', how='outer')
df_merged = pd.merge(df_merged, df_services_revenue, on='Year', how='outer')

# ordonarea rândurilor după an
df_merged = df_merged.sort_values(by='Year')

# completarea valorilor lipsă cu 0 -> DE INLOCUIT
df_merged = df_merged.fillna(0)
df_merged = df_merged.set_index('Year')

# afișarea data frame-urilor combinate și completate
pd.options.display.max_columns = None
print('Data Frame combinat și completat cu valori 0:\n', df_merged)

# media revenue-urilor obtinute de companie pe fiecare divizie
sum_apple = df_merged['Apple Revenue'].sum()
print('\nSuma veniturilor Apple: ', df_merged['Apple Revenue'].sum(),
      '\nMedia veniturilor Apple: ', df_merged['Apple Revenue'].mean())
print('Valoarea mediana a veniturilor Apple: ', df_merged['Apple Revenue'].median())

sum_iphone = df_merged['iPhone Revenue'].sum()
print('\nSuma veniturilor iPhone: ', df_merged['iPhone Revenue'].sum(),
      '\nMedia veniturilor iPhone: ', df_merged['iPhone Revenue'].mean())
print('Valoarea mediana a veniturilor iPhone: ', df_merged['iPhone Revenue'].median())

sum_iPad = df_merged['iPad Revenue'].sum()
print('\nSuma veniturilor iPad: ', df_merged['iPad Revenue'].sum(),
      '\nMedia veniturilor iPad: ', df_merged['iPad Revenue'].mean())
print('Valoarea mediana a veniturilor iPad: ', df_merged['iPad Revenue'].median())

sum_mac = df_merged['Mac Revenue'].sum()
print('\nSuma veniturilor Mac: ', df_merged['Mac Revenue'].sum(),
      '\nMedia veniturilor Mac: ', df_merged['Mac Revenue'].mean())
print('Valoarea mediana a veniturilor Mac: ', df_merged['Mac Revenue'].median())

sum_accessories = df_merged['Accessories Revenue'].sum()
print('\nSuma veniturilor Accessories: ', df_merged['Accessories Revenue'].sum(),
      '\nMedia veniturilor Accessories: ', df_merged['Accessories Revenue'].mean())
print('Valoarea mediana a veniturilor Accessories: ', df_merged['Accessories Revenue'].median())

sum_services = df_merged['Services Revenue'].sum()
print('\nSuma veniturilor Services: ', df_merged['Services Revenue'].sum(),
      '\nMedia veniturilor Services: ', df_merged['Services Revenue'].mean())
print('Valoarea mediana a veniturilor Services: ', df_merged['Services Revenue'].median())

sum_others = sum_apple - sum_iphone - sum_iPad - sum_mac - sum_accessories - sum_services
print('\nVenituri Apple obtinute din alte surse: ' + str(sum_others))
print('Procent: ' + str((sum_others * 100)/sum_apple) + '%')

# functii
plot_boxplot(df_merged, 'Apple Revenue', title='Boxplot al medianei si quartilelor veniturilor Apple din 2006 pana in prezent',
             ylabel='Valoare')

# plot pentru reprezentarea grafica a ascensiunii firmei
plot_venituri(df_apple_revenue, index='Year', column_name='Apple Revenue', title='Grafic de linie privind veniturile Apple',
              xlabel='Anul', ylabel='Venit ($bn)')

# show pentru functiile create
show()

# lucru cu dictionar
dict_merged = df_merged.to_dict()
print('\nDataFrame-ul transformat in dictionar:\n', dict_merged.keys())
for value in dict_merged.values():
    print(value)

# filtrarea dictionarului pentru a nu contine elemente nule
dict_filtrat = {k: {an: valoare for an, valoare in v.items() if valoare != 0} for k, v in dict_merged.items()}
dict_filtrat_final = {k: v for k, v in dict_filtrat.items() if v}

print('\nDictionar fara valori nule:\n')
for value in dict_filtrat_final.values():
    print(value)

print('\nValorile maxime pentru fiecare cheie:\n' + str(obtine_maximele(dict_filtrat_final)))

# eliminarea randurilor din data frame-ul merge-uit care au un element = 0
# for key, value in df_merged.items():
#     if value == 0:
#         df_merged = df_merged.drop(key, axis=0)

df = df_merged.query('`Apple Revenue` != 0 and `iPhone Revenue` != 0 and `iPad Revenue` != 0 and '
                            '`Mac Revenue` != 0 and `Accessories Revenue` != 0 and `Services Revenue` != 0')

print('\nData Frame-ul fara inregistrari ce contin valoarea 0:\n' )
print(df)


