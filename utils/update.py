import subprocess
import os

# Update from git
os.chdir("../")
subprocess.call("git stash", shell=True) # stash any changes made on the server, just in case
subprocess.call("git pull", shell=True)

# Set permissions
subprocess.call("chmod -R 777 .", shell=True)
subprocess.call("chmod 400 it/devKey.pem", shell=True)

# Run Django Processes
os.chdir("code")
subprocess.call("./manage.py collectstatic", shell=True)
subprocess.call("./manage.py syncdb", shell=True)
subprocess.call("./manage.py migrate", shell=True)

# Restart Bitnami-Stack Apache
os.chdir("/home/bitnami/stack")
subprocess.call("./ctlscript.sh restart apache", shell=True)


print "\n\n** Update complete **"
