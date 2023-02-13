# Passuggestor


This simple script aims to help you perform a custom dictionnary attack against the domain and applications passwords of a given organisation. It takes the name of the organisation, it's password policy and the year of the script's execution and comes up with a list of potential passwords combining the company name with numbers and special caracters making sure that these passwords comply with password policy.

If you're in charge of cybersecurity of your organization this script can also help you to think about passwords which you might blacklist.

*** Disclaimer ***

Only use this script against organiszation's which your authorized to perform offensive attacks against. Use it on your own risk.

Usage : 
* Default password policy and cmd output : *$python3 passuggestor.py -c \<corp name\>*
* Specific password policy and cmd output : *$python3 passuggestor.py -c \<corp name\> -p \<minimum password length\> -y \<year\>*
* Specifying output file : *$python3 passuggestor.py -c \<corp name\> -p \<minimum password length\> -y \<year\> -o \<output file name\>*

![VirtualBox_Kali-Linux-2022 2-virtualbox-amd64_12_02_2023_18_13_06](https://user-images.githubusercontent.com/19476977/218326674-decc11ad-a1fd-47e5-b2f4-d5ac499c2e9f.png)
