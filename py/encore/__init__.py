import check50

@check50.check()
def exists():
    """encore.py exists"""
    check50.exists("encore.py")

@check50.check(exists)
def adds_and_plays_in_fifo_order():
    """plays songs in the order they were added"""
    check50.run("python3 encore.py") \
        .stdin("ADD Anti-Hero") \
        .stdin("ADD Flowers") \
        .stdin("PLAY") \
        .stdout(r"Now playing: Anti-Hero", "Now playing: Anti-Hero") \
        .stdin("PLAY") \
        .stdout(r"Now playing: Flowers", "Now playing: Flowers") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def play_on_empty_lineup():
    """PLAY on an empty lineup prints Nothing to play"""
    check50.run("python3 encore.py") \
        .stdin("PLAY") \
        .stdout(r"Nothing to play", "Nothing to play") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def lineup_rejects_a_sixth_song():
    """a 6th ADD is rejected once 5 songs are already waiting"""
    check50.run("python3 encore.py") \
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
def back_on_empty_history():
    """BACK before anything has played says so"""
    check50.run("python3 encore.py") \
        .stdin("BACK") \
        .stdout(r"Nothing has played yet", "Nothing has played yet") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def back_reports_most_recent_first():
    """BACK is LIFO: it reports the most recently played song first"""
    check50.run("python3 encore.py") \
        .stdin("ADD Anti-Hero") \
        .stdin("ADD Flowers") \
        .stdin("PLAY") \
        .stdin("PLAY") \
        .stdin("BACK") \
        .stdout(r"Last played: Flowers", "Last played: Flowers") \
        .stdin("BACK") \
        .stdout(r"Last played: Anti-Hero", "Last played: Anti-Hero") \
        .stdin("BACK") \
        .stdout(r"Nothing has played yet", "Nothing has played yet") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def back_does_not_requeue_the_song():
    """popping a song off history with BACK does not put it back in the lineup"""
    check50.run("python3 encore.py") \
        .stdin("ADD Anti-Hero") \
        .stdin("PLAY") \
        .stdin("BACK") \
        .stdin("PLAY") \
        .stdout(r"Nothing to play", "Nothing to play") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def unrecognized_command_prints_huh():
    """a command that isn't ADD, PLAY, BACK, or DONE prints Huh?"""
    check50.run("python3 encore.py") \
        .stdin("SKIP") \
        .stdout(r"Huh\?", "Huh?") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def lowercase_back_prints_huh():
    """commands are case-sensitive: lowercase back is not BACK"""
    check50.run("python3 encore.py") \
        .stdin("back") \
        .stdout(r"Huh\?", "Huh?") \
        .stdin("DONE") \
        .exit(0)

@check50.check(exists)
def done_ends_the_program():
    """DONE ends the program cleanly"""
    check50.run("python3 encore.py") \
        .stdin("DONE") \
        .exit(0)
