# File: src/config/paths.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_TEMPLATE_DIR = os.path.join(BASE_DIR, "project_template")
PROJECTS_DIR = os.path.join(BASE_DIR, "projects")
