import requests

class SnowRequests(object):
    def __init__(self, instance:str, user:str, password:str) -> None:
        self.instance = instance
        self.user = user
        self.password = password
        self.api = '/api/now/table/sys_dictionary?'
        self.fields = 'sysparm_fields=name,element,internal_type,reference.name,dependent_on_field'
        self.excludeReferenceLink = 'sysparm_exclude_reference_link=True'
        self.noCount = 'sysparm_no_count=true'
        self.data = None
    def buildQuery(self, tables:list) -> None:
        self.query = 'sysparm_query=nameIN'
        for t in tables:
            self.query += str(t) + ','
        self.query = self.query[0:-1]
        self.query += '^internal_type!=collection&^ORDERBYname'
    def getData(self) -> None:
        headers = {"Content-Type":"application/json","Accept":"application/json"}
        url = self.instance 
        url += self.api 
        url += self.query + '&'
        url += self.fields + '&'
        url += self.excludeReferenceLink + '&'
        url += self.noCount
        response = requests.get(url, auth=(self.user, self.password), headers=headers)
        if response.status_code != 200:
            response.raise_for_status()
        self.data = response.json()
        


