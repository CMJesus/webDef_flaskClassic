from finanzas import app

# Aquí comenzamos a establecer las rutas:

@app.route("/")
def inicio():
    return "Flask en marcha"