# Use the open and read methods to slurp the entire contents of your pelican.txt file
open_file = open('pelican.txt', 'r')
read_file = open('pelican.txt').read()
# Display the type of the returned data and print the contents of the returned data.
print(read_file)

# What data type is the output?
print(type(read_file))
# String

# Now, write some code that will read the pelican.txt file into a list and then output the number of items within the list.
pelican_list = open('pelican.txt').read().splitlines()
print(pelican_list)
print(len(pelican_list))
# 5

# Now use a loop to iterate over and print the contents of the file. Be sure not to include any blank lines in the output.
for lines in open_file:
    print(lines, end="")