from model.project import Project


def test_add_project(app):
    project = Project(name='sdjfajf', description='asdhfgsfd')
    app.project.create_project(project)



