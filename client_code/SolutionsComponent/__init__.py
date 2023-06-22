from ._anvil_designer import SolutionsComponentTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SolutionsComponent(SolutionsComponentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.label_output.text +=  self.problem_Solution()
    
  def problem_Solution(self):
    s1 = ("On the basis of highest threat level of the city here is the Problem Solution that how we can reduce the threat level of the city according to different prospective from which threat level is calculated.")
    s2 = ("1)	Temperature:\nThere are several ways to reduce the Urban Heat Island effect\n•	Plant more Trees \n•	Green infrastructure\n•	Reduce reflective surfaces. \n•	Build smart buildings.")
    s3 = ("\n2)	Air Pollution:\nThis Is What You Can Do to Help Reduce Air Pollution \n•	Keep your car well tuned and maintained. Follow the mechanics instructions, such as changing the air filters, and checking the silencers\n•	Drive Eco Friendly hybrid cars\n•	Avoid excessive idling of your car\n•	Choose environmentally friendly cleaners\n•	Advocate for emission reductions from power plants")
    s4 = ("\n3)	Water Pollution:\nWater pollution can be reduced with some efforts, such as\n•	 A regular qualitative and quantitative monitoring of fresh water resources.\n•	 Construct proper sanitary landfill sites.\n•	 Investigate ground water quality.\n•	Provide government help for waste management by industries.\n•	Dispose of unwanted paints or oils carefully. They should not be thrown into drains or sewers.")
    s5 = ("\n4)	Noise Pollution:\nSimple steps to reduce noise pollution at home or offices \n•	Close the Windows.\n•	Shut the Door when using noisy Machines\n•	Lower the volume.\n•	Go Green by planning trees.\n•	Control Noise level near sensitive areas.")
    
    return (s1 + s2 + s3 + s4 + s5)
    
    