import os
import re

def lexical_parser1( input ):
   # split string
   parsed_input = input.split("to",1)
   return parsed_input;
 
def lexical_parser2( input ):
   # split string
   parsed_input = input.split(",",1)
   return parsed_input;
   
f = open("program.txt","r")

human_input = f.read()

parsed_input1 = lexical_parser1(human_input)

print parsed_input1[0].strip()

parsed_input2 = lexical_parser2(parsed_input1[1])

print parsed_input2[0].strip()
print parsed_input2[1].strip()

f.close()
      
