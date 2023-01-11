from flask import Flask, render_template, request, flash
import math

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"


def fac(x):
    num = 1
    i = 1
    while i <= int(x):
        num *= i
        i += 1
    return num


def convertTo2dArray(arr):
    num = int(len(arr) ** 0.5)
    given_matrix = []
    for z in range(num):
        given_matrix.append([])
        for zz in range(num):
            given_matrix[-1].append(int(arr[num * z + zz]))
    return given_matrix


def det(mat):
    if len(mat) == 1:
        return mat[0][0]

    else:
        ans = 0

        for i in range(len(mat)):
            sub_mat = []
            for rows in range(len(mat) - 1):
                sub_mat.append([])

            for rows in range(len(mat) - 1):
                for j in range(len(mat)):
                    if i != j:
                        sub_mat[rows].append(mat[rows + 1][j])

            ans += ((-1) ** i) * mat[0][i] * det(sub_mat)

        return ans


@app.route("/")
def index():
    flash("Write expression:")
    return render_template("index.html")


@app.route("/result", methods=['POST', 'GET'])
def greeter():
    flash(det(convertTo2dArray(eval(request.form['name_input']))))
    return render_template("index.html")


app.run()
