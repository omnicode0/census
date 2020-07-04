#!/usr/bin/env python3

import webbrowser

yesOrNo = None #initializing variable containing whether user wants to open the webpage or not

print('Welcome! This program will navigate you to the area on the Census website where you can download data to suit your needs.')
print()

while yesOrNo != 'yes' or yesOrNo != 'no':
  yesOrNo = str(input('Would you like me to open the webpage in your default browser? say "yes" or "no": '))

  if yesOrNo == 'yes':
    print('It looks like you want us to open the webpage! Here you go.')
    webbrowser.open('https://www.census.gov/data/tables.html')
    break
  
  elif yesOrNo == 'no':
    print('We hope you have a nice day!')
    break

  else:
    print('I couldn\'t understand you! What did you mean? Please respond in lower case and no spaces "yes" or "no"')
