from typing import List, Tuple
import json
from collections import Counter
import re  # Para usar expresiones regulares
from memory_profiler import memory_usage

def count_user_mentions(file_path: str) -> List[Tuple[str, int]]:
    mention_counts = Counter()

    # Leer el archivo y contar menciones en una sola pasada
    with open(file_path, 'r') as file:
        for line in file:
            # Cargar el tweet y extraer el contenido
            content = json.loads(line.strip())["content"]
            
            # Contar menciones directamente sin almacenamiento intermedio
            mention_counts.update(re.findall(r'@(\w+)', content))

    # Obtener los 10 usuarios más mencionados
    return mention_counts.most_common(10)

def q3_memory(file_path: str) -> float:
    # Utilizar memory_usage para medir el uso de memoria
    mem_usage = memory_usage((count_user_mentions, (file_path,)), max_usage=True)
    return mem_usage

# Ejemplo de uso
file_path = 'farmers-protest-tweets-2021-2-4.json'

# Obtener y mostrar los top 10 usuarios más mencionados
top_users = count_user_mentions(file_path)
print("Top 10 usuarios más mencionados:")
for username, count in top_users:
    print(f"{username}: {count}")

# Calcular y mostrar la memoria utilizada
memory_used = q3_memory(file_path)
print(f"Memoria máxima utilizada: {memory_used:.2f} MiB")
