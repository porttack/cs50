import check50

@check50.check()
def exists():
    """palindromes.py exists"""
    check50.exists("palindromes.py")

@check50.check(exists)
def my_mom_has_a_very_level_civic():
    """checking for 3 palindromes"""
    check50.run("python3 palindromes.py").stdin("My mom has a very level civic.").stdout("3\n").exit(0)

@check50.check(exists)
def does_my_mom_have_a_kayak():
    """checking for 2 palindromes"""
    check50.run("python3 palindromes.py").stdin("Does my mom have a kayak?").stdout("2\n").exit(0)

@check50.check(exists)
def How_was_your_race():
    """checking for 1 palindromes"""
    check50.run("python3 palindromes.py").stdin("How was your race? I heard your racecar broke?").stdout("1\n").exit(0)

@check50.check(exists)
def Skibidi_rizzler():
    """checking for 0 palindromes"""
    check50.run("python3 palindromes.py").stdin("Are you a Skibidi Rizzler?").stdout("0\n").exit(0)

@check50.check(exists)
def My_cats_nickname_is_Tacocat():
    """checking for 1 palindromes"""
    check50.run("python3 palindromes.py").stdin("My cats nickname is Tacocat, because he sure does loves tacos!").stdout("1\n").exit(0)

@check50.check(exists)
def bob_deified_to_sign():
    """checking for 4 palindromes"""
    check50.run("python3 palindromes.py").stdin("Bob deified to sign the deed to sign away his radar.").stdout("4\n").exit(0)

@check50.check(exists)
def The_murdrum_wore_a_bib():
    """checking for 2 palindromes"""
    check50.run("python3 palindromes.py").stdin("The murdrum wore a bib.").stdout("2\n").exit(0)
