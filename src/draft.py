errordict = {"erro1": "e1",
             "erro2": "e2",
             "erro3": "e3"
             }

def write_form(dict1):
    print 'Our error message: %(erro1)s is %s' % dict1
    

write_form(errordict)  
    