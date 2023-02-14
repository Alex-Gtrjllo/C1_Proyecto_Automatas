import requests
from bs4 import BeautifulSoup as b

class calificaciones:
    def __init__(self, link, matricula, password):
        self.link = link
        self.matricula = matricula
        self.password = password

    def obtener_datos(self):
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
        codigo_html = soup.decode('utf-8')
        return codigo_html
    
if __name__ == '__main__':
    calificaciones("https://platinum.upchiapas.edu.mx/alumnos/calificaciones/historial", '193262', 'SqeadsltV=(h+c)*a_up19').obtener_datos()
