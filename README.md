# Passuggestor


This simple script aims to help you perform a custom dictionnary attack against Domain and applications passwords of a given organisation. It takes the name of the organisation, it's password policy and the year of the script's execution
and comes up with a list of potential passwords combining the company name with numbers and special caracters making sure that these passwords comply with password policy.

Usage : python3 passuggestor.py -c <corp name> -p <minimum password length> -y <year> -o <output file name>
