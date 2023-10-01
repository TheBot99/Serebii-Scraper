import json
import os
import time

import requests
from bs4 import BeautifulSoup

All_Parameters = json.load(open("All_Parameters.json", "r"))
Generations_Pokemon_In = json.load(open("Generations_Pokemon_In.json", "r+"))

def Convert_DexNumber_To_3_Digits(DexNumber):
    DexNumber = str(DexNumber)
    if len(DexNumber) == 1:
        DexNumber = "00" + DexNumber
    elif len(DexNumber) == 2:
        DexNumber = "0" + DexNumber
    return DexNumber

def Check_What_Generations_In(DexNumber):
    try:
        os.mkdir("Serebii/"+DexNumber)
    except:
        print("Folder Already Exists")
    Generations_Pokemon_In_Local = {}
    Generations_Pokemon_In_Local[DexNumber] = []
    print(Generations_Pokemon_In_Local)
    Base_URL = All_Parameters["Base_URL"]
    Generations = All_Parameters["Generations"]


    for i in Generations:
        URL_id = Generations[i]["URL_id"]
        URL = Base_URL.replace("URL_id", URL_id).replace("DexNumber", DexNumber) 
        Page = requests.get(URL)
        Soup = BeautifulSoup(Page.content, 'html.parser')
        if Soup.title.string != "404 Error":
            Generations_Pokemon_In_Local[DexNumber].append(i)
            Generations_Pokemon_In.update(Generations_Pokemon_In_Local)
            File = open("Serebii/"+DexNumber+"/"+i+".html", "w" , encoding='utf-8')
            File.write(str(Soup.prettify()))
            File.close()
            print(Generations_Pokemon_In_Local)
            

        
            

            
    json.dump(Generations_Pokemon_In, open("Generations_Pokemon_In.json", "w"), indent=4)




def Download_No_Gen_Page(DexNumber, DexNumberString):
    NatDexPage = requests.get("https://www.serebii.net/pokemon/nationalpokedex.shtml")
    NatDexSoup = BeautifulSoup(NatDexPage.content, 'html.parser')
    NatDexSoupReference = NatDexSoup.find("table", {"class": "dextable"}).tr.find_next_siblings()[DexNumber].find_all("td")[1].a["href"]
    print(NatDexSoupReference)
    PokemonPage = requests.get("https://www.serebii.net"+NatDexSoupReference)
    PokemonSoup = BeautifulSoup(PokemonPage.content, 'html.parser')
    File = open("Serebii/"+DexNumberString+"/No_Gen.html", "w" , encoding='utf-8')
    File.write(str(PokemonSoup.prettify()))
    File.close()
    print("No Gen Page Downloaded")




start_time_of_program = time.time()

DexNumber = 1
Total_Number_Of_Pokemon = 1017
while DexNumber <= 1:
    start_time = time.time()
    DexNumberString = Convert_DexNumber_To_3_Digits(DexNumber)
    #Check_What_Generations_In(DexNumberString)
    Download_No_Gen_Page(DexNumber, DexNumberString)
    DexNumber += 1
    print("--- %s seconds --- for Dex Number " % (time.time() - start_time) + DexNumberString)

print("--- %s seconds ---" % (time.time() - start_time_of_program)+" for all Pokemon")