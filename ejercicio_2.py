"""
2. Los top 10 emojis más usados con su respectivo conteo. Debe incluir las siguientes funciones:
```python
def q2_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python
Returns: 
[("✈️", 6856), ("❤️", 5876), ...]
"""
from typing import List, Tuple
import json
from collections import Counter
import emoji  # Asegúrate de tener la librería emoji instalada

def count_emojis(file_path: str) -> List[Tuple[str, int]]:
    emoji_counts = Counter()

    # Abrir el archivo y leer línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line.strip())
            content = tweet["content"]

            # Contar solo emojis en el contenido del tweet
            for character in content:
                if emoji.is_emoji(character):  # Verificar si el carácter es un emoji
                    emoji_counts[character] += 1

    # Obtener los 10 emojis más comunes
    top_emojis = emoji_counts.most_common(10)

    return top_emojis

# Ejemplo de uso
file_path = 'farmers-protest-tweets-2021-2-4.json'

# Obtener y mostrar los top 10 emojis utilizados
top_emojis = count_emojis(file_path)
print("Top 10 emojis más usados:")
for emoji_char, count in top_emojis:
    print(f"{emoji_char}: {count}")
