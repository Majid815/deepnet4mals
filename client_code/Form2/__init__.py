from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
from .. import Module1

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.changed = False
    # Any code you write here will run when the form opens.
    


  def on_upload(self, file, **event_args):
    self.changed =True
    pass

  def go_analyze(self, **event_args):
    if self.changed:
      exe_file = self.exe_loader.file
      Module1.name = exe_file.name
      Module1.size = int(exe_file.get_length()/1024)
      if Module1.size > 10000:
        Notification('File too large, select another file small than 10MB', title='MAX SIZE ERROR').show()
      else:
        Module1.results = anvil.server.call('get_file', exe_file)
        print(Module1.results)
        open_form('Form3')
    else:
      Notification('Please select a file from your computer', title='NO FILE SELECTED').show()



