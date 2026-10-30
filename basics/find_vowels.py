print("Enter a word to find vowel (only small latter).")

word = input("Word:")
count = 0

for i in word :
    if i=="a"  or i=="e"   or i=="i" or i=="o"  or i=="u"  :
        count = count+1
print(count)    


