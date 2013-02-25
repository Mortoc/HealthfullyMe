import subprocess, os, sys, shutil

# create the virtualenv
# install all the prereqs available in pip
# install the stripe API
print "\nSetting up VirtualEnv\n"
subprocess.call(
	"virtualenv ../site --distribute && " +
	"chmod -R 777 ../site && " +
	"source ../site/bin/activate && " +
	"pip install Django psycopg2 dj-database-url south django-tastypie && " +
	"pip install --index-url https://code.stripe.com --upgrade stripe", 
	shell=True
)

reqs_file = "requirements.txt"
print "Saving requirements to " + reqs_file
subprocess.call("pip freeze > " + reqs_file, shell = True)

print "*******************************************"
print "*                                         *"
print "* Completed installing prereqs.           *"
print "* Use source 'site/bin/activate' to       *"
print "* enable the virtualenv                   *"
print "*                                         *"
print "*******************************************"

