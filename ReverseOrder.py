word = str(input("please enter a sentence: "))
def reverse1(word):
    word1 = word.split()
    #word1.reverse()
    #print(word1)
    #return " ".join(word1)
    return " ".join(word.split()[::-1])

print(reverse1(word))