from django.contrib.auth.models import User
from core.encode import email_to_username

def from_csv(filename):
    all_lines = open(filename).readlines()
    total_lines = len(all_lines)
    current_line = 0
    for line in all_lines:
        current_line += 1
        if line:
            line_split = line.split(',')
            
            firstname = line_split[0]
            lastname = line_split[1]
            email = line_split[2]
            password = line_split[3].rstrip()
            
            username = email_to_username(email) 
            
            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                # create the user here but only save it if the auth code is good
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = firstname
                user.last_name = lastname
                
                user.save()
            
            print "(" + str(current_line) + " of " + str(total_lines) + ") Processed: " + line