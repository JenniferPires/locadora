from config import *

class Filme(db.Model):

    id = db.Column(db.Integer, primary_key=True) 
    titulo = db.Column(db.String(254)) 
    data_lancamento = db.Column(db.String(254))
    preco = db.Column(db.Float)

    def __str__(self):
        return self.titulo + ", " + self.data_lancamento + ", " + \
        str(self.preco)

    def json(self):
        return {
          "id" : self.id,
          "titulo" : self.titulo,
          "data_lancamento" : self.data_lancamento,
          "preco" : self.preco
        }        

if __name__ == "__main__":
  
    db.create_all()

    
    titanic = Filme(titulo = "Titanic", data_lancamento = "05-09-1997", 
      preco = 10.99)

    homens_de_preto = Filme(titulo = "MIB: Homens de Preto", data_lancamento = "01-02-2005", 
      preco = 1.99)

    covid_19 = Filme(titulo = "Fim dos Tempo", data_lancamento = "05-09-2020", 
      preco = 100.99)

    outro_filme = Filme(titulo = "Outro filme", data_lancamento = "25-12-2010", 
      preco = 0.99)

    db.session.add(titanic)
    db.session.add(homens_de_preto)
    db.session.add(covid_19)
    db.session.add(outro_filme)
    db.session.commit()
    
    filmes_recuperados = db.session.query(Filme).all()

    print(filmes_recuperados)

    for f_r in filmes_recuperados:
          
      print(f_r)
      print(f_r.json())