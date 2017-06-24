'''
------------------------
----BASIC-INFO
------------
Creation
    JakubP (June 2017)
Library full name
    JakubP's Word-delimeted File Format
------------------------
----DETAILS
------------
Format was created to store Python Dictionaries in file.
There are no dependencies outside this package.
------------------------
----LIST-OF-FUNCTIONS
get_grammar()
load(filename)
write(filename, data)
------------
'''

#Define grammar
def get_grammar():
    defines = {
        "scope_bgn"         : "!bgn",
        "scope_end"         : "!end",
        "status_load"       : "*load",
        "status_ignore"     : "*ignore",
        "tuple_begin"       : "<",
        "tuple_end"         : ">",
        "char_comment"      : "#",
        "tuple_sep"         : " ",
    }
    return defines


################
#LOAD WDF FILE
def load(filename):
    try:
        import filestream
        import search
    except:
        print("WDF:Load:::This library requires")
        print(" > \"FILESTREAM\" package")
        print(" > \"SEARCH\" package ")
    #Load defines
    defines = get_grammar()
    #Load file
    wordlist = filestream.read(filename, "words")
    #Delete SingleWordComments from WordList
    wordlist = search.remove_elms_with(wordlist, defines["char_comment"], 0)

    #Initialize
    loadmode = 0
    newlist = []
    tuplemode = 0
    current_tuple = ""

    #Main Analysis Loop
    for q in range(len(wordlist)):
        if wordlist[q-1] == defines["status_load"]:
            if wordlist[q-2] == defines["scope_bgn"]:
                loadmode = 1
        if wordlist[q] == defines["scope_end"]:
            loadmode = 0
        if loadmode == 1:
            savethis = 1
            savetuple = 0
            if wordlist[q][0] == defines["tuple_begin"]:
                tuplemode = 1
                savethis = 0
            elif wordlist[q][0] == defines["tuple_end"]:
                tuplemode = 0
                savetuple = 1

            if tuplemode == 1:
                current_tuple += wordlist[q] + defines["tuple_sep"]
            if tuplemode == 0:
                newlist.append(wordlist[q])

            if savetuple == 1:
                del newlist[-1]
                newlist.append(current_tuple[2:-1])
                current_tuple = ""

    #Wrap data into Dictionaries
    data = {}
    for q in enumerate(newlist[:-1]):
        index = q[0]
        if index %2 == 0:
            data.update({ newlist[index]: newlist[index+1], })

    #Done
    return data



################
#CREATE WDF FILE
#Input: List of dictionaries
def write(filename, data):
    try:
        import filestream
    except:
        print("WDF:Load:::This library requires")
        print(" > \"FILESTREAM\" package")
    #Load defines
    defines = get_grammar()
    output = ""
    for q in enumerate(data):
        current_dic = data[q[0]]
        bgn_active = defines["scope_bgn"] + " " + defines["status_load"]
        output += bgn_active + "\n"
        for x in enumerate(current_dic):

            #WordTuple Creation
            if len(current_dic[x[1]].split()) > 1:
                crnt = current_dic[x[1]]
                if crnt[0] != defines["tuple_begin"]:
                    crnt = defines["tuple_begin"] + " " + crnt
                    crnt += " " + defines["tuple_end"]
                    current_dic[x[1]] = crnt

            spaces = ""
            for i in range(20- len(x[1])):
                spaces += " "
            output += "    " + x[1] + spaces + current_dic[x[1]] + "\n"
        output += defines["scope_end"] + "\n\n\n"
    #print(output)
    filestream.write(filename, output, "str", "append")
