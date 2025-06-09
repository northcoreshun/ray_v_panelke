init python:
    # Уберите из списка ненужные названия экранов, если не хотите их заменять.
    RVP_SCREENS = [
        "say",
        "nvl",
        "text_history_screen",
        "game_menu_selector"
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
            text what id "what" font font_rvp outlines [(2, '#000', 0, 0)] color "#ffdd7d" pos(.1,.865) text_align(.5) xmaximum .8 size 35 line_spacing 1
            if who:
                text who id "who" font font_who_rvp outlines [(2, '#000', 0, 0)] pos(.1,.82) size 35 line_spacing 1

        elif persistent.font_size == "small":
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/backward_%s.png") pos(.02,.88) action ShowMenu("text_history")
            imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png") pos(.895,.86) action HideInterface()
            if not config.skipping:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/forward_%s.png") pos(.92,.88) action Skip()
            else:
                imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/fast_forward_%s.png") pos(.92,.88) action Skip()
            text what id "what" font font_rvp outlines [(2, '#000', 0, 0)] color "#ffdd7d" pos(.1,.865) text_align .55 xmaximum .8 size 28 line_spacing 2
            if who:
                text who id "who" font font_who_rvp outlines [(2, '#000', 0, 0)] pos(.1,.82) size 35 line_spacing 2

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
                        text who id who_id font font_rvp_who size 35
                    text what id what_id font font_rvp size 35
                elif persistent.font_size == "small":
                    if who is not None:
                        text who id who_id font font_rvp_who size 28
                    text what id what_id font font_rvp size 28
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

screen rvp_text_history_screen:

    predict False tag menu

    $ xmax = 1600
    $ xposition = 100

    $ history_text_size = 21
    $ history_name_size = 22

    if persistent.font_size == "large":
        $ history_text_size = 28
        $ history_name_size = 29

    elif persistent.font_size == "giant":
        $ history_text_size = 36
        $ history_name_size = 37

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    window background Frame("images/gui/choice/"+persistent.timeofday+"/choice_box.png") left_padding 75 right_padding 75 bottom_padding 120 top_padding 120:
        viewport id "text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0
            has vbox
            for h in _history_list:
                if h.who:
                    text h.who:
                        font font_who_rvp
                        ypos 0
                        xpos xposition
                        xalign 0.0
                        size history_name_size
                        if "color" in h.who_args:
                            color h.who_args["color"]
                textbutton h.what style "log_button" text_font font_rvp text_style "normal_day" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#40e138" xpos 100
        vbar value YScrollValue("text_history_screen") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb "images/gui/settings/vthumb.png" xoffset 1700

screen rvp_game_menu_selector:
    $ timeofday = persistent.timeofday
    modal True tag menu
    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    add get_image("gui/ingame_menu/"+timeofday+"/ingame_menu.png") xalign 0.5 yalign 0.5
    imagemap:
        if _preferences.language == "spanish":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_es_%s.png") xalign 0.5 yalign 0.5
        elif _preferences.language == "italian":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_it_%s.png") xalign 0.5 yalign 0.5
        elif _preferences.language == "english":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_en_%s.png") xalign 0.5 yalign 0.5
        elif _preferences.language == "chinese":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_ch_%s.png") xalign 0.5 yalign 0.5
        elif _preferences.language == "french":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_fr_%s.png") xalign 0.5 yalign 0.5
        elif _preferences.language == "portuguese":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_pg_%s.png") xalign 0.5 yalign 0.5
        else:
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_%s.png") xalign 0.5 yalign 0.5
        hotspot (0, 83, 660, 65) focus_mask None clicked MainMenu()
        hotspot (0, 148, 660, 65) focus_mask None clicked ShowMenu('save')
        hotspot (0, 213, 660, 65) focus_mask None clicked ShowMenu('load')
        hotspot (0, 278, 660, 65) focus_mask None clicked (ShowMenu('preferences'), Hide('game_menu_selector'))
        hotspot (0, 343, 660, 65) focus_mask None clicked ShowMenu('quit')