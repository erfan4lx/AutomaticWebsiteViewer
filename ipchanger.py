import os
import time
banner = """                                                
  [[ye]]*   )                              (        
[[re]]` )  /(    )        (      )         )\    )  
 [[ye]]( )(_))( /(   (    )\    (      (  ((_)( /(  
[[re]](_(_()) )(_))  )\ )((_)   )\  '  )\  _  )(_)) 
[[gr]]|_   _|((_)_  _(_/( (_) _((_))  ((_)| |((_)_  
  [[gr]]| |  / _` || ' \))| || '  \()/ _ \| |/ _` | 
  |_|  \__,_||_||_| |_||_|_|_| \___/|_|\__,_| 

  M4nifest0 Cyber Security Team [erfan4lx]
  Unidentified Cyber Security Team [erfan4lx]
  Vortex Cyber Security Team [erfan4lx]
  
  github.com/erfan4lx  
  youtube.com/channel/UCHL7e6sD1eXIBIvjBYnXYEQ\n\n
"""
print(banner)
time.sleep(3)
os.system("cd core && bash setup.sh")
time.sleep(1)
os.system("clear")
print(banner)
op=str(input("Did you already initialize it(Y/n) :"))
if((op=="N") or (op=="n")):
 os.system("cd core && bash init.sh")
else:
 pass
os.system("cd core && bash vpn.sh")


