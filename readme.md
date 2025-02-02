# Образовательный проект

## Описание
Это программное обеспечение было создано исключительно для образовательных целей. Оно предназначено для изучения и понимания принципов работы компьютерных систем и сетей. Использование этого ПО в других целях не рекомендуется и может нарушать законодательство.

## Предупреждение
Автор не несет ответственности за использование данного ПО в незаконных или несанкционированных целях. Пользователи обязаны соблюдать законодательство своих стран и правила использования программного обеспечения.

## Лицензия
Это программное обеспечение лицензировано под [Авторскую лицензию](LICENSE). Вы можете использовать, изменять и распространять его для некоммерческих целей с обязательным указанием авторства и сохранением условий лицензии.

## Установка и использование
Программное обеспечение написано на Python 3.11.3. Для корректной работы выполните следующие шаги:

1. **Установка необходимых библиотек:**
    - Убедитесь, что у вас установлен Python 3.11.3.
    - Создайте виртуальное окружение (рекомендуется, но не обязательно):
        ```bash
        python -m venv env
        source env/bin/activate  # для Linux/Mac
        .\env\Scripts\activate  # для Windows
        ```
    - Установите библиотеки, указанные в файле requirements.txt:
        ```bash
        pip install -r requirements.txt
        ```
2. **Размещение файлов:**
    - Поместите файл main.py в один каталог с папкой images, содержащей все необходимые изображения.
3. **Запуск приложения:**
    - Откройте десктопную версию Telegram и запустите окно blum.
    - Запустите скрипт main.py:
        ``` bash
        python main.py
        ```
    - Ожидайте вывода в консоль сообщения "Off", сигнализирующего о запущенном софте, но о выключенном переключателе.
4. **Использование переключателя:**

    - **Нажмите клавишу `"F9"` для активации переключателя (вывод в консоль "On" будет сигнализировать о включенном переключателе).**
    - Нажмите кнопку "Play" в окне blum и ожидайте результата. Программа автоматически будет собирать все звездочки и начинать новую игру.
    - Для временной остановки работы софта нажмите `"F9"`.
### Пример структуры каталогов:
```bash
/path/to/your/project
│
├── main.py
├── requirements.txt
└── /images
    ├── 20.png
    ├── 25.png
    └── ...
```
## Контакты
Если у вас есть вопросы или предложения, свяжитесь со мной по дискорду shrram.