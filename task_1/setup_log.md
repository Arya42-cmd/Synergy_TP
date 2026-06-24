# Setup Log

```bash
mkdir Synergy_TP
cd Synergy_TP

mkdir task_1
mkdir task_1\src
mkdir task_1\data

python -m venv venv

pip install requests

pip freeze > task_1\requirements.txt

python task_1\src\hello.py
```