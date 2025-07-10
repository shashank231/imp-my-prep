"""
Kar
|_Raj
    |_Sha
        |_Dev1
        |_Dev2
    |_Sha2
|_Harsh
    |_Us
        |_Luv
"""


dict1 = {
    "US": ["Luv"],
    "Kar": ["Raj", "Harsh"],
    "Raj": ["Sha", "Sha2"],
    "Harsh": ["US"],
    "Sha": ["Dev1", "Dev2", "Dev3"],
    "Dev1": ["abc", "def"],
    "def": ["ghi"],
}

def findManager():
    return "Kar"

def _print_chart(map, mgr, lvl):
    mgr_lvl = lvl
    jr_lvl = (lvl + 1)
    sjr_lvl = (lvl + 2)
    if lvl==1:
        print(" "*(mgr_lvl), end="")
        print(f"|_{mgr}")

    junrs = map.get(mgr)
    if junrs:
        for jun in junrs:
            print(" "*(jr_lvl), end="")
            print(f"|_{jun}")
            _print_chart(map, jun, sjr_lvl)


def printOrgChart(map):
    manager = findManager()
    _print_chart(map, manager, 1)

printOrgChart(dict1)


