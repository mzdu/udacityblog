#Using list
list1 = [11,12,12,12,1,21]

#list是 不能通过增加任意index来增加容量的
list1[10] = 11000

print list1

#pydev debugger: starting
#Traceback (most recent call last):
#  File "C:\eclipse\plugins\org.python.pydev_2.7.1.2012100913\pysrc\pydevd.py", line 1397, in <module>
#    debugger.run(setup['file'], None, None)
#  File "C:\eclipse\plugins\org.python.pydev_2.7.1.2012100913\pysrc\pydevd.py", line 1090, in run
#    pydev_imports.execfile(file, globals, locals) #execute the script
#  File "D:\workspace\udacityblog\src\list_change.py", line 4, in <module>
#    list1[10] = 11000
#IndexError: list assignment index out of range
