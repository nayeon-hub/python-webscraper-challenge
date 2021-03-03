import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

country = []
code = []

result = requests.get(url)
soup = BeautifulSoup(result.text,"html.parser")
table = soup.find("table",{"class":"table"})
row = table.find_all("tr")

for i in range(1,len(row)):
  r = row[i].find_all("td")
  country.append(r[0].string)
  code.append(r[2].string)

code.remove(None)
code.remove(None)
code.remove(None)
country.remove("ANTARCTICA")
country.remove("PALESTINE, STATE OF")
country.remove("SOUTH GEORGIA AND THE SOUTH    SANDWICH ISLANDS")

print("Hello! Please choose select a country by number")
for c in range(len(country)):
  print(f"#{c} {country[c]}")


while True:
  try : 
    num = int(input("#:"))
    if 0 <= num and num <= 267:
      print(f"You choose {country[num]}\nThe currency code is {code[num]}")
    elif num == -1:
      break
    else:
      print("choose a number from the list.")
  except ValueError:
    print("That wasn't a number")


