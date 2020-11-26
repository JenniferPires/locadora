from config import *
from os.path import exists as fileexists
from os import remove as removefile
from sqlalchemy import exc
import sys

class Filme(db.Model):

  id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
  titulo = db.Column(db.String(254)) 
  data_lancamento = db.Column(db.String(254))
  preco = db.Column(db.Float)

  def __str__(self):

    return f"{self.titulo}, {self.data_lancamento}, {str(self.preco)}"

  def json(self):

    return {

      "id": self.id,
      "titulo": self.titulo,
      "data_lancamento": self.data_lancamento,
      "preco": self.preco

    }

class TipoDeMidia(db.Model):

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  nome = db.Column(db.String(254))
  midia_fisica = db.Column(db.Boolean)

  def __str__(self):

    return f"Tipo de midia: {self.nome}\nMídia física: {self.midia_fisica}\n"

  def json(self):

    return {

      "id": self.id,
      "nome": self.nome,
      "midia_fisica": self.midia_fisica

    }

class Midia(db.Model):
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  data_aquisicao = db.Column(db.String(254))
  filme_id = db.Column(db.Integer, db.ForeignKey(Filme.id))
  tipo_de_midia_id = db.Column(db.Integer, db.ForeignKey(TipoDeMidia.id))
  filme = db.relationship("Filme", backref="filme", uselist=False)
  tipo_de_midia = db.relationship("TipoDeMidia", backref="tipo_de_midia", uselist=False)

  def __str__(self):

    return f"ID do filme: {self.filme_id}\n{str(self.tipo_de_midia)}Data de aquisicao: {self.data_aquisicao}"

  def json(self):

    return {

      "id": self.id,
      "data_aquisicao": self.data_aquisicao,
      "filme_id": self.filme_id,
      "tipo_de_midia_id": self.tipo_de_midia_id,
      "filme": self.filme.json(),
      "tipo_de_midia": self.tipo_de_midia.json()

    }

if __name__ == "__main__":

  if fileexists(arquivobd):
    removefile(arquivobd)

  db.create_all()
  
  titanic = Filme(titulo = "Titanic", data_lancamento = "05-09-1997", 
    preco = 10.99)

  homens_de_preto = Filme(titulo = "MIB: Homens de Preto", data_lancamento = "01-02-2005", 
    preco = 1.99)

  covid_19 = Filme(titulo = "Fim dos Tempo", data_lancamento = "05-09-2020", 
    preco = 100.99)

  outro_filme = Filme(titulo = "Outro filme", data_lancamento = "25-12-2010", 
    preco = 0.99)

  try:

    db.session.add(titanic)
    db.session.add(homens_de_preto)
    db.session.add(covid_19)
    db.session.add(outro_filme)
    
    db.session.commit()
  
  except exc.IntegrityError as e:

    print("[-] IntegrityError [Filme]!")
    print(e)

    sys.exit(-1)
    db.session.rollback()

  cd = TipoDeMidia(nome = "CD", midia_fisica = True)
  cassete = TipoDeMidia(nome = "Cassete", midia_fisica = True)
  bluray = TipoDeMidia(nome = "Blu-ray", midia_fisica = True)
  mp4 = TipoDeMidia(nome = "MP4", midia_fisica = False)

  try:    

    db.session.add(cd)
    db.session.add(cassete)
    db.session.add(bluray)
    db.session.add(mp4)

    db.session.commit()

  except exc.IntegrityError as e:

    print("[-] IntegrityError [TipoDeMidia]!")
    print(e)

    sys.exit(-1)

    db.session.rollback()

  # titanic
  midia_titanic_mp4_1 = Midia(data_aquisicao = "15/11/2020", filme = titanic, tipo_de_midia = mp4)
  midia_titanic_bluray_1 = Midia(data_aquisicao = "15/11/2020", filme = titanic, tipo_de_midia = bluray)

  # homens de preto
  midia_homens_de_preto_cd_1 = Midia(data_aquisicao = "10/11/2020", filme = homens_de_preto, tipo_de_midia = cd)

  # covid_19
  midia_covid_19_cassete_1 = Midia(data_aquisicao = "01/01/2020", filme = covid_19, tipo_de_midia = cassete)

  # outro filme
  midia_outro_filme_bluray_1 = Midia(data_aquisicao = "25/07/2025", filme = outro_filme, tipo_de_midia = bluray)

  try:

    db.session.add(midia_titanic_mp4_1)
    db.session.add(midia_titanic_bluray_1)
    db.session.add(midia_homens_de_preto_cd_1)
    db.session.add(midia_covid_19_cassete_1)
    db.session.add(midia_outro_filme_bluray_1)

    db.session.commit()

  except exc.IntegrityError as e:

    print("[-] IntegrityError [Midia]!")
    print(e)

    sys.exit(-1)

    db.session.rollback()

  print()

  print("[+] Filmes", end="\n\n")

  for filme in db.session.query(Filme).all():
    
    print(str(filme), end="\n\n")
    print(filme.json())

  print()

  print("[+] Midias", end="\n\n")

  for midia in db.session.query(Midia).all():

    print()
    print(str(midia), end="\n\n")
    print(midia.json())