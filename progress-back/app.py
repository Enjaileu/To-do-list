import json
from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema, ObjectType, String, Field, Int, List

from utils.json_management import read, write, is_correct_database
import config.database as database_conf

app = Flask(__name__)

# Chargement initial des données depuis le fichier JSON
if is_correct_database(database_conf.PATH):
    data = read("database.json", database_conf.STRUCTURE)
else:
    data = {'task_lists':''}
    write(database_conf.PATH, data)


class Task(ObjectType):
    id = Int()
    title = String()
    value = Int()

    def __str__(self):
        return f"Task GraphQL object;\n{', '.join(f'{field}={getattr(self, field)}' for field in ['id', 'title', 'value'])}"

class TaskList(ObjectType):
    id = Int()
    name = String()
    tasks = List(Task)

    def __str__(self):
        task_list_info = f"TaskList GraphQL object;\n{', '.join(f'{field}={getattr(self, field)}' for field in ['id', 'name'])}"
        tasks_info = '\nTasks:\n' + '\n'.join(str(task.id) for task in self.tasks)
        return task_list_info + tasks_info

class Query(ObjectType):
    task_lists = List(TaskList)

    def resolve_task_lists(self):
        # Renvoie toutes les listes de tâches
        return [TaskList(id=list_data['id'], name=list_data['name'], tasks=list_data['tasks']) for list_data in data['task_lists']]

class Mutation(ObjectType):
    add_task = Field(Task, task_list_id=Int(required=True), title=String(required=True), value=Int(required=True))
    remove_task = Field(Task, task_id=Int(required=True))

    def resolve_add_task(self, task_list_id, title, value):
        # Ajoute une tâche à la liste de tâches spécifiée
        task = Task(id=len(data['tasks']) + 1, title=title, value=value)
        for list_data in data['task_lists']:
            if list_data['id'] == task_list_id:
                list_data['tasks'].append({'id': task.id, 'title': task.title, 'value': task.value})
                break

        # Sauvegarde des données mises à jour dans le fichier JSON
        write(database_conf.PATH, data)
        
        return task

    def resolve_remove_task(self, task_id):
        # Supprime la tâche avec l'ID spécifié
        task = None
        for list_data in data['task_lists']:
            for task_data in list_data['tasks']:
                if task_data['id'] == task_id:
                    task = Task(id=task_data['id'], title=task_data['title'], value=task_data['value'])
                    list_data['tasks'].remove(task_data)
                    break
            if task:
                break

        # Sauvegarde des données mises à jour dans le fichier JSON
        write(database_conf.PATH, data)

        return task

schema = Schema(query=Query, mutation=Mutation)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
