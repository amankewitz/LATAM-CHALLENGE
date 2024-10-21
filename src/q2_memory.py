from typing import List, Tuple
import json
from collections import defaultdict
import emoji  # Asegúrate de tener la librería emoji instalada
from memory_profiler import memory_usage

def count_emojis(file_path: str) -> List[Tuple[str, int]]:
    emoji_counts = defaultdict(int)  # Usamos un diccionario para contar emojis

    # Abrir el archivo y leer línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line.strip())
            content = tweet["content"]

            # Contar solo emojis en el contenido del tweet
            for character in content:
                if emoji.is_emoji(character):  # Verificar si el carácter es un emoji
                    emoji_counts[character] += 1

    # Obtener los 10 emojis más comunes sin usar una lista intermedia
    top_emojis = sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_emojis

def q2_memory(file_path: str) -> float:
    # Usar una función lambda para encapsular la llamada a count_emojis
    mem_usage = memory_usage((lambda: count_emojis(file_path),), max_usage=True)

    return max(mem_usage) if isinstance(mem_usage, list) else mem_usage

# Ejemplo de uso
file_path = 'farmers-protest-tweets-2021-2-4.json'

# Obtener y mostrar los top 10 emojis utilizados
top_emojis = count_emojis(file_path)
print("Top 10 emojis más usados:")
for emoji_char, count in top_emojis:
    print(f"{emoji_char}: {count}")

# Calcular y mostrar la memoria utilizada
memory_used = q2_memory(file_path)
print(f"Memoria máxima utilizada: {memory_used:.2f} MiB")  # Mostrar el valor máximo de memoria
