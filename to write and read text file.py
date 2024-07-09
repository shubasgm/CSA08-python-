# Writing to a text file
def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

# Reading from a text file
def read_from_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content

# Updating a text file
def update_file(filename, new_content):
    with open(filename, 'a') as f:
        f.write(new_content)

# Example usage
filename = 'example.txt'

# Write to the file
write_to_file(filename, 'This is the initial content.')

# Read from the file
print('Initial content:')
print(read_from_file(filename))

# Update the file
update_file(filename, '\nThis is the updated content.')

# Read from the file again
print('\nUpdated content:')
print(read_from_file(filename))

