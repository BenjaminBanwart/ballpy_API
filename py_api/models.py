from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Reptile(db.Model):
    __tablename__ =  'reptiles' 
    
    id = db.Column(db.Integer, primary_key = True) 
    reptile = db.Column(db.String(250)) 
    name = db.Column(db.Text) 