from pathlib import Path

# Папки проекта
ROOT = Path(__file__).resolve().parent
SRC = Path(ROOT, "src")

# Файлы данных
ITEMS = Path(SRC, "items_bad.csv")
ENCODING = 'CP1251'
