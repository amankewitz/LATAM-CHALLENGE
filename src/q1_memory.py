import json
from datetime import datetime
from collections import defaultdict
from typing import List, Tuple
from memory_profiler import memory_usage

def q1_time(file_path: str) -> List[Tuple[datetime.date, str, int, int]]:
    date_counts = defaultdict(int)  # Contador para las fechas
    user_counts = defaultdict(lambda: defaultdict(int))  # Contador para los usuarios por fecha

    # Leer el archivo línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line.strip())
            tweet_date = datetime.fromisoformat(tweet["date"]).date()
            username = tweet["user"]["username"]

            # Actualizar conteos
            date_counts[tweet_date] += 1
            user_counts[tweet_date][username] += 1

    # Encontrar las 10 fechas con más tweets
    top_dates = sorted(date_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    results = []
    for date, total_tweets in top_dates:
        # Encontrar el usuario con más tweets en esa fecha
        if user_counts[date]:  # Verifica que haya usuarios
            top_user, user_count = max(user_counts[date].items(), key=lambda x: x[1])
        else:
            top_user, user_count = None, 0  # Si no hay usuarios
        results.append((date, total_tweets, top_user, user_count))

    return results

def q1_memory(file_path: str) -> float:
    mem_usage = memory_usage((q1_time, (file_path,)), max_usage=True, include_children=True)
    return mem_usage  # Devuelve el uso máximo de memoria directamente

# Ejemplo de uso
file_path = 'farmers-protest-tweets-2021-2-4.json'

# Obtener y mostrar las top 10 fechas con más tweets y los usuarios correspondientes
top_dates_users = q1_time(file_path)
print("Top 10 fechas con más tweets y los usuarios correspondientes:")
for date, total_tweets, user, user_tweets in top_dates_users:
    print(f"{date} ({total_tweets} tweets): {user} ({user_tweets} tweets)")

# Calcular y mostrar la memoria utilizada
memory_used = q1_memory(file_path)
print(f"Memoria máxima utilizada: {memory_used} MiB")


