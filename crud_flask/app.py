# pip install flask 
# pip install Flask-SQLAlchemy 
# pip install Flask-Migrate 
# pip install Flask-Script 
# pip install pymysql 
# flask db init 
# flask db migrate -m "Migração Inicial" 
# flask db upgrade
# flask run --debug

from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Reserve
app.config['SECRET_KEY'] = ['2c1685c157fe2450fda443a0753bb69f']

# drive://reserva:senha@servidor/banco_de_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/flaskg2"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dados', methods=['POST'])
def dados():
    flash('Dados enviados!')
    dados = request.form
    return render_template('dados.html', dados=dados)

@app.route('/reserve')
def reserva():
    u = Reserve.query.all()
    print(u)
    return render_template('reserve_lista.html', dados=u)

@app.route('/reserve/add')
def reserva_add():
    return render_template("reserve_add.html")

@app.route('/reserve/save', methods=['POST'])
def reserve_save():
    data = request.form.get('data')
    cliente = request.form.get('cliente')
    servico = request.form.get('servico')
    if data and cliente and servico:
        reserve = Reserve(data, cliente, servico)
        db.session.add(reserve)
        db.session.commit()
        flash('Usuário cadastrado com sucesso!!!')
        return redirect('/reserve')
    else:
        flash('Preencha todos os campos')
        return redirect('/reserve/add')

@app.route('/reserve/remove/<int:id>')
def reserve_remove(id):
    if id > 0:
        reserve = Reserve.query.get(id)
        db.session.delete(reserve)
        db.session.commit()
        flash('Reserva removida com sucesso!!!')
        return redirect('/reserve')
    else:
        flash('Caminho Incorreto!')
        return redirect('/reserve')
    
@app.route('/reserve/edita/<int:id>')
def reserva_edita(id):
    reserve = Reserve.query.get(id)
    return render_template("reserva_edita.html", dados = reserva)

@app.route('/reserva/edita/save', methods=['POST'])
def reserva_edita_save():
    nome = request.form.get('nome')
    email = request.form.get('email')
    idade = request.form.get('idade')
    id = request.form.get('id')
    if id and nome and email and idade:
        reserva = reserva.query.get(id)
        reserva.nome = nome
        reserva.email = email
        reserva.idade = idade
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/reserva')
    else:
        flash('Faltando dados!!')
        return redirect('/reserva')

if __name__ == '__main__':
    app.run()