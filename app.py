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
from models import Vendas
app.config['SECRET_KEY'] = ['ch3Gu743RaM4c0nh4C0mun1sm0']

# drive://reserve:senha@servidor/banco_de_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/vendas"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vendas')
def vendas():
    u = Vendas.query.all()
    print(u)
    return render_template('vendas_lista.html', dados=u)

@app.route('/vendas/add')
def reserve_add():
    return render_template("vendas_add.html")

@app.route('/vendas/save', methods=['POST'])
def reserve_save():
    data = request.form.get('data')
    valor = request.form.get('valor')
    vendedor = request.form.get('vendedor')
    if data and valor and vendedor:
        vendas = Vendas(data, valor, vendedor)
        db.session.add(vendas)
        db.session.commit()
        flash('Venda cadastrada')
        return redirect('/vendas')
    else:
        flash('Preencha todos os campos')
        return redirect('/vendas/add')

@app.route('/vendas/remove/<int:id>')
def vendas_remove(id):
    if id > 0:
        vendas = Vendas.query.get(id)
        db.session.delete(vendas)
        db.session.commit()
        flash('Venda removida!')
        return redirect('/vendas')
    else:
        flash('Incorreto')
        return redirect('/vendas')
    
@app.route('/vendas/editar/<int:id>')
def vendas_editar(id):
    vendas = Vendas.query.get(id)
    return render_template("vendas_editar.html", dados = vendas)

@app.route('/vendas/editar/save', methods=['POST'])
def vendas_editar_save():
    data = request.form.get('data')
    valor = request.form.get('valor')
    vendedor = request.form.get('vendedor')
    id = request.form.get('id')
    if id and data and valor and vendedor:
        vendas = Vendas.query.get(id)
        vendas.data = data
        vendas.valor = valor
        vendas.vendedor = vendedor
        db.session.commit()
        flash('Venda atualizada com sucesso!')
        return redirect('/vendas')
    else:
        flash('Complete todos os dados!!')
        return redirect('/vendas')

if __name__ == '__main__':
    app.run()

