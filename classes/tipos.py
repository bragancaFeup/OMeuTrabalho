# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class Tipos

"""""
#%% Class Tipos
# Import the generic class
from classes.gclass import Gclass

class Tipos(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_name']
    # Class header title
    header = 'Tiposs'
    # field description for use in, for example, in input form
    des = ['Code','Name']
    # Constructor: Called when an object is instantiated
    def __init__(self, code,name):
        super().__init__()
        # Object attributes
        self._code = code
        self._name = name

        # Add the new object to the Tipos_login list
        Tipos.obj[code] = self
        Tipos.lst.append(code)

    # Object properties
    # getter methodes
    # code property getter method
    @property
    def code(self):
        return self._code
    # name property getter method
    @property
    def name(self):
        return self._name
    
    # name property setter method
    @name.setter
    def name(self, name):
        self._name = name