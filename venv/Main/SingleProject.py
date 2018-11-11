import os

import Utils

# autor: Oliver Kramer
# email: oliver.kramer@senacor.com
# alle rechte liegen beim autor und dürfen nur in abstimmung mit selbigen geaendert werden
# erstellt bei der ersten ausfuehrung die verifizierungs datei
# bei wiederholter ausfuehrung wird beim start die verifizierung durchgefuehrt.


projects=[]
source = "/appdata/abinitio/data/EDW/TestData/TEstDataContainer"
target = "/appdata/abinitio/data/EDW/EDW_ENTW/input_data/EDW"

def get_projects():
    return os.listdir(source)


def EP():
    projects=get_projects()
    print("Die vorhandenen Projekte sind:")
    for p in projects:
        print "\t",p
    in_proj = raw_input("Fue weclhes Projekt soll die Version geaendert werden?")
    os.chdir(os.path.join(source,in_proj))
    print "Vorhandene Versionen:"
    Utils.get_versions(".")
    link_v=raw_input("Welche version soll verlinkt werden?")
    try:
        os.symlink(os.path.join(source,in_proj,link_v), os.path.join(target,in_proj))
    except:
        #os.chdir(target)
        os.unlink(os.path.join(target,in_proj))
        os.symlink(os.path.join(source, in_proj, link_v), os.path.join(target, in_proj))