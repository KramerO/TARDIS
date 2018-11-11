import os

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


def link_menue():
    print("Sind sie sich sicher?")
    menue_points = {1: "Ja", 2: "nein"}

    while True:
        options = menue_points.keys()
        options.sort()
        for entry in options:
            print "\t", entry, menue_points[entry]

        selection = raw_input("Please Select:")
        if selection == '1':
            AP()
        elif selection == '2':
            quit()
        else:
            print "Unknown Option Selected!"

def AP():
    projects=get_projects()
    versions = {}
    for p in sorted(projects):
        #print p
        versions[p] = sorted(os.listdir(os.path.join(source,p)),reverse=True)[0]


    for pro in versions.keys():
        try:
            os.symlink(os.path.join(source, pro, versions[pro]), os.path.join(target, pro))
        except:
            os.unlink(os.path.join(target, pro))
            os.symlink(os.path.join(source, pro, versions[pro]), os.path.join(target, pro))
    print("PIPI-fein")
    quit()
