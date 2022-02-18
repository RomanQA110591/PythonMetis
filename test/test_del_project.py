from model.project import Project
import random


def test_del_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="test"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.del_project(project.name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
