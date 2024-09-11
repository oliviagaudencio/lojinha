from database import db

class Vendas(db.Model):
    __tablename__ = "vendas"
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.Date)
    valor = db.Column(db.Float(10,2))
    vendedor = db.Column(db.String(100))

    def __init__(self, data, valor, vendedor):
        self.data = data
        self.valor = valor
        self.vendedor = vendedor

    def __repr__(self):
        return "<Vendedor {}>".format(self.vendedor)