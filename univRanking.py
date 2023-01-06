# Author: Raed LNU
# Date: 17 November 2022
import pandas as pd

# selectedCountry = input("Please enter the country name:").upper()
def getInformation(selectedCountry, rankingFileName, captialsFileName):
    
    
    # initializing all the variables
    worldRank=99999
    
    nationalRank=99999
    
    maxScore=99999
    
    list_uniNum=[]
    
    sumScore=0
    
    uni0 = ''
    
    uni1 = ''
    
    avgScore = 0
    
    scoreRelative = 0
    
    selectedCountry = selectedCountry.upper()
    
    rankList = []
    
    countries=[]
    
    continentName=''
    
    capitalName=''
    
    countryInCon = []
    
    rankInCon = []
    
    #reading both the csv files using pandas
    uniFile = pd.read_csv(rankingFileName)
    
    capFile = pd.read_csv(captialsFileName)
   #opens and write to the output.txt file
    outFile = open("output.txt", "w", encoding='utf8')
    
   #Part 1
   # Returns the num of universities
    uniNum = len(uniFile['Institution name'])
    
   
# Part 2: 
    country_list=[]
    
    for a in range(len(uniFile)):
        if(uniFile['Country'][a]not in country_list):
            country_list.append(uniFile['Country'][a])
            finalCountry = pd.unique(country_list).tolist()

    # Display all available continent name in order given the capFile.csv file as a list corresponding to abv output
    #Part 3
    Continent = []
    
    Continent = [elem.upper() for elem in capFile["Continent"]]
    
    finalContinent = pd.unique(Continent)
    
    
   #Part 4
   
    for a in range(len(uniFile)):
        # Add a country to the rank list.
        if(selectedCountry==uniFile['Country'][a].upper()):
            rankList.append(a)
            # Checks if a world rank is greater than the world rank.
            if (uniFile['World Rank'][a]<worldRank):
                worldRank=uniFile['World Rank'][a]
                uni0=uniFile['Institution name'][a].upper()
               
               #Part 5
               # Compute the sum score from the given uni file.
               
               # Check if the national rank is greater than the given one.
            if (uniFile['National Rank'][a]<nationalRank):
                nationalRank=uniFile['National Rank'][a]
                # Compute the sum score and sets uni1 accordingly
                uni1=uniFile['Institution name'][a].upper()
            sumScore += uniFile['Score'][a]
   
   # Computes the average score for the selected country.
    for i in range (len(uniFile)):
        # Computes the average score for the selected country.
        if (selectedCountry == uniFile['Country'][i].upper()):
            list_uniNum.append(uniFile['Institution name'][i])        
    avgScore= round((sumScore/len(list_uniNum)),2)
   
    
    #Part 6 
    # Returns a tuple of country and continent names.
    for a in range(len(capFile)):
        if(selectedCountry==capFile['Country Name'][a].upper()):
            capitalName = capFile['Capital'][a]
            continentName=capFile['Continent'][a]
            # Returns a list of countries.
    for a in range(len(capFile)):
        if(str(continentName).upper()==str(capFile['Continent'][a]).upper()):
            if(capFile['Country Name'][a] not in countries):
                countries.append(capFile['Country Name'][a])
   
    
   #Part 7
   # Add all countries in the uniFile.
    for con in uniFile['Country']:
        if con in countries:
            countryInCon.append(con)
   
   # Rank each country in a list in descending order
    for a in range(len(countryInCon)):
        for b in range(len(uniFile)):
            if (countryInCon[a] == uniFile["Country"][b]):
                rankInCon.append(b)
   
   # Returns a uniFile with a unique score for each continent
    rankInCon = list(dict.fromkeys(rankInCon))
    topRankInList = min(rankInCon)
    maxScore = uniFile["Score"][topRankInList]            
    continentName = continentName.upper()
   
   # Computes a score relative to the average score.
    scoreRelative = avgScore / maxScore * 100
    
   #Part 8 
   
   # Returns a list of all the unique names in the list.
    capofUni = []
    for con in list_uniNum:
        elem = [z for z in capitalName if z in con]
        if (len(elem) == len(capitalName)):
            capofUni.append(con)  
           
    #Writes to the output.txt file
    #1 
    outFile.write(f"Total number of universities => {uniNum}\n\n")
    #2
    outFile.write(f"Available Countries => {finalCountry}\n\n")
    #3
    outFile.write(f"Available Continents => {finalContinent}\n\n")
    #4
    outFile.write(f"At international rank => {worldRank} the university name is=> {uni0}")
    #5
    outFile.write(f"At national rank => {nationalRank} the university name is => {uni1}\n\n")
    #6
    outFile.write(f"The average Score => {avgScore}%\n\n")
    #7
    outFile.write(f"The relative score to the top university in {continentName} is => ({avgScore} / {maxScore}) x 100% = {scoreRelative}%\n\n")
    #8
    outFile.write(f"The capital is  => {capitalName}")
    #9
    outFile.write("The universities that hold the capital name => ")
    # Writes all capofUni to a to the output file
    for e, element in enumerate(capofUni):
        # Displays the line number
        outFile.write(f"\n#{i+1} {element}")