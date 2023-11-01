wordDict = open("WorldleDict").read().splitlines()
letterValues = {
    "a" : 8500,
    "e" : 7800,
    "s" : 6500,
    "o" : 5100,
    "r" : 5050,
    "i" : 5000,
    "l" : 4100,
    "t" : 4050,
    "n" : 4000,
    "u" : 3500,
    "d" : 3000,
    "c" : 2950,
    "y" : 2800,
    "m" : 2750,
    "p" : 2450,
    "h" : 2450,
    "b" : 2200,
    "g" : 2000,
    "k" : 1800,
    "f" : 1400,
    "w" : 1350,
    "v" : 1000,
    "z" : 500,
    "j" : 400,
    "x" : 250,
    "q" : 150}
guesswords = []
yellowLetters = []
notinWord = []
guess = ['_', '_', '_', '_', '_']
newDict = wordDict.copy()

def value(str):
    total = 0
    seen = set()
    for i in str:
        total += letterValues[i]
        if i in seen:
            total -= letterValues[i]/2
        seen.add(i)
    return total

def Check(word):
    for letter in notinWord:
        if letter in word:
            newDict.remove(word)
            return
    for tup in yellowLetters:
        letter = tup[0]
        pos = tup[1]-1
        if letter not in word:
            newDict.remove(word)
            return
        elif word[pos] == letter:
            newDict.remove(word)
            return
    for i in range(len(guess)):
        if guess[i] != '_':
            if word[i] != guess[i]:
                newDict.remove(word)
                return



def pickword():
    global wordDict
    for word in wordDict:
        Check(word)
    wordDict = newDict.copy()
    mx = 0
    for word in wordDict:
        n = value(word)
        if n > mx:
            w = word
            mx = n
    return w

def main():
    print("Welcome to the WordleCracker")
    print("I recommend slate as a first guess, but you can choose whatever you wish!")
    count = 0
    while True:
        if count != 0:
            boolean = input("Was your guess right? (y/n)")
            if boolean == "y":
                break
        if count < 1:
            word = input("Enter your guess here: ")
        guesswords.append(word)
        yellows = input("Enter where the yellows were: for example 4 means there was a yellow at letter 4: ")
        greens = input("Enter where the greens were: for example 4 means there was a green at letter 4: ")
        for i in yellows:
            i = int(i)
            yellowLetters.append((word[i - 1], int(i)))
        for i in greens:
            i = int(i)
            guess[i-1] = word[i-1]
        for i in range(1, 6):
            if str(i) not in greens and str(i) not in yellows and word[i-1] not in guess:
                t = True
                for tup in yellowLetters:
                    if tup[0] == word[i-1]:
                        t = False
                if t:
                    notinWord.append(word[i - 1])
        word = pickword()
        print(word)
        count += 1

    print("congrats!")


main()

