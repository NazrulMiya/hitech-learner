# String of class 'str' is created using either Single Quote or Double Quote

quote_1 = 'single quoted'
quote_2 = "double quoted"

print(quote_1, quote_2,'\n')

# Special Escape Characters
new_line = 'line1\nline2\nline3\n'
print(new_line)

tab_char = 'col1\tcol2\tcol3\t'
print(tab_char)

backslash = 'the backslash : \\'
print(backslash)


#raw string is used to prevent escape sequence interpretation
raw_new_line = r'line1\nline2\nline3\n'
print(raw_new_line)

raw_backslash = r'the backslash : \\'
print(raw_backslash)

# Operations
sub_text = 'double'
print('\nsub_text = ',sub_text)
print(sub_text + sub_text)
print('_'*40)
print('Length of String ', len(sub_text))
print('Min Character in Alphabetical Order ',min(sub_text))
print('Max Character in Alphabetical Order ',max(sub_text))
print('Check a string presents in another string ', sub_text in quote_2)
print('Check a string not presents in another string ', sub_text not in quote_1)

# String Functions
stmt = 'The quick brown fox jumps over the lazy dog'
print('\nOccurence of a Character ', stmt.count('o'))
print('Index of First Occurence of a Character ', stmt.index('u'))
print('Index of First Occurence within a range ', stmt.index('u', 7, 26))

print('returns the index of first occurrence of the substring (if found). If not found, it returns -1.', stmt.find('o'))
print('If the string starts with ', stmt.startswith('The'))
print('If the string ends with ',stmt.endswith('The'))
print('If the string ends with ',stmt.endswith('dog'))
print('Convert into Uppercase ', stmt.upper())
print('Convert into Lowercase ', stmt.lower())
print('First Character into Uppercase ', stmt.capitalize())

stmt = 'The, quick,brown,fox,jumps,over,the,lazy,dog'
print('\nSplitting a string and returns list ', stmt.split(','))
print('if no delimiter given then by default splits based on whitespace')


email = 'abc123@gmail.com'
print('\nCheck if string contains only alpahbetics ', email.isalpha())
name = 'rocky'
print('\nCheck if string contains alpahbetics ', name.isalpha())

mobile = '123454'
print('\nCheck if string contains digit ', mobile.isdigit())
address = '4th Cross'
print('\nCheck if string contains digit ', address.isdigit())




print('\nReplace chars in a string ', address.replace('4th' , '5th'))

stmt = ' Assanitation '
print('\nTriming from both start and end :', stmt.strip())
print('Trimming Chars :', stmt.strip('on '))


