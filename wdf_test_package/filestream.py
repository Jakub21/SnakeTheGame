'''
------------------------
----BASIC-INFO
------------
Creation
    JakubP (June 2017)
Library full name
    JakubP's Filestream Control Library
------------------------
----DETAILS
------------
Library was created to make filestream manipulation easier.
There are no external dependencies.
------------------------
----LIST-OF-FUNCTIONS
readlength(filename)
read(filename, type)
write(filename, input_data, data_type, mode= "append", separators= [" ", "\n"])
testlib(filename0, filename1)
------------
------------------------
----TESTING
------------
Import this library and call:
    >filestream.testlib((STR/ExistingFile)filename0, (STR)filename1)
Whole library must be imported.
------------------------
'''


#----#----#----#----#----#----#----#----
#Input
    #(STR)Filename
#Output
    #None
#Return
    #(INT)NumOfLines
#----#----#----#----
def readlength(filename):
    incr = 1
    with open(filename) as enr:
        for incr, line in enumerate(enr):
            pass
    return incr+1


#----#----#----#----#----#----#----#----
#Input
    #Filename
    #(STR)Type ValidValues("str" / "words" / "lines")
#Output
    #When InvalidArgument was given: ErrorMessage
#Return
    #(STR / LIST)Content
      #Content of file in format specified by "type" input:
       #Str returns whole file as a string, saves invilible chars.
       #Words returns list of words in file. Ignores invilible chars.
       #Lines returns list of lines in file. Invisible chars are loaded too.
#----#----#----#----
def read(filename, type):
    fstr = open(filename, "r")
    if type == "str":
        output = fstr.read()
    elif type == "words":
        q = fstr.read()
        output = q.split()
    elif type == "lines":
        output = fstr.readlines()
    else:
        print("!>>Filestream:Read InvalidArgument:Type")
    return output


#----#----#----#----#----#----#----#----
#Input
    #(STR)Filename
    #(STR / LIST / DICTIONARY)InputData
    #(STR)iMode ValidValues("str" / "list" / "dic")
    #(STR-Optional)oMode ValidValues("replace" / "append");
        #Default(append)
    #(LIST[STR]-Optional)Separators;
        #Default([" ", "\n"])
#Output
    #When InvalidArgument was given: ErrorMessage
    #Writes content to file(filename)
#Return
    #Function does not return anything.
#----#----#----#----
def write(filename, input_data, i_mode, o_mode = "append", seps = [" ", "\n"]):
    #Convert to STR
    outp_str = ""
    count_seps = len(seps)
    if i_mode == "list":
        for q in enumerate(input_data):
            index = q[0]
            outp_str += input_data[index] + seps[index%count_seps]

    elif i_mode == "dic":
        for q in enumerate(input_data):
            index = q[1]
            outp_str += index + seps[0]
            outp_str += input_data[index] + seps[1]

    elif i_mode == "str":
        outp_str = input_data

    #Write to file
    if o_mode == "replace":
        file0 = open(filename, "w")
    elif o_mode == "append":
        file0 = open(filename, "a")
    try:
        file0.write(outp_str)
        file0.close()
    except:
        print("FILESTREAM>>> Invalid argument MODE for function WRITE")


#----#----#----#----#----#----#----#----
#TEST_LIBRARY
#Input
    #Filename0 (STR(Existing file name))
    #Filename1 (STR)
#Output
    #Print content of file(filename0) at screen
    #Write content of file(filename0) to file(filename1)
#Return
    #None
#----#----#----#----
def testlib(filename0, filename1):
    print ("\n")
    #List of functions
    '''
        file_lenght_00(filename)
        file_load_lines_00(filename)
        file_load_words_00(filename)
        file_write_over_00(filename, input_data)
        file_write_append_00(filename, input_data)
    '''
    #Filename0 for reading
    #Filename1 for writting
    file_len = file_lenght_00(filename0)
    loaded_lines = file_load_lines_00(filename0)
    loaded_words = file_load_words_00(filename0)
    file_write_over_00(filename1, loaded_lines)
    file_write_append_00(filename1, loaded_words)

    print ("\nTEST RETURNS:\n")
    print ("Lines:\n", loaded_lines, "\n\n")
    print ("Words:\n", loaded_words, "\n\n")


#
