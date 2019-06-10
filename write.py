f = open('newfile.txt', 'a') # opens the data.txt file for 'a' append & stored  in 'f' file handle. 
lines = ['Hello','World','Welcome','To','File IO']
text = '\n'.join(lines)
f.writelines(text)
f.close() # close our file handle = f
