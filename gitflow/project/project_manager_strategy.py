#!/usr/bin/env python
# encoding: utf-8

import os

from gitflow.project.angular_project import AngularProject
from gitflow.project.maven_project import MavenProject
from gitflow.project.python_project import PythonProject


class ProjectManagerStrategy:

    @staticmethod
    def get_instance(path):
        os.chdir(path)
        if os.path.exists('pom.xml'):
            return MavenProject(path)
        elif os.path.exists('package.json'):
            return AngularProject(path)
        elif os.path.exists('setup.py'):
            return PythonProject(path)
        else:
            raise NotImplementedError('Project not supported!')
