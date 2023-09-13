import string
import random
from django.core.files.storage import FileSystemStorage

def saveFile(folder, format, file, name=None):

    if not name:
        caracteres = 30
        name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=caracteres))

    fss = FileSystemStorage()
    file = fss.save(folder + name + '.' + format, file)
    file_url = fss.url(file)
    return name