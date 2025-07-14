#ШАБЛОНЫ КОДА
#ФАЙЛ ДЛЯ ТОГО, ЧТОБЫ ХРАНИТЬ ОСНОВНЫЕ КОДОВЫЕ КОНСТРУКЦИИ И БЫСТРО КОПИРОВАТЬ И ВСТАВЛЯТЬ
python:
    """
    #Время суток - цвет спрайтов и текстбоксов
    $ persistent.sprite_time = 
    $ _time

    #Новелльный режим
    $ set_mode_rvp(nvl)
    window show
    nvl clear
     with dissolve
    window hide
    #Возврат в обычный режим
    $ set_mode_rvp()

    #Музыкальная пауза
    call pause_rvp("")#Задел для функции, пока не обращаем внимания на него
    $ renpy.notify(Щёлкните для продолжения)
    $ renpy.pause()

    #Карусель спрайтов - уже не используется, но оставил
    show :
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
     with dissolve
    window hide
    show :
        ease 1 pos(-0.3,0.5)

    #Фон двигается сверху вниз
    scene bg dom_rvp:
        pos (0,-360)
        linear 10.0 pos (0,0)
    with dissolve

    #Отрицательное мотание головой
    show bg :
        align(.5,.5) zoom 1.5
        ease .5 align(.1,.5) zoom 1.5
    show un serious sport:
        align(.5,.3) zoom 1.5
        ease .5 align(1.2,.3) zoom 1.5
    $renpy.pause(.5)
    show bg kitchen_rvp:
        align(.1,.5) zoom 1.5
        ease .5 align(.9,.5) zoom 1.5
    show un serious sport:
        align(1.2,.3) zoom 1.5
        ease .5 align(-.2,.3) zoom 1.5
    $renpy.pause(.5)

    #Весь вывод текста и полоски
    play music raindrops_sandr_rvp fadein 1
    #Вывод белой полоски
    show white:
        subpixel True
        align (.5,.5)
        easein_expo 1.5 crop (480,3,1440,3)
    #Вывод текста
    show textimg _rvp:
        subpixel True
        crop (0,0,1920,270)
        anchor (0.,1.)
        pos (0.,.5)
        pause 2.
        easein_expo 1.5 crop (0,0,1920,850)#чем больше последняя коорда, тем больше выдвигается
    show textimg _rvp as textimg2:
        subpixel True
        crop (0,810,1920,270)
        anchor (0.,0.)
        pos (0.,.5)
        pause 2.
        easein_expo 1.5 crop (0,270,1920,810)#чем меньше вторая коорда, тем больше выдвигается
    #Скрытие всего
    $ renpy.pause()
    stop music fadeout 2
    hide white
    hide textimg _rvp
    hide textimg _rvp as textimg2
    $ renpy.pause(2.0)

    #Уход персонажа с плавным исчезновением
    show  with dspr:
        align(.,.)
        ease 1 pos(.,.5) alpha 0

    #Появление персонажа плавно крупным планом
    show un_rvp smile pioneer2:
        anchor(.5,.5) pos(.1,.5) zoom 1.25 alpha 0
        ease 1.5 xpos(.25) alpha 1

    #Шаблон новой главы
    label :
    stop music fadeout 2
    $ renpy.show(black)
    $ renpy.with_statement(fade3)
    $ renpy.pause(2.0, hard=True)
    $ new_chapter(0, u'Рай в панельке: Часть .')
    $ persistent.sprite_time = 
    $ _time

    #Смена фона
    scene bg  with dissolve

    #Смена цг
    show cg  with dissolve

    #Текст со своим шрифтом и цветом
    show text {font=[font_rvp]}{color=ffdd7d}{size=50}Не забудь поставить кавычки with dissolve

    #Вызов функции анимации текста
    call showtext_rvp(Верхний текст,Нижний текст)

    #Включить/выключить музыку
    play music  fadein 1
    #из оригинала
    play music music_list[''] fadein 1
    stop music fadeout 1

    #Наложить пикчу полупрозрачно
    show :
        alpha .7
    with dissolve
    hide 

    #Эмбиент
    play ambience  fadein 1
    stop ambience fadeout 1

    #Ходьба
    scene bg :
        align(.5,.5) zoom 1.05
        ease .5 offset(25,25)
        ease .5 offset(0,0)
        ease .5 offset(-25,25)
        ease .5 offset(0,0)
        repeat

    #Бег плюс зум
    scene bg int_bus_on_square_rvp:
        align(.5,.5) zoom 1.05
        parallel:
            ease 5 zoom 2
        parallel:
            ease .3 offset(25,25)
            ease .3 offset(0,0)
            ease .3 offset(-25,25)
            ease .3 offset(0,0)
            repeat

    #Моргание глазом
    window hide
    show blink
    scene bg black with dissolve
    $ renpy.pause(1.0)
    show unblink
    window show
    """