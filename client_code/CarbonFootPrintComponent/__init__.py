from ._anvil_designer import CarbonFootPrintComponentTemplate
from anvil import *

class CarbonFootPrintComponent(CarbonFootPrintComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.
    self.total = 0
    self.name = ""
  
    # user's name
  def text_name_pressed_enter(self, **event_args):
    self.name = self.text_name.text
    print("name entered: ", self.name)
    self.text_name.text = " "
  
  
    self.card_name.visible = False
    self.card_info.visible = True
    self.card_1.visible = True
 
    
   #  button click functions  
  def submit_click(self, **event_args):
    try:
      self.total = int(self.rb1.get_group_value())
      self.card_1.visible = False
      self.card_2.visible = True
    except TypeError:
      alert("Please select an option and then press the submit button")
    
      
  def submit2_click(self, **event_args):
    if self.card_1.visible is False:
      self.card_2.visible = True
      try:
        self.total += int(self.rb5.get_group_value())
        self.card_2.visible = False
        self.card_3.visible = True
      except TypeError:
        alert("Please select an option and then press the submit button")
        
      
  def submit3_click(self, **event_args):
    if self.card_2.visible is False:
      self.card_3.visible = True
      try:
        self.total += int(self.rb12.get_group_value())
        print("current total: ", self.total)
        self.card_3.visible = False
        self.card_4.visible = True
      except TypeError:
        alert("Please select an option and then press the submit button")
        
  def submit4_click(self, **event_args):
    if self.card_3.visible is False:
      self.card_4.visible = True
      try:
        self.total += int(self.rb13.get_group_value())
        print("current total: ", self.total)
        self.card_4.visible = False
        self.card_5.visible = True
      except TypeError:
        alert("Please select an option and then press the submit button")
        
      
  def submit5_click(self, **event_args):
      if self.card_4.visible is False:
        self.card_5.visible = True
        try:
          self.total += int(self.rb17.get_group_value())
          print("current total: ", self.total)
          self.card_5.visible = False
          self.card_transport.visible = True
          self.card_6.visible = True
        except TypeError:
          alert("Please select an option and then press the submit button")
          
  def submit6_click(self, **event_args):
    try:
      self.total += int(self.rb21.get_group_value())
      print("current total: ", self.total)
      self.card_6.visible = False
      self.card_7.visible = True
    except TypeError:
      alert("Please select an option and then press the submit button")
  
  def submit7_click(self, **event_args):
    try:
      self.total += int(self.rb25.get_group_value())
      print("current total: ", self.total)
      self.card_7.visible = False
      self.card_8.visible = True
    except TypeError:
      alert("Please select an option and then press the submit button")

  def submit8_click(self, **event_args):
    try:
      self.total += int(self.rb29.get_group_value())
      self.card_8.visible = False
      print("current total: ", self.total)
      self.label_2.visible = False
      self.card_transport.visible = False
      self.printResult()
    except TypeError:
      alert("Please select an option and then press the submit button")
    
   # result  
  def printResult(self):
    self.label_info.align = "center"
    if self.total < 60:
      self.label_info.text = self.name + ", your total carbon footprint is: " + str(self.total) + " which is less than 60 points!\nYou are making a small but an important impact on this beautiful planet!"
    elif self.total > 60:
      self.label_info.text = self.name + ", your total carbon footprint is: " + str(self.total) + " which is greater than 60 points!\nYou might want to look for some ways to reduce that check the probable solutions section for more info"
    elif self.total == 60:
      self.label_info.text = self.name + ", your total carbon footprint is: " + str(self.total) + "!\nYou might want to look for some ways to reduce that check the probable solutions section for more info"
      
  





  







