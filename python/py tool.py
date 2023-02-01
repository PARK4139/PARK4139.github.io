# -*- coding: cp949 -*-
import time

class dataHandlingtool:
    def printDataAll():
        print("#not prepared this function,yet")
    def printDataAllasAdministrator():
        print("#not prepared this function,yet")
    def printTimeDataAll():
        print("#not prepared this function,yet")
    def printPersonalDataAll(self):
        print (f'__name : {self.__name}')
        print (f'__currentAge : {self.__currentAge}')
        print (f'__currentPhoneNumber : {self.__currentPhoneNumber}')
        print (f'__birthday : {self.__birthday}')
    # def returnDataAll(self):
    def saveDatatoDB():
        print("#not prepared this function,yet")
    def saveDatatoTextFile(self):
        print("#not prepared this function,yet")
                
                
# class Tool():
    # def initializeDataStorage():
        # DataStorage.gate = "closed"
        # DataStorage.data1 = ""
        # print( 'DataStorage.gate : '+DataStorage.gate)
        # print( 'DataStorage.data1 : '+DataStorage.data1)
    # def openDataStorage():
        # DataStorage.gate = "opened"
        # print( 'DataStorage.gate : '+DataStorage.gate)
    # def save(data):
        # if(DataStorage.gate == "opened"):
            # DataStorage.data1=data
            # print( DataStorage.data1+'saved'+' in the DataStorage')
        # elif (DataStorage.gate == "closed"):
            # print( "Tool can't put +data+\nbecause dataStorage is closed\n please, open dataStorage and try again")
    # def closeDataStorage():
        # DataStorage.gate = "closed"
        # print( 'DataStorage.gate : '+DataStorage.gate)
    # def lookUpDataStorage():
        # print( 'DataStorage.gate : '+DataStorage.gate)
        # print( 'DataStorage.data1 : '+DataStorage.data1)

class data:
    gate="open"
    data1=""

class timeData:
    def __init__(self):
        self.__currentTime=""
        self.__previousTime=""
         
class personalData:
    def __init__(self,remark):
        self.__name="jungHoonPark"
        self.__currentAge=""
        self.__currentPhoneNumber="currentPhoneNumber"
        self.__birthday="1994 04 05"
        self.remark=""
# _____________________________________________________________________________  [  empty class  ] 
class nothing:
    pass