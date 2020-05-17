import re,os,ast,json
import datetime
import pandas as pd
from combineFileUtility import fileJSONLogic as fjl
#inputpath ="/home/satyajeet29/SWB_CombineFiles/DataFiles/".replace('/','//')
#outputpath= "/home/satyajeet29/SWB_CombineFiles/outputPath/".replace('/','//')
inputpath ="/Users/satyajeetpradhan/SWB_Covid_19/DataFiles/".replace('/','//')
outputpath= "/Users/satyajeetpradhan/SWB_Covid_19/outputPath/".replace('/','//')

subDirList = ['PaloAlto','WashingtonDC','SunnyVale','set0','set1','set2','set3','set4','set5','USA']
#subDirList = ['set1']
#subDirList = ['PaloAlto']
#obtain files from given subdirectory

for dirVal in subDirList:
    filepath = inputpath+dirVal+'//'
    fileOutPath = outputpath + dirVal + '//'
    fileList =os.listdir(filepath)
    fileList.sort()
    for file in fileList[-2:]:
        if ".txt" in file:
            print(str(datetime.datetime.now()) + " : " + dirVal  +" "+file + " started")
            df = fjl.jsonParse(filepath+file)
            #df.to_csv(fileOutPath+ file[:-3] + 'csv', encoding="utf-8")
            df.to_csv(fileOutPath + 'Unique_' +file[:-3] + 'csv', encoding="utf-8")
            print(str(datetime.datetime.now())+" : "+ dirVal  +" "+ file + " created")
            print("\n")
            del df
