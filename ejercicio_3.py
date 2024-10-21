"""
3. El top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos. Debe incluir las siguientes funciones:
```python
def q3_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python
Returns: 
[("LATAM321", 387), ("LATAM_CHI", 129), ...]
```
"""
from typing import List, Tuple
import json
from collections import Counter
import re  # Para usar expresiones regulares

def count_user_mentions(file_path: str) -> List[Tuple[str, int]]:
    mention_counts = Counter()

    # Abrir el archivo y leer línea por línea
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line.strip())
            content = tweet["content"]

            # Encontrar todas las menciones en el contenido del tweet
            mentions = re.findall(r'@(\w+)', content)
            mention_counts.update(mentions)

    # Obtener los 10 usuarios más mencionados
    top_users = mention_counts.most_common(10)

    return top_users

# Ejemplo de uso
file_path = 'farmers-protest-tweets-2021-2-4.json'

# Obtener y mostrar los top 10 usuarios más mencionados
top_users = count_user_mentions(file_path)
print("Top 10 usuarios más mencionados:")
for username, count in top_users:
    print(f"{username}: {count}")

