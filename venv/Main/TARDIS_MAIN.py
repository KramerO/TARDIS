import AllProjects
import FirstRun
from SingleProject import EP
from consols import getTerminalSize

#import console

projects=[]
source = "/appdata/abinitio/data/EDW/TestData/TEstDataContainer"


# autor: Oliver Kramer
# email: oliver.kramer@senacor.com
# alle rechte liegen beim autor und dürfen nur in abstimmung mit selbigen geaendert werden
# erstellt bei der ersten ausfuehrung die verifizierungs datei
# bei wiederholter ausfuehrung wird beim start die verifizierung durchgefuehrt.





def welcome():
    TARDIS=["######################################################################",
"#                                                                    #",
"#                                                                    #",
"#                                                                    #",
"#                                                                    #",
"#                                                                    #",
"#                                                                    #",
"#     T.A.R.D.I.S Total Abgefahrenes Daten Informations System       #",
"#                       version:ERIDIUM                              #",
"#                                                                    #",
"#                                                                    #",
"#                                                                    #",
"#                                                                    #",
"#                                                                    #",
"######################################################################"]
    w = getTerminalSize()[0]
    for l in TARDIS:
        print(l.center(w," "))

def menue():
    print("Einbinde der Testdaten")
    menue_points = {1: "Einzelprojekt", 2: "Alle Projekte", 3: "Exit"}
    while True:
        options=menue_points.keys()
        options.sort()
        for entry in options:
            print "\t",entry, menue_points[entry]

        selection = raw_input("Please Select:")
        if selection == '1':
            EP()
        elif selection == '2':
            AllProjects.link_menue()
        elif selection == '3':
            quit()
        else:
            print "Unknown Option Selected!"


def main():
    FirstRun.init_file()
    welcome()
    menue()


if __name__ == "__main__":
    main()