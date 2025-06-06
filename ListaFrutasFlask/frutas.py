class Fruta:
    def __init__(self):
        self._id = None     
        self._nome = ""     
        self._cor = ""      

    def set_id(self, id): 
        self._id = id
    def set_nome(self, nome): 
        self._nome = nome
    def set_cor(self, cor): 
        self._cor = cor

 
    def get_id(self): 
        return self._id
    def get_nome(self): 
        return self._nome
    def get_cor(self): 
        return self._cor
