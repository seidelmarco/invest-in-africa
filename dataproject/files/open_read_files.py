fhand_caledonia = open('caledonia.txt', 'r')
fhand_impala = open('impala.txt', 'r')
print(fhand_caledonia)
print(fhand_impala)

#While the file handle does not contain the data for the file, it is quite easy to construct a for loop to read through
# and count each of the lines in a file:

count = 0
for line in fhand_caledonia:
    count += 1
print('Line Count:', count)

#ONLY! If you know the file is relatively small compared to the size of your main memory, you can read the whole file
# into one string using the read method on the file handle.

fhand_caledonia = open('caledonia.txt')
one_big_string = fhand_caledonia.read()
print(len(one_big_string))
print(one_big_string[:100])
print('------------------------------------')
fhand_caledonia = open('caledonia.txt')
count = 0

for line in fhand_caledonia:
    count += 1
    line = line.rstrip()  #um newline-blanke-linien zu strippen
    # Skip 'uninteresting lines' ('not' ist der Trick - ohne not wird jede Zeile geparsed, dann muss print aber indented sein
    if not line.startswith('BlackRock'):
        continue
    # Process our 'interesting' line
    print(f'Line-Nr.: {count} -- {line}')
    if line.find('blackrock'):
        print(f'Line-Nr.: {count} -- {line}')

print('------------------------------------')

'''
Since find looks for an occurrence of a string within another string and either returns the position of the string 
or -1 if the string was not found, we can write the following loop to show lines which contain the string “...” 

Ohne -1 schreibt print den gesamten Text (String) - der Trick ist -1 und continue, um den neuen String ... rauszulösen
'''

try:
    fname = input('Enter filename: ')
    fhand = open(fname)
    count = 0
    query = input('Enter search query: ').lower()

    for line in fhand:
        count += 1
        line = line.rstrip()
        if line.find(query) == -1:
            continue
        elif line.startswith(query):
            print(f'Line-Nr.: {count} -- {line}')
        else:
            print(f'Line-Nr.: {count} -- {line}')

except FileNotFoundError:
    print('Diese Datei existiert in diesem Verzeichnis nicht.')

# Variante, um try und except enger zu gestalten mit exit()
'''
fname = input('Enter filename: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('Selber bla bla.')
    exit()
count = 0
query = input('Enter search query: ').lower()
for line in fhand:
    count += 1
    line = line.rstrip()
    if line.find(query) == -1:
        continue
    print(f'Line-Nr.: {count} -- {line}')
'''

fileout = open('fileout.txt', 'w')
print(fileout)
line1 = 'If the file already exists, opening it in write mode clears out the old data and starts fresh, so be careful!\n'
line2 = 'If the file doesn’t exist, a new one is created.\n'
line3 = 'The write method of the file handle object puts data into the file, returning the number of characters\n'
line4 = 'written. The default write mode is text for writing (and reading) strings.\n'
fileout.write(line1)
fileout.write(line2)
fileout.write(line3)
fileout.write(line4)
fileout.close()
print(repr(line1))
print(repr(line2))






