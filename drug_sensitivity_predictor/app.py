from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        gene_data = request.files.get('gene_data')
        biomarker_data = request.files.get('biomarker_data')
        drug_type = request.form.get('drug_type')
        cancer_type = request.form.get('cancer_type')

        predicted_ic50 = predict_ic50(gene_data, biomarker_data, drug_type, cancer_type)

        return redirect(url_for('result', ic50=predicted_ic50))

    return render_template('input.html')

def predict_ic50(gene_data, biomarker_data, drug_type, cancer_type):
    return 1.23  # Placeholder for model prediction logic

@app.route('/result')
def result():
    predicted_ic50 = request.args.get('ic50')
    return render_template('result.html', ic50=predicted_ic50)

@app.route('/download')
def download_csv():
    data = {'IC50': [request.args.get('ic50')]}
    df = pd.DataFrame(data)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    return send_file(io.BytesIO(csv_buffer.getvalue().encode()), mimetype='text/csv', as_attachment=True, download_name='ic50_prediction.csv')

if __name__ == '__main__':
    app.run(debug=True)
