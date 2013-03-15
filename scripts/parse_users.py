from core.models import HMUser

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
            
            try:
                user = HMUser.objects.get(email = email)
            except HMUser.DoesNotExist:
                # create the user here but only save it if the auth code is good
                user = HMUser.objects.create_user(email=email, password=password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
            
            print "(" + str(current_line) + " of " + str(total_lines) + ") Processed: " + line