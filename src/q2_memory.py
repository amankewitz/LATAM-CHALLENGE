import json
from datetime import datetime
from typing import List, Tuple
from memory_profiler import memory_usage

def q1_time(file_path: str) -> List[Tuple[datetime.date, str, int, int]]:
    date_counts = {}  # Diccionario simple para contar tweets por fecha
    user_counts = {}  # Diccionario para contar tweets por usuario en cada fecha

    # Abrir el archivo y procesar línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line.strip())
            tweet_date = datetime.fromisoformat(tweet["date"]).date()
            username = tweet["user"]["username"]

            # Contar tweets por fecha
            if tweet_date in date_counts:
                date_counts[tweet_date] += 1
                user_counts[tweet_date][username] = user_counts[tweet_date].get(username, 0) + 1
            else:
                date_counts[tweet_date] = 1
                user_counts[tweet_date] = {username: 1}

    # Encontrar las 10 fechas con más tweets
    top_dates = sorted(date_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    # Preparar la lista de resultados
    results = []
    for date, _ in top_dates:
        # Encontrar el usuario con más tweets en esa fecha
        top_user = max(user_counts[date].items(), key=lambda x: x[1], default=(None, 0))
        total_tweets = date_counts[date]
        results.append((date, total_tweets, top_user[0], top_user[1]))

    return results

def q2_memory(file_path: str) -> float:
    mem_usage = memory_usage((q1_time, (file_path,)), max_usage=True)
    return mem_usage  # Devuelve el uso máximo de memoria directamente

# Ejemplo de uso
file_path = 'farmers-protest-tweets-2021-2-4.json'

# Obtener y mostrar las top 10 fechas con más tweets y los usuarios correspondientes
top_dates_users = q1_time(file_path)
print("Top 10 fechas con más tweets y los usuarios correspondientes:")
for date, total_tweets, user, user_tweets in top_dates_users:
    print(f"{date} ({total_tweets} tweets): {user} ({user_tweets} tweets)")

# Calcular y mostrar la memoria utilizada
memory_used = q2_memory(file_path)
print(f"Memoria máxima utilizada: {memory_used:.2f} MiB")
