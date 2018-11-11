import os


# autor: Oliver Kramer
# email: oliver.kramer@senacor.com
# alle rechte liegen beim autor und dürfen nur in abstimmung mit selbigen geaendert werden
# erstellt bei der ersten ausfuehrung die verifizierungs datei
# bei wiederholter ausfuehrung wird beim start die verifizierung durchgefuehrt.

def get_versions(path):
    versions = os.listdir(path)
    print("Es existeiren die folgenden Versionen:")
    for v in versions:
        print "\t",v
    return versions