f = open('/home/ubuntu/environment/files/relative_data.txt', 'r') # opens the data.txt file for 'r' reading & stored  in 'f' file handle
lines = f.read() # calls the readlines method
f.close() # close our file handle = f
print(lines) # print results to screen
