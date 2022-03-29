from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import random
import string
from datetime import date

#PROGRAM METADATA
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<user>:<password>@localhost/<Database>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #para ocultar los warnings

db = SQLAlchemy(app)
ma = Marshmallow(app)
#IDs GENERATOR
ID_NUM_LEN = 2
ID_CHARS_LEN = 6
ADMITED_NUMS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
authentication_code =""


def _id_generator():
    deck_chars = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    id_part2 = random.sample(ADMITED_NUMS,ID_NUM_LEN)
    id_part1 = random.sample(deck_chars,ID_CHARS_LEN)
    id_final = id_part1 + id_part2
    #Pasamos a string mediante lista de comprehension
    id_final = ''.join([str(elem) for elem in id_final])
    #print("ID FINAL: ",id_final," cant: ",len(id_final)," tipo: ",type(id_final))
    return id_final

#Clase Almunos
class Alumno(db.Model):
    __tablename__ = "Alumnos"
    id = db.Column('Id',db.String(20), primary_key = True, nullable = False)
    email = db.Column(db.String(50),nullable = False,unique = True)
    password = db.Column(db.String(150),nullable = False,unique=False)
    activation_code = db.Column(db.String(50),nullable = True,unique = False)
    last_login =  db.Column(db.String(20),nullable = False,unique = False)
    activation = db.Column(db.Boolean,nullable = False,unique = False, default = False)
    
    def __init__(self,id,email,password,activation_code,last_login,activation):
        self.id = id
        self.email = email
        self.password = password
        self.activation_code = activation_code
        self.last_login = last_login
        self.activation = activation

db.create_all()#Lee todas las clases y las crea en tabla en nuestra base de datos

#Creamos un schema para interactuar rapidamente
class AlumnosSchema(ma.Schema):#Para imprimir y mostrar
    class Meta:
        fields = ('id','email','password','activation_code','last_login','activation')

alumno_schema = AlumnosSchema()#Un usuario

@app.route('/create_alumno',methods=['GET'])
def  create_alumno():
    print(request.json)
    id = _id_generator()
    # email = (request.json['email'])
    # password = request.json['password']
    email = 'mhere@gmail.com'
    password='pepe'
    activation_code = _id_generator() + _id_generator()
    last_login = date.today()
    new_alumno = Alumno(id,email,password,activation_code,last_login,0)
   
    
    db.session.add(new_alumno)
    db.session.commit()
    
    
    print(type(alumno_schema.jsonify(new_alumno)))
    return 'new-user-registered' 

@app.route('/get_alumnos',methods=['GET']) # No es optimo pero es la unica forma
def get_alumnos():
    result = []
    all_alumnos = Alumno.query.all()
    for i in all_alumnos:
        
        result.append(alumno_schema.dump(i))
        print(result)
    # print(alumno_schema.dump(all_alumnos[1]))
    print(result)
    return  {'Alumnos':result}   #Lo guardamos en el schema para mostrar al usuario

# @app.route('/get_alumno/<user_email>',methods=['GET']) # No funciona
# def get_alumno(user_email):
#     alumno = None
#     alumno = Alumno.query.filter_by(email = user_email).first()
#     print(alumno)
#     if alumno:
#         return 'true'
#     else:
#         return 'false'

@app.route('/get_alumno/<user_email>',methods=['GET']) # No funciona  
def set_activation_code(user_email):
    activation_code = 'wvRMhGD83MGBeCj59'
    alumno = None
    alumno = Alumno.query.filter_by(email = user_email).first()
    if alumno.activation_code == activation_code:
        return 'True'
    else:
        return 'False'



# @app.route('/filtro',methods=['GET']) # No funciona
# def get_alumnos_filtro():
#     result = []
#     alumnos = Alumno.query.filter(Alumno.last_login == date.today()).limit(2).all()
#     for i in alumnos:
#         result.append(alumno_schema.dump(i))
#     # print(alumno_schema.dump(all_alumnos[1]))
#     #print(result)
#     return  {'Almunos':result}


@app.route('/filtro',methods=['GET']) # No funciona
def get_alumnos_filtro():
    result = {}
    alumnos = Alumno.query.all()
    for i in alumnos:
        result[str(i.email)]=alumno_schema.dump(i) #Ponemos como clave del diccionario el email
    # print(alumno_schema.dump(all_alumnos[1]))
    #print(result)
    
    return  {'Alumnos':result}
    # print(result['manuelcereaizos@gmail.com'])
    # return result


if __name__ == '__main__':
    app.run(debug=True)
