'''
------------------------
----BASIC-INFO
------------
Creation
    JakubP (June 2017)
Library full name
    JakubP's Search Engine
------------------------
----DETAILS
------------
Library was created to make searching and related manipulations easier.
There are no external dependencies.
------------------------
----LIST-OF-FUNCTIONS
lookfor(subject, look_in, mode, scope)
count(subject, look_in, start_at, end_at)
remove_elms_with(subject, element, position)
------------
------------------------
----TESTING
------------
Import this library and call:
    >search.testlib((LIST)input_list, (STR)subject)
Whole library must be imported.
Test won't influence your data
------------------------
'''


#----#----#----#----#----#----#----#----
#Input
    #(STR)Subject
    #(LIST)LookIn
    #(INT)StartAt
#Output
    #None
#Return
    #(INT)IndexOfList that is equal to Subject
#----#----#----#----
def lookfor(subject, look_in, mode, scope = (0, 0)):
    start_at = scope[0]
    end_at = scope[1]
    if end_at == 0:
        end_at = len(look_in)-start_at
    target = look_in[start_at:end_at]
    for q in enumerate(target):
        index = q[0]
        if mode == "equals":
            if target[index] == subject:
                return index + start_at
        elif mode == "contains":
            if subject in target[index]:
                return index + start_at
        else:
            print("SEARCH.LOOKFOR: Error: InvalidArgument \"MODE\"")
            return


def count(subject, look_in, scope = (0, 0)):
    howmany = 0
    look_in = look_in[start_at:end_at]
    for q in enumerate(look_in):
        index = q[0]+start_at
        if look_in[index] == subject:
            howmany += 1
    return howmany

def remove_elms_with(subject, element, position):
    newtable = []
    new_index = 0
    for q in enumerate(subject):
        index = q[0]
        if subject[index][position] != element:
            newtable.append(subject[index])
            new_index += 1
    return newtable

def testlib(input, subject):
    pass
