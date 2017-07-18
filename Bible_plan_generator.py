# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 13:43:47 2017

@author: joelb
"""


def get_tokens(reference):
    """breaks a bible reference frame
    (in format 'Gen1-10, Ps8-16,17,18')
    into tokens that each contain a region seperated from the others by a coma"""
    comma_seperated_references=[]
    s=''
    for i in range(len(reference)):
        if(reference[i]==" "):
            pass
        else:
            if(reference[i]==',' or reference[i]==';'):
                comma_seperated_references.append(str(s))
                s=''
            else:
                s=s+reference[i]
    comma_seperated_references.append(str(s))
    return comma_seperated_references

def get_book(token):
    """given a token (as returned by above funcion), this returns the book that it is in or '' if there is none
    (as in Ps 17,19, where 19 fits in a seperate token"""
    book=''
    for i in range(len(token)):
        if(token[i].isalpha() or (token[i].isdigit()) and token[min(len(token)-1,i+1)].isalpha()):
            book=book+token[i]
        else:
            return book
    return book

def complete_tokens(tokens):
    """Completes the bookless tokens in a list of tokens extracted from a line in get_tokens"""
    tk=list(tokens)
    book=get_book(tk[0])
    for i in range(1,len(tk)):
        if(get_book(tk[i])==''):
            tk[i]=book+tk[i]
        else:
            book=get_book(tk[i])
    return tk
        
def parse_token(token):
    """Breaks down a token into it's individual passages.
    The token is assumed to always contain a book.
    A list of tokens therefore has to have been through complete_token."""
    book=get_book(token)
    beg=''
    end=''
    starting=True
    returned_list=[]
    hifen=False
    for i in range(len(book),len(token)):
        if(token[i].isdigit()):
            if(starting):
                beg=beg+token[i]
            else:
                end=end+token[i]
        elif(token[i]=='-'):
            hifen=True
            starting=False
    if(hifen):
        for i in range(int(beg),1+int(end)):
            returned_list.append([book,i])
    else:
        returned_list.append([book,beg])
    return returned_list

def parse_token_list(tokens):
    """parses all the tokens in a list extracted from get_tokens, after being completed with books"""
    passages=[]
    for i in range(len(tokens)):
        p=parse_token(tokens[i])
        passages=passages+p
    return passages

def parse_line(line):
    """Parses a line to get all it's individual passages"""
    tokens=get_tokens(line)
    tokens=complete_tokens(tokens)
    print(tokens)
    return parse_token_list(tokens)

def parse_table(table):
    """Parses a whole table of passages using above functions.
    The result is a list of individual chapters in the format [<book, string>, <chapter,int>] """
    list_of_passages=[]
    for i in range(len(table)):
        list_of_passages=list_of_passages+parse_line(table[i])
    return list_of_passages

#Tested on a list of chronologically ordered passages
C=[]
C.append('Gen 1-11 ')
C.append('Job 1-42 ')
C.append('Gen 12-50 ')
C.append('Ex 1-40 ')
C.append('Lev 1-27 ')
C.append('Num 1-36 ')
C.append('Deut 1-34 ')
C.append('Ps 90, 91 ')
C.append('Josh 1-24 ')
C.append('Judg 1-21 ')
C.append('Ruth 1-4 ')
C.append('1 Sam 1-20 ')
C.append('Ps 11, Ps 59 ')
C.append('1 Sam 21-24 ')
C.append('Ps 7, 27, 31, 34, 52, 56, 120, Ps. 140-142 ')
C.append('1 Sam 25-27 ')
C.append('Ps 17, Ps 35, Ps 54, Ps 63 ')
C.append('1 Sam 28-31, Ps 18 ')
C.append('Ps 121, 123-125, 128-130 ')
C.append('2 Sam 1-4 ')
C.append('Ps 6, 8-10, 14, 16, 19, 21 ')
C.append('1 Chr 1-2 ')
C.append('Ps 43-45, 49, 84-85, 87 ')
C.append('1 Chr 3-5 ')
C.append('Ps 73, Ps 77-78 ')
C.append('1 Chr 6 ')
C.append('Ps 81, Ps 88, Ps 92-93 ')
C.append('1 Chr 7-10 ')
C.append('Ps 102-104 ')
C.append('2 Sam 5, 1 Chr 11-12 ')
C.append('Ps 133 ')
C.append('Ps 106-107 ')
C.append('2 Sam 6; 1 Chr 13-16 ')
C.append('Ps 1-2, 15, 22-24, 47, 68 ')
C.append('Ps 89, Ps 96, Ps 100, Ps 101, Ps 105, 132 ')
C.append('2 Sam 7; 1 Chr 17 ')
C.append('Ps 25, 29, 33, 36, 39 ')
C.append('2 Sam 8-9, 1 Chr 18 ')
C.append('Ps 50, 53, 60, 75, 76 ')
C.append('2 Sam 10, 1 Chr 19, Ps 20 ')
C.append('Ps 65-67, Ps 69-70 ')
C.append('2 Sam 11-12, 1 Chr 20 ')
C.append('Ps 32, Ps 51, Ps 86, Ps 122 ')
C.append('2 Sam 13-15 ')
C.append('Ps 3-4, 12-13, 28, 55 ')
C.append('2 Sam 16-18 ')
C.append('Ps 26, 40, 58, 61-62, 64 ')
C.append('2 Sam 19-21 ')
C.append('Ps 5, Ps 38, Ps 41-42 ')
C.append('2 Sam 22-23, Ps 57 ')
C.append('Ps 95, Ps 97-99 ')
C.append('2 Sam 24, 1 Chr 21-22, Ps 30 ')
C.append('Ps 108-110 ')
C.append('1 Chr 23-25 ')
C.append('Ps 131, 138-139, 143-145 ')
C.append('1 Chr 26-29, Ps 127 ')
C.append('Ps 111-118 ')
C.append('1 Kgs 1-2, ')
C.append('Ps 37, 71, 94, 119 ')
C.append('1 Kgs 3-4, 2 Chr 1, ')
C.append('Ps 72 ')
C.append('Sng 1-8 ')
C.append('Prov 1-24 ')
C.append('1 Kgs 5-6, 2 Chr 2-3 ')
C.append('1 Kgs 7, 2 Chr 4 ')
C.append('1 Kgs 8, 2 Chr 5 ')
C.append('2 Chr 6-7, Ps 136 ')
C.append('Ps 134, Ps 146-150 ')
C.append('1 Kgs 9, 2 Chr 8 ')
C.append('Prov 25-29 ')
C.append('Eccl 1-12 ')
C.append('1 Kgs 10-11, 2 Chr 9 ')
C.append('Prov 30-31 ')
C.append('1 Kgs 12-14 ')
C.append('2 Chr 10-12 ')
C.append('1 Kgs 15; 2 Chr 13-16 ')
C.append('1 Kgs 16; 2 Chr 17 ')
C.append('1 Kgs 17-22 ')
C.append('2 Chr 18-23 ')
C.append('Obad 1, Ps 82-83 ')
C.append('2 Kgs 1-13 ')
C.append('2 Chr 24 ')
C.append('2 Kgs 14, 2 Chr 25 ')
C.append('Jonah 1-4 ')
C.append('2 Kgs 15, 2 Chr 26 ')
C.append('Isa 1-8 ')
C.append('Amos 1-9 ')
C.append('2 Chr 27, ')
C.append('Isa 9-12 ')
C.append('Mic 1-7 ')
C.append('2 Chr 28, 2 Kgs 16-17 ')
C.append('Isa 13-27 ')
C.append('2 Kgs 18:1-8, 2 Chr 29-31 ')
C.append('Ps 48 ')
C.append('Hos 1-14 ')
C.append('Isa 28-48 ')
C.append('2 Kgs 18-19 ')
C.append('Ps 46, Ps 80, Ps 135 ')
C.append('Isa 49-66 ')
C.append('2 Kgs 20-21 ')
C.append('2 Chr 32-33 ')
C.append('Nahum 1-3 ')
C.append('2 Kgs 22-23, 2 Chr 34-35 ')
C.append('Zeph 1-3 ')
C.append('Jer 1-40 ')
C.append('Ps 74, Ps 79 ')
C.append('2 Kgs 24-25, 2 Chr 36 ')
C.append('Hab 1-3 ')
C.append('Jer 41-52 ')
C.append('Lam 1-5 ')
C.append('Ezek 1-48 ')
C.append('Joel 1-3 ')
C.append('Dan 1-12 ')
C.append('Ezra 1-6 ')
C.append('Ps 137 ')
C.append('Hag 1-2 ')
C.append('Zech 1-14 ')
C.append('Est 1-10 ')
C.append('Ezra 7-10 ')
C.append('Neh 1-13 ')
C.append('Ps 126 ')
C.append('Mal 1-4 ')
C.append('Luke 1, John 1 ')
C.append('Matt 1, Luke 2 ')
C.append('Matt 2, ')
C.append('Matt 3, Mark 1, Luke 3 ')
C.append('Matt 4, Luke 4-5, ')
C.append('Mark 2 ')
C.append('John 2-5 ')
C.append('Matt 12; Mark 3, ')
C.append('Luke 6 ')
C.append('Matt 5-8 ')
C.append('Luke 7 ')
C.append('Matt 11 ')
C.append('Luke 11 ')
C.append('Matt 13, Luke 8 ')
C.append('Mark 4-5 ')
C.append('Matt 9-10 ')
C.append('Matt 14, Mark 6, ')
C.append('Luke 9 ')
C.append('John 6 ')
C.append('Matt 15, Mark 7 ')
C.append('Matt 16, Mark 8, ')
C.append('Matt 17, Mark 9, ')
C.append('Matt 18 ')
C.append('John 7-8 ')
C.append('John 9-10 ')
C.append('Luke 10-16 ')
C.append('John 11 ')
C.append('Luke 17-18 ')
C.append('Matt 19, Mark 10 ')
C.append('Matt 20-21 ')
C.append('Luke 19 ')
C.append('Mark 11, John 12 ')
C.append('Matt 22, Mark 12 ')
C.append('Matt 23, Luke 20-21 ')
C.append('Mark 13 ')
C.append('Matt 24-26 ')
C.append('Mark 14 ')
C.append('Luke 22, ')
C.append('John 13-17 ')
C.append('Matt 27, Mark 15 ')
C.append('Luke 23, John 18-19 ')
C.append('Matt 28, Mark 16 ')
C.append('Luke 24, John 20-21 ')
C.append('Acts 1-14 ')
C.append('Jas 1-5 ')
C.append('Acts 15-16 ')
C.append('Gal 1-6 ')
C.append('Acts 17 ')
C.append('1 Thes 1-5 ')
C.append('2 Thes 1-3 ')
C.append('Acts 18-19 ')
C.append('1 Cor 1-16 ')
C.append('2 Cor 1-13 ')
C.append('Acts 20 ')
C.append('Rom 1-16 ')
C.append('Acts 21-28 ')
C.append('Col 1-4, ')
C.append('Phm 1 ')
C.append('Eph 1-6 ')
C.append('Phil 1-4 ')
C.append('1 Tim 1-6 ')
C.append('Titus 1-3 ')
C.append('1 Pet 1-5 ')
C.append('Heb 1-13 ')
C.append('2 Tim 1-4 ')
C.append('2 Pet 1-3, ')
C.append('Jude 1 ')
C.append('1 Jn 1-5 ')
C.append('2 Jn 1 ')
C.append('3 Jn 1 ')
C.append('Rev 1-22 ')


p=(parse_table(C))
for i in range(len(p)):
    print(p[i])
