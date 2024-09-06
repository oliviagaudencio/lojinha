from database import db

class Reserve(db.Model):
    __tablename__ = "reserve"
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.Date)
    cliente = db.Column(db.String(100))
    servico = db.Column(db.String(100))

    def __init__(self, data, cliente, servico):
        self.data = data
        self.cliente = cliente
        self.servico = servico

    def __repr__(self):
        return "<Reserva {}>".format(self.cliente)