scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

nickname = input("Pseudo: ")

score = input("Score: ")
score = int(score)

scores[nickname] = score

print(f"Score de Elocin03: {scores['Elocin03']}")
print(f"Score de {nickname}: {scores[nickname]}")