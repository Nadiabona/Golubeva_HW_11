import json, pprint

from config import CANDIDATES_DATA_LOC


class CandidatesManager:
    def __init__(self, path):
        self.path = path
        self.data = None
        self.load()

    def __repr__(self):
        return f"CandidatesManager {self.path}"

    def load(self) -> list[dict]:
        """Возвращает список кандидатов из файла"""
        with open(self.path) as file:
            self.data = json.load(file)
        return self.data

    def get_all(self):
        """Получение всех кандидатов"""
        candidates = self.data
        return candidates

    def get_by_pk(self, pk):
        """Возвращает кандидата по id"""
        candidates = self.data
        for candidate in candidates:
            if candidate['id'] == pk:
                return candidate
        #если не находится кандидат, вернется None

    def get_by_name(self, name):
        """Возвращает кандидата по имени"""
        candidates = self.data
        name = name.lower()
        candidates_found = [candidate for candidate in candidates if name in candidate['name'].lower()]
        return candidates_found


    def get_by_skill(self, skill_name):
        candidates = self.data
        candidates_with_skills = []
        skill_name = skill_name.lower()
        for candidate in candidates:
            #"Делим строку на отдельные навыки во избежания ложных результатов"""
            candidate_skills = candidate['skills'].lower().split(', ')
            if skill_name in candidate_skills:
                candidates_with_skills.append(candidate)

        return candidates_with_skills

# manager = CandidatesManager(CANDIDATES_DATA_LOC)
#
# data1 = manager.get_all()
# # for person in data:
# #     print (person ['name'])
# pprint.pprint(data1)






