from model.project import Project
from random import randrange

def test_remove_project(app):
    if app.project.count() == 0:
        app.project.create_project(Project(name="New one"))
    old_projects = app.project.get_project_list()
    number = randrange(len(old_projects))
    app.project.delete_project_by_index(number)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
