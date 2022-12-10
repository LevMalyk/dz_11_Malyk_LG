import json

candidates_list = "candidates.json"


def load_candidates_from_json():
    """
    :return: Возвращает распаковынный список кандидатов из файлв json
    """
    with open("candidates.json", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates


def get_candidate(uid):
    """
    :param uid: Получает id кандидата
    :return: Возвращает кандидата по id
    """
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate
    return None


def get_name_list():
    """
    :return: Возвращает список с именамами всех кандидатов
    """
    candidates = load_candidates_from_json()
    result =[]
    for candidate in candidates:
        result.append(candidate["name"])
    return result


def get_candidates_by_name(candidate_name):
    """
    :param candidate_name: Имя конкретного кандидата
    :return: Возвращает данные на указанного кандитата
    """
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["name"] == candidate_name:
            return candidate
    return None


def get_candidates_list_by_name(name):
    """
    :return: Сравнивает и возвращает кандидата при совпадении букв имени
    """
    candidates = load_candidates_from_json()
    user_counter = 0
    result = []
    for candidate in candidates:
        if name.lower() in candidate["name"].lower():
            result.append(candidate["name"])
            user_counter += 1
    return user_counter, result


def get_candidates_by_skill(skill_name):
    """
    :return: Возвращает список кандидатов с задаными наваками
    """
    candidates = load_candidates_from_json()
    user_counter = 0
    result = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            result.append(candidate)
            user_counter += 1
    return user_counter, result
