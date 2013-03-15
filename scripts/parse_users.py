from core.models import HMUser

def from_csv(filename):
    all_lines = open(filename).readlines()
    total_lines = len(all_lines)
    current_line = 0
    
    users_to_save = []
    for line in all_lines:
        current_line += 1
        if line:
            line_split = line.split(',')
            
            firstname = line_split[0].strip()
            lastname = line_split[1].strip()
            email = line_split[2].lower().strip()
            password = line_split[3].strip()
            
            try:
                user = HMUser.objects.get(email = email)
            except HMUser.DoesNotExist:
                user = HMUser.objects.create_user(email=email, password=password)
                
            user.first_name = firstname
            user.last_name = lastname
            user.is_legacy = True
            
            user.save()
            print "({0} of {1}) Processed: {2}".format(current_line, total_lines, line)