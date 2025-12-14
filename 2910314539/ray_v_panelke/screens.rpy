init python:
    # Уберите из списка ненужные названия экранов, если не хотите их заменять.
    RVP_SCREENS = [
        "say",
        "nvl",
        "text_history_screen",
        "game_menu_selector"
    ]
#    rvp_screens_on = False #Переменная отображает, включены ли экраны РвП
#    deact = False

    def rvp_screen_save():  # Функция сохранения экранов из оригинала.
        for name in RVP_SCREENS:
            renpy.display.screen.screens[
                ("rvp_old_" + name, None)
            ] = renpy.display.screen.screens[(name, None)]

    def rvp_screen_act():  # Функция замены экранов из оригинала на собственные.
        config.window_title = u"Рай в панельке"  # Здесь вводите название Вашего мода.
#        global rvp_screens_on
#        rvp_screens_on = True
        for (
            name
        ) in (
            RVP_SCREENS
        ):
            renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[
                ("rvp_" + name, None)
            ]

    def rvp_screens_deact():  # Функция обратной замены.
        # Пытаемся заменить экраны.
#        global rvp_screens_on
        try:
            config.window_title = u"Бесконечное лето"
#            rvp_screens_on = False
            for name in RVP_SCREENS:
                renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[
                    ("rvp_old_" + name, None)
                ]
        except:  # Если возникают ошибки, то мы выходим из игры, чтобы избежать Traceback
            renpy.quit()

    # Объединяем функцию сохранения экранов и замены в одну.
    def rvp_screens_save_act():
        rvp_screen_save()
        rvp_screen_act()

    # Функция для автоматического включения кастомного интерфейса при загрузке сохранения с названием Вашего мода
#    def rvp_activate_after_load():
#        global rvp_screens_on
#        global save_name
#        global deact
#        if "Рай в панельке" in save_name and not rvp_screens_on:
#            rvp_screens_save_act()
#        if "Рай в панельке" not in save_name and rvp_screens_on:
#            deact = True # Вот это не происходит, хотя должно
#            rvp_screens_deact()

    # Добавляем функцию в Callback
#    config.after_load_callbacks.append(rvp_activate_after_load)

screen rvp_say:
    window background None id "window":
        $ timeofday = persistent.timeofday
        padding(-1,-1) #хз почему но нужен этот отступ, ренпай багует 
        button:
            xsize .06875
            background "gui back_for_rvp"
            hover_background Fixed("gui left_bar_rvp", "lefttext")
            action ShowMenu("text_history")

        button:
            xoffset -1
            xalign 1.
            xsize .06875
            background "gui back_for_rvp"
            hover_background Fixed("gui right_bar_rvp", "righttext")
            action Skip()

        if persistent.font_size == "large":
            text what id "what" font font_rvp outlines [(3,'#000',0,0)] color "#ffdd7d" pos(.1,.865) text_align(.5) xmaximum .8 size 35 line_spacing 1
            if who:
                text who id "who" font font_who_rvp outlines [(2,'#000',0,0)] pos(.1,.82) size 35 line_spacing 1
#style почему-то не работает тут
        elif persistent.font_size == "small":
            text what id "what" font font_rvp outlines [(3,'#000',0,0)] color "#ffdd7d" pos(.1,.865) text_align .55 xmaximum .8 size 28 line_spacing 2
            if who:
                text who id "who" font font_who_rvp outlines [(2,'#000',0,0)] pos(.1,.82) size 35 line_spacing 2
        
        imagebutton auto get_image("gui/dialogue_box/"+timeofday+"/hide_%s.png") pos(.895,.82) action HideInterface()

screen rvp_nvl:
    $ timeofday = persistent.timeofday
    window background Frame(get_image("gui/choice/"+timeofday+"/choice_box.png"),50,50) xfill True yfill True yalign .5 left_padding .091 right_padding .091 bottom_padding .078 top_padding .078:
        has vbox
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if persistent.font_size == "large":
                    if who is not None:
                        text who id who_id font font_who_rvp size 35
                    text what id what_id font font_rvp size 35
                elif persistent.font_size == "small":
                    if who is not None:
                        text who id who_id font font_who_rvp size 28
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

    button:
        offset(-1,-1) #а тут ещё и padding не работает(( 
        xsize .06875
        background "gui back_for_rvp"
        hover_background Fixed("gui left_bar_rvp", "lefttext")
        action ShowMenu("text_history")

    button:
        offset(1,-1) #а тут ещё и padding не работает(( 
        xalign 1.
        xsize .06875
        background "gui back_for_rvp"
        hover_background Fixed("gui right_bar_rvp", "righttext")
        action Skip()

screen rvp_text_history_screen:

    predict False tag menu

    $ xmax = .833
    $ xposition = .052

    $ history_text_size = 21
    $ history_name_size = 22

    if persistent.font_size == "large":
        $ history_text_size = 28
        $ history_name_size = 29

    elif persistent.font_size == "giant":
        $ history_text_size = 36
        $ history_name_size = 37

    button style "blank_button" pos(0,0) xfill True yfill True action Return()

    window background Frame("images/gui/choice/"+persistent.timeofday+"/choice_box.png") left_padding .039 right_padding .039 bottom_padding .111 top_padding .111:
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
                        xalign .0
                        size history_name_size
                        if "color" in h.who_args:
                            color h.who_args["color"]
                textbutton h.what style "log_button" text_font font_rvp text_style "normal_day" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xmaximum xmax text_hover_color "#40e138" xpos .052
        vbar value YScrollValue("text_history_screen") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb "images/gui/settings/vthumb.png" xoffset .885

screen rvp_game_menu_selector:
    $ timeofday = persistent.timeofday
    modal True tag menu
    button style "blank_button" pos(0,0) xfill True yfill True action Return()

    add get_image("gui/ingame_menu/"+timeofday+"/ingame_menu.png") align(.5,.5)
    imagemap:
        if _preferences.language == "spanish":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_es_%s.png") align(.5,.5)
        elif _preferences.language == "italian":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_it_%s.png") align(.5,.5)
        elif _preferences.language == "english":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_en_%s.png") align(.5,.5)
        elif _preferences.language == "chinese":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_ch_%s.png") align(.5,.5)
        elif _preferences.language == "french":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_fr_%s.png") align(.5,.5)
        elif _preferences.language == "portuguese":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_pg_%s.png") align(.5,.5)
        else:
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_%s.png") align(.5,.5)
        hotspot (0, 83, 660, 65) focus_mask None clicked Show("rvp_main_menu_confirm", transition = dissolve)
        hotspot (0, 148, 660, 65) focus_mask None clicked ShowMenu('save')
        hotspot (0, 213, 660, 65) focus_mask None clicked ShowMenu('load')
        hotspot (0, 278, 660, 65) focus_mask None clicked (ShowMenu('preferences'), Hide('game_menu_selector'))
        hotspot (0, 343, 660, 65) focus_mask None clicked ShowMenu('quit')
#    text "Отключено" style "rvp"

screen rvp_main_menu_confirm:

    modal True

    add get_image("gui/o_rly/base.png")
    text u"Вы действительно хотите выйти в главное меню?\nНесохраненные данные будут потеряны." text_align .5 align(.5,.46) color "#64483c" font header_font size 30
    textbutton u'Да' text_size 60 style "log_button" text_style "settings_link" align(.3,.65) action [Function(rvp_screens_deact), MainMenu(confirm=False)]
    textbutton u'Нет' text_size 60 style "log_button" text_style "settings_link" align(.7,.65) action Return()