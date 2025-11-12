L=[12,14,19,15,22]
print(L[4])
for index in range (1000):
    print("coucou à la personne",index)   
def palindrome (mot):
    if mot ==mot [::-1]:
        return "se mot est palindrome "
    else:
        return "se mot est ps palindrome"
print(palindrome("radar"))
print(palindrome("été "))