import check50

@check50.check()
def exists():
    """pathfinder.py exists"""
    check50.exists("pathfinder.py")

@check50.check(exists)
def decodes_a_single_letter():
    """decodes "41" as "A" """
    check50.run("python3 pathfinder.py").stdin("41").stdout("A\n").exit(0)

@check50.check(exists)
def decodes_sol():
    """decodes "534F4C" as "SOL" """
    check50.run("python3 pathfinder.py").stdin("534F4C").stdout("SOL\n").exit(0)

@check50.check(exists)
def decodes_status():
    """decodes "535441545553" as "STATUS" """
    check50.run("python3 pathfinder.py").stdin("535441545553").stdout("STATUS\n").exit(0)

@check50.check(exists)
def decodes_hi_mom():
    """decodes "4849204D4F4D" as "HI MOM" """
    check50.run("python3 pathfinder.py").stdin("4849204D4F4D").stdout("HI MOM\n").exit(0)

@check50.check(exists)
def decodes_not_dead():
    """decodes "4E4F542044454144" as "NOT DEAD" """
    check50.run("python3 pathfinder.py").stdin("4E4F542044454144").stdout("NOT DEAD\n").exit(0)

@check50.check(exists)
def decodes_punctuation():
    """decodes "4D41525321" as "MARS!" """
    check50.run("python3 pathfinder.py").stdin("4D41525321").stdout("MARS!\n").exit(0)
