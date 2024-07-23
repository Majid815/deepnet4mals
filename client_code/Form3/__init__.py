from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
from .. import Module1

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.f_name.text = Module1.name
    self.f_size.text = str(Module1.size) + 'KB'

    decision = ''
    n_mal = 0
    sum_mal = 0
    for s in Module1.results[1:]:
      if s>0.5:
        n_mal += 1
        sum_mal += s
    if n_mal>2:
      sum_mal = sum_mal/n_mal
    else:
      sum_mal = sum(Module1.results[1:])/4
      
    if sum_mal>0.5:
      decision = 'MALWARE'
      self.decision.foreground = 'RED'
    else:
      decision = 'SAFE'
      self.decision.foreground = 'GREEN'
    self.decision.text = decision
    # Any code you write here will run when the form opens.
    
    self.golb.data = [go.Pie(labels=['safe', 'malicious'], values = [ 1-sum_mal, sum_mal], hole=.7)]
    self.cnn.data = [go.Pie(labels=['safe', 'malicious'], values = [1-Module1.results[1], Module1.results[1]], hole=.7)]
    self.rnn.data = [go.Pie(labels=['safe', 'malicious'], values = [1-Module1.results[2], Module1.results[2]], hole=.7)]
    self.fnn1.data = [go.Pie(labels=['safe', 'malicious'], values = [1-Module1.results[3], Module1.results[3]], hole=.7)]
    self.fnn2.data = [go.Pie(labels=['safe', 'malicious'], values = [1-Module1.results[4], Module1.results[4]], hole=.7)]
