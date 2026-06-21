from flask import Flask, render_template, request, redirect, url_for
from models import db, Task

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    prioridade = request.args.get("prioridade")

    if prioridade:
        tarefas = Task.query.filter_by(
            prioridade=prioridade
        ).all()
    else:
        tarefas = Task.query.all()

    return render_template(
        "index.html",
        tarefas=tarefas
    )


@app.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        nova_tarefa = Task(
            titulo=request.form["titulo"],
            descricao=request.form["descricao"],
            prioridade=request.form["prioridade"],
            status=request.form["status"]
        )

        db.session.add(nova_tarefa)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("create.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    tarefa = Task.query.get_or_404(id)

    if request.method == "POST":

        tarefa.titulo = request.form["titulo"]
        tarefa.descricao = request.form["descricao"]
        tarefa.prioridade = request.form["prioridade"]
        tarefa.status = request.form["status"]

        db.session.commit()

        return redirect(url_for("index"))

    return render_template(
        "edit.html",
        tarefa=tarefa
    )


@app.route("/delete/<int:id>")
def delete(id):

    tarefa = Task.query.get_or_404(id)

    db.session.delete(tarefa)
    db.session.commit()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
    