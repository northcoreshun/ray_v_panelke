init python:
    # Уберите из списка ненужные названия экранов, если не хотите их заменять.
    RVP_SCREENS = [
        "say",
        "nvl"
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


screen rvp_say:
    window background None id "window":
        $ timeofday = persistent.timeofday
        if persistent.font_size == "large":
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") pos(.02,.86) action ShowMenu("text_history")
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png") pos(.895,.82) action HideInterface()
            if not config.skipping:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") pos(.92,.86) action Skip()
            else:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") pos(.92,.86) action Skip()
            text what id "what" font "ray_v_panelke/images/gui/Inter-Hewn.otf" outlines [(2, '#000', 0, 0)] color "#ffdd7d" pos(.1,.865) text_align(.5) xmaximum .8 size 35 line_spacing 1
            if who:
                text who id "who" font "ray_v_panelke/images/gui/trafaret.ttf" outlines [(2, '#000', 0, 0)] pos(.1,.82) size 35 line_spacing 1

        elif persistent.font_size == "small":
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") pos(.02,.88) action ShowMenu("text_history")
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png") pos(.895,.86) action HideInterface()
            if not config.skipping:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") pos(.92,.88) action Skip()
            else:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") pos(.92,.88) action Skip()
            text what id "what" font "ray_v_panelke/images/gui/Inter-Hewn.otf" outlines [(2, '#000', 0, 0)] color "#ffdd7d" pos(.1,.865) text_align .55 xmaximum .8 size 28 line_spacing 2
            if who:
                text who id "who" font "ray_v_panelke/images/gui/trafaret.ttf" outlines [(2, '#000', 0, 0)] pos(.1,.82) size 35 line_spacing 2

screen rvp_nvl:
    $ timeofday = persistent.timeofday
    window background Frame(get_image("gui/choice/"+timeofday+"/choice_box.png"),50,50) xfill True yfill True yalign 0.5 left_padding 175 right_padding 175 bottom_padding 150 top_padding 150:
        has vbox
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if persistent.font_size == "large":
                    if who is not None:
                        text who id who_id font "ray_v_panelke/images/gui/trafaret.ttf" size 35
                    text what id what_id font "ray_v_panelke/images/gui/Inter-Hewn.otf" size 35
                elif persistent.font_size == "small":
                    if who is not None:
                        text who id who_id font "ray_v_panelke/images/gui/trafaret.ttf" size 28
                    text what id what_id font "ray_v_panelke/images/gui/Inter-Hewn.otf" size 28
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"

    imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") xpos 38 ypos 924 action ShowMenu("text_history")

    if not config.skipping:
        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") xpos 1768 ypos 949 action Skip()
    else:
        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") xpos 1768 ypos 949 action Skip()