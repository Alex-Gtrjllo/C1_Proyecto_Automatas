import requests
from bs4 import BeautifulSoup as b

class calificaciones:
    def __init__(self, link, matricula, password):
        self.link = link
        self.matricula = matricula
        self.password = password

    def obtener_materias(self):
        url = 'https://platinum.upchiapas.edu.mx/alumnos/login'

        client = requests.Session()
        html= client.get(url)
        content = html.content
        soup = b(content, "html.parser")

        crsf = soup.find('input', {'name': '_token'}).get('value')

        login_information = {
            '_token': crsf,
            'Matricula': self.matricula,
            'Password': self.password,
        }

        client.post('https://platinum.upchiapas.edu.mx/alumnos/login', data=login_information)
        html = client.get(self.link)
        content = html.content
        soup = b(content, "html.parser")

        materias = soup.find("table", {"class":"califTable"})
        totalMaterias = []
        for rows in materias.find_all('tr', {"class":"Approved"}):
            totalMaterias.append(rows.find('td', {"nowrap":"nowrap"}).text)
            
        for rows in materias.find_all('tr', {"class":"Failed"}):
            totalMaterias.append(rows.find('td', {"nowrap":"nowrap"}).text)

        # for i in totalMaterias:
        #     print(i)
        # print('el total de materias son:', len(totalMaterias))
        return totalMaterias