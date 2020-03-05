def strip_string(s):
    import re
    replaced_string1 = re.sub('[^\\w/]+', '_', s)
    replaced_string = re.sub('[_]+', '_', replaced_string1)
    return replaced_string
print(strip_string('h^&ell`.,  |o w/p]{+p_____orld'))
