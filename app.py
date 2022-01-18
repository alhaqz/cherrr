from flask import Flask, render_template, request
import recommendation

app = Flask(__name__, template_folder='templates')
cheryls=recommendation.my_array

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('home.html', cheryls=cheryls)

    if request.method == 'POST':
        hotels = request.form['daftarhotel']
        res = recommendation.recommendations(hotels)
        names=[]
        for i in range(len(res)):
            names.append(res[i])
        return render_template('akhir.html', result=names, cheryls=cheryls)

    else:
        return render_template('home.html')
 

if __name__ == '__main__':
    app.run(debug=True)
