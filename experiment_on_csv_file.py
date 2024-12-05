import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("/Users/kshitijagnihotri/Downloads/Housing.csv")

data.index = data.index + 1 # i used this to start the indexes from 1
print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset Statistics:")
print(data.describe())

print("\nMissing values in the dataset:")
print(data.isnull().sum())

sorted_data = data.sort_values(by='price', ascending=False)
print("\nTop 5 most expensive houses:")
print(sorted_data.iloc[:5])

plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='blue', marker='o')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()

labels = ['Python', 'Java', 'C++', 'Ruby']
sizes = [40, 30, 20, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')
plt.show()

plt.plot([1, 10, 100], [1, 10, 100])
plt.yscale('log')
plt.xscale('log')
plt.title('Logarithmic Scale')
plt.show()

