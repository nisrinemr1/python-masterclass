scores = {"MokoSempai": 16, "Grungi": 30, "Elocin03": 56}

nickname = input("Pseudo: ")

score = input("Score: ")
score = int(score)

scores[nickname] = score

for key, value in scores.items():
    print(f"{key}: {value}")
