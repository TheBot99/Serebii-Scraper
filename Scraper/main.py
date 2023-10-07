from bs4 import BeautifulSoup
import json
import os
from DataScrapers import *


DexNumber = 18
Generation = 0
while DexNumber <= 18:
    Generations_Pokemon_In = json.load(open("Generations_Pokemon_In.json", "r+"))
    DexNumberString = Convert_DexNumber_To_3_Digits(DexNumber)
    NumberOfGenerationsPokemonIn = len(Generations_Pokemon_In[DexNumberString])
    #NumberOfGenerationsPokemonIn = 1

    while Generation < NumberOfGenerationsPokemonIn:
        GenerationName = Generations_Pokemon_In[DexNumberString][Generation]
        Soup = Get_Soup_From_File(f"Serebii/{DexNumberString}/{GenerationName}.html")
        PokemonName = Get_Pokemon_Name_From_Soup(Soup, DexNumberString)
        Forms = Check_If_Pokemon_Has_Forms(DexNumberString)
        #PokemonType = Get_Pokemon_Type_From_Soup(Soup, GenerationName)
        try:
            os.mkdir("Pokemon Data/"+DexNumberString)
        except:
            pass
        
        os.system("cls")
        print(GenerationName)
        print()
        print(DexNumberString)
        print(PokemonName)
        # if PokemonType == []:
        #     raise Exception("Pokemon Type not found")
        # else:
        #     print(PokemonType)
        print(Forms)
        print()

        PokemonData = {}
        PokemonData["Dex Number"] = DexNumberString
        PokemonData["PokemonName"] = PokemonName
        #PokemonData["PokemonType"] = PokemonType
        PokemonData["Forms"] = Forms


        json.dump(PokemonData, open("Pokemon Data/"+DexNumberString+"/"+GenerationName+".json", "w"), indent=4)
        json.dump(Generations_Pokemon_In[DexNumberString], open("Pokemon Data/"+DexNumberString+"/Generations "+DexNumberString+" In.json", "w"), indent=4)
    
        Generation += 1
        

    DexNumber += 1
    Generation = 0




