from typing import List, Tuple
import json
from collections import Counter
import re  # Para usar expresiones regulares
import time  # Para medir el tiempo de ejecución

def count_user_mentions(file_path: str) -> List[Tuple[str, int]]:
    mention_counts = Counter()

    # Compilar la expresión regular fuera del bucle para mayor eficiencia
    mention_pattern = re.compile(r'@(\w+)')

    # Abrir el archivo y leer línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line.strip())
            content = tweet["content"]

            # Encontrar todas las menciones en el contenido del tweet
            mentions = mention_pattern.findall(content)
            mention_counts.update(mentions)

    # Obtener los 10 usuarios más mencionados
    top_users = mention_counts.most_common(10)

    return top_users

def q3_time(file_path: str) -> float:
    start_time = time.time()  # Iniciar el temporizador
    count_user_mentions(file_path)  # Llamar a la función que cuenta menciones
    end_time = time.time()  # Finalizar el temporizador
    return end_time - start_time  # Devolver el tiempo transcurrido

# Ejemplo de uso
file_path = 'farmers-protest-tweets-2021-2-4.json'

# Obtener y mostrar los top 10 usuarios más mencionados
top_users = count_user_mentions(file_path)
print("Top 10 usuarios más mencionados:")
for username, count in top_users:
    print(f"{username}: {count}")

# Calcular y mostrar el tiempo utilizado
execution_time = q3_time(file_path)
print(f"Tiempo de ejecución: {execution_time:.4f} segundos")

