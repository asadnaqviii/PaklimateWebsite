import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from .AddCityDataComponent import AddCityDataComponent

from anvil import *

class Node:
  def __init__(self, cName, cTemp, airPol, landPol, waterPol, noisePol):
    self.cityName = cName
    self.cityTemperature = cTemp

    self.airPol = airPol
    self.landpol = landPol
    self.waterPol = waterPol
    self.noisePol = noisePol
    
    self.threatLevel = 0 
    self.next = None
    
    
   

# contians all the linkedlist related functions, remove the ones which we wont need
class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0
    
     # used by insertFront  
    self.threatLIST=[]
    self.cityLIST=[]

  def display(self, dis):
    temp = self.head

    if self.head is None:
      print('No head!')

    while temp is not None:
      r = ("\n\n\t\tCity           : " + str(temp.cityName) + "\n\t\tTemperaure     : " + str(temp.cityTemperature) + "\n\t\tAir Pollution  : " + str(temp.airPol) 
      + "\n\t\tland Pollution : " + str(temp.landpol) + "\n\t\tWater Pollution: " + str(temp.waterPol) + "\n\t\tNoise Pollution: " + str(temp.noisePol) + "\n\t\tThreat Level   : " + str(temp.threatLevel) + "\n")
      dis.append(r)
      temp = temp.next
    return dis
     # todo: update 
  def InsertFront(self, cName, cTemp, airPol, landPol, waterPol, noisePol):
    checkingNode = self.head 
    comparedcurr = None
    
    while checkingNode is not None:
      if self.size != 0:
       if checkingNode.cityName.lower() != cName.lower():
        checkingNode = checkingNode.next
       else: 
        comparedcurr = cName
        print("CITY ALREADY EXISTS")
       
    if self.size == 0 or comparedcurr == None:  
      self.size += 1
      
    newNode = Node(cName, cTemp, airPol, landPol, waterPol, noisePol)
    if self.head is None:
      self.head = newNode
      alert("New City added to monitor \n Check Display Section!")
    else:
      newNode.next = self.head
      self.head = newNode
      alert("New Node inserted into Linkedlist \n Check Display Section!")
  
  def DeleteFront(self):
      if self.head is not None:
        temp = self.head
        self.head = self.head.next
        temp = None 
        self.size -= 1


  def InsertEnd(self, cName, cTemp, airPol, landPol, waterPol, noisePol):
    newNode = Node(cName, cTemp, airPol, landPol, waterPol, noisePol)
    self.size += 1

    if self.head is None:
      self.head = newNode
    else:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      temp.next = newNode


  def DeleteEnd(self):
      temp = self.head
      while temp.next.next is not None:
        secondLast = temp.next
        temp = temp.next
      temp.next = None
      self.size -= 1

  def InsertAfterNode(self, prevNode, cName, cTemp, airPol, landPol, waterPol, noisePol):
      newNode = Node(cName, cTemp, airPol, landPol, waterPol, noisePol)

      self.size += 1
      if prevNode is None:
        print('Given Node doesnot exist!')
        return
      else:
        newNode.next = prevNode.next
        prevNode.next = newNode

  def DeleteAfterNode(self, prevNode):
      if prevNode is None:
        print('Given Node doesnot exist!')
        return
      else:
        nodeToDelete = prevNode.next
        prevNode.next = prevNode.next.next
        nodeToDelete = None
        self.size -= 1

  def InsertAtPos(self, pos, cName, cTemp, airPol, landPol, waterPol, noisePol):
    if pos < 1:
      print('Position should be greater than 0!')
      return
    elif pos == 1:
      self.InsertFront(cName, cTemp, airPol, landPol, waterPol, noisePol)
    else:
      prevNode = self.head

      for i in range(1, pos - 1):
        if prevNode is not None:
          prevNode = prevNode.next

      if prevNode is not None:
        self.InsertAfterNode(prevNode, cName, cTemp, airPol, landPol, waterPol, noisePol)
      else:
        print("\nThe previous node is null.")  

  def DeleteAtPos(self, pos):
    if pos < 1:
      print('Position should be greater than 0!')
      return
    elif pos == 1 and self.head is not None:
      self.DeleteFront()
      self.size -= 1
    else:
      prevNode = self.head

      for i in range(1, pos - 1):
        if prevNode is not None:
          prevNode = prevNode.next

      if prevNode is not None and prevNode.next is not None:
        nodeToDelete = prevNode.next
        prevNode.next = prevNode.next.next
        nodeToDelete = None
        self.size -= 1
      else:
        print("\nThe previous node is null.")  
        
        

  def GetSize(self):
    s = 'Size of linked list: ' + str(self.size)
    return s
  
  def citySORTED(self,threatlist):
    curr=self.head
    i=0 
    n = len(threatlist)
    while i<n:
      curr=self.head
      while curr is not None:
        if curr.threatLevel == self.threatLIST[i]:
         self.cityLIST.append(curr.cityName ) #store the city name corresponding to its threat level

        curr=curr.next
      i+=1
    return self.cityLIST #CITY LIST SORTED
  def threatSORTING(self,threatlist,Nodecurrent):#bubble sort used
    while Nodecurrent is not None:      #store all the threat levels
      threatlist.append(Nodecurrent.threatLevel)      
      Nodecurrent = Nodecurrent.next
    #print("Unsorted: \n\t") #unsorted list of threat levels to check
    #print(threatlist)
    n=len(threatlist)
    #bubble sort threat levels
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if threatlist[j] > threatlist[j + 1] :
                threatlist[j], threatlist[j + 1] = threatlist[j + 1], threatlist[j]
    #print("Sorted: ") #sorted list of threat levels to check
    #print(threatlist)
    self.threatLIST=threatlist
    return self.threatLIST
  #def calcThreat and Sort
  def calcThreat(self):
    Nodecurrent = self.head
    if self.head is None:
      print('No head!')

    while Nodecurrent is not None:
      result=0
      result=result+(Nodecurrent.airPol/10)
      result=result+(Nodecurrent.landpol/10)
      result=result+(Nodecurrent.waterPol/10)
      result=result+(Nodecurrent.noisePol/10)
      result=result+(Nodecurrent.cityTemperature/10)
      Nodecurrent.threatLevel=result
  
      Nodecurrent = Nodecurrent.next    
  
  def threatSort(self, citylist):
    threatlist=[]
  #  citylist=[]
    Nodecurrent=self.head
    if self.head is None:
      print('No head!')   
    
    threatlist=self.threatSORTING(threatlist, Nodecurrent)
    self.cityLIST=self.citySORTED(threatlist)
    print()
    
    curr=self.head
    i=0 
    n = len(threatlist)
    while i<n:
      curr=self.head
      while curr is not None:
        if curr.threatLevel == threatlist[i]:
         citylist.append("\nCity Name: " + curr.cityName + "\n Threat Level: " + str(threatlist[i]) + "\n") #store the city name corresponding to its threat level
         
        curr=curr.next
      i+=1
    return (citylist)
    
  def Update(self, cityInput, inputTemp, inputAir, inputLand, inputWater, inputNoise):
    c=self.head
    c.cName = cityInput
    while c != None:
        c.cName = cityInput
        if c.cityName.lower() == cityInput.lower():
          alert("City Found! Check Display section for updated city information")
          
          print('Old Temperature Levels: ', c.cityTemperature)
          c.cityTemperature = int(inputTemp.text)
          print('new temp', c.cityTemperature)

          print('old Air Pollution Levels: ', c.airPol) 
          c.airPol = int(inputAir.text)
          print('New Air Pollution Level:', c.airPol)

          print('old Land Pollution Levels: ', c.landpol)
          c.landpol = int(inputLand.text)
          print('New Air Pollution Level:', c.landpol)

          print('old Water Pollution Levels: ', c.waterPol)
          c.waterPol = int(inputWater.text)
          print('New Air Pollution Level:', c.waterPol)
          
          print('old Noise Pollution Levels: ', c.noisePol)
          c.noisePol = int(inputNoise.text)
          print('New Air Pollution Level:', c.noisePol)
          return True # data found'''
        
        c = c.next
      
          
      
  

    return alert("City Not Found! Try entering the name of the existing cities.") # Data Not found

  

myList = LinkedList()
# data insert:


myList.InsertEnd("Islamabad" ,12 , 32.2 , 36.06 , 51.54 , 47.44)#Stores some cities data by admins
myList.InsertEnd("Karachi" , 12 , 78 , 86.03 , 68.84 , 69.8)
myList.InsertEnd("Lahore", 10, 190, 57, 75.64 , 64.74)
myList.InsertEnd("Quetta", 7, 78.57 , 92.64, 65.25, 68.42)
myList.InsertAtPos(2,"Peshawar", 13, 70.95, 61.72, 55.47, 54.69)
myList.calcThreat()

# temp

