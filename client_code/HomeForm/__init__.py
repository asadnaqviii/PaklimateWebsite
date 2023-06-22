from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ._anvil_designer import HomeFormTemplate
from .. import navigation


class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.base_title = self.label_title.text
    user = anvil.users.get_user()
    self.set_account_state((user))
    navigation.home_form = self
    navigation.go_home()
    
    #FOR NOW
    '''self.link_displaydata_click()
    self.link_add_click()
    self.link_home_click()
    self.link_account_click()'''
    
    
  def link_displaydata_click(self, **event_args):
    navigation.go_displaydata()

  def link_access_click(self, **event_args):
    navigation.go_accessdata()
  
  def link_add_click(self, **event_args):
    navigation.go_addmeasurement()

  def link_addcitydata_click(self, **event_args):  #for addcitydata
    navigation.go_addcitydata()
    
  def link_calculatesort_click(self, **event_args):
    navigation.go_threatlevelcalculator()
  
  def link_carbonfootprint_click(self, **event_args):
    navigation.go_carbonfootprint()
  
  def link_home_click(self, **event_args):
    navigation.go_home()
    #self.link_add.role = 'selected'
    
  def link_solutions_click(self, **event_args):
    navigation.go_solutions()
    
  def link_account_click(self, **event_args):
    navigation.go_account()
    
  def set_active_nav(self, state):
    self.link_home.role = 'selected' if state == 'home' else None
    self.link_account.role = 'selected' if state == 'acccount' else None
    self.link_displaydata.role = 'selected' if state == 'displaydata' else None
    
  def load_component(self, cmpt):
    self.column_panel_content.clear()
    self.column_panel_content.add_component(cmpt)

  def link_register_click(self, **event_args):
    user = anvil.users.signup_with_form(allow_cancel=True)
    set_account_state(user)
    navigation.go_home()
    
    
  def set_account_state(self, user):
    self.link_account.visible = user is not None
    self.link_logout.visible = user is not None
    self.link_login.visible = user is None
    self.link_register.visible = user is None

  def link_logout_click(self, **event_args):
    anvil.users.logout()
    self.set_account_state(None)
    navigation.go_home()

  def link_login_click(self, **event_args):
    user = anvil.users.login_with_form(allow_cancel= True)
    self.set_account_state(user)
    navigation.go_home()

  
    




  






 









  







 



