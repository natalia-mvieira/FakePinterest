from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto, FotoCompartilhada

with app.app_context():
    database.create_all()