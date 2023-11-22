# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import subprocess

class DummySensor(object):
    def read_value(self):
        bash_line = "hciconfig hci0 reset".split(' ')
        process = subprocess.run(bash_line, check=False, capture_output=False)

        bash_line = "hcitool -i hci0 scan".split(' ')
        process = subprocess.run(bash_line, check=False, capture_output=True)
        out = str(process.stdout, 'UTF-8')

        out = out.split('\n')
        out = [s.strip('\t') for s in out]
        out = [s.replace('\t','|') for s in out]
        out = [tuple(s.split("|")) for s in out]
        out = [t for t in out if len(t) == 2]
        print(out)

        out_str = ""
        for index, tup in enumerate(out):
            out_str += tup[0]
            if index != len(out) - 1:
                out_str += ", "

        return out_str

if __name__ == '__main__':
    sensor = DummySensor()
    print(sensor.read_value())
