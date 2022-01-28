## Module header template
- This doc explains the steps that a developer should take to write the module's template each time when they create new module in pycharm
- This also highlights set of metadata that one should have in their module
- This makes your code writing look professional 
- This configuration can save your time

Configuration steps in Pycharm : Ctrl+Alt+S -> Settings/Preferences -> Editor -> File and Code Templates -> Python scripts

- References 
https://www.jetbrains.com/help/pycharm/using-file-and-code-templates.html#syntax
https://stackoverflow.com/questions/1523427/what-is-the-common-header-format-of-python-files
http://epydoc.sourceforge.net/manual-fields.html#module-metadata-variables
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module desciption: 
Description of what ${NAME} does.
"""
# ${NAME} created at ${DATE}
__author__ = "Abhay Kumar"
__date__ = "${DATE}"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = ""
__email__ = ""
__status__ = "POC"

 if __name__ == '__main__': 
    pass
    
'''
