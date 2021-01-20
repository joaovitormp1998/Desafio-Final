import json
from application.model.entity.Pessoa import Pessoa

class PessoaDAO:
    def __init__(self):
        with open ('application\\products.json') as product_file: # BUSCANDO LISTA DE PESSOAS JSONL
            pessoa_list = json.load(product_file)
        self._pessoas = []

        for produto in pessoa_list:# CONVERTENDO LISTA
             self._pessoas.append(Pessoa(produto['id'], produto['image'], produto['name'], produto['description'], produto['oldPrice'], produto['price'], produto['installments']['count'], produto['installments']['value']))

    def get_pessoas(self):
        return self._pessoas