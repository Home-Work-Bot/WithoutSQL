PATH = "./config/"
def getAdmins()->dict:
    a = set()
    with open(PATH + "admins", 'r') as f:
        names = f.read().split()
        for n in names:
            a.add(n)
    return a
def getSubjects()->dict:
    s = []
    with open(PATH + "subjects", 'r') as f:
        subjects = f.read().split()
        for f in subjects:
            s.append(f)
    return s

def getState():
    d = dict()
#getData()