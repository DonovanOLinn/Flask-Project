import requests as r




class Pokemon:
    def __init__(self, data):
        self.name = data['name']
        self.types = data['types'][0]['type']['name']
        self.height = data['height']
        self.weight = data['weight']
        self.base_experience = data['base_experience']
        self.ident = data['id']
        self.abilities = [v['ability']['name'] for v in data['abilities']]
        self.sprite = data['sprites']['front_default']




