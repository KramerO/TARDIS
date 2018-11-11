import getpass
import os
from time import sleep


# autor: Oliver Kramer
# email: oliver.kramer@senacor.com
# alle rechte liegen beim autor und dürfen nur in abstimmung mit selbigen geaendert werden
# erstellt bei der ersten ausfuehrung die verifizierungs datei
# bei wiederholter ausfuehrung wird beim start die verifizierung durchgefuehrt.

def init_file():
    home=os.environ['HOME']
    if os.path.exists(os.path.join(home,'.verify.ver')):
        user = getpass.getuser()
        ver_file=open(os.path.join(home,'.verify.ver'),"rb")
        lines = ver_file.readlines()
        abgl = open("verify.ver", "rb")
        abgl_lines = abgl.readlines()
        for l in range(len(abgl_lines) - 1):
            if lines[l] not in abgl_lines[l]:
                print ("oh no! Verifizierung fehlgeschlagen.")
                quit()




        if user in lines[len(lines)-1]:
            print("User erfolgreich verifiziert.")
        else:
            print("Der Angemeldete User darf das Programm nicht ausfuehren!")
            sleep(3)
            quit()
    else:
        user = getpass.getuser()
        in_file = open("./verify.ver","rb")
        lines = in_file.readlines()
        in_file.close()
        line_space = len(lines[0])
        fill_str = user
        for i in range(line_space-len(user)):
            fill_str = fill_str+"#"
        lines.append(fill_str)
        out_file=open(os.path.join(home,'.verify.ver'),"wb")
        for l in lines:
            out_file.write(l)
        out_file.close()
