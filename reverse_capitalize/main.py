words = input().split(',')

capitalized = [word.strip().capitalize() for word in words]
capitalized.reverse()

for word in capitalized:
    print(word)
