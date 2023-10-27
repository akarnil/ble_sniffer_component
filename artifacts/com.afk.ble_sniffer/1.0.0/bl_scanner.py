#!/usr/bin/env python3

MAC_LIST_PATH = '/tmp/ble_macs'

def get_bl_devices():
    import subprocess


    BASH_LINE = "hcitool -i hci0 lescan".split(' ')
    process = subprocess.run(BASH_LINE, check=False, capture_output=True)
    out = str(process.stdout, 'UTF-8')

    out = out.split('\n')
    out = [s.strip('\t') for s in out]
    out = [s.replace('\t','|') for s in out]
    out = [tuple(s.split("|")) for s in out]
    out = [t for t in out if len(t) == 2]
    print(out)

    with open(MAC_LIST_PATH, "w", encoding="UTF-8") as file:
        for index, tup in enumerate(out):
            file.write(tup[0])
            if index != len(out) - 1:
                file.write(", ")


if __name__ == "__main__":
    get_bl_devices()
