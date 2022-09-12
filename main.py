from flask import Flask, render_template
from config import CANDIDATES_DATA_LOC

from candidates_manager import CandidatesManager

app = Flask(__name__)

manager = CandidatesManager(CANDIDATES_DATA_LOC)

@app.route('/')

def page_index():
    candidates = manager.get_all()
    return render_template('list.html', candidates = candidates)


@app.route('/candidate/<int:person_id>')
def page_candidate_person(person_id):
    candidate = manager.get_by_pk(person_id)
    if candidate is None:
        render_template("404.html")

    return render_template('card.html', candidate = candidate)

@app.route('/search/<candidate_name>')
def page_search_for_candidate(candidate_name):
    candidates = manager.get_by_name(candidate_name)
    candidates_len = len(candidates)

@app.route('/skill/<skill_name>')
def page_search_by_skill(skill_name):
    candidates = manager.get_by_skill(skill_name)
    candidates_len = len(candidates)

    if candidates is None:
        render_template("404.html")

    return render_template('list_by_skill.html', candidates=candidates, candidates_len = candidates_len, skill_name = skill_name)



app.run(debug = True)