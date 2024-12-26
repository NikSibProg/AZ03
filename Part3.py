import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL для парсинга
url = "https://www.divan.ru/category/divany"

# Запрос к сайту
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Парсинг данных о диванах
sofas = []
for item in soup.find_all('div', class_='some-class-name'):  # Замените на актуальный селектор
    name = item.find('h3').text.strip()
    price = item.find('span', class_='price-class-name').text.strip().replace('₽', '').replace(' ', '')
    sofas.append({'Название': name, 'Цена': int(price)})

# Сохранение в CSV
df = pd.DataFrame(sofas)
df.to_csv('sofas.csv', index=False)

# Анализ данных
average_price = df['Цена'].mean()
print(f"Средняя цена на диваны: {average_price} ₽")

# Гистограмма цен
plt.hist(df['Цена'], bins=20, color='purple', alpha=0.7, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
