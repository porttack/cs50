import check50

@check50.check()
def exists():
    """battery.py exists"""
    check50.exists("battery.py")

@check50.check(exists)
def plain_percentage():
    """reports a plain percentage between 81 and 99"""
    check50.run("python3 battery.py").stdin("1.35/1.5").stdout(r"90%", "90%").exit(0)

@check50.check(exists)
def good_at_nominal():
    """reports GOOD at exactly 100%"""
    check50.run("python3 battery.py").stdin("1.5/1.5").stdout(r"GOOD \(100%\)", "GOOD (100%)").exit(0)

@check50.check(exists)
def good_above_nominal():
    """reports GOOD above 100%"""
    check50.run("python3 battery.py").stdin("1.65/1.5").stdout(r"GOOD \(110%\)", "GOOD (110%)").exit(0)

@check50.check(exists)
def good_at_top_boundary():
    """reports GOOD at exactly 120%, the top of the valid range"""
    check50.run("python3 battery.py").stdin("1.8/1.5").stdout(r"GOOD \(120%\)", "GOOD (120%)").exit(0)

@check50.check(exists)
def low_at_boundary():
    """reports LOW at exactly 80%"""
    check50.run("python3 battery.py").stdin("1.2/1.5").stdout(r"LOW \(80%\)", "LOW (80%)").exit(0)

@check50.check(exists)
def low_below_boundary():
    """reports LOW well under 80%"""
    check50.run("python3 battery.py").stdin("0.75/1.5").stdout(r"LOW \(50%\)", "LOW (50%)").exit(0)

@check50.check(exists)
def reprompts_on_non_numeric():
    """reprompts when the input isn't numeric"""
    check50.run("python3 battery.py") \
        .stdin("abc/1.5") \
        .stdin("1.35/1.5") \
        .stdout(r"90%", "90%") \
        .exit(0)

@check50.check(exists)
def reprompts_on_zero_nominal():
    """reprompts on a zero nominal voltage (ZeroDivisionError)"""
    check50.run("python3 battery.py") \
        .stdin("1.35/0") \
        .stdin("1.35/1.5") \
        .stdout(r"90%", "90%") \
        .exit(0)

@check50.check(exists)
def reprompts_on_negative_measured():
    """reprompts on a negative measured voltage"""
    check50.run("python3 battery.py") \
        .stdin("-1/1.5") \
        .stdin("1.35/1.5") \
        .stdout(r"90%", "90%") \
        .exit(0)

@check50.check(exists)
def reprompts_on_negative_nominal():
    """reprompts on a negative nominal voltage"""
    check50.run("python3 battery.py") \
        .stdin("1.35/-1.5") \
        .stdin("1.35/1.5") \
        .stdout(r"90%", "90%") \
        .exit(0)

@check50.check(exists)
def reprompts_on_implausibly_high_reading():
    """reprompts when the reading would be over 120%"""
    check50.run("python3 battery.py") \
        .stdin("1.95/1.5") \
        .stdin("1.35/1.5") \
        .stdout(r"90%", "90%") \
        .exit(0)

@check50.check(exists)
def reprompts_on_raw_ratio_over_120_even_if_rounded_percent_is_not():
    """reprompts on a raw reading over 120%, even when it would round down to a valid-looking 120%"""
    check50.run("python3 battery.py") \
        .stdin("1.8045/1.5") \
        .stdin("1.35/1.5") \
        .stdout(r"90%", "90%") \
        .exit(0)

@check50.check(exists)
def reprompts_on_missing_slash():
    """reprompts when the input has no slash at all"""
    check50.run("python3 battery.py") \
        .stdin("1.5") \
        .stdin("1.5/1.5") \
        .stdout(r"GOOD \(100%\)", "GOOD (100%)") \
        .exit(0)

@check50.check(exists)
def reprompts_on_too_many_parts():
    """reprompts when the input has more than one slash"""
    check50.run("python3 battery.py") \
        .stdin("1.5/1.5/1.5") \
        .stdin("1.5/1.5") \
        .stdout(r"GOOD \(100%\)", "GOOD (100%)") \
        .exit(0)
