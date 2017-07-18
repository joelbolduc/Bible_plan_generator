# Bible_plan_generator
Creates a standardised ordered list of bible passages from a list of string representing each passages.
String can contain multiple chapters, either seperated by hiphens or commas. For instance, Gen 1-10, 17, 25, Ps2,Ps9-17.
Spaces may be left or omitted.
The function parse_table will convert whole table into a list of individual passages in format [<book,string>,<chapter,int>]
