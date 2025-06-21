#python program that accepts a word from the user and reverses it
word = input("Enter a word: ")
rev = ''
for i in range(-1,-(len(word)+1),-1):
    ch = word[i]
    rev = rev + ch
print(rev)