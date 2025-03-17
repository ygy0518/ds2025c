import random

random_number = random.randint(1, 100)
win = False

for guesses in range(7):
    print(f"{7-guesses}번 기회 남음. 숫자 입력 : ", end="")
    guess = int(input())

    if random_number == guess:
        print("정답")
        win = True
        break
    elif random_number < guess:
        print("더 작아")
    else:
        print("더 커")