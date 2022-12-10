from flask import Flask, render_template

from utils import get_name_list, get_candidates_by_name, get_candidates_list_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_main():
    """
    Главная страницйа со списком всех кандидатов
    """
    items = get_name_list()
    return render_template('list.html', items=items)


@app.route("/candidate/<name>")
def page_candidate(name):
    """
    Страница с информацией о кандидате
    """
    user_data = get_candidates_by_name(name)
    return render_template('single.html', user=user_data)


@app.route("/search/<name>")
def page_candidates_name(name):
    """
    Страница с результатами поиска кандидата по имени
    """
    user_counter, user_name = get_candidates_list_by_name(name)
    return render_template('search.html',counter=user_counter, users=user_name)


@app.route("/skill/<skill>")
def page_candidates_skills(skill):
    """
    Страница с результатами поиска кандидата по наваку
    """
    skill_counter, user_skill = get_candidates_by_skill(skill)
    return render_template('skill.html', counter=skill_counter, skills=user_skill)


app.run()
