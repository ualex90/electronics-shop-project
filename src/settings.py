from pathlib import Path

# Папки проекта
ROOT = Path(__file__).resolve().parent.parent
SRC = Path(ROOT, "src")

# Файлы данных
ITEMS = Path(SRC, "items.csv")
ENCODING = 'CP1251'
