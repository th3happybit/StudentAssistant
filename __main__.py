#!/usr/bin/python

#Oussama Messabih
#email : giantscrusher@gmail.com

#Project : Student Assistant 

from speak import speak
from listen import listen
from functions import profilegen
from functions import schelude, timenow

def main():
	timenow.timenow()
	schelude.telltds('Sunday')
if __name__ == '__main__':
    main()