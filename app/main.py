# app/main.py

def add(a: int, b: int) -> int:
"""Addition simple — testable par pytest."""
return a + b


if __name__ == "__main__":
# Exécution minimale pour démonstration
print("Exemple: add(2,3) =", add(2, 3))