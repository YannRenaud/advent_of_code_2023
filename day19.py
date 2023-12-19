rules = {
    "px":  ["a<2006:qkq", "m>2090:A", "rfg"],
    "pv":  ["a>1716:R", "A"],
    "lnx": ["m>1548:A", "A"],
    "rfg": ["s<537:gd", "x>2440:R", "A"],
    "qs":  ["s>3448:A", "lnx"],
    "qkq": ["x<1416:A", "crn"],
    "crn": ["x>2662:A", "R"],
    "in":  ["s<1351:px", "qqz"],
    "qqz": ["s>2770:qs", "m<1801:hdj", "R"],
    "gd":  ["a>3333:R", "R"],
    "hdj": ["m>838:A", "pv"]
}


rule = "a<2006"
x=787
m=2655
a=1222
s=2876


def action(x, m, a, s, rule):
    for r in rule:
        if "A" in r or "R" in r:
            return r
        elif r in rules.keys():
            print(r)
            return action(x, m, a, s, rules[r])
        else:
            ev, dest = r.split(":")
            if eval(ev):
                print(dest)
                return action(x, m, a, s, rules[dest])

r = action(x, m, a, s, rules["px"])

e, d = 'a<2006:qkq'.split(":")