def palindrome():
    name = input("please enter a word: ")

    try:
        namecheck = str(name)
    except:
        print("please enter a string")
        palindrome()

    name1 = name[::-1]
    print(name1)

    if name.lower() ==  name1.lower():
        print("given letter is palindrome")
    else:
        print("given letter is not palindrome")
palindrome()


def reverse(a):
    word = ''
    for i in range(len(a)):
        word+=a[-1-i]
    print(word)

reverse("dominate")
print("dominate")
