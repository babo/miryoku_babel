#!/usr/bin/env python3
import sys


def main():
    name = sys.argv[1]
    assert name, "Need an argument with the name of the new layout"
    u_name = name.upper()
    l_name = name.lower()

    with open("./readme.org") as fd:
        raw = fd.read()

    assert f"~MIRYOKU_ALPHAS={u_name}~" not in raw, "Already there"

    ch = []
    tmp = []
    skip_until = True
    for l in raw.splitlines(keepends=True):
        if skip_until:
            if l.startswith("**** layer-body"):
                skip_until = False
        else:
            if "BEAKL15" in l or "beakl15" in l:
                tmp.append(l)
                l = l.replace("BEAKL15", u_name).replace("beakl15", l_name)
            elif tmp:
                if not l.strip():
                    ch.append(l)
                for x in tmp:
                    ch.append(x)
                tmp = []
        ch.append(l)

    with open("readme.org", "w") as fd:
        for l in ch:
            print(l, file=fd, end="")


if __name__ == "__main__":
    main()
