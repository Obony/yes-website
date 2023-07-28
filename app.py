from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Nairobi, Kenya',
    'salary': 'Kshs 56,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Nairobi, Kenya',
    'salary': 'Kshs 75,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Nairobi, Kenya',
    'salary': 'Kshs 85,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Nairobi, Kenya'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                           jobs=JOBS, 
                           company_name='Yes')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
