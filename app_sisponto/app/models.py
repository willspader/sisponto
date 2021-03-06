import hashlib
from datetime import datetime

from flask import request

from sqlalchemy.orm import relationship, backref

from sqlalchemy import ForeignKeyConstraint

from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    is_admin = db.Column(db.Boolean)
    password_hash = db.Column(db.String(256))
    jornada = db.Column(db.Integer)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    bio = db.Column(db.Text)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    cpf = db.Column(db.String(11))
    avatar_hash = db.Column(db.String(256))
    talks = db.relationship('Talk', lazy='dynamic', backref='author')

    projeto = db.relationship("RelUsuProj", back_populates="usuario")

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if (self.email is not None) and (self.avatar_hash is None):
            self.avatar_hash = hashlib.md5(self.email.encode('utf-8')).hexdigest()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def serializeFuncionario(self):
        return {
            'id' : self.id,
            'perfil' : self.is_admin,
            'nome' : self.name,
            'jornada' : self.jornada,
            'email' : self.email
        }

    def gravatar(self, size=100, default='identicon', rating='g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        hash = self.avatar_hash or hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return "{url}/{hash}?s={size}&d={default}&r={rating}".format(url=url, hash=hash, size=size, default=default, rating=rating)

class Talk(db.Model):
    __tablename__ = 'talks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    slides = db.Column(db.Text())
    video = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    venue = db.Column(db.String(128))
    venue_url = db.Column(db.String(128))
    date = db.Column(db.DateTime())

class Cliente(db.Model):
    __tablename__ = 'TBCliente'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpfCnpj = db.Column(db.String(14), nullable=False, unique=True)
    nome = db.Column(db.String(64), nullable=False)
    tipoPessoa = db.Column(db.String(1), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)

    def __init__(self, cpfCnpjRecebido, nomeRecebido, tipoPessoaRecebido, emailRecebido):
        self.cpfCnpj = cpfCnpjRecebido
        self.nome = nomeRecebido
        self.tipoPessoa = tipoPessoaRecebido
        self.email = emailRecebido

    def serialize(self):
        return {
            'id' : self.id,
            'cpfCnpj' : self.cpfCnpj,
            'nome' : self.nome,
            'tipoPessoa' : self.tipoPessoa,
            'email' : self.email
        }

class Projeto(db.Model):
    __tablename__ = 'TBProjeto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricaoProj = db.Column(db.String(256), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('TBCliente.id'))
    cliente = db.relationship("Cliente", backref=backref("TBCliente", uselist=False))

    usuario = db.relationship("RelUsuProj", back_populates="projeto")

    def __init__(self, descricaoRecebida, idCliente):
        self.descricaoProj = descricaoRecebida
        self.cliente_id = idCliente

    def serializeProjeto(self):
        return {
            'id' : self.id,
            'descricao' : self.descricaoProj,
            'cliente_id' : self.cliente_id,
            'cliente_nome' : self.cliente.nome
        }

class RelUsuProj(db.Model):
    __tablename__ = 'TBRelUsuProj'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    projeto_id = db.Column(db.Integer, db.ForeignKey('TBProjeto.id'), primary_key=True)
    is_coordenador = db.Column(db.Boolean)

    usuario = db.relationship("User", back_populates="projeto")
    projeto = db.relationship("Projeto", back_populates="usuario")

    def serializeIndex(self):
        return {
            'codigoProj' : self.projeto.id,
            'usuario' : self.usuario.name,
            'descricao' : self.projeto.descricaoProj,
            'perfil': self.is_coordenador
        }

    def serializeRelacoes(self):
        return {
            'codigoProj' : self.projeto.id,
            'codigoUsu' : self.usuario.id,
            'descProj' : self.projeto.descricaoProj,
            'nomeFunc' : self.usuario.name
        }

class RegistroDias(db.Model):
    __tablename__ = 'TBRegistroDias'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datahr_inicio = db.Column(db.String(19))
    datahr_fim = db.Column(db.String(19))
    descricao = db.Column(db.String(256))

    user_id = db.Column(db.Integer, nullable=False)
    projeto_id = db.Column(db.Integer, nullable=False)

    ForeignKeyConstraint(['user_id', 'projeto_id'], ['RelUsuProj.user_id', 'RelUsuProj.projeto_id'])

    atividade_id = db.Column(db.Integer, db.ForeignKey('TBAtividades.id'))

    atividade = db.relationship("Atividades", backref=backref("TBAtividades", uselist=False))

    def __init__(self, datahr_inicio_r, datahr_fim_r, descricaoRecebida, usuarioRecebido, projetoRecebido, atividadeRecebida):
        self.datahr_inicio = datahr_inicio_r
        self.datahr_fim = datahr_fim_r
        self.descricao = descricaoRecebida
        self.user_id = usuarioRecebido
        self.projeto_id = projetoRecebido
        self.atividade_id = atividadeRecebida

    def serializeRegistros(self, descProjeto):
        return {
            'datahr_inicio' : self.datahr_inicio,
            'datahr_fim' : self.datahr_fim,
            'descricao' : self.descricao,
            'descProjeto' : descProjeto
        }

class Atividades(db.Model):
    __tablename__ = 'TBAtividades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricaoAtv = db.Column(db.String(32))

    def serializeAtividades(self):
        return {
            'id' : self.id,
            'descricao' : self.descricaoAtv
        }

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))