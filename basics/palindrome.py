word = input("Enter a word :")

reverse_word = ""
flage = 0

for i in word:
     reverse_word = i+reverse_word
if reverse_word == word :          
# reverse_word = reverse_word+i
 print(f"reverse word : {reverse_word}")
 print("the word is palindrome .")
else :
   print("the word is not palindrome")