init python:
    # Уберите из списка ненужные названия экранов, если не хотите их заменять.
    RVP_SCREENS = [
        "say"
#        "nvl",
#        "text_history_screen",
#        "game_menu_selector"
    ]

    def rvp_screen_save():  # Функция сохранения экранов из оригинала.
        for name in RVP_SCREENS:
            renpy.display.screen.screens[
                ("rvp_old_" + name, None)
            ] = renpy.display.screen.screens[(name, None)]

    def rvp_screen_act():  # Функция замены экранов из оригинала на собственные.
        config.window_title = u"Рай в панельке"  # Здесь вводите название Вашего мода.
        for (
            name
        ) in (
            RVP_SCREENS
        ):
            renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[
                ("rvp_" + name, None)
            ]

    def rvp_screens_diact():  # Функция обратной замены.
        # Пытаемся заменить экраны.
        try:
            config.window_title = u"Бесконечное лето"
            for name in RVP_SCREENS:
                renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[
                    ("rvp_old_" + name, None)
                ]
        except:  # Если возникают ошибки, то мы выходим из игры, чтобы избежать Traceback
            renpy.quit()
    # Функция для автоматического включения кастомного интерфейса при загрузке сохранения с названием Вашего мода
    def rvp_activate_after_load():
        global save_name
        if "Рай в панельке" in save_name:
            rvp_screen_save()
            rvp_screen_act()

    # Добавляем функцию в Callback
    config.after_load_callbacks.append(rvp_activate_after_load)

    # Объединяем функцию сохранения экранов и замены в одну.
    def rvp_screens_save_act():
        rvp_screen_save()
        rvp_screen_act()