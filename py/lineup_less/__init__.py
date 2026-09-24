import check50

@check50.check()
def exists():
    """lineup_less.py exists"""
    check50.exists("lineup_less.py")

@check50.check(exists)
def adds_and_plays_in_fifo_order():
    """plays songs in the order they were added"""
    check50.run("python3 lineup_less.py") \
        .stdin("ADD Anti-Hero") \
        .stdin("ADD Flowers") \
        .stdin("PLAY") \
        .stdout(r"Now playing: Anti-Hero", "Now playing: Anti-Hero") \
        .stdin("PLAY") \
        .stdout(r"Now playing: Flowers", "Now playing: Flowers") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def add_reports_added():
    """ADD prints Added: <song>"""
    check50.run("python3 lineup_less.py") \
        .stdin("ADD Sunroof") \
        .stdout(r"Added: Sunroof", "Added: Sunroof") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def add_preserves_spaces_in_title():
    """a multi-word song title survives ADD intact"""
    check50.run("python3 lineup_less.py") \
        .stdin("ADD Anti Hero") \
        .stdout(r"Added: Anti Hero", "Added: Anti Hero") \
        .stdin("PLAY") \
        .stdout(r"Now playing: Anti Hero", "Now playing: Anti Hero") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def play_on_empty_lineup():
    """PLAY on an empty lineup prints Nothing to play"""
    check50.run("python3 lineup_less.py") \
        .stdin("PLAY") \
        .stdout(r"Nothing to play", "Nothing to play") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def lineup_rejects_a_sixth_song():
    """a 6th ADD is rejected once 5 songs are already waiting"""
    check50.run("python3 lineup_less.py") \
        .stdin("ADD A") \
        .stdin("ADD B") \
        .stdin("ADD C") \
        .stdin("ADD D") \
        .stdin("ADD E") \
        .stdin("ADD F") \
        .stdout(r"Lineup is full", "Lineup is full") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def full_lineup_still_plays_normally():
    """a full lineup still plays its songs in order despite the rejection"""
    check50.run("python3 lineup_less.py") \
        .stdin("ADD A") \
        .stdin("ADD B") \
        .stdin("ADD C") \
        .stdin("ADD D") \
        .stdin("ADD E") \
        .stdin("ADD F") \
        .stdin("PLAY") \
        .stdout(r"Now playing: A", "Now playing: A") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def unrecognized_command_prints_huh():
    """a command that isn't ADD, PLAY, or DONE prints Huh?"""
    check50.run("python3 lineup_less.py") \
        .stdin("SKIP") \
        .stdout(r"Huh\?", "Huh?") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def bare_add_prints_huh():
    """ADD with nothing after it prints Huh?, not a crash"""
    check50.run("python3 lineup_less.py") \
        .stdin("ADD") \
        .stdout(r"Huh\?", "Huh?") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def lowercase_add_prints_huh():
    """commands are case-sensitive: lowercase add is not ADD"""
    check50.run("python3 lineup_less.py") \
        .stdin("add Flowers") \
        .stdout(r"Huh\?", "Huh?") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def done_ends_the_program():
    """DONE ends the program cleanly"""
    check50.run("python3 lineup_less.py") \
        .stdin("DONE") \
        .exit(0)
