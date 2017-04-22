import magic
from django.core.exceptions import ValidationError
def validate_mime_type(value):
    supported_types=['video/mp4',]
    with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
        mime_type=m.id_buffer(value.file.read(1024))
        value.file.seek(0)
    if mime_type not in supported_types:
        raise ValidationError(u'Unsupported file type.')