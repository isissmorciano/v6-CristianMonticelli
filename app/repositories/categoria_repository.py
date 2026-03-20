from app.db import get_db

def get_all_categories():
    db = get_db()
    query = '''
            SELECT *
            FROM categorie 
            ORDER BY id'''
       
        
    categorie = db.execute(query).fetchall()
    return [dict(categoria) for categoria in categorie]

def create_category(nome) -> None:
    db = get_db()
    query = '''
            INSERT INTO categorie (nome)
            VALUES (?)'''
    cursor = db.execute(query, (nome,))
    db.commit()
    return cursor.lastrowid

def get_category_by_id(category_id):
    db = get_db()
    query = '''
            SELECT *
            FROM categorie 
            WHERE id=?'''
        
    prodotto = db.execute(query,(category_id,)).fetchone()
    if prodotto:
        return dict(prodotto)
    return None

def get_category_by_name(nome):
    db = get_db()
    query = '''
            SELECT *
            FROM categorie 
            WHERE nome=?'''
        
    prodotto = db.execute(query,(nome,)).fetchone()
    if prodotto:
        return dict(prodotto)
    return None

