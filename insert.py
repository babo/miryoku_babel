#!/usr/bin/env python3

def main():
    with open('./readme.org') as fd:
        raw = fd.readlines()

    ch = []
    tmp = []
    skip_until = True
    for l in raw:
        if skip_until:
            if l.startswith('**** layer-body'):
                skip_until = False
        else:
            if 'BEAKL15' in l or 'beakl15' in l:
                tmp.append(l)
                l = l.replace('BEAKL15', 'GALLIUM').replace('beakl15', 'gallium')
            elif tmp:
                if not l.strip():
                    ch.append(l)
                for x in tmp:
                    ch.append(x)
                tmp = []
        ch.append(l)

    with open('readme.org', 'w') as fd:
        for l in ch:
            print(l, file=fd,end='')

if __name__ == '__main__':
    main()
