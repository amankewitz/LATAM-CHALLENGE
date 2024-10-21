"""
1. Las top 10 fechas donde hay más tweets. Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días. Debe incluir las siguientes funciones:
```python
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
Returns: 
[(datetime.date(1999, 11, 15), "LATAM321"), (datetime.date(1999, 7, 15), "LATAM_CHI"), ...]
"""
import json
from datetime import datetime
from collections import Counter, defaultdict
from typing import List, Tuple

def q1_time(file_path: str) -> List[Tuple[datetime.date, str, int, int]]:
    # Inicializar un contador para las fechas y un diccionario para los usuarios
    date_counts = Counter()
    user_counts = defaultdict(Counter)

    # Abrir el archivo y procesar línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line.strip())
            tweet_date = datetime.fromisoformat(tweet["date"]).date()
            username = tweet["user"]["username"]

            # Contar tweets por fecha
            date_counts[tweet_date] += 1
            # Contar tweets por usuario en esa fecha
            user_counts[tweet_date][username] += 1

    # Encontrar las 10 fechas con más tweets
    top_dates = date_counts.most_common(10)

    # Preparar la lista de resultados
    results = []
    for date, _ in top_dates:
        # Encontrar el usuario con más tweets en esa fecha
        if user_counts[date]:  # Verifica que haya usuarios
            top_user, user_count = user_counts[date].most_common(1)[0]
        else:
            top_user, user_count = None, 0  # Si no hay usuarios

        total_tweets = date_counts[date]
        results.append((date, total_tweets, top_user, user_count))

    return results

# Ejemplo de uso
file_path = 'farmers-protest-tweets-2021-2-4.json'

# Obtener y mostrar las top 10 fechas con más tweets y los usuarios correspondientes
top_dates_users = q1_time(file_path)
print("Top 10 fechas con más tweets y los usuarios correspondientes:")
for date, total_tweets, user, user_tweets in top_dates_users:
    print(f"{date} ({total_tweets} tweets): {user} ({user_tweets} tweets)")