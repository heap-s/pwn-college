import subprocess

output = open("/tmp/cssjjw", 'w')
subprocess.call("/challenge/embryoio_level20", stdout=output)
