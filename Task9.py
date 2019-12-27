import re


def first():
    rows = ['abcdefg', 'abcde', 'abc']
    for row in rows:
        if re.search("abc", row):
            print('We found a match! ', row)


def second():
    rows = ['abc123xyz', 'define "123', 'var g = 123;']
    for row in rows:
        if re.search("123", row):
            print('We found a match! ', row)


def third():
    rows = ['cat.', '869.', '?=+.', 'abc1']
    for row in rows:
        if re.search("...\.", row):
            print('We found a match! ', row)


def fourth():
    rows = ['can', 'man', 'fan', 'dan', 'ran', 'pan']
    for row in rows:
        if re.search("[cfm]an", row):
            print('We found a match! ', row)


def fifth():
    rows = ['hog', 'dog', 'bog']
    for row in rows:
        if re.search("[^b]og", row):
            print('We found a match! ', row)


def sixth():
    rows = ['Ana', 'Bob', 'Cpc', 'aax', 'bby', 'ccz']
    for row in rows:
        if re.search("[A-C][n-p][a-c]", row):
            print('We found a match! ', row)


def seventh():
    rows = ['wazzzzzup', 'wazzzup', 'wazup']
    for row in rows:
        if re.search("..z{2,5}..", row):
            print('We found a match! ', row)


def eighth():
    rows = ['aaaabcc', 'aabbbbc', 'aacc', 'a']
    for row in rows:
        if re.search("a+b*c+", row):
            print('We found a match! ', row)


def ninth():
    rows = ['1 file found?', '2 files found?', '24 files found?', 'No files found.']
    for row in rows:
        if re.search("\d+ files? found\?", row):
            print('We found a match! ', row)


def tenth():
    rows = ['1.   abc', '2.	abc', '3.           abc', '4.abc']
    for row in rows:
        if re.search("\d.\s+abc", row):
            print('We found a match! ', row)


def eleventh():
    rows = ['Mission: successful', 'Last Mission: unsuccessful', 'Next Mission: successful upon capture of target']
    for row in rows:
        if re.search("^Mission: successful$", row):
            print('We found a match! ', row)


def twelfth():
    rows = ['file_record_transcript.pdf', 'file_07241999.pdf', 'testfile_fake.pdf.tmp']
    for row in rows:
        if re.search("^(file_\d*\D*)\.pdf$", row):
            print('We found a match! ', row)


def thirteenth():
    rows = ['Jan 1987', 'May 1969', 'Aug 2011']
    for row in rows:
        if re.search("(\w+ (\d{1,4}))", row):
            print('We found a match! ', row)


def fourteenth():
    rows = ['1280x720', '1920x1600', '1024x768']
    for row in rows:
        if re.search("(\d+)x(\d+)", row):
            print('We found a match! ', row)


def fifteenth():
    rows = ['I love cats', 'I love dogs', 'I love logs', '	I love cogs']
    for row in rows:
        if re.search("I love (cats|dogs)", row):
            print('We found a match! ', row)


def sixteenth():
    rows = ['The quick brown fox jumps over the lazy dog.',
            'There were 614 instances of students getting 90.0% or above.',
            'The FCC had to censor the network for saying &$#*@!.']
    for row in rows:
        if re.search("The.*", row):
            print('We found a match! ', row)


if __name__ == '__main__':
    first()
    second()
    third()
    fourth()
    fifth()
    sixth()
    seventh()
    eighth()
    ninth()
    tenth()
    eleventh()
    twelfth()
    thirteenth()
    fourteenth()
    fifteenth()
    sixteenth()
