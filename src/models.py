from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    titulo = db.Column(db.String(100), nullable=False)

    descricao = db.Column(db.Text, nullable=False)

    prioridade = db.Column(db.String(20), nullable=False)

    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Task {self.titulo}>"