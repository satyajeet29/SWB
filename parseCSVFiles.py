import re,os,ast,json
import datetime
import pandas as pd
from combineFileUtility import fileParseLogic as fpl
inputpath ="/home/satyajeet29/SWB_CombineFiles/DataFiles/".replace('/','//')
outputpath= "/home/satyajeet29/SWB_CombineFiles/outputPath/".replace('/','//')
#subDirList = ['PaloAlto','USA','WashingtonDC','SunnyVale','set0','set1','set2','set3','set4','set5']
subDirList = ['PaloAlto']
#obtain files from given subdirectory

for dirVal in subDirList:
    filepath = inputpath+dirVal+'//'
    fileOutPath = outputpath + dirVal + '//'
    fileList =os.listdir(filepath)
    for file in fileList:
        print(str(datetime.datetime.now()) + " : " + dirVal  +" "+file + " started")
        df, dfuniq = fpl.fileParse(filepath+file)
        #df.to_csv(fileOutPath+ file[:-3] + 'csv', encoding="utf-8")
        dfuniq.to_csv(fileOutPath + 'Unique_' +file[:-3] + 'csv', encoding="utf-8")
        print(str(datetime.datetime.now())+" : "+ dirVal  +" "+ file + " created")



