# Учимся командной работе в GitHub.

## Задачи
0. Прочитать весь README.md (этот большой текст) до конца. 
1. Кто-то из группы форкает этот репозиторий и делится со всеми в группе.
2. Каждый участник берёт себе по задаче и создаёт отдельную ветку.
3. После решения задачи в своей ветке, участники делают Pull Request в главную ветку (main).
4. Участники проверяют реквесты друг друга, и, если всё хорошо, то подтверждают пулл реквест.
4.1. Если что-то не так, то оставляют комментарий и требуют доработки.

# Теория
## [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow), или как использовать GitHub в команде
Если просто всем скачать ветку main и пушить сразу в неё все изменения без каких либо проверок, то:
1) Код рано или поздно сломается из-за упущенной баги.
2) Кодобаза начнёт загрязняться, так как стиль добавляемого кода никем не проверяется.

Чтобы избежать этого, многие команды используют т.н. GitHub flow - особый процесс работы с GitHub репозиторием, который обеспечивает больше уровней проверки кода и позволяет поддерживать более высокое качество кодобазы.

### Процесс
1. При появлении желания внести в код какое-то изменение (например, исправление бага или новая фича), создаётся новая ветка (с наглядным названием, вроде `feature-add-new-userclass` или `fix-connetion-lag`), и человек начинает работать в ней. 
2. После внесения всех изменений, человек пушит свои изменение на GitHub (всё ещё в свою ветку), а затем создаёт Pull Request в основную ветку.
![](https://docs.github.com/assets/cb-87213/images/help/pull_requests/pull-request-review-edit-branch.png)
> Pull Request (пулл реквест) - запрос на внесение изменений из другой ветки. Чтобы внести изменения, один из разработчиков должен проверить код и подтвердить что всё хорошо. В ином случае, можно оставить комментарий с указаниями проблем прямо в коде.

3. Pull Request проверяется другими разработчиками, они оставляют замечания и просят исправить код.
4. Разработчки исправляет указанные замечания, коммитит и пушит в свою ветку. Коммит автоматически присоединяется к Pull Request.
5. После финальной проверки, Pull Request подтверждают и начинается процесс внесения изменений (merge).
6. Если новый и старый код расходятся в чём-то кроме внесённых разработчиком изменений, то нужно вручную выбрать правильную версию. Если такого нет - то всё произойдёт автоматически.
8. Остаётся только удалить ветку в которой происходила разработка.




## Поддержка кода
В командной разработке очень важно поддерживать читаемый и чистый код, чтобы любой мог быстро разобраться, что в нём происходит.

### Как этого добиться?
  - Хорошая структура кода, например [SOLID](https://ru.wikipedia.org/wiki/SOLID_(%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BD%D0%BE-%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)).
  - Хороший кодстайл ([PEP8](https://peps.python.org/pep-0008/), [Google Style Guide](https://google.github.io/styleguide/)).
  - Комментарии к коду
  - `requirements.txt` - файл с версиями библиотек, которые используются в коде.
  - Типизация
  
    ![](https://cdn-ak.f.st-hatena.com/images/fotolife/t/tereka/20160924/20160924004700.png)
    
### Как себе помочь?
  - Использовать виртуальное окружение (для воспроизводимости кода).
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```
  - Использовать [`pipreqs`](https://github.com/bndr/pipreqs) для наполнения `requirements.txt`. Альтернатива - [`poetry`](https://python-poetry.org/)
  - Генерировать шаблоны для комментариев с помощью IDE ([плагин для VS Code](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring))
  
    ![](https://github.com/NilsJPWerner/autoDocstring/raw/HEAD/images/demo.gif)
 
  - Использовать линтеры (программы, которые проходятся по всему коды и находят плохие и вредные практики). Например, [flake8](https://flake8.pycqa.org/en/latest/) + [плагины](https://github.com/DmytroLitvinov/awesome-flake8-extensions).
    ```bash
    pip install flake8
    flake8 ./mycode.py 
    ```
  - Использовать type checker (проверщик типов, помогает находить баги в коде) - [mypy](https://mypy.readthedocs.io/en/stable/getting_started.html).
    ```bash
    pip install mypy
    mypy ./mycode.py 
    ```
  - Использовать форматировщики кода ([black](https://black.readthedocs.io/en/latest/)). Как использовать - см. ниже. 
    ```bash
    pip install black
    black ./mycode.py 
    ```
  - [pre-commit](https://pre-commit.com/) хуки (позволяют при каждом коммите/пуше автоматически производить операции над кодом, например, применять к нему последовательно `black`, `flake8` и `mypy`). [Список хуков](https://pre-commit.com/hooks.html).
    ```bash
    pip install pre-commit
    pre-commit install
    pre-commit run --all-files
    ```
  - [GitHub Actions](https://github.com/features/actions) (позволяет автоматизировать любые действия при заливке кода на гитхаб (линтинг, форматтирование, тестирование, сборка, ...).
  - [GitHub Copilot](https://github.com/features/copilot) (пишет код за тебя по текстовому описанию) [**требует перепроверки!**].
 
 
 ## Гайды 
 ### Pre-commit
 Для включения pre-commit, нужно добавить в корневую папку файл `.pre-commit-config.yaml`. Он описывает, какие действия нужно производить над кодом при коммите. 
 Пример начинки файла:
 ```yaml
 repos:
    # форматирует код
-   repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
    - id: black
      args: ["-S"]
      types: [python]


    # удаляет лишние импорты
-   repo: https://github.com/PyCQA/autoflake
    rev: v2.0.0
    hooks:
    -   id: autoflake
        types: [python]
        
    # сортирует импорты
-   repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        args: ["--profile", "black"]
        types: [python]

    # дополнительные проверки и исправления
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
    - id: check-added-large-files
    - id: detect-private-key
    - id: double-quote-string-fixer
    - id: end-of-file-fixer

    # линтер
-   repo: https://gitlab.com/pycqa/flake8
    rev: 5.0.0
    hooks:
      - id: flake8
        additional_dependencies: ["flake8-bugbear==22.9.23","flake8-bandit==4.1.1"]
        types: [python]

    # проверяет ошибки типизации
-   repo: local
    hooks:
      - id: mypy
        name: mypy
        entry: mypy
        language: system
        types: [python]
 ```
 
 ### GitHub Actions
 Чтобы использовать GitHub Actions для дополнительной проверки кода, нужно создать в корне репозитория папки и файл `.github/workflows/<имя файла>.yaml`. Пример начинки такого файла (применяет к коду flake8 и mypy):
 ```yaml
 name: Проверка
on: [push]
jobs:
  linter:
    name: Линтер
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Установка Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Установка зависимостей
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install mypy==0.991 flake8==6.0.0
    - name: Flake8
      run: flake8 $(git ls-files '*.py')
    - name: MyPy
      run: mypy $(git ls-files '*.py')
 ```

