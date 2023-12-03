'''
A School File contains information about the profs that teach at different schools. Here is a sample School File,
schools.txt:

SCHOOL UTM
PROF 62 Daniel Zingaro
PROF 7 Petersen
SCHOOL Hogwarts
PROF 9 Hagrid
PROF 10 Albus Dumbledore
PROF 2 Minerva McGonagall
PROF 4567 Lupin
PROF 7 Flitwick

Notice that each school begins with a line that consists of the word SCHOOL followed by the school name. Each line
for this school consists of the word PROF, the prof's ID, and then the prof's name. There are no blank lines in the
file.
Write the code for the following function that takes an open School File and returns a dictionary. Each key in the
dictionary is a school name, and each value is a list of the profs that teach at that school.
For example, if the function were called on schools.txt, like this:
read_all_schools(open('schools.txt'))
Then the result might be this dictionary:
{'UTM': ['Daniel Zingaro', 'Petersen'],
'Hogwarts': ['Hagrid', 'Albus Dumbledore', 'Minerva McGonagall', 'Lupin', 'Flitwick']}
'''
from typing import TextIO
def read_all_schools(f: TextIO) -> dict[str, list[str]]:
    '''f is an open School File.
    Return a dictionary where each key is the name of a school,
    and each value is the list of profs that teach at that school.
    '''
    # Your code here
    


f = open("Final Reveiw/school_file.txt",'r')
exc = {'UTM': ['Daniel Zingaro', 'Petersen'],'Hogwarts': ['Hagrid', 'Albus Dumbledore', 'Minerva McGonagall', 'Lupin', 'Flitwick']}
print(read_all_schools(f) == exc)
f.close()
