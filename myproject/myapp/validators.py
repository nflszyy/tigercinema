from django.core.exceptions import ValidationError
def validate_mime_type(value):
    supported_types=['video/mp4',]
    if value.content_type not in supported_types:
    	raise ValidationError(u'Unsupported file type.')