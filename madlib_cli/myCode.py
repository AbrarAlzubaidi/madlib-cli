# def parse_template(constant):
# lst=[]
    # # to find all keywords that inside {} and store it inside newList
    # newList = re.findall(r'\{.*?\}', constant) 
    # print(newList)
    # #  loop through the newlist and remove each value that inside {} then push it into lst array
    # for i in newList:
    #     word=i.strip("{ }")
    #     print(word)
    #     lst.append(word)    
    # print(lst)
    # return lst

# def read_sample():
#     try:
#         fin=open('madlib_cli/Sample.txt','r')
#         word= ['{Adjective}','{Noun}']
#         answerAdj=[]
#         answerNoun=[]
#         s=" "
#         count=1
#         while s:
#             s=fin.readline()
#             l=s.split()
#             for key in word:
#                 if key in l:
#                     split1=key.split("{")
#                     split2=split1[1].split("}")
#                     print("enter "+split2[0])
#                     if split2[0] == "Noun":
#                         answer=input()
#                         answerNoun.append(answer)

#                     else:
#                         answer=input()
#                         answerAdj.append(answer)
#             count+=1
        
#         replace(word,answerAdj,answerNoun)


#     except FileNotFoundError:
#         print('sorry the file not found here')

# def replace(keyword, answerAdj,answerNoun): 
#     keyword=keyword
#     answerAdj=answerAdj
#     answerNoun=answerNoun

#     fout = open("madlib_cli/out.txt", "w")
#     fin= open('madlib_cli/Sample.txt','r') 
#     # for line in fin:
        
#         # if keyword[0] in line and keyword[1] in line:
#             # word2=keyword[0].format(Adjective=answerAdj[0],Noun=answerNoun[0]) 
#     line=fin.readline()
#     word2=answerAdj[0]
#     word3=answerNoun[0]
#     fout.write(line.replace(keyword[0], word2))
#     fin.close()
#     fout.close()
#     replaceNoun(keyword[1], word3)
#     # fout.write(line.replace(keyword[1], word3))

#         # else:
#         #     word2=keyword[1].format(Adjective=" ",Noun=answerNoun[0]) 
#         #     fout.write(line.replace(keyword[1], word2))

    
                   
# def replaceNoun(keyword,answer):
    
#     fin = open("madlib_cli/out.txt", "r")
#     line=fin.readline()
    
#     fout = open("madlib_cli/outg.txt", "w")
#     fout.write(line.replace(keyword, answer))
      

# if __name__=="__main__":
#     welcoming()
#     read_sample()
#     # replace()
   