from ._anvil_designer import AddCityDataComponentTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from .. import linkedList

class AddCityDataComponent(AddCityDataComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    cityName = ""
    cityTemp = 0
    airPol = 0
    landPol = 0
    waterPol = 0
    noisePol = 0
    
  def button_AddData_click(self, **event_args):
    self.label_error.visible = False
    error = self.CheckError()
    if error:
      self.label_error.text = error
      self.label_error.visible = True
    
    self.SetInput()
    
  def SetInput(self):
    cityName = self.textBox_city.text
    
    cityTemp = self.textBox_Temp.text
    airPol = self.textBox_Airpol.text
    landPol = self.textBox_Landpol.text
    waterPol = self.textBox_Waterpol.text
    noisePol = self.textBox_NoisePol.text
    
    linkedList.myList.InsertFront(cityName, cityTemp, airPol, landPol, waterPol, noisePol)
   
  
  def CheckError(self):
    if not self.textBox_city.text:
      return("City Name is required")
    
    if not self.textBox_Airpol.text:
      return("Air Pollution level is required")
    
    if not self.textBox_Landpol.text:
      return("Land Pollution level is required")
    
    if not self.textBox_Waterpol.text:
      return("Water Pollution level is required")
    
    if not self.textBox_NoisePol.text:
      return("Noise Pollution level is required")
    

    
