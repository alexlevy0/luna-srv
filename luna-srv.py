import time


def main():
    for i in range(10):
        print(f"Ligne {i}: contenu de test")
        time.sleep(1)  # Attendre 1 seconde entre chaque ligne


if __name__ == "__main__":
    main()
