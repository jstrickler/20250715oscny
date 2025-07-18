from subprocess import run, PIPE, CalledProcessError

try:
    proc = run("netstat -an", capture_output=True)
except CalledProcessError as err:
    print(err)
else:
    if proc.returncode == 0:
        for line in proc.stdout.decode().splitlines():
            if "LISTEN" in line:
                print(line)