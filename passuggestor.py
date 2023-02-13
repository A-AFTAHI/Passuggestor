#!/bin/env python



import sys

import argparse

import datetime







# Author : A-AFTAHI

# Date : 12/02/2023



# This simple script aims to help you perform a custom dictionnary attack against Domain and applications passwords of a given organisation. It takes the name of the organisation, it's password policy and the year of the script's execution

# and comes up with a list of potential passwords combining the company name with numbers and special caracters making sure that these passwords comply with password policy.



# Usage : python3 passuggestor.py -c <corp name> -p <minimum password length> -y <year> -o <output file name>





# CMapping : This method uses Character substitution ro suggest some common alternatives which can be used for specific letters in a password replacing them with numbers and special characters



def CMapping (corp):

  L = [corp]

  

  Lchar = ['o', 's', 'e', 'a', 'i', 't', 'g', 'G']

  Lspecial = ['0', '$', '3', '@', '1', '7', '9', '6']

  

  for i in range(len(Lchar)):

    if Lchar[i] in corp:

      counter = corp.count(Lchar[i])

      L.append(corp.replace(Lchar[i], Lspecial[i], 1))

      

      if counter > 1:

        L.append(corp.replace(Lchar[i], Lspecial[i]))

  

  return L







# NameFormatting : This method takes the company's name including character subsitution options and produces diffrent versions based on letters case



def NameFormatting (corpL):

  

  L = []

  

  for corp in corpL:

    lower = corp.lower()

    upper = corp.upper()

    Fupper = corp.capitalize()

    backwards = corp[::-1]

  

    L.append(lower)

    L.append(upper)

    L.append(Fupper)

  

  return L





# Padding : This method checks the length of each suggested password to verify if it complies with the password policy. If doesn't we append some characters to it until it's inline with the policy.



def padding (password, policy):

  

  Lpassword = password

  

  while len(Lpassword) < policy :

    Lpassword = Lpassword + '@'

    

  return Lpassword

  





# SuggPass This is the main method which combines all the outputs of the other functions and suggest passwords



def SuggPass (corpL, policy, year):

  

  passwords = []

  Links = ['@', '.', '-', '_','']

  

  Lcorp = corpL

  Lpolicy = policy

  Lyear = year

  

  for corp in Lcorp:

    for Link in Links:

      password1 = corp + Link + str(Lyear)          # password with this year

      passwords.append(padding(password1, Lpolicy))      

      

      password2 = corp + Link + str(Lyear-1)        # password with last year

      passwords.append(padding(password2, Lpolicy))    

      

      password3 = corp + Link + str(Lyear-2)        # password with 2 years before

      passwords.append(padding(password3, Lpolicy))    

      

      password4 = corp + Link + str(1)

      passwords.append(padding(password4, Lpolicy))

      

      password5 = corp + Link + str(123)

      passwords.append(padding(password5, Lpolicy))

      

      password6 = corp + Link + 'adm'

      passwords.append(padding(password6, Lpolicy))

      

      password7 = corp + Link + 'pass'

      passwords.append(padding(password7, Lpolicy))

      

      password8 = corp + Link + 'svc'

      passwords.append(padding(password8, Lpolicy))

      

      password9 = 'adm' + Link + corp

      passwords.append(padding(password9, Lpolicy))

      

      password10 = 'pass' + Link + corp

      passwords.append(padding(password10, Lpolicy))

      

      password11 = 'svc' + Link + corp

      passwords.append(padding(password11, Lpolicy))

    

  return passwords

  





# That's the Main 



def main(): 

  

 

  CurrentYear = datetime.date.today().strftime("%Y")

  # handling parameters

  argParser = argparse.ArgumentParser()

  argParser.add_argument("-c", "--corp", help="company's name")

  argParser.add_argument("-p", "--policy", default=8, type=int, help="The password's minimal length indicated in the password policy. The default value is 8")

  argParser.add_argument("-y", "--year", default=CurrentYear, type=int, help="The year of reference you want the passwords to be based on. The fault value is the current year.")

  argParser.add_argument("-o", "--out", help="The output file. If not specified the output will be printed in the terminal")



  try:

    args = argParser.parse_args()



    corp = args.corp

    policy = args.policy

    year = args.year

    

    

    corpList = NameFormatting(CMapping(corp))  # The corporation names list

  

    passwordList = SuggPass(corpList, policy, year)  # The list of passwords

    

    

    # Handling the final output

    if args.out != None:

      

      fil = open(args.out,'w')

      

      for password in passwordList:

        fil.write(password+"\n")

      fil.close()

    

    else:

      for password in passwordList:

        print(password)



  

  except AttributeError: 

    argParser.print_help()

    sys.exit(0)





if __name__ == "__main__":

   main()
