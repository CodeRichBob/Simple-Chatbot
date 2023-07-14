from flask import Flask, render_template, request
import openai


app = Flask(__name__)
openai.api_key = "pk-anmKKyctTKKIbnqIpidxwiELFeDnHWiSSOUZBvqYyNqAHvuY"
openai.api_base = 'https://api.pawan.krd/v1'


@app.route('/',methods=['GET','POST'])
def index():
    result = None
    if request.method == 'POST':
        prompt = request.form['text']


        output = openai.Completion.create(
            prompt=prompt,
            model= "text-davinci-003",
            max_tokens= 256
        )

        result = output["choices"][0]["text"]

    return render_template('index.html', result=result)


if __name__== '__main__':
    app.run(debug = True)