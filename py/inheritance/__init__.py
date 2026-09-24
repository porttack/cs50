import re

import check50

LINE_RE = re.compile(
    r"^(?P<indent> *)(?P<label>[A-Za-z-]+) \(Generation (?P<gen>\d+)\): blood type (?P<alleles>[A-Z]{2})$"
)

# The base spec is fixed at 3 generations: a child, their 2 parents, and
# their 4 grandparents, printed pre-order (person, then parent 0's whole
# subtree, then parent 1's).
EXPECTED_SHAPE = [
    ("Child", 0),
    ("Parent", 1),
    ("Grandparent", 2),
    ("Grandparent", 2),
    ("Parent", 1),
    ("Grandparent", 2),
    ("Grandparent", 2),
]


def run_and_parse():
    """Runs inheritance.py once and parses its output into a list of
    {"indent", "label", "gen", "alleles"} dicts, one per printed line."""
    run = check50.run("python3 inheritance.py")
    output = run.stdout()
    if run.exitcode != 0:
        raise check50.Failure(f"expected exit code 0, not {run.exitcode}")

    lines = [line for line in output.split("\n") if line.strip()]
    people = []
    for line in lines:
        match = LINE_RE.match(line)
        if not match:
            raise check50.Failure(f"unexpected line of output: {line!r}")
        people.append(
            {
                "indent": match.group("indent"),
                "label": match.group("label"),
                "gen": int(match.group("gen")),
                "alleles": match.group("alleles"),
            }
        )
    return people


def alleles_trace_back(child_alleles, parent_a_alleles, parent_b_alleles):
    """True if child_alleles could have come from one allele each of
    parent_a_alleles and parent_b_alleles, in either order."""
    a, b = child_alleles
    return (a in parent_a_alleles and b in parent_b_alleles) or (
        a in parent_b_alleles and b in parent_a_alleles
    )


@check50.check()
def exists():
    """inheritance.py exists"""
    check50.exists("inheritance.py")


@check50.check(exists)
def prints_correct_shape():
    """prints 7 lines: Child, Parent, 2 Grandparents, Parent, 2 Grandparents"""
    # Alleles are random, so run it a few times rather than trusting one sample.
    for _ in range(3):
        people = run_and_parse()
        if len(people) != 7:
            raise check50.Failure(f"expected 7 lines of output, got {len(people)}")
        for person, (expected_label, expected_gen) in zip(people, EXPECTED_SHAPE):
            if person["label"] != expected_label or person["gen"] != expected_gen:
                raise check50.Failure(
                    f"expected \"{expected_label} (Generation {expected_gen})\", "
                    f"got \"{person['label']} (Generation {person['gen']})\""
                )
            if person["indent"] != "    " * expected_gen:
                raise check50.Failure(
                    f"expected {4 * expected_gen} spaces of indentation before "
                    f"a generation {expected_gen} line, got {len(person['indent'])}"
                )


@check50.check(exists)
def alleles_are_valid():
    """every printed blood type is two characters, each A, B, or O"""
    for _ in range(3):
        people = run_and_parse()
        for person in people:
            alleles = person["alleles"]
            if len(alleles) != 2 or any(allele not in "ABO" for allele in alleles):
                raise check50.Failure(f"invalid blood type printed: {alleles!r}")


@check50.check(exists)
def alleles_trace_to_parents():
    """each person's two alleles each came from one of their two parents"""
    for _ in range(3):
        people = run_and_parse()
        child, parent0, grandparent0, grandparent1, parent1, grandparent2, grandparent3 = people

        if not alleles_trace_back(child["alleles"], parent0["alleles"], parent1["alleles"]):
            raise check50.Failure("the child's alleles don't trace back to their two parents")
        if not alleles_trace_back(
            parent0["alleles"], grandparent0["alleles"], grandparent1["alleles"]
        ):
            raise check50.Failure(
                "the first parent's alleles don't trace back to their two parents"
            )
        if not alleles_trace_back(
            parent1["alleles"], grandparent2["alleles"], grandparent3["alleles"]
        ):
            raise check50.Failure(
                "the second parent's alleles don't trace back to their two parents"
            )
