# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: class Filmes

"""""
#%% Class Filmes
# Import the generic class
from classes.gclass import Gclass

from classes.tipos import Tipos

class Filmes(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 1
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_code','_name','_tipo','_link']
    # Class header title
    header = 'Filmes'
    # field description for use in, for example, in input form
    des = ['Code','Name','Tipo','Link']
    # Constructor: Called when an object is instantiated
    def __init__(self, code,name,tipo,link):
        super().__init__()
        # Uncomment in case of auto number on
        if code == 'None':
            codes = Filmes.getatlist('_code')
            if codes == []:
                code = str(1)
            else:
                code = str(max(map(int,Filmes.getatlist('_code'))) + 1)
        
        # Object attributes
        
        # Check the customer referential integrity
        if tipo in Tipos.lst:
            self._code = code
            self._name = name
            self._tipo = tipo
            self._link = link
            # Add the new object to the Order list
            Filmes.obj[code] = self
            Filmes.lst.append(code)
        else:
            print('Tipos ', tipo, ' not found')

       

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
    # tipo property getter method
    @property
    def tipo(self):
        return self._tipo
    # link property getter method
    @property
    def link(self):
        return self._link
    
    # name property setter method
    @name.setter
    def name(self, name):
        self._name = name
    # tipo property setter method
    @tipo.setter
    def tipo(self, tipo):
        if tipo in Tipos.lst:
            self._tipo = tipo
        else:
            print('Tipos ', tipo, ' not found')    
        
    # link property setter method
    @link.setter
    def link(self, link):
        self._link = link
   