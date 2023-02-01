# _____________________________________________________________________________  [  plan ]
# mainSpace.py : 시스템을 운용할 main 파일로 사용할 예정이다.
# tool.py : mainSpace.py 내에서 필요한 기능들을 넣어둔 파일.
# dataFrame.py : 특정 목적을 위한 dataFrame을 object(class) 형태로 작성한다. 
# data.py : 시스템을 운용하며 만들어진 intance에 


# _____________________________________________________________________________  [  predictedProgramWorkingSenario as program perspective  ] 
# _____________________________________________________________________________  [  predictedProgramWorkingSenario as usr perspective  ] 
# _____________________________________________________________________________  [  predictedProgramWorkingSenario as developer perspective  ] 
# 1 : excute mainSpace.py     # 개인정보를 핸들링 하기로 한다.
# 2 : mainSpace.py에서 필요한 기능을 tool에서 가져온다.
# dataFrame.py의 object를 instance화 시켜 사용할 예정이다.


# _____________________________________________________________________________  [  development policy  ] 
# mainSpace.py를 main 으로 삼는다.

# _____________________________________________________________________________  [  plan Alpha.py  ]
# _____________________________________________________________________________  [  declareModules  ] 
# from tool import *
# from dataFrame import personalityDataFrame
# from dataFrame import rfCommunicationDataFrame
# from dataFrame import pwmCommunicationDataFrame
# from dataFrame import wifiCommunicationDataFrame
# from data import personalityData
# from data import rfCommunicationData
# from data import pwmCommunicationData
# from data import wifiCommunicationData
# _____________________________________________________________________________  [  initializeDataFrame  ] 
# personalityDataFrame.name=""
# personalityDataFrame.age=""
# personalityDataFrame.phoneNumber=""
# personalityDataFrame.homeAddress=""
# personalityDataFrame.officeAddress=""
# personalityDataFrame.academyAddress=""


# _____________________________________________________________________________  [  generate dataFrame as Instance  ] 
# _____________________________________________________________________________  [  plan dataFrame.py  ] 
# _____________________________________________________________________________  [  plan data.py  ] 
# _____________________________________________________________________________  [  plan tool.py  ] 
# tool.destroyDataAll()


# ____________________________________________________________________________________________________________________________________________________________
# _____________________________________________________________________________  [  mainSpace.py  ] 

# _____________________________________________________________________________  [  doPythonRestartPythonAtCurrentDirectory  ]

# _____________________________________________________________________________  [  setCodingWay  ] 
# -*- coding: cp949 -*-

# _____________________________________________________________________________  [  bring Tool class from Tool.py package  ] 
# from tool import *
from tool import dataHandlingtool
from tool import data
dataHandlingtool.printDataAll()
data.gate
data.data1


personalData.name
personalData.name="jhp"
personalData.name


Tool.initializeDataStorage()
Tool.openDataStorage()
Tool.save("stupidPerson")
Tool.closeDataStorage()
Tool.lookUpDataStorage()




tool.initializeDataStorage()
tool.openDataStorage()
tool.save("test")
tool.closeDataStorage()
tool.lookUpDataStorage()

