from subprocess import run, PIPE, CalledProcessError

proc = run("cmd /c dir", stdout=PIPE, stderr=PIPE)
# print(proc)
print(proc.returncode)
print(proc.stdout.decode())
print('-' * 60)
print(proc.stderr.decode())