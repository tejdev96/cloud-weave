from flask import Flask, render_template, request, jsonify
from my_flask_app.services.gcloud_services import create_dataproc_cluster

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-dataproc-cluster', methods=['POST'])
def create_dataproc_cluster_route():
    cluster_name = request.form.get('cluster_name')
    result_cluster_name = create_dataproc_cluster(cluster_name)
    return jsonify({'status': 'Dataproc cluster creation triggered', 'cluster_name': result_cluster_name})

if __name__ == '__main__':
    app.run(debug=True)
