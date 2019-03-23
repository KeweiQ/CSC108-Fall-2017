""" CSC108 Assignment 3: Social Networks - Starter code """
from typing import List, Tuple, Dict, TextIO


def get_first_name(s: List[str]) -> str:
    """Get a person's first name from string s which elements are words
    of his/her name.
    
    >>> get_first_name(['Haley', 'Gwendolyn', 'Dunphy'])
    'Haley Gwendolyn'
    """
    
    a = ''
    
    for i in range(len(s) - 1):
        a = a + ' ' + s[i]
        
    return a.strip()

def get_full_name(file: str) -> str:
    """Get a person's full name from string s which elements are words
    of his/her name.
    
    >>> get_full_name('Dunphy, Haley Gwendolyn')
    'Haley Gwendolyn Dunphy'
    """
    
    a = file.split()
    c = ''
    
    for i in range(1, len(a)):
        c = c + ' ' + a[i]
    c = c.lstrip() + ' ' + a[0].rstrip(',')
    
    return c

def check_in_friends(person: str, person_to_friends: Dict[str, List[str]]) \
                     -> bool:
    """Check if a person is in person_to_friends dic.
    """
    
    return person in person_to_friends

def check_in_networks(person: str, person_to_networks: Dict[str, List[str]]) \
                      -> bool:
    """Check if a person is in person_to_networks dic.
    """
    
    return person in person_to_networks

def get_score_from_friends_v1(person: str, p: str, person_to_friends: \
                              Dict[str, List[str]]) -> int:
    """Add score if both person and p has same friend in person_to_friends dic.
    """
    
    s = 0
    
    if person in person_to_friends and p in person_to_friends:
        for i in person_to_friends[p]:
            if i in person_to_friends[person]:
                s = s + 1
    
    return s

def get_score_from_friends_v2(person: str, p: str, person_to_friends: \
                              Dict[str, List[str]]) -> int:
    """Add score if both person and p has same friend.
    """
    
    s = 0
    
    if person in person_to_friends:
        if p in person_to_friends[person]:
            s = s + 1
    
    return s

def get_score_from_networks(person: str, p: str, person_to_networks: \
                            Dict[str, List[str]]) -> int:
    """Add score if both person and p belongs to same network
    in person_to_networks dic.
    """
    
    s = 0
    
    if person in person_to_networks and p in person_to_networks:
        for i in person_to_networks[p]:
            if i in person_to_networks[person]:
                s = s + 1    
    
    return s

def get_score_from_families(score: int, person: str, p: str) -> int:
    """Add score if person and p have same family name.
    """
    
    s = 0
    a = person.split()
    b = p.split()
    
    if score != 0 and a[-1] == b[-1]:
        s = 1
            
    return s

def already_friend(person: str, p: str, person_to_friends: \
                   Dict[str, List[str]]) -> bool:
    """Check whether p is already a friend pf person.
    """
    
    a = False
    
    if person in person_to_friends and p in person_to_friends[person]:
        a = True
        
    return a

def recommendations_append(data: tuple, recommendations: List[tuple]) -> None:
    """Judge whether score is zero and whether should append data to recommendations.
    """
    
    if data[1] != 0 and data not in recommendations:
        recommendations.append(data)

def sort_order(r: List[tuple]) -> List[tuple]:
    """Sort the recomendation order.
    
    >>> sort_order([('Luke Dunphy', 1), ('Cameron Tucker', 1), \
     ('Mitchell Pritchett', 2), ('Phil Dunphy', 1)])
    [('Mitchell Pritchett', 2), ('Cameron Tucker', 1), ('Luke Dunphy', 1), \
('Phil Dunphy', 1)]
    """
    
    a = 0
    b = 1
    end = len(r) - 1
    
    while end != 0:
        for i in range(end):
            if r[i][1] < r[i + 1][1]:
                r[i], r[i + 1] = r[i + 1], r[i]
        end = end - 1
    while a < len(r) and b < len(r):
        while b < len(r) and r[b][1] == r[a][1]:
            b = b + 1
        end = b - a
        while end != 0:
            for i in range(a, b - 1):
                if r[i][0] > r[i + 1][0]:
                    r[i], r[i + 1] = r[i + 1], r[i]
            end = end - 1                
        a = b
        b = b + 1
        
    return r

def assign_data(data1: str, data2: str, d: Dict[str, List[str]]) -> None:
    """Judge whether data1 is a key in d and whether need add data2 in d.
    
    >>> i = {'c': ['b']}
    >>> assign_data('a', 'b', i)
    >>> i
    {'c': ['b'], 'a': ['b']}
    """
    
    if data1 not in d:
        d[data1] = [data2]
    elif data1 in d and data2 not in d[data1]:
        d[data1].append(data2)

def sort_dict(d: Dict[str, List[str]]) -> None:
    """Sort the values in dict in alphabetical order.
    """
    
    for i in d:
        d[i].sort()
        
def remove_new_line(p: list) -> None:
    """Remove new line character in elements of p.
    """
    
    for i in range(len(p)):
        if p[i] != '\n':
            p[i] = p[i].rstrip('\n')      


def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """

    p = profiles_file.readlines()
    a = 0
    b = 1
    
    remove_new_line(p)
    while a < len(p) and b < len(p):
        if ',' in p[b]:
            assign_data(get_full_name(p[a]), get_full_name(p[b]), person_to_friends)
            b = b + 1
        elif ',' not in p[b] and p[b] != '\n':
            assign_data(get_full_name(p[a]), p[b], person_to_networks)
            b = b + 1
        else:
            a = b + 1
            b = b + 2
            
    sort_dict(person_to_friends)
    sort_dict(person_to_networks)    

def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """Return the average number of friends that people who appear as keys
    in the given "person to friends" dictionary have.
    
    >>> get_average_friend_count({'Jay Pritchett': ['Claire Dunphy', \
     'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', \
     'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett', \
     'Jay Pritchett', 'Luke Dunphy'], 'Mitchell Pritchett': ['Cameron Tucker', \
     'Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], \
     'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'], \
     'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], \
     'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': \
     ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': \
     ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'], 'Luke Dunphy': \
     ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']})
    2.5454545454545454
    """
    
    person = 0
    friends = 0
    
    if person_to_friends != {}:
        for i in person_to_friends:
            person = person + 1
            friends = friends + len(person_to_friends[i])
        avg = friends / person
    else:
        avg = 0.0
    
    return avg
    
def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last_name_to_first_names" dictionary based on the given 
    "person_to_friends" dictionary.
    Names in the list should be unique: no one should be listed more than once.
    
    >>> get_families({'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
     'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', \
     'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', \
     'Luke Dunphy'], 'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', \
     'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': \
     ['Gloria Pritchett', 'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': \
     ['Dylan D-Money', 'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy', \
     'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], \
     'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'], \
     'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', \
     'Phil Dunphy']})
    {'Pritchett': ['Gloria', 'Jay', 'Mitchell'], 'Dunphy': ['Alex', 'Claire', \
'Haley Gwendolyn', 'Luke', 'Phil'], 'Delgado': ['Manny'], 'Tucker': ['Cameron'], \
'D-Money': ['Dylan'], 'D-Cat': ['Chairman', 'Gilbert']}
    """

    people = []
    p = []
    f = ''
    last_name_to_first_names = {}
    
    for person in person_to_friends:
        if person not in p:
            p.append(person)
        for friend in person_to_friends[person]:
            if friend not in p:
                p.append(friend)
    for i in p:
        people = i.split()
        f = get_first_name(people)
        assign_data(people[-1], f, last_name_to_first_names)
        people = []
        f = ''
            
    sort_dict(last_name_to_first_names)
        
    return last_name_to_first_names

def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "network_to_people" dictionary based on the given
    "person_to_networks" dictionary.
    The values in the dictionary are sorted alphabetically.
    
    >>> invert_network({'Claire Dunphy': ['Parent Teacher Association'], \
     'Manny Delgado': ['Chess Club'], 'Mitchell Pritchett': ['Law Association'], \
     'Alex Dunphy': ['Chess Club', 'Orchestra'], 'Cameron Tucker': \
     ['Clown School', 'Wizard of Oz Fan Club'], 'Phil Dunphy': \
     ['Real Estate Association'], 'Gloria Pritchett': ['Parent Teacher Association']})
    {'Parent Teacher Association': ['Claire Dunphy', 'Gloria Pritchett'], \
'Chess Club': ['Alex Dunphy', 'Manny Delgado'], 'Law Association': \
['Mitchell Pritchett'], 'Orchestra': ['Alex Dunphy'], 'Clown School': \
['Cameron Tucker'], 'Wizard of Oz Fan Club': ['Cameron Tucker'], \
'Real Estate Association': ['Phil Dunphy']}
    """

    network_to_people = {}
    
    for person in person_to_networks:
        for i in person_to_networks[person]:
            assign_data(i, person, network_to_people)
    sort_dict(network_to_people)
        
    return network_to_people

def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
    person: str) -> List[str]:
    """Given a "person to friends" dictionary and the name of a person, return 
    the list of names of people who are friends of the named person's friends. 
    The returned list should be sorted in alphabetical order and should not 
    contain the original person.
    The name of a friend of a friend should appear in the returned list once 
    for each mutual friend.
    
    >>> get_friends_of_friends({'Jay Pritchett': ['Claire Dunphy', \
     'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', \
     'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett', \
     'Jay Pritchett', 'Luke Dunphy'], 'Mitchell Pritchett': ['Cameron Tucker', \
     'Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], \
     'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'], \
     'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], \
     'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': \
     ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': \
     ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'], 'Luke Dunphy': \
     ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']}, \
     'Jay Pritchett')
    ['Cameron Tucker', 'Gloria Pritchett', 'Luke Dunphy', 'Manny Delgado', \
'Mitchell Pritchett', 'Phil Dunphy']
    >>>
    """
    
    f = []
    
    for people in person_to_friends[person]:
        for i in person_to_friends[people]:
            if i != person:
                f.append(i)
    f.sort()
    
    return f

def make_recommendations(person: str, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> List[Tuple[str, int]]:
    """Return the friend recommendations for the given person as a list of 
    tuples where the first element of each tuple is a potential friend's name 
    and the second element is that potential friend's score. 
    Only potential friends with non-zero scores should be included in the list.
    The recommendations should be sorted from highest to lowest score.
    If multiple people have the same score, they should be sorted alphabetically.
    
    >>> make_recommendations('Jay Pritchett', {'Jay Pritchett': ['Claire Dunphy', \
     'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', \
     'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett', \
     'Jay Pritchett', 'Luke Dunphy'], 'Mitchell Pritchett': ['Cameron Tucker', \
     'Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], \
     'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'], \
     'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], \
     'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': \
     ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': \
     ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'], 'Luke Dunphy': \
     ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']}, \
     {'Claire Dunphy': ['Parent Teacher Association'], 'Manny Delgado': \
     ['Chess Club'], 'Mitchell Pritchett': ['Law Association'], 'Alex Dunphy': \
     ['Chess Club', 'Orchestra'], 'Cameron Tucker': ['Clown School', \
     'Wizard of Oz Fan Club'], 'Phil Dunphy': ['Real Estate Association'], \
     'Gloria Pritchett': ['Parent Teacher Association']})
    [('Mitchell Pritchett', 2), ('Cameron Tucker', 1), ('Luke Dunphy', 1), \
('Phil Dunphy', 1)]
    """
    
    score = 0
    a = check_in_friends(person, person_to_friends)
    b = check_in_networks(person, person_to_networks)
    recommendations = [] 
    
    if a or b is True:
        for p in person_to_friends:
            if already_friend(person, p, person_to_friends) is False and p != person:
                score += get_score_from_friends_v1(person, p, person_to_friends)
                score += get_score_from_networks(person, p, person_to_networks)
                score += get_score_from_families(score, person, p)
                recommendations_append((p, score), recommendations)
                score = 0
        for p in person_to_networks:
            if already_friend(person, p, person_to_friends) is False and p != person:
                score += get_score_from_friends_v1(person, p, person_to_friends)
                score += get_score_from_networks(person, p, person_to_networks)
                score += get_score_from_families(score, person, p)
                recommendations_append((p, score), recommendations)
                score = 0              
        for p in person_to_friends:
            for i in person_to_friends[p]:
                if already_friend(person, i, person_to_friends) is False and i != person:
                    score += get_score_from_friends_v2(person, p, person_to_friends)
                    score += get_score_from_networks(person, i, person_to_networks)
                    score += get_score_from_families(score, person, i)
                    recommendations_append((i, score), recommendations)
                    score = 0              
    if recommendations != []:
        recommendations = sort_order(recommendations)
    
    return recommendations


if __name__ == '__main__':
    import doctest
    doctest.testmod()