import re

def welcoming():
    print("Welcom in madlib game !")
"""
Adjective  #6  ---> Enter an Adjective 6 times 
A First Name  #2 ---> Enter A First Name 2 times
Past Tense Verb  #1 ---> Enter Past Tense Verb 1 times
Plural Noun  #5 ---> Enter Plural Noun 5 times
Large Animal  #1 ---> Enter Large Animal 1 times
Small Animal  #1 ---> Enter Small Animal 1 times
A Girl's Name #1 ---> Enter A Girl's Name 1 times
Number 1-50 #1 ---> Enter Number 1-50 1 times
First Name's #1 ---> Enter First Name's 1 times
Number  #2 ---> Enter Number 2 times

# total number of times:21

"""
def read_template(filePath="madlib_cli/assets/Sample.txt"):
    """
    open the Sample.txt file and read it 
    """
    try: 

        file = open(filePath,'r')
        content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError('The file not found')
        
   
def parse_template(constant): # constant refers to the text
    """
    Returns a list of key-words that inside {} in the given text
    """
    word = ""
    parsed_text = ""
    parsed_words = []
    status = 0 # outside of curly braces
    for ch in constant:      
        if ch == "{":
            status = 1 # inside curly braces
            parsed_text = parsed_text + ch
        elif ch == "}":
            status = 0
            parsed_text = parsed_text + ch
            parsed_words.append(word)
            word = ""
        elif status == 0:
            parsed_text = parsed_text + ch
        else:
            word = word + ch
    
    return parsed_text, tuple(parsed_words)
    
    
def merge(constant , words):  

    """
    Returns a string with user input strings 
    """ 
    # we use string.format() to add user answers to the empty  
    return constant.format(*words)
     

def copyFile(text):
    # print(text)
    file = open('madlib_cli/assets/copy_file.txt','w')
    file.write(text)
    
def print_copy_file():
    file = open('madlib_cli/assets/copy_file.txt')
    lines=file.readlines()
    for line in lines:
        print(line)
    file.close()

user_answers=[]
def ask_user(words):
    for i in range (len(words)):
        input_val=input('>> Enter %s  '%(words[i]))
        user_answers.append(input_val)
 


if __name__=="__main__":
    welcoming()
    content = read_template()
    lst = parse_template(content)
    ask_user(lst[1])
    textWithAnswers=merge(lst[0],user_answers)
    copyFile(textWithAnswers)
    print_copy_file()
    

