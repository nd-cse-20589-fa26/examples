#!/usr/bin/env python3

class Person:                                   # Discuss: Class as templates
    def __init__(self, first: str, last: str):  # Discuss: Constructor
        self.first = first
        self.last  = last

    def __lt__(self, other):                    # Discuss: Magic/Dunder methods
        if self.last == other.last:
            return self.first < other.first
        return self.last < other.last

People = (
    Person('Peter'      , 'Parker'),
    Person('Mary Jane'  , 'Watson'),
    Person('Gwen'       , 'Stacy'),
    Person('Peter'      , 'Bui'),
    Person('Joshua'     , 'Bui'),
)

# Sort -> Error b/c no __lt__

'''
for p in sorted(People):
    print(p.first, p.last)
'''

# Sort by first name

'''
for p in sorted(People, key=lambda p: p.first):
    print(p.first, p.last)
'''

# Sort by last name then first name

'''
for p in sorted(People, key=lambda p: (p.last, p.first)):
    print(p.first, p.last)
'''

# Sort -> After implementing __lt__

for p in sorted(People):
    print(p.first, p.last)
