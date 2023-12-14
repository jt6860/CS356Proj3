# -*- coding: utf-8 -*-
"""
@author: John Torres
"""

# Creating a Dictionary 
# Key, Value = US State, US State Capital 
Dict = {'Alabama': 'Montgomery', 
        'Alaska': 'Juneau', 
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'St. Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'}

# Dictionary pre-enumeration
# Dict length
print('Dictionary pre-enumeration: ')
print(Dict)
print('')

# Command that enumerates the contents of key–values in the dictionary.
print('Enumerated dictionary: ')
enumDict = tuple(enumerate(Dict.items()))
print(enumDict)
print('')

# Dict length
print('Dict length: ')
print(len(Dict))
print('')

# Command that lists all keys.
print('Keys: ')
print(Dict.keys()) 
print('')

# Command that lists all values.
print('Values: ')
print(Dict.values())
print('')

# Command that replaces key number "1" with a new value.
# 1 is Alaska, Juneau will change to Anchorage
print('Value at [1] - Before: ')
print(enumDict[1])
print('Value at [1] - After: ')
Dict['Alaska']  =  'Anchorage'
enumDict = tuple(enumerate(Dict.items()))
print(enumDict[1])