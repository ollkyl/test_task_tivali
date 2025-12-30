# API tests for JSONPlaceholder (/posts)

Набор простых API-тестов для эндпоинта `/posts` публичного сервиса JSONPlaceholder.
Тесты написаны на Python с использованием pytest и requests.

## Установка зависимостей

```bas
requests==2.32.3
pytest==8.3.3

```

## Запуск тестов

```bash
python -m pytest tests -v
```

## Структура проекта

- `tests/` — API тесты  
  - `test_posts.py` — тесты для `/posts`
  - `conftest.py` — общие фикстуры (`session`, `base_url`)
- `requirements.txt` — зависимости проекта
- `.gitignore` — файлы, исключённые из репозитория

## Пример вывода

```text
================= test session starts =================
platform win32 -- Python 3.11.9, pytest-8.3.3, pluggy-1.6.0 -- C:\Users\Olga\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Olga\Documents\work\test_task_3       
plugins: anyio-4.12.0
collected 9 items                                      

tests/test_posts.py::TestPosts::test_get_posts PASSED [ 11%]
tests/test_posts.py::TestPosts::test_get_post_by_id[1]PPASSED [ 22%]
tests/test_posts.py::TestPosts::test_get_post_by_id[50] PASSED [ 33%]
tests/test_posts.py::TestPosts::test_get_post_by_id[100]
 PASSED [ 44%]
tests/test_posts.py::TestPosts::test_create_post PASSED [ 55%]
tests/test_posts.py::TestPosts::test_update_post[1-updated title] PASSED [ 66%]
tests/test_posts.py::TestPosts::test_update_post[2-another title] PASSED [ 77%]
tests/test_posts.py::TestPosts::test_delete_post PASSED [ 88%]
tests/test_posts.py::TestPosts::test_get_invalid_post PASSED [100%]

================== 9 passed in 1.30s ==================
```
