import check50

@check50.check()
def exists():
    """square.py exists"""
    check50.exists("square.py")

@check50.check(exists)
def square_size_4():
    """Square of size 4"""
    check50.run("python3 square.py").stdin("4") \
        .stdout("####") \
        .stdout("#  #") \
        .stdout("#  #") \
        .stdout("####") \
        .exit(0)

@check50.check(exists)
def square_validate_input():
    """Validate square input"""
    check50.run("python3 square.py") \
        .stdin("0") \
        .stdin("-1") \
        .stdin("9") \
        .stdin("2") \
            .stdout("##").stdout("##") \
            .exit(0)
