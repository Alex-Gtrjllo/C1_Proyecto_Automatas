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
        cal = []
        for rows in materias.find_all('tr', {"class":"Approved"}):
            aux = []
            for columns in rows.find_all('span', {"class":"ApprovedBadge"}):
                aux.append(columns.text)
            cal.append(aux)
            totalMaterias.append(rows.find('td', {"nowrap":"nowrap"}).text)
            
        # for rows in materias.find_all('tr', {"class":"Failed"}):
        #     aux = []
        #     for columns in rows.find_all('span', {"class":"ApprovedBadge"}):
        #         aux.append(columns.text)
        #     cal.append(aux)
        #     totalMaterias.append(rows.find('td', {"nowrap":"nowrap"}).text)

        # for i in range(len(totalMaterias)):
        #     print("La materia: ", totalMaterias[i], " tiene calificaciones: ", cal[i])
        # print('el total de cali son:', len(cal))
        # for i in materias:
        #     print(i)
        # print('el total de materias son:', len(totalMaterias))
        return totalMaterias, cal
        # print(materias)
    
# if __name__ == '__main__':
    # calificaciones("https://platinum.upchiapas.edu.mx/alumnos/calificaciones/historial", '193262', 'SqeadsltV=(h+c)*a_up19').obtener_materias()
    