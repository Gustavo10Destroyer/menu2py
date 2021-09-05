import sys
import menu2py

my_menu1 = menu2py.Menu()
my_menu2 = menu2py.Menu()

def callback(menu, option_id):
  print()
  
  if menu.id == my_menu1.id:
    if option_id == 0:
      my_menu2.run()
    elif option_id == 1:
      sys.exit()
  elif menu.id == my_menu2.id:
    if option_id == 0:
      my_menu1.run()
    elif option_id == 1:
      sys.exit()

opt1 = menu2py.Option("Ir para o Menu 2", callback)
opt2 = menu2py.Option("Sair", callback)

opt3 = menu2py.Option("Voltar para o Menu 1", callback)
opt4 = menu2py.Option("Sair", callback)

my_menu1.addOption(opt1)
my_menu1.addOption(opt2)

my_menu2.addOption(opt3)
my_menu2.addOption(opt4)

my_menu1.run()