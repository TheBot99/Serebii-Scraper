from bs4 import BeautifulSoup


def Convert_DexNumber_To_3_Digits(DexNumber):
    DexNumber = str(DexNumber)
    if len(DexNumber) == 1:
        DexNumber = "00" + DexNumber
    elif len(DexNumber) == 2:
        DexNumber = "0" + DexNumber
    return DexNumber


def Get_Soup_From_File(File):
    File = open(File, "r", encoding='utf-8')
    Soup = BeautifulSoup(File, 'html.parser')
    File.close()
    return Soup


def Get_Pokemon_Name_From_Soup(Soup, DexNumberString):
    Pokemon_Name = Soup.find("title").string
    Pokemon_Name = Pokemon_Name.replace("Serebii.net Pokédex", "")
    Pokemon_Name = Pokemon_Name.replace("-", "")
    Pokemon_Name = Pokemon_Name.replace(" ", "")
    Pokemon_Name = Pokemon_Name.replace("\n", "")
    Pokemon_Name = Pokemon_Name.replace("\r", "")
    Pokemon_Name = Pokemon_Name.replace("\t", "")
    Pokemon_Name = Pokemon_Name.replace("é", "e")
    Pokemon_Name = Pokemon_Name.replace("♀", "F_")
    Pokemon_Name = Pokemon_Name.replace("♂", "M_")
    Pokemon_Name = Pokemon_Name.replace(f"#{DexNumberString}", "")
    return Pokemon_Name


def Get_Pokemon_Type_From_Soup(Soup, GenerationName):
    All_Types = ["Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground",
                 "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy", "Normal"]
    Pokemon_Type = []
    


def Check_If_Pokemon_Has_Forms(DexNumberString):
    soup = Get_Soup_From_File(f"Serebii/{DexNumberString}/No_Gen.html")
    FindAlternateFormTitle = soup.find("td", string="Alternate Forms")
    print(FindAlternateFormTitle)
    print(soup)

Check_If_Pokemon_Has_Forms("019")

