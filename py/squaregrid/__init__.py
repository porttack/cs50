import check50

@check50.check()
def exists():
    """square_grid.py exists"""
    check50.exists("square_grid.py")

@check50.check(exists)
def square_grid_size_4():
    """Square Grid of size 4"""
    check50.run("python3 square_grid.py").stdin("4") \
        .stdout("####") \
        .stdout("#  #") \
        .stdout("#  #") \
        .stdout("####") \
        .exit(0)

@check50.check(exists)
def square_grid_validate_input():
    """Validate square grid input"""
    check50.run("python3 square_grid.py") \
        .stdin("0") \
        .stdin("-1") \
        .stdin("9") \
        .stdin("2") \
            .stdout("##").stdout("##") \
            .exit(0)
