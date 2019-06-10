import re # library for regular expressions
import collections # library that helps count the occurences of words 

text = open('book.txt').read().lower() # read everything into a string and in lower case
words = re.findall('\w+', text) # 'findall' ensures all occurances of t5he pattern are found. '\w+' = w is not a white-space & + is one or more.  
print(collections.Counter(words).most_common(10)) # Counter method used to help find 10 most common words

