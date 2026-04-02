from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

@app.route("/len/<pass_len>")
def generate_pass(pass_len):
    if not pass_len.isdigit():
        return jsonify({"error": "la longitud tiene que ser un numero"}), 400

    pass_len = int(pass_len)

    if pass_len <= 0:
        return jsonify({"error": "la longitud tiene que ser mayor a 0"}), 400

    letras = string.ascii_letters
    numeros = string.digits
    speciales = string.punctuation
    
    caracteres = letras + numeros + speciales
    pwd = ""
    
    for _ in range(pass_len):
        pwd += random.choice(caracteres)
         
    return jsonify({"password": pwd})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
