#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pytest selenium
echo "Виртуальное окружение создано, pip, pytest, selenium установлены."
