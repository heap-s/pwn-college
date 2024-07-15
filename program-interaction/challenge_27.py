import subprocess

output = open('/tmp/fnnofu', 'w')

subprocess.call('/challenge/embryoio_level27', stdout=output)

with open('/tmp/fnnofu', 'r') as f:
    print(f.read())
