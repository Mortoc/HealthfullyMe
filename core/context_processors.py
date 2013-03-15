from django.conf import settings
    
def config_data(request):
    return { 'SEGMENT_IO_KEY' : settings.SEGMENT_IO_KEY, }