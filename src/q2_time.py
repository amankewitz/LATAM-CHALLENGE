from typing import List, Tuple
import json
from collections import Counter
import emoji
import time

def count_emojis(file_path: str) -> List[Tuple[str, int]]:
    emoji_counts = Counter()

    # Abrir el archivo y procesar línea por línea
    with open(file_path, 'r') as file:
        # Usar una lista de comprensión para contar emojis en un solo paso
        for line in file:
            content = json.loads(line.strip()).get("content", "")
            # Solo contar emojis en una línea
            emoji_counts.update(filter(emoji.is_emoji, content))

    # Obtener los 10 emojis más comunes
    return emoji_counts.most_common(10)

def q2_time(file_path: str) -> float:
    start_time = time.time()
    count_emojis(file_path)
    end_time = time.time()
    
    return end_time - start_time

# Ejemplo de uso
file_path = 'farmers-protest-tweets-2021-2-4.json'

# Obtener y mostrar los top 10 emojis utilizados
top_emojis = count_emojis(file_path)
print("Top 10 emojis más usados:")
for emoji_char, count in top_emojis:
    print(f"{emoji_char}: {count}")

# Calcular y mostrar el tiempo de ejecución
execution_time = q2_time(file_path)
print(f"Tiempo de ejecución: {execution_time:.4f} segundos")
