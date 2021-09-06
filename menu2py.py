import os
import sys
import uuid

def RenderFG(text, color):
  out = "\033[38;2;" + str(color[0]) + ";" + str(color[1]) + ";" + str(color[2]) + "m"
  out += str(text)
  out += "\033[0m"
  
  return out

def RenderBG(text, color):
  out = "\033[48;2;" + str(color[0]) + ";" + str(color[1]) + ";" + str(color[2]) + "m"
  out += str(text)
  out += "\033[0m"
  
  return out

class Option:
  def __init__(self, text, callback):
    self.text = text
    self.callback = callback
    self.text_color = [255, 255, 255]
    self.background_color = [0, 0, 0]

class Menu:
  def __init__(self):
    self.id = uuid.uuid4()
    self.selected = 0
    self.options = []
    
    self.hide_bg = True
    self.clear_on_exit = True
    
    self.selection_fg_color = [0, 0, 0]
    self.selection_bg_color = [255, 255, 255]
    
    self.width, self.height = os.get_terminal_size()
  
  def run(self):
    index = 0
    
    for option in self.options:
      space = " " * (self.width - len(option.text))
      
      if index == self.selected:
        sys.stdout.write("\r" + RenderBG(RenderFG(option.text, self.selection_fg_color), self.selection_bg_color) + space + "\n")
      else:
        if self.hide_bg:
          sys.stdout.write("\r" + RenderFG(option.text, option.text_color) + "\n")
        else:
          sys.stdout.write("\r" + RenderBG(RenderFG(option.text, option.text_color), option.background_color) + space + "\n")
      
      index += 1
  
    os.system("stty -F /dev/tty cbreak min 1") or None
    os.system("stty -F /dev/tty -echo") or None
    
    while True:
      key = sys.stdin.read(1)
      
      if key == "\n":
        if self.clear_on_exit:
          print("\033[F" * len(self.options), end="")
        
        self.options[self.selected].callback(self, self.selected)
        break
      elif key == "w":
        if self.selected > 0:
          self.selected -= 1
      elif key == "s":
        if len(self.options) > (self.selected + 1):
          self.selected += 1
      
      self.update()
  
  def update(self):
    print("\033[F" * len(self.options), end="")
    
    index = 0
    
    for option in self.options:
      if index == self.selected:
        sys.stdout.write("\r" + RenderBG(RenderFG(option.text, self.selection_fg_color), self.selection_bg_color) + "\n")
      else:
        space = " " * (self.width - len(option.text))
        
        if self.hide_bg:
          sys.stdout.write("\r" + RenderFG(option.text, option.text_color) + space + "\n")
        else:
          sys.stdout.write("\r" + RenderBG(RenderFG(option.text, option.text_color), option.background_color) + space + "\n")
      
      index += 1
  
  def addOption(self, option):
    self.options.append(option)