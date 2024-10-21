import json
from datetime import datetime
from collections import Counter, defaultdict
from typing import List, Tuple

# Función para encontrar las 10 fechas con más tweets y los usuarios correspondientes
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

# Función para analizar el uso de memoria (aquí puedes agregar lógica relacionada al uso de memoria)
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Inicializar un contador para las fechas y un diccionario para los usuarios
    date_user_pairs = []

    # Abrir el archivo y procesar línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line.strip())
            tweet_date = datetime.fromisoformat(tweet["date"]).date()
            username = tweet["user"]["username"]

            # Guardar pares de fecha y usuario
            date_user_pairs.append((tweet_date, username))

    return date_user_pairs

# Ejemplo de uso
file_path = 'farmers-protest-tweets-2021-2-4.json'

# Obtener y mostrar las top 10 fechas con más tweets y los usuarios correspondientes
top_dates_users = q1_time(file_path)
print("Top 10 fechas con más tweets y los usuarios correspondientes:")
for date, total_tweets, user, user_tweets in top_dates_users:
    print(f"{date} ({total_tweets} tweets): {user} ({user_tweets} tweets)")

# Obtener y mostrar las fechas y usuarios analizadas por q1_memory
date_user_pairs = q1_memory(file_path)
print("\nFechas y usuarios procesados por q1_memory:")
for date, user in date_user_pairs[:10]:  # Mostrar solo los primeros 10 como ejemplo
    print(f"{date}: {user}")
