from ._anvil_designer import UpdateDataComponentTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import linkedList

class UpdateDataComponent(UpdateDataComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  
  def submit_click(self, **event_args):
    linkedList.myList.Update(self.text_city.text, self.text_temp, self.text_airpol, self.text_landpol, self.text_waterpol, self.text_noisepol)
    


