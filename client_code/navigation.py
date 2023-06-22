import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .DisplayComponent import DisplayComponent
from .HomeAnonComponent import HomeAnonComponent
from .AccountComponent import AccountComponent
from .HomeDetailsComponent import HomeDetailsComponent
from .AddCityDataComponent import AddCityDataComponent
from .ThreatCalculatorComponent import ThreatCalculatorComponent
from .CarbonFootPrintComponent import CarbonFootPrintComponent
from .SolutionsComponent import SolutionsComponent
from .UpdateDataComponent import UpdateDataComponent


home_form = None

def get_form():
  if home_form is None:
    raise Exception("You must set the home form first.")
    
  return home_form


def go_displaydata():
  set_title("Display Data")
  set_active_nav('displaydata')
  form = get_form()
  form.load_component(DisplayComponent())
  
def go_accessdata():
  set_title("Update/Access Data")
  set_active_nav('accessdata')
  
  user = require_acccount()
  if not user:
    go_home()
    return
    
  form = get_form()
  form.load_component(UpdateDataComponent())


def go_addmeasurement():
  set_title("Add Measurement")
  set_active_nav('addmeasurement')
  form = get_form()
  form.load_component(AddNodeComponent())

def go_addcitydata():
  set_title("Add City Data")
  set_active_nav('addcitydata')
  
  user = require_acccount()
  if not user:
    go_home()
    return
    
  form = get_form()
  form.load_component(AddCityDataComponent())
  
def go_threatlevelcalculator():
  set_title("Threat Level Calculator")
  set_active_nav('threatlevelcalculator')
  form = get_form()
  form.load_component(ThreatCalculatorComponent())
  
def go_carbonfootprint():
  set_title("Carbon Footprint Calculator")
  set_active_nav('carbonfootprint')
  form = get_form()
  form.load_component(CarbonFootPrintComponent())
  
def go_solutions():
  set_title("Probable Solutions")
  set_active_nav('solutions')
  form = get_form()
  form.load_component(SolutionsComponent())

def go_home():
  set_active_nav('home')
  set_title("")
  form = get_form()
  user = anvil.users.get_user()
  if user:
    form.load_component(HomeDetailsComponent())
  else:
    form.load_component(HomeAnonComponent())
      
  
def go_account():
  set_active_nav('account')
  set_title("Your Account")
  
  user = require_acccount()
  if not user:
    go_home()
    return
  form = get_form()
  form.load_component(AccountComponent())
  
def set_active_nav(state):
  form = get_form()
  form.set_active_nav(state)
  
  
def set_title(text):
  form = get_form()
  base_title = form.base_title
  
  if text:
    form.label_title.text = base_title + " - " + text
  else:
    form.label_title.text = base_title
    
    
def require_acccount():
  user = anvil.users.get_user()
  if user:
    return user
  
  user = anvil.users.login_with_form(allow_cancel=True)
  form = get_form()
  form.set_account_state(user)
  return user
  
    
    
    
    