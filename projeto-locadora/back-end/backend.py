from config import *
from modelo import Filme

@app.route("/")
def padrao():
    return "Rota padrão - locadora"

@app.route("/listar_filmes")
def listar_filmes():

    filmes = db.session.query(Filme).all()
    retorno = []    
    for f in filmes:
        retorno.append(f.json())
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/incluir_filme", methods=['post'])
def incluir_filme():

    dados = request.get_json()

    preco = 0.0

    try:
        preco = float(dados.get("preco"))
    except Exception as e:
        return {"resultado":"Favor inserir um valor válido no campo de preço"}

    """
    print("="*120)
    print(dados)
    print("-"*120)
    print("preco 1: ", dados['preco'])
    print("preco 2: ", dados.get("preco"))
    print("="*120)
    """

    novo_filme = Filme(**dados)
    db.session.add(novo_filme)
    db.session.commit()
    return {"resultado":'ok'}

if __name__ == "__main__":

    app.run(debug=True)