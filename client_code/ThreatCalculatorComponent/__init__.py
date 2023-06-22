from ._anvil_designer import ThreatCalculatorComponentTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from .. import linkedList


class ThreatCalculatorComponent(ThreatCalculatorComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    linkedList.myList.calcThreat()
    self.printList()
    self.ConfigurePlot()

   
   
   # self.label_sortThreat.text += self.printList()
    #self.label_threatSort.visible =  True
  def printList(self):
    dis = []
    linkedList.myList.threatSort(dis)
    
    for index in range(linkedList.myList.size):
      self.label_sortThreat.text += dis[index]
      

  def bSol_click(self, **event_args):
     alert('Check the probable solutions section for learning about ways to reduce the threat level')

  def ConfigurePlot(self):
    self.plot_1.layout.title = 'Threat Level Bar Graph'
    self.plot_1.layout.xaxis.title = 'Cities'
    self.plot_1.layout.yaxis.title = 'Threat level'
    
    # Plot some data
    self.plot_1.data = [
      go.Bar(
        x = linkedList.myList.cityLIST,
        y = linkedList.myList.threatLIST,
        
        marker = dict(color = 'rgb(167, 190, 211)',)
      )
    ]
    





 