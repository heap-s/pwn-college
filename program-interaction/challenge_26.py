import subprocess

with open('/tmp/kjlwlp', 'w') as wf:
    wf.write("narcpemu")

input = open('/tmp/kjlwlp')

subprocess.call('/challenge/embryoio_level26', stdin=input)
