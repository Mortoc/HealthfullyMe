from dateutil import tz

def show_time_as(date, target_timezone, strftime = "%b %d %Y %I:%M %p"):
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz(target_timezone)
        
        time = date
        time = time.replace(tzinfo=from_zone)

        # Convert time zone
        time = time.astimezone(to_zone)

        return time.strftime( strftime )