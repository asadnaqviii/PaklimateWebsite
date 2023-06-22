from ._anvil_designer import DisplayComponentTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# backend
from .. import linkedList


class DisplayComponent(DisplayComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.ShowSizeOnForm()
    linkedList.myList.calcThreat()
    
    # printing data
    for index in range(linkedList.myList.size):
      self.ShowDataOnForm(self.label_output, index, index)

        
  
   # print the current size of linked list   
  def ShowSizeOnForm(self):
    self.label_getsize.visible =  True
    self.label_getsize.text = linkedList.myList.GetSize()

  # printing the nodes on label
  def ShowDataOnForm(self, label, nodeNumber,indexNumber):
    nodeList = []
    linkedList.myList.display(nodeList)
    label.visible = True
    label.content += "City # " + str(indexNumber + 1) + nodeList[indexNumber] 
   
    
 




  

  


