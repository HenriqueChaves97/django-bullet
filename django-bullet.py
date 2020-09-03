import sys
import os
from pathlib import Path

def get_locale_package(package):
    locale = os.getcwd() + f"/{package}"
    return locale    

def model_app_name(app_name):
    return '--' + app_name

def main():
    scaffold_command_package = sys.argv[2].split(':')
    aplicativos = []

    if 'package' in scaffold_command_package:
        if len(scaffold_command_package)==2:
            os.system(f'django-admin startproject {scaffold_command_package[1]}')
        else:
            print("Type 'package:<ProjectName>' for usage.")
    else:
        print(f"Unknown command: {scaffold_command_package[0]}") 
        print("Type 'package:<ProjectName>' for usage.")
    
    def create_app(commands):
        if len(commands)==2:
            os.mkdir(f'{get_locale_package(scaffold_command_package[1])}/{commands[1]}')
            os.system(f'django-admin startapp {commands[1]} {get_locale_package(scaffold_command_package[1])}/{commands[1]}')
        else:
            print("Type 'package:<ProjectName>' for usage.")

    cont = 0
    check_apps = []
    for command in sys.argv:
        app = command.split(":")
        if 'app' in app:
            print('level 1', app)            
            aplicativos.append(app[1])
            create_app(app)
            cont += 1
        elif cont == 0:
            pass
        else:
            for app_name in aplicativos:
                if app_name not in check_apps:
                    for i in sys.argv:                        
                        if model_app_name(app_name) in i.split(':'):
                            print("model is valid")                
                    check_apps.append(app_name)                   
                else:
                    pass                  
            cont -= 1

if __name__=='__main__':
    if sys.argv[1] == 'scaffold':
        main()
    elif sys.argv[1] == 'help':
        print("django-scaffold.py <command> :")
        print(" <scaffold>")
        print(" <help>")
    else:
        print(f"Unknown command: {sys.argv[1]}") 
        print("Type 'django-scaffold.py help' for usage.")
