# Write a line of code to create a file handle to open and append to a file called pelican.txt
new_file = open('pelican.txt', 'a+')

# Append the following line to the file using the write method of the file handle: “A wonderful bird is the pelican,”
new_file.write('A wonderful bird is the pelican\n')

# Append the following second line using the write method: “His bill holds more than his belican.”
new_file.write('His bill holds more than his belican\n')

# Create a list that contains the following lines:
lines = ['He can take in his beak,\nEnough food for a week,\nBut I’m damned if I see how the helican.\n']

# Append this list to the file using the writelines method.
new_file.writelines(lines)

# Why are the “\n” required?
# To put them on a new line in the .txt file