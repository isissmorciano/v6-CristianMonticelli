from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from app.repositories import categoria_repository , product_repository

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint('main', __name__)

#3. Visualizzare la lista dei giochi
@bp.route('/')
def index():


    lista_categorie = categoria_repository.get_all_categories()
    
    return render_template('index.html', lista_categorie = lista_categorie)

@bp.route('/categoria/<id>')
def categoria_by_id(id):
    categoria = categoria_repository.get_category_by_id(id)
    prodotti = product_repository.get_prodotto_category_by_id(categoria['id'])

    return render_template('partite_gioco.html',categoria=categoria,prodotti=prodotti)

@bp.route("/crea_categoria", methods=("GET", "POST"))
def crea_categoria():
    if request.method == "POST":
        nome = request.form["nome"]
        
        if not nome:
            error = "Il nome è obbligatorio."
    
        if error is not None:
            flash(error)
        else:
            # Creiamo il canale
            categoria_repository.create_category(nome)
            return redirect(url_for("main.index"))
        
    return render_template('create_gioco.html')

@bp.route("/crea_prodotto", methods=("GET", "POST"))
def crea_prodotto():
    if request.method == "POST":
        categoria_nome = request.form["categoria_nome"]
        nome = request.form["nome"]
        prezzo = request.form["prezzo"]
        
        if not nome:
            error = "Il nome è obbligatorio."
    
        if error is not None:
            flash(error)
        else:
            categoria_id = categoria_repository.get_category_by_name(categoria_nome)
            product_repository.create_product(categoria_id["id"],nome,prezzo)
            return redirect(url_for("main.index"))
        
    return render_template('create_gioco.html')

  