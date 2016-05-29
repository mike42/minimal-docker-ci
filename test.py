import json
import subprocess

# Container name (could also be retrieved from docker-compose.yml)
container_name = 'foo_1'

# Get IP address of container from the output of 'docker inspect'
try:
    container_json = subprocess.check_output(['docker', 'inspect', container_name])
    container_nets = json.loads(container_json)[0]['NetworkSettings']['Networks']
    container_ip = container_nets.itervalues().next()['IPAddress']
except Exception as e:
    print(e)
    exit(1)

# See if we get "Hello world" on port 5000 when we connect
server_port = '5000'
server_expected = 'Hello World\n'
ret = subprocess.check_output(['nc', container_ip, server_port])
print(ret)
if ret == server_expected:
    print('PASS: Output was correct')
    exit(0)
else:
    print('FAIL: Output was not correct')
    exit(1)

