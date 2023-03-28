import matplotlib.pyplot as plt

def plot_venituri(dataframe, index, column_name, title, xlabel, ylabel):
    plt.plot(dataframe[index], dataframe[column_name])
    plt.scatter(dataframe[index], dataframe[column_name], color='red')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def plot_boxplot(dataframe, columne_name, title, ylabel):
    plt.boxplot(dataframe[columne_name].values)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.show()

def show():
    plt.show()

def obtine_maximele(dictionar):
    maxs = {}
    for key, values in dictionar.items():
        max_year = max(values, key=values.get)
        maxs[key] = (max_year, values[max_year])
    return maxs