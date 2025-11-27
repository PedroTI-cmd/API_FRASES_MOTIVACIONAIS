from flask import Flask, jsonify, request

app = Flask(__name__)

# Listas de frases
frases_namoro = [
    "Bom dia, meu amor.",
    "Acordei pensando em você."
]

frases_bom_dia = [
    "Bom dia! Que seu dia seja incrível.",
    "Tenha um ótimo dia!"
]

frases_divorcio = [
    "Cada fim é um novo começo.",
    "Aprendi, cresci e sigo em frente."
]

# Endpoint raiz apenas para teste
@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "API de frases funcionando!"
    })


# Endpoint de filtragem
@app.route("/frases", methods=["GET"])
def get_frases():
    categoria = request.args.get("categoria")

    if categoria == "namoro":
        frases = frases_namoro
    elif categoria == "bomdia":
        frases = frases_bom_dia
    elif categoria == "divorcio":
        frases = frases_divorcio
    else:
        frases = []

    return jsonify({
        "categoria": categoria,
        "total": len(frases),
        "frases": frases
    })


if __name__ == "__main__":
    app.run(debug=True)
