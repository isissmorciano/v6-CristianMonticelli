from app.db import get_db

def get_all_products():
    db = get_db()
    query = '''
            SELECT *
            FROM prodotti 
            ORDER BY id'''
       
        
    prodotti = db.execute(query).fetchall()
    return [dict(prodotto) for prodotto in prodotti]
from app.db import get_db

def get_all_products():
    db = get_db()
    query = '''
            SELECT *
            FROM prodotti 
            ORDER BY id'''
       
        
    prodotti = db.execute(query).fetchall()
    return [dict(prodotto) for prodotto in prodotti]

def create_product(category_id, nome, prezzo) -> None:
    db = get_db()
    query = '''
            INSERT INTO prodotti (category_id, nome, prezzo)
            VALUES (?,?,?)'''
    cursor = db.execute(query, (category_id, nome, prezzo,))
    db.commit()
    return cursor.lastrowid

def get_prodotto_category_by_id(category_id):
    db = get_db()
    query = '''
            SELECT *
            FROM prodotto 
            WHERE categoria_id=?'''
    print("--------------------------------------------------------")
    print(query)
    categorie = db.execute(query,(category_id,)).fetchall()

    return [dict(categoria) for categoria in categorie]


def get_product_by_id(product_id):
    db = get_db()
    query = '''
            SELECT *
            FROM prodotti 
            WHERE id=?'''
    print("--------------------------------------------------------")
    print(query)
        
    prodotto = db.execute(query,(product_id,)).fetchone()
    if prodotto:
        return dict(prodotto)
    return None

