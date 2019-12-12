from gensim.summarization.summarizer import summarize
from flask import Flask, request, render_template
from wtforms import Form, FloatField, validators, TextAreaField

app = Flask(__name__)

class InputForm(Form):
    ratio = FloatField(
        label='Ratio (ie: 0.3)', default=0.3,
        validators=[validators.InputRequired()])
    text = TextAreaField(
        label='Text', default='',
        validators=[validators.InputRequired()], )

@app.route('/', methods=['GET', 'POST'])


def main():
    form = InputForm(request.form)
    if request.method == 'GET': 
        return render_template('summary_app_index.html', form=form)
    if request.method == 'POST' and form.validate():       
        ratio = form.ratio.data
        text = form.text.data
        print('predicting...')
        prediction = predict(text, ratio)
        print('prediction done')
        print(prediction)
        #return render_template('summary_app_output.html', form=form, prediction=prediction)
        return render_template('summary_app_index.html', form=form,prediction=prediction, text=text)

def predict(text, ratio):
    return summarize(text, ratio)

if __name__ == "__main__":
    app.run(debug=True)
