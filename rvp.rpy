#ГЛОБАЛЬНЫЕ ИЗМЕНЕНИЯ:
#РЕЖИССУРА АЛЮМИНИЯ
#ГЕНЕРАТОР СПРАЙТОВ, ТИТРОВ ИЗ БКРР
#CAMERA
#функция ВЕРНУТЬСЯ НАЗАД, анимация перемотки SaturationMatrix(0,0)
#Обновление 2.9:
#новое меню
#демоверсия части 2Б

#Обновление до 3.0:
#НОВАЯ ЧАСТЬ 2Б
#ЛИКВИДАЦИЯ ТЕКСТБОКСОВ
#добить фон вокзала внутри
#добавить th, где надо
#412-бг:сюда бы автобус с противоположного вида
#цг:вид из автобуса ночной
#426 и 1536-бг:сделать вечернюю площадь
#699-включить музон из лмр японский как в ЯОД
#1300-заменить на появление таблички с текстом капсом, без текстбоксов ниже
#1330-цг:Семен держит Алису за руку как Кетрин в лмр
#1405-бг:по хорошему тут надо отдельный фон, но пока его нет
#1511-звук: рвущегося пододеяльника
#1493-бг: комната сюда бгшку позже
#1757-бг: при перерисовке заменить номер на 1664 и добавить рога, а то непонятно, что это троллейбус
#1762-звук: здесь и много где добавить звук дверей, из оригинала не подходит
#1787-бг:убрать троллейбус, заменить на многоэтажки
#1886-бг:добавить вид от водительского сидения
#1894-звук:эмбиент работы в депо, что-то типа как в кружке, но более грубое.
#у спрайта хниды резкие края у рубашки
#1998-звук: удара по железной двери
#2027-цг: где Семён лежит как Гослинг/попугай Кеша
#2081-спрайт: на темном фоне un_coat плохо выглядит, белый контур слегка виден
#2112-бг:заменить двор на погружение под воду
#2327-цг: Лена и Михалыч разговаривают с лейтом, второй мент вяжет гниду и лежит Семён
#2640-звук: флешбека
#2860-показать кассету анимацией снизу вверх
#туда же-звук: вставки кассеты
#
init:
    $ config.developer = True
    $ mods["rvp"] = "Рай в панельке"
    $ chars_define_rvp()

    #Титры
    $ rvp_credits_ = "Спасибо за прочтение части \n\n\n\n Сценарий - northcoreshun\n\n"
    $ rvp_credits_b2 = "Спасибо за прочтение части 2Б!\n\n\n\n Сценарий - northcoreshun\n\n Код - northcoreshun\n\n Работа в Photoshop - By Jack\n\n ХУДОЖНИК ЦГ И СПРАЙТОВ - PETER KORS\n\n ОТБЛАГОДАРИТЕ ЕГО ДОНАТОМ ПОЖАЛУЙСТА, ССЫЛКА В ОПИСАНИИ\n\n Благодарности:\n\n Noldor - вычитка\n\n poi - автообъявление"
    $ rvp_credits_b1 = "Спасибо за прочтение части 1Б!\n\n\n\n Сценарий - northcoreshun\n\n Код - Flip Flaps, northcoreshun\n\n Помощь с фонами - Андрей Серебро\n\n Новые спрайты в фш - Андрей Фоксаров\n\n ХУДОЖНИК ЦГ И СПРАЙТОВ - PETER KORS\n\n ОТБЛАГОДАРИТЕ ЕГО ДОНАТОМ ПОЖАЛУЙСТА, ССЫЛКА В ОПИСАНИИ\n\n Редакторы - Денис Плеханов, Арсений Ожигин, Максим Болдин\n\n Благодарность:\n\n Лапенко и анониму за поддержку мода донатом.\n\n\n Были использованы материалы других модов.\n\n Авторам также выражаю благодарность."
    $ rvp_credits_a1 = "Спасибо за прочтение части 1А!\n\n\n\n Сценарий - northcoreshun\n\n Код и работа в Photoshop - northcoreshun\n\n Благодарность:\n\n Храм Богини Лены - за публикацию и за полезную критику по тексту.\n\n Андрей Бганко, Денис Плеханов, Ольга Левченко и другие бета-читатели - за помощь с текстом.\n\n Cyber Patsan - за помощь с кодом и передачу полезных навыков кодинга.\n\n\n Были использованы материалы других модов.\n\n Авторам также выражаю благодарность."

label rvp:
    scene bg black with dissolve
    play music plastinki_rvp fadein 1
    call screen menu_rvp

screen a_rvp:
    add "bg square_rvp":
        align(0.,0.)
        crop (0,0,960,1080)
    text "Сторона А" size 70 align(.17,.3) outlines [(2.,"#000",0,0)]
    add "white":
        align (.5,.5)
        crop (3,0,3,1080)
    add "un_rvp smile coat" align(.5,.5)
screen b_rvp:
    add "bg square_lmr_day_rvp":
        anchor(0.,0.) pos(.5,.0)
        crop (960,0,1920,1080)
    text "Сторона Б" size 70 align(.8,.3) outlines [(2.,"#000",0,0)]
    add "white":
        align (.5,.5)
        crop (3,0,3,1080)
    add "un_rvp smile pioneer2" align(.5,.5)

screen menu_rvp:
    tag menu
    modal False
    imagemap:
        ground Transform("bg universam_rvp", alpha=0.1)
        hotspot((0, 0, 960, 1080)):
            hovered [Show("a_rvp", transition=Dissolve(0.5))]
            unhovered [Hide("a_rvp", transition=Dissolve(1.0))]
            action [Hide("a_rvp", transition=Dissolve(0.5)),Jump("a1")]
        hotspot((960, 0, 1920, 1000)):
            hovered [Show("b_rvp", transition=Dissolve(0.5))]
            unhovered [Hide("b_rvp", transition=Dissolve(1.0))]
            action [Hide("b_rvp", transition=Dissolve(0.5)),Show("side_b_rvp")]
        hotspot((960, 1000, 1920, 1080)):
            action [Jump("backrooms")]

screen b1_rvp:
    add "cg un_dv_rvp":
        align(0.,0.)
        crop (480,0,960,1080)
    text "Часть 1" size 70 align(.2,.47) outlines [(2.,"#000",0,0)]
    add "white":
        align (.5,.5)
        crop (3,0,3,1080)
screen b2_rvp:
    add "cg un_roof_rvp":
        anchor(0.,0.) pos(.5,.0)
        crop (480,0,1440,1080)
    text "Часть 2 (DEMO)" size 70 align(.8,.45) outlines [(2.,"#000",0,0)]
    add "white":
        align (.5,.5)
        crop (3,0,3,1080)

screen side_b_rvp:
    tag menu
    modal False
    imagemap:
        ground Transform("bg ext_internat_rvp", alpha=0.1)
        hotspot((0, 0, 960, 1080)):
            hovered [Show("b1_rvp", transition=Dissolve(0.5))]
            unhovered [Hide("b1_rvp", transition=Dissolve(1.0))]
            action [Hide("b1_rvp", transition=Dissolve(0.5)),Jump("b1")]
        hotspot((960, 0, 1920, 1000)):
            hovered [Show("b2_rvp", transition=Dissolve(0.5))]
            unhovered [Hide("b2_rvp", transition=Dissolve(1.0))]
            action [Hide("b2_rvp", transition=Dissolve(0.5)),Jump("b2")]

label backrooms:
    stop music fadeout 2
    $ renpy.show("black")
    $ renpy.with_statement(fade3)
    $ renpy.pause(2.0, hard=True)

    $ ichoose_narr_center = Character (None, color="#FF4500", what_color="#FFB600", screen="ichoose_centerscrn")
    $ ichoose_un_center = Character (u'Лена', color="#b956ff", what_color="#FFB600", screen="ichoose_centerscrn")

    #Трансформы для техтбоксов
    transform ich_trans_hoverbox:
        alpha 0.
        on idle:
            ease .5 alpha 0.
        on hover:
            ease .25 alpha 1.
    transform ich_trans_ltArrow:
        alpha .25
        on idle:
            ease .5 alpha .25
        on hover:
            ease .25 alpha 1.
    transform ich_trans_rtArrow:
        rotate 180
        alpha .25
        on idle:
            ease .5 alpha .25
        on hover:
            ease .25 alpha 1.
    transform ichoose_who:
        alpha 0.
        easein_quad 0.25 alpha 1.
    transform ichoose_what:
        alpha 0.
        easein_quad 0.25 alpha 1.

    ichoose_narr_center "Текст"
    ichoose_un_center "Текст"

    play music nv_st_rvp
    show nvlogo2_rvp:
        align(.5,.5)
    show nvlogo_rvp behind nvlogo2:
        align(.5,.5)
        linear 6 rotate -900
    with dissolve
    $ renpy.pause(4.5)
    stop music fadeout 2
    scene bg black with dissolve
    jump rvp
    
#Функция вывода превьюшки
label showtext_rvp(image1,image2):
    play music raindrops_sandr_rvp fadein 1
    #Вывод белой полоски
    show white:
        subpixel True
        align (.5,.5)
        easein_expo 1.5 crop (480,3,1440,3)
    #Вывод текста
#    show text "{color=#FFFFFF}{size=+15}     Текст" as image1:
    show image1:
        subpixel True
        crop (0,0,1920,100)
        anchor (0.,1.)
        pos (0.,.5)
        pause 2.
        easein_expo 1.5 crop (0,0,1920,850)#чем больше последняя коорда, тем больше выдвигается
#    show text "{color=#FFFFFF}{size=+15}     Текст" as image2:
    show image2:
        subpixel True
        crop (0,810,1920,270)
        anchor (0.,0.)
        pos (0.,.5)
        pause 2.
        easein_expo 1.5 crop (0,270,1920,810)#чем меньше вторая коорда, тем больше выдвигается
    $ renpy.pause()
    stop music fadeout 2
    hide white
    hide image1
    hide image2
    $ renpy.pause(2.0)


#Новый текстбокс
screen ichoose_centerscrn:
    frame:
        align (.5,1.)
        background None
        imagebutton:
            idle "gui accessibility_vignette_rvp"
            align (.5,1.)
            yoffset 8
            at ich_trans_hoverbox
            action Return()
        imagebutton: 
            idle "gui arrow_single_rvp"
            at ich_trans_ltArrow
            anchor (.5,.5)
            pos (.075,.9)
            action ShowMenu("text_history")
        imagebutton: 
            if not config.skipping:
                idle "gui arrow_single_rvp" 
            else:
                idle "gui arrow_double_rvp"
            at ich_trans_rtArrow
            anchor (.5,.5)
            pos (.925,.9)
            action Skip()
    window id "window":
        background None
        align (.5,1.)
        ysize 200
        vbox:
            align (.5,.5)
            if who:
                text who:
                    id "who"
                    font "ray_v_panelke/images/gui/calibri.ttf"
                    text_align (.5)
                    xmaximum (1000)
                    xalign .5
                    size 32
                    line_leading 8
                    at ichoose_who
            text what:
                id "what"
                font "ray_v_panelke/images/gui/calibri.ttf"
                text_align (.5)
                xmaximum (1000)
                outlines [(2.,"#000",0,0)]
                xalign .5
                size 32
                line_leading 8
                at ichoose_what

#Плавный выход из мода
label exit:
    stop sound fadeout 2
    stop music fadeout 2
    stop ambience fadeout 2
    scene black with dissolve2
    return

label a1:
    stop music fadeout 2
    $ renpy.show("black")
    $ renpy.with_statement(fade3)
    $ renpy.pause(2.0, hard=True)
    $ new_chapter(0, u'Рай в панельке: Сторона А.')
    $ persistent.sprite_time = "day"
    $ day_time
    
    play music raindrops_sandr_rvp fadein 1
    #Вывод белой полоски
    show white:
        subpixel True
        align (.5,.5)
        easein_expo 1.5 crop (480,3,1440,3)
    #Вывод текста
    show textimg kanon1_rvp:
        subpixel True
        crop (0,0,1920,270)
        anchor (0.,1.)
        pos (0.,.5)
        pause 2.
        easein_expo 1.5 crop (0,0,1920,850)#чем больше последняя коорда, тем больше выдвигается
    show textimg epilogue_rvp as textimg2:
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
    hide textimg kanon1_rvp
    hide textimg epilogue_rvp as textimg2
    $ renpy.pause(2.0)

    play music lyudi_nadoeli_rvp fadein 1
    #Вывод белой полоски
    show white:
        subpixel True
        align (.5,.5)
        easein_expo 1.5 crop (480,3,1440,3)
    #Вывод текста
    show textimg up_a_rvp:
        subpixel True
        crop (0,0,1920,270)
        anchor (0.,1.)
        pos (0.,.5)
        pause 2.
        easein_expo 1.5 crop (0,0,1920,810)#чем больше последняя коорда, тем больше выдвигается
    show textimg dn_a_rvp as textimg2:
        subpixel True
        crop (0,810,1920,270)
        anchor (0.,0.)
        pos (0.,.5)
        pause 2.
        easein_expo 1.5 crop (0,270,1920,810)#чем меньше вторая коорда, тем больше выдвигается
    #Скрытие всего
    $ renpy.pause(5.0)
    hide white
    hide textimg up_a_rvp
    hide textimg dn_a_rvp as textimg2
    
    show prologue_dream
    with fade
    window show
    "Последнее время мне не снятся сны."
    "Ночи пролетают быстро, и не успеваешь отдохнуть перед новым днём. Днём, полным рутинной работы, скучной, серой действительности." with dissolve
    "Будильник поднимет меня своим звоном, и я ни свет ни заря отправлюсь на смену. Работа, конечно, не пыльная, но довольно монотонная." with dissolve
    window hide

    scene bg kvartira_rvp
    show unblink
    show black:
        alpha 0.8
    show prologue_dream
    with fade
    
    window show
    "К вечеру смена заканчивается, и я прихожу домой в одинокую квартиру." with dissolve
    "Она ещё не вернулась. То занятия до вечера, то тренировки." with dissolve
    "А потом она сидит на кухне и учит свой патан и гисту." with dissolve
    "Мне тоже надо. Я же не просто работник, а ещё и студент." with dissolve
    "{b}Какая же это всё соковыжималка!{/b}" with dissolve
    "Сначала работа, потом учёба. У неё очная учёба, где надо всё зубрить."  with dissolve
    "Живём в складчину с моей маленькой зарплаты и её стипендии. От получки до получки. Вроде хватает." with dissolve
    window hide

    scene bg universam_rvp:
        align(.0,.0)
        ease 1 zoom 1.05
    show un_rvp shy coat:
        anchor(.5,.5) pos(.1,.5) zoom 1.25 alpha 0
        ease 1.5 xpos(.25) alpha 1
    show prologue_dream
    with fade

    window show
    "Но копить не получается, даже порадовать себя вкусной едой выходит редко." with dissolve
    "Хотя Лена старается изо всех сил приготовить что-то приятное для нас обоих из тех продуктов, которые мы берём в универсаме “Нагорный”." with dissolve
    "Со всей этой учебной и рабочей деятельностью нет сил и времени друг для друга." with dissolve
    "Встаём мы в разное время, потом большую часть дня проводим в разных местах, вечером тоже много сидим, каждый в своём углу. Я в комнате, она на кухне." with dissolve
    "А ночью, обессиленные, ложимся спать." with dissolve
    window hide

    scene bg vasyunina_rvp
    show prologue_dream
    with fade
    window show
    "А выходные? Да всё этот чёртов график “два через два”." with dissolve
    "То у меня выходные, у неё учёба, то наоборот." with dissolve
    "Бывают дни, когда у нас обоих выходные, но все планы срываются – то мне позвонят идти на смену, то у неё какие-то дела." with dissolve
    "Но вот вроде сегодня, наконец, совпало и ничто не помешает провести эти два дня вместе. Надо только эту смену оттрубить." with dissolve
    window hide

    scene bg vasyunina_rvp with dissolve
    $ renpy.pause(2)    
    window show
    "С такими мыслями я подходил к троллейбусному депо. Моему месту работы." with dissolve
    window hide

    scene bg ext_trolley_rvp with dissolve
    window show
    "До рассвета ещё далеко, часы на вахте показывали пять утра. Смена начинается." with dissolve
    "Взяв листок, я иду к своему троллейбусу под номером 1480." with dissolve
    "Проверка узлов, запуск двигателя, прогрев кабины и салона."
    play sound_loop sfx_bus_interior_moving fadein 4
    "Зима не за горами, чувствуются холода, но снег ещё не выпал." with dissolve
    "Лена ещё спит, наверное." with dissolve
    "Интересно, в этот день удастся её подвезти до института?" with dissolve
    play sound sfx_intro_bus_engine_start
    "Пару раз я замечал её фиолетовые хвостики через лобовое стекло и аккуратно подъезжал к ней. " with dissolve
    "Она тоже меня видела и всегда заходила в переднюю дверь." with dissolve
    window hide

    scene bg int_trolley_rvp
    show un_rvp smile2 coat
    show prologue_dream
    with fade
    window show
    un "Доброе утро, Сёма!"
    show un_rvp smile2 coat:
        align(.5,.5)
        ease 1 pos(.8,.5) alpha 0
    with dissolve
    "Но поговорить в рейсе не удавалось, опасное это дело, могу отвлечься. А я, чай, не «Окой» управляю, да и не одного себя везу." with dissolve
    "Чёрт, местные словечки уже прилипают к моей речи. Как, например “чай”, который не в значении напитка, а как частица “всё-таки”." with dissolve
    "Ну, вот и выезжать пора. Покидаю ворота первого депо и выхожу на маршрут." with dissolve
    window hide
    scene bg ext_trolley_rvp with dissolve
    window show
    "Довольно интересно получилось, что я вожу троллейбус. После переезда в Горький стал искать работу." with dissolve
    "Чтобы не тратить время и деньги на дорогу, искал работу у дома. Да и Лена просила, чтобы работа была недалеко, ей так спокойнее было за меня." with dissolve
    "Всё, что я имел – корочка слесаря и три года работы на заводе. Рядом было троллейбусное депо на улице Ивлиева. Пришёл туда и спросил, не нужны ли слесари." with dissolve
    nd "Слесари нам не нужны. А вот водителей не хватает на семнадцатом маршруте. Если не работал, ничего страшного, у нас курсы есть, стипендию платим. Ну что, согласен?" with dissolve
    "Пришлось согласиться. Прошёл обучение, недавно корочку получил и полноценно стал работать." with dissolve
    "Водителям платили немного. Неудивительно, почему не хватало кадров. Лена получала столько же со стипендии, сколько я с зарплаты." with dissolve
    "Правда ради этого ей приходилось зубрить весь материал и сдавать экзамены без права на ошибку. Даже одна четвёрка могла уменьшить ей стипендию в два раза." with dissolve
    "А значит, уменьшала наш бюджет и приводила к нищете." with dissolve
    "Но Лена справлялась, по крайней мере, до переезда, сдавать сессию на отлично. Хотя ради этих несчастных оценок она каждый день сидела по несколько часов и учила." with dissolve
    window hide
    
    stop sound_loop fadeout 1
    scene bg kvartira_rvp
    show un shy sport
    show prologue_dream
    with fade

    window show
    "Лена однажды предложила бросить свои занятия спортом и тоже найти хоть какую-то подработку после учебы, но я наотрез отказался." with dissolve
    "По себе знаю, как сильно это временами может давить, ведь я сам совмещаю работу и учебу." with dissolve
    "А у Лены очная форма обучения и тренировки для неё хоть какая-то отдушина в отрыве от учебы и повседневной серости, и лишать её этого я себе не позволил бы." with dissolve
    "Хоть она под вечер и приходит уставшая, я вижу в её глазах, что ей нравятся эти занятия." with dissolve
    "Возможно, сказалось желание Слави приучить всех к спорту, и Лена подхватила этот настрой. Пусть она будет разносторонне развита, а я буду работать." with dissolve
    window hide
    
    play sound sfx_intro_bus_engine_start
    scene bg square_rvp with dissolve
    play sound_loop sfx_bus_interior_moving fadein 4
    
    window show
    me "«Бориса Корнилова»! Следующая остановка – «Адмирала Васюнина»!" with dissolve
    "Какая же она молодец. Не то, что я… кое-как на заочном учусь. Единственное оправдание – работа. Такие мы с ней разные. Лена посвящает себя учёбе и спорту." with dissolve
    stop sound fadeout 2
    "Может в принципе и одна жить, без меня. Закончит мед, будет хорошим врачом, им платят нормально." with dissolve
    "А я так и буду троллейбус водить. Союз интеллигенции и рабочего класса." with dissolve
    "Не всё, конечно, было так плохо. Лене в наследство досталась пусть и однокомнатная, но уютная, с хорошим убранством, квартира." with dissolve
    "Всё же это был и своеобразный укор мне – когда нам негде было жить, спасение пришло со стороны Лены." with dissolve
    "Я тогда не смог добыть нам нормальный кров, не считая комнаты в коммуналке, которую мы бы всё равно не потянули. Так что жильём я обеспечить нас обоих не смог." with dissolve
    "И зачем я ей?" with dissolve
    "В меде хоть и немного парней, но она может найти себе какого-нибудь богатого. И жить с ним не в однушке от покойной родственницы, а в многокомнатной квартире." with dissolve
    "Порой мне кажется, что наша встреча в Совёнке была роковой случайностью." with dissolve
    play sound sfx_intro_bus_engine_start
    "Ей не нужен неудачник типа меня, она достойна чего-то большего." with dissolve
    me "Остановка «Улица Адмирала Васюнина»! Следующая – «Надежды Сусловой»!" with dissolve
    "Так ведь мало того, что она меня не бросила, она ещё и поддерживает меня." with dissolve
    window hide
    
    stop sound fadeout 2
    stop sound_loop fadeout 1
    show bg kvartira_rvp
    show un smile2 sport
    show prologue_dream
    with fade

    window show
    un "Сёма, это не плохо, что ты водителем работаешь. И мне не стыдно за тебя. Ты же можешь расти в этом направлении." with dissolve
    me "Да куда там расти, можно баранку крутить десятками лет." with dissolve
    un "Так у тебя же руки золотые, на заводе тебя хвалили. Спроси, может, слесари нужны или ещё кто." with dissolve
    window hide

    scene bg square_rvp with dissolve
    play sound_loop sfx_bus_interior_moving fadein 4
    play sound sfx_intro_bus_engine_start
    
    window show
    "Правильно она, конечно, это всё говорит. Вот только, боюсь, не светит мне ни повышение, ни даже эта работа в будущем." with dissolve
    me "«Улица Надежды Сусловой»! Следующая – «Ванеева»!" with dissolve
    "До депо уже дошли слухи о сокращении бюджета на общественный транспорт." with dissolve
    stop sound fadeout 2
    "Причём не просто зарплаты подрежут, но ещё и подвижной состав спишут, а персонал уволят." with dissolve
    "Мужики на измене сидят, непонятно, кого в таком случае оставят, кого уволят." with dissolve
    "В любом случае, меня вряд ли оставят из-за малого опыта. Меня им не жалко уволить – молодой, найду себе работу." with dissolve
    "Не знаю, как я скажу Лене, что меня уволили. И как жить не знаю." with dissolve
    "Хотя почему же, пойду на шабашку какую-нибудь." with dissolve
    "И вот опять же, зачем Лене это всё?" with dissolve
    "Муж-неудачник, получающий копейки." with dissolve
    "Ах да, я же учусь. Только не уверен, что доучусь. В здешний политех принимать не хотели, думали, не потяну. А ведь ещё сессию сдавать скоро." with dissolve
    play sound sfx_intro_bus_engine_start
    "Горький – город крупный, институты тут посерьёзнее, чем там, откуда мы летом переехали." with dissolve
    me "«Улица Ванеева»! Следующая – «Бориса Панина»!" with dissolve
    "Раньше чуть голос не срывал, объявляя эти остановки. Сейчас научился уже говорить громко, да только толку в этом горлопанстве." with dissolve
    window hide
    
    stop sound_loop fadeout 1
    stop sound fadeout 2
    $ renpy.pause(3)

    window show
    "Сука, опять ус слетел с провода." with dissolve
    "Открываю дверь, подхожу к месту аварии." with dissolve
    "Ус конечно никак не хотел ловиться, но я настаивал на том, чтобы он вернулся к своей обязанности быть проводником тока." with dissolve
    "Работаем дальше." with dissolve
    "Захожу в кабину и веду дальше. Впереди долгий рабочий день." with dissolve
    window hide
    
    stop music fadeout 3
    $ renpy.pause(3)

    scene bg vasyunina_rvp with dissolve
    play sound_loop sfx_bus_interior_moving fadein 4
    play music trolleybus_rvp fadein 1   
    window show
    "К третьему часу дня смена закончилась." with dissolve
    "С чувством облегчения я катил на своём электротранспорте на восток, к депо." with dissolve
    "Смена выдалась трудной, усы слетали с проводов раза в два чаще обычного." with dissolve
    "Один раз чуть в аварию не попал, причём по своей вине, задумался о вечере. Но это всё позади, остались считанные метры и я свободен." with dissolve
    window hide
    scene bg ext_trolley_rvp with dissolve
    window show
    "Часы в салоне показывали три часа дня. Я завёл троллейбус в гараж, провёл все необходимые процедуры по выключению машины." with dissolve
    stop sound_loop fadeout 1
    play ambience ambience_cold_wind_loop
    "Затем сразу пошёл и сдал смену. Лена ещё нескоро вернётся." with dissolve
    "Ладно, можно пока посидеть в депо и пообщаться с кем-нибудь." with dissolve
    "Контингент в депо составлял довольно типичный пролетариат." with dissolve
    "Три года работы на заводе, конечно, научили тому, как быть своим в их окружении, но во мне оставался домосед-интеллигент, не дававший окончательно стать рабочим классом." with dissolve
    "С ними не поговоришь о высоком, как иногда можно было с собеседниками на имиджбордах, но у них можно было набраться житейского опыта." with dissolve
    "Да и, можно подумать, как будто на имиджбордах мы о высоком говорили." with dissolve
    "Вот ведь что вспомнил! Интернет, имиджборды… когда-то была жизнь в других условиях и другом времени." with dissolve
    "Впрочем, не особо по ней скучаю." with dissolve
    "Я сидел на стоянке и ждал других водил. С ними у меня были наилучшие отношения в депо." with dissolve
    "Со слесарями всё было непросто – о них ходила дурная слава, что они приблатнённые раздолбаи с руками явно не из плеч." with dissolve
    "Из-за них и приходилось мучиться, потому что делали кое-как. Вдобавок я им завидовал в душе, что они занимают должность, которую я хотел, когда устраивался в депо." with dissolve
    "Если бы мне дали написать список того, что погубит в ближайшее время Союз, наверное, первым на листе появилось бы слово из четырёх букв - блат." with dissolve
    play sound sfx_intro_bus_engine_start
    "Вдруг из-за поворота возникли ещё двое “рогатых”. Я узнал их. Это были два водителя, работавших на одном маршруте со мной." with dissolve
    stop sound fadeout 2
    "По сложившейся пролетарской традиции я их называл по отчеству Михалыч и Иваныч." with dissolve
    show mh4_rvp at left with dissolve
    show iv4_rvp at right with dissolve
    "Первый был работягой довольно приличного вида, второй немного вызывал у меня неприязнь запущенной внешностью, но по характеру был довольно безобидным." with dissolve
    "Через несколько минут мы уже разговаривали. После смены мы обсуждали, кто как отработал, не забывая при этом обругать слесарей." with dissolve
    me "Ну ладно, мужики, я пойду."
    mh4 "Погоди, Семён, к нам присоединиться не желаешь?"
    me "А куда вы собрались, к кому-то в общагу депошную? Ходили уже, неуютно там." with dissolve
    mh4 "Да не, зачем сразу в общагу то? В гараже посидим без лишних глаз. Слесаря как раз позвали, у них выходной завтра. Дёрнем немного." with dissolve
    me "Не знаю, мужики… я с женой уже договорился время провести, и так на выходных почти с ней не вижусь." with dissolve
    iv4 "Э… ну ты чё, под каблуком в натуре, я не пойму. Успеешь к жене, мы тебя там в кандалы не закуём." with dissolve
    "Второй водитель говорил уже немного заплетавшимся языком. На мгновение в голове возникла мысль ему зубы пересчитать, чтобы за языком следил. И когда он успел накатить?" with dissolve
    mh4 "Иваныч, не наезжай." with dissolve
    "Более трезвый водитель успокоил своего товарища." with dissolve
    mh4 "Сёмыч у нас порядочный семьянин, почти не пьет, вот и стесняется. Не хочет он собачиться на ночь глядя, и сковородкой по башке получать как ты." with dissolve
    iv4 "Да я…" with dissolve
    mh4 "Все, угомонись. Семён, мы набухиваться не будем, просто немного выпьем и посидим. Немного хоть посиди, а?" with dissolve
    me "Ну, пойдёмте тогда." with dissolve
    window hide
    show mh4_rvp at left:
        ease 1.5 pos(1.1,0.5)
    show iv4_rvp at right:
        ease 1.5 pos(1.3,0.5)
    stop music fadeout 4
    stop ambience fadeout 2

    play music tuman_rvp fadein 2
    scene bg int_garage_rvp with dissolve
    window show
    "Последний раз пил с Алисой в августе, поминали Витю." with dissolve
    play sound sfx_open_metal_hatch
    "В гараже реально тепло, уютно." with dissolve
    "Один из слесарей, который работал с восьмидесятого года и жил не в общаге, а в квартире, купил гараж и позвал на “новоселье”." with dissolve
    "Идти далеко не пришлось – много гаражей настроили в низине за депо." with dissolve
    "Часть города, называемая местными “нагорной”, делилась на низины, застроенными гаражами и высокими местами, на которых строились дома." with dissolve
    "Место, где мы жили с Леной, тоже называлось Нагорным микрорайоном…" with dissolve
    "Вечер как-то быстро пролетел. Хоть я и выпил не так много, пару рюмок, но этого было достаточно, чтобы развязать мой язык и высказать мужикам недовольство своей жизнью." with dissolve
    "В процессе этого я потерял счёт времени." with dissolve
    window hide
    $ renpy.pause(2)
    window show
    show mh4_rvp at left with dissolve
    me "Да я в Лениноморске на заводе уважаемым человеком был. До старшего смены с нуля за два года дорос! А здесь баранку кручу, блин…" with dissolve
    mh4 "Да, Семён, непростой ты судьбы человек." with dissolve
    window hide
    $ renpy.pause(1)
    window show
    "Всё проходило довольно мирно, мы втроём познакомились со слесарями. Не самые плохие люди оказались, но не всё было так просто…" with dissolve
    show iv4_rvp at right with dissolve
    show gn_rvp nasmeh with dissolve
    voicegn "Семён, а что мы тебя раньше не видели в нашем кругу?" with dissolve
    "Был у них в коллективе один мутный тип, даже имя его никак не мог запомнить. А вот он меня, похоже, знал хорошо." with dissolve
    iv4 "А он у нас порядочный семьянин." with dissolve
    "Вот придурок. Небось, у самого каждый день ссоры со своей женой, вот и завидует." with dissolve
    voicegn "Значит вот как, жёнушка есть. А я видел тебя с ней, красивая." with dissolve
    "Это ещё что за базар пошёл. Где он мог видеть нас?" with dissolve
    "Хотя чему удивляться, мы с Леной часто ходили гулять до того же универсама за продуктами." with dissolve
    voicegn "И кем она работает, продавщицей?" with dissolve
    me "Нет, в меде учится." with dissolve
    voicegn "Ты посмотри-ка, а водила наш с интеллигенцией водится." with dissolve
    voicegn "И зачем ты ей? Чё она нормального мужика найти не может?" with dissolve
    "У меня потемнело в глазах от злости." with dissolve
    mh4 "Э, слышь, криворучка, кончай трепаться. Ты бы лучше наши тралики так чинил, как до людей докапываешься." with dissolve
    me "Чё ты там про мою сказал?" with dissolve
    mh4 "Сёмыч, не слушай его, он дурной, от него жена ушла просто, вот он и бесится." with dissolve
    show gn_rvp zloy with dspr
    voicegn "Да пошла она! Все они бабы сволочи, твоя тоже, наверняка!" with dissolve
    voicegn "Думаешь, пока ты тут сидишь, она ждёт тебя? Ага, размечтался." with dissolve
    show gn_rvp smile with dspr
    voicegn "Небось уже к другому пошла развлекаться. Но лучше ко мне, я бы её без внимания не оставил." with dissolve
    "Я вскипал от ненависти к этому ублюдку. Нужно было проучить его." with dissolve
    me "Пойдём-ка, выйдем." with dissolve
    scene bg int_garage_rvp:
        align(0.9,0.5)
        ease 2 zoom 3
    show gn_rvp smile:
        align(0.5,0.5)
        ease 1.5 pos(1.3,0.5)
    window hide
    
    stop music fadeout 2
    $ persistent.sprite_time = "night"
    $ night_time
    scene bg ext_garage_rvp with dissolve
    show gn_rvp smile with dissolve
    play ambience ambience_cold_wind_loop
    play music music_list["pile"] fadein 2
    $ renpy.pause(2)
    
    window show
    "Я вышел из гаража, затем вышел он." with dissolve
    "Больше уже ничего говорить не хотелось. Хотелось лишь одним ударом заставить его сожалеть о сказанном." with dissolve
    window hide
    
    play sound sfx_armature_swish
    play sound sfx_grate_hand_fall
    
    show gn_rvp smile:
        align(0.5,0.5)
        ease 0.5 pos(-0.2,0.5)
    window show
    "Я замахнулся, но промазал, попав по железной двери гаража. Гулкий удар по гаражу." with dissolve
    "А он воспользовался этим, схватил меня за волосы и треснул головой об эту дверь." with dissolve
    scene bg ext_garage_rvp:
        align(0.3,0.5)
        ease 1 zoom 1.5
    play sound sfx_grate_hand_fall
    "Это был второй удар." with dissolve
    "Вот же гнида, взбесил и ударил исподтишка!" with dissolve
    show blink
    "Я закрыл глаза от боли." with dissolve
    "Положение моё казалось безвыходным, как вдруг рука отпустила меня." with dissolve
    "С той стороны я услышал звуки перепалки и драки. Мужики мне помочь решили, что ли?" with dissolve
    play sound sfx_bodyfall_1
    "Я уже был не боец и, пройдя пару шагов, упал считать звёзды, что называется." with dissolve
    scene anim stars_1
    show unblink
    stop music fadeout 2
    "Надо было через бедро бросить, ну что же я…" with dissolve
    "Краем глаза я увидел фигуры, похожие на милиционеров. Этого ещё не хватало." with dissolve
    "Как же голова болит..." with dissolve
    window hide

    play music music_list["meet_me_there"] fadein 2
    window show
    "Лёжа у гаража, я смотрел на небо." with dissolve
    "Было слышно возню и знакомые голоса, видимо наша доблестная милиция занималась этим хмырём. Так ему и надо." with dissolve
    scene anim stars_3 with dissolve
    "Хм, ноябрь, а звёзды видно." with dissolve
    "Помню, как с Леной смотрели на них в Совёнке. Это было всего-то три года назад." with dissolve
    "Помню, как в прошлой жизни читал в интернете про то, что любовь живёт три года. Видимо мы с Леной не исключение..." with dissolve
    show blink
    "Я закрыл глаза и начал вспоминать..." with dissolve
    window hide

    scene bg intro_xx
    show prologue_dream
    with fade
    
    window show
    "Как я уснул в автобусе в тот вечер..." with dissolve
    window hide

    scene bg ext_camp_entrance_day
    show prologue_dream
    with fade
    
    window show
    "...и проснулся в пионерлагере." with dissolve
    window hide

    scene cg epilogue_un
    show prologue_dream
    with fade
    
    window show
    "Как познакомился с ней и остался в её мире." with dissolve
    window hide

    scene bg black
    show prologue_dream
    with fade
    
    window show
    "Сначала я думал, что будет трудно строить новую жизнь. А оказалось, что это было ещё легко." with dissolve
    "Это были цветочки по сравнению с настоящей взрослой жизнью, с которой я, считай, не справился." with dissolve
    "Я не смог справиться, не смог дать ей то, что она заслуживает." with dissolve
    "Только бы она не видела меня сейчас." with dissolve
    "Не буду никуда вставать, буду лежать и замёрзну. Утром мужики найдут мой окоченевший труп. Сегодня как раз температура ночью ниже нуля..." with dissolve
    window hide
    
    $ renpy.pause(1)
    scene bg black with dissolve
    
    window show
    "Руки коснулось что-то тёплое. Другая рука." with dissolve
    "Взяв меня за запястье, она потянула вверх. На ощупь и по температуре очень знакомо." with dissolve
    "Слушаясь её, я медленно приподнялся и сел." with dissolve
    window hide
    $ renpy.pause(0.5)
    window show
    "И тут я понял." with dissolve
    window hide

    scene anim stars_1 with dissolve
    show un_rvp normal coat:
        align(.5,.5)#эта команда нужна, потому что спрайт почему-то слева 
        matrixcolor BrightnessMatrix(-1)
    with dissolve
    $ renpy.pause(2)
    window show
    "Нет, только не это." with dissolve
    "Господи, неужели она смотрит на меня сейчас в этот момент, когда я просто опустился на самое дно?" with dissolve
    "Я не хотел открывать глаза." with dissolve
    "Казалось, я увижу её и умру от стыда." with dissolve
    "До последнего я надеялся на то, что мои веки закрывают мои зрачки от кого-то другого." with dissolve
    voiceun "Ты глаза-то открой." with dissolve
    "Её голос." with dissolve
    scene bg black with dissolve
    "Всё, теперь никаких надежд. Я разлепил веки." with dissolve
    scene anim stars_1
    show un_rvp normal coat
    show unblink
    "И тут же устремился взглядом в пару зелёных глаз." with dissolve
    "В них было много злости, разбавленной сожалением." with dissolve
    "Было ощущение, что она видит эту картину уже далеко не в первый раз, хотя я впервые напился в гараже." with dissolve
    "Несколько секунд мы смотрели друг другу в глаза. Её молчание было оглушающим." with dissolve
    un "Идём домой." with dissolve
    window hide
    scene anim stars_3 with dissolve
    window show
    "В её голосе слышалась сдавленная боль и злость." with dissolve
    "Она сейчас хотела высказать всё, что у неё на душе, но сдерживала себя. Я без промедления встал и пошёл за ней." with dissolve
    window hide
    scene bg dvor_rvp with dissolve
    window show
    "За время лежания на холодной земле я успел протрезветь и мог идти, не теряя равновесия." with dissolve
    "Путь до дома пролегал по серым дворам между панельных домов. Ещё немного шатаясь, я следовал за ней." with dissolve
    "Мы шли молча." with dissolve
    "Что она думала?" with dissolve
    "Наверное, какой я конченый и опустившийся алкаш." with dissolve
    "Какая она дура, что тогда пошла за меня замуж." with dissolve
    "О том, что наше счастье закончилось, только начавшись." with dissolve
    "Всё ведь шло к этому ещё там." with dissolve
    "Перестали платить зарплату на заводе. Перебивались заработками, потом переехали сюда." with dissolve
    "И вот, не выдержав груза работы и учёбы, груза ответственности, я опустился на дно. Не думаю, что она меня расцелует за это." with dissolve
    "И так всю мою жизнь нужно какие-то препятствия преодолевать, не имея под собой опоры. Будто барахтанье в море во время шторма." with dissolve
    "Ты сражаешься изо всех сил со стихией, но всё захлёбываешься." with dissolve
    "В конце концов, без опоры под ногами ты теряешь последние силы и сдаёшься." with dissolve
    window hide

    stop music fadeout 2
    scene bg dom_rvp:
        align(.0,.0)
        linear 10.0 pos(0,-360)
    with dissolve

    window show
    "Вот и наш дом на улице Васюнина." with dissolve
    stop ambience fadeout 2
    "Лена сама открыла дверь в подъезд, затем в квартиру." with dissolve
    play sound sfx_open_door_1
    "Мы зашли внутрь, я закрыл дверь." with dissolve
    window hide

    $ persistent.sprite_time = "day"
    $ day_time
    play sound sfx_close_door_1
    play ambience ambience_medstation_inside_night
    scene bg prih_rvp with dissolve
    show un_rvp normal coat with dissolve
    $ renpy.pause(2)
    window show
    "Лена сделала пару шагов, но вдруг развернулась и посмотрела на меня." with dissolve
    "По лицу читалось, что она была как бурлящий вулкан, который вот-вот извергнется." with dissolve
    "Её молчание было громче всех криков." with dissolve
    un "Семён… что это было?" with dissolve
    "Устало сказала она. Ситуация её вымотала." with dissolve
    me "Не знаю." with dissolve
    un "Ладно… как сегодня поработал?" with dissolve
    me "Нормально, смену отработал." with dissolve
    un "Так, а дальше что было?" with dissolve
    me "Сидел, ждал в депо, когда ты придёшь." with dissolve
    un "Почему… ты не пошёл домой после смены… как обычно?" with dissolve
    "Её голос был убийственно холоден и спокоен." with dissolve
    "Однако как она ни старалась, он выдавал бурю эмоций в ней." with dissolve
    "Ещё немного и…" with dissolve
    me "Меня мужики позвали с ними посидеть в гараже немного." with dissolve
    play music music_list["awakening_power"]
    un "То есть ты хотел провести вечер с женой, но пока меня ждал, решил ещё и накатить с мужиками? И с теми успеть и со мной?" with dissolve
    "Лена начала понемногу повышать голос." with dissolve
    me "Ну… да." with dissolve
    show un_rvp angry coat with dissolve
    un "Объясни мне тогда почему я тут сидела как дура одна!" with dissolve
    "Лена разозлилась не на шутку. Мой план провалился, и она пострадала из-за этого." with dissolve
    un "Всегда приходил с работы раньше меня и именно когда мы хотели провести вечер вместе…" with dissolve
    "Чёрт, сколько же я там пробыл…" with dissolve
    un "Я уж думала, случилось ли чего на работе, в аварию попал или током ударило!" with dissolve
    un "Позвонила в депо, сказали, что ты нормально смену отработал без происшествий." with dissolve
    un "Позвонила в больницу. Мне сказали, не привозили им такого товарища. Я уже сижу и не знаю, что и думать!" with dissolve
    "Твою мать…" with dissolve
    un "А ты лежишь где-то за гаражами!" with dissolve
    un "Тебя какой-то хмырь побил, чуть в отделение не забрали!" with dissolve
    un "Тебе вечер не с женой, а в милиции хотелось провести?" with dissolve
    un "Ты мне скажи одно – почему сегодня-то? Что случилось?! У тебя умер кто-то?" with dissolve
    un "Нет же, кто у тебя мог умереть, у тебя никого кроме меня нет, мужиков ты своих пару месяцев знаешь." with dissolve
    "Вдруг я всполыхнул, будто эти слова были искрой, взорвавший порох внутри меня. Из глубин души пошло всё раздражение, вся боль, накопившаяся за месяцы." with dissolve
    me "Лен, я не знаю, почему я так поступил, наверное потому что устал от жизни этой нелепой, от работы, на которой копейки платят, от того что у нас сил нет, и мы не говорим друг с другом как тогда, заела нас эта жизнь!" with dissolve
    un "Тебя жизнь заела? Так почему ты всегда молчишь и ничего не говоришь?! Почему такие сюрпризы мне даришь?!" with dissolve
    me "Я молчал, потому что не хотел расстраивать тебя." with dissolve
    un "Зато сейчас прямо обрадовал. Очень умно – копить в себе, а потом пойти напиться и подраться." with dissolve
    me "…" with dissolve
    me "И ты, правда, меня ждала?" with dissolve
    un "Конечно! А потом пошла{w=0.3} искать тебя." with dissolve
    un "И еле успела, сидел бы сейчас в вытрезвителе со своим собутыльником!" with dissolve
    "Вдруг вспомнились его слова..." with dissolve
    window hide
    
    scene bg int_garage_rvp
    show gn_rvp nasmeh
    show prologue_dream
    with fade
    $ renpy.pause(2)
    
    window show
    voicegn "И зачем ты ей? Че она нормального мужика найти не может?" with dissolve
    window hide
    
    scene bg prih_rvp with dissolve
    show un_rvp normal coat with dissolve
    
    window show
    me "Ну и дура ты, Лена. Лучше бы к другому мужику пошла. Чем меня, дурака... Бросила бы меня, и я бы там замёрз и умер." with dissolve
    show un_rvp angry coat with dissolve
    un "Ты совсем идиот?! Что за бред ты несёшь…" with dissolve
    show un_rvp normal coat with dissolve
    un "...ох, ладно, иди спать уже." with dissolve    
    stop music fadeout 2
    window hide
    show un_rvp normal coat:
        anchor(0.5,0.5) pos (0.5,0.5)
        ease 1 pos(-0.2,0.5)
    window show
    "Лена, наконец, сдвинулась с места, разулась, сняла пальто и пошла по квартире." with dissolve
    "Несмотря на мой выплеск праведного гнева на нелёгкую жизнь, она одержала верх. Правда была на её стороне." with dissolve
    un "Да за что мне судьба такая, постоянно с алкашами жить! Чем я заслужила такое?!" with dissolve
    "Это было уже слышно в глубине квартиры. Я остался стоять у двери." with dissolve
    "О чём это она? Ах да, отец…" with dissolve
    "Чёрт, похоже, я ей напомнил главный кошмар её детства." with dissolve
    "Что будет дальше? Если она не дура, а она не дура, то развод." with dissolve
    "Затем выселение из квартиры, потому что квартира от её родственницы." with dissolve
    "Я, конечно, опустился, но не до такого уровня, чтобы делить не моё имущество. Соберу пожитки и пойду по миру." with dissolve
    "Теперь в общаге депошной жить… отвратительно." with dissolve
    "Ну, а зачем Лене такой неудачник? Она сама себя обеспечит без моей помощи. Найдёт себе достойного мужчину, при деньгах. Захочет, вообще работать не будет, сможет дома творчеством заниматься." with dissolve
    "Я задумался – а что делать дальше? Собирать вещи?" with dissolve
    "Она не говорила это делать. Да и куда идти, на ночь глядя." with dissolve
    "Пойти извиняться? Конечно, надо извиниться за всё это, но она сейчас явно не намерена разговаривать." with dissolve
    "Всё же попробую, не ложиться же просто спать." with dissolve
    "Я тоже разулся, снял пальто и пошёл на кухню." with dissolve
    window hide
    scene bg prih_rvp:
        align(0.1,0.5)
        ease 2 zoom 3
    scene bg kitchen_rvp with dissolve
    window show
    "Лена сидела за столом и пила чай." with dissolve
    "Вид у неё был подавленный и задумчивый." with dissolve
    show un normal sport with dissolve
    me "Лена… ну прости меня." with dissolve
    "Выглядело это жалко." with dissolve
    "Я вроде и правильно сделал, но как будто для приличия." with dissolve
    "Нужно было раскаяться по-настоящему. Не осознав причины своего проступка, я был недостоин прощения." with dissolve
    un "Завтра поговорим ещё. А сейчас иди спать." with dissolve
    show un serious sport with dissolve
    un "А хотя стой. Встань-ка у раковины." with dissolve
    scene bg kitchen_rvp:
        align(0.5,0.5)
        ease 2 zoom 1.5
    show un serious sport:
        align(0.5,0.3)
        ease 2 zoom 1.5
    "Лена потихоньку наклонила мою голову и нежно потрогала место удара." with dissolve
    un "Сразу говори, как себя чувствуешь? Не тошнит? Голова не кружится? Сильно болит?" with dissolve
    show bg kitchen_rvp:
        align(0.5,0.5) zoom 1.5
        ease 0.5 align(0.1,0.5) zoom 1.5
    show un serious sport:
        align(0.5,0.3) zoom 1.5
        ease 0.5 align(1.2,0.3) zoom 1.5
    $renpy.pause(0.5)
    show bg kitchen_rvp:
        align(0.1,0.5) zoom 1.5
        ease 0.5 align(0.9,0.5) zoom 1.5
    show un serious sport:
        align(1.2,0.3) zoom 1.5
        ease 0.5 align(-.2,0.3) zoom 1.5
    $renpy.pause(0.5)
    show bg kitchen_rvp:
        align(0.9,0.5) zoom 1.5
        ease 0.5 align(0.5,0.5) zoom 1.5
    show un serious sport:
        align(-.2,0.3) zoom 1.5
        ease 0.5 align(0.5,0.3) zoom 1.5
    $renpy.pause(0.5)
    "Я помотал головой, отрицая симптомы, хотя голова гудела знатно."
    "Лена пристально смотрела мне в глаза. Взгляд был всё ещё сердитый, но в глубине её изумрудных глаз виднелось беспокойство." with dissolve
    "Она достала из кухонного шкафчика бутылёк с зелёнкой, бинт и вату." with dissolve
    window hide
    
    play sound sfx_open_water_sink
    $ renpy.pause(1)
    play sound_loop sfx_water_sink_stream fadein 1
    
    window show
    "Поставила мою голову под кран и помыла под холодной водой." with dissolve
    stop sound_loop fadeout 1
    play sound sfx_close_water_sink
    "Выключив воду, взяла немного ваты, смочила зелёнкой и обработала ушибленное место. Затем обмотала голову бинтом." with dissolve
    show un serious sport:
        align (.5,.3) zoom 1.5
    un "Теперь иди. Повязку до утра не снимай." with dissolve
    scene bg kitchen_rvp:
        align(0.1,0.5) zoom 1.5
        ease 2 zoom 3
    $renpy.pause(.5)
    scene bg kvartira_rvp
    show black:
        alpha 0.8
    "Я поплёлся в комнату." with dissolve
    play sound sfx_bed_squeak1
    "Плюхнулся на диван “чебурашку”. И кто его так назвал…" with dissolve
    window hide
    
    play sound_loop sfx_head_heartbeat fadein 2
    $ renpy.pause(1)
    
    window show
    "..." with dissolve
    "Ну и денёк." with dissolve
    "Я бы мог ещё поразмышлять о том, как я плох и недостоин её." with dissolve
    "Но всё уже сказано самому себе." with dissolve
    show blink
    "Лучше просто провалюсь в сон и дождусь нового дня." with dissolve
    window hide

    stop sound_loop fadeout 2
    stop ambience fadeout 2
    $ renpy.pause(2)
    scene bg prih_rvp with dissolve
    play music music_list["drown"] fadein 2
    
    window show
    "Наконец-то я дома, мы с Сёмой проведём эти выходные вместе. Я ему приготовлю его любимый суп, он так рад будет. Наверное, тяжёлый день выдался." with dissolve
    window hide
    scene bg kitchen_rvp with dissolve
    window show
    "Фух, устала. Надо чайник поставить, чаю попью хоть." with dissolve
    "Куда он пропал, у него же смена должна была закончиться четыре часа назад." with dissolve
    "Может с ним что-то случилось на работе? Надо позвонить в депо." with dissolve
    window hide
    $ renpy.pause(1.0)
    window show
    "Хм, странно, в депо сказали, он сдал смену без происшествий." with dissolve
    window hide
    
    scene bg kvartira_rvp
    show black:
        alpha 0.8
    with dissolve
    
    window show
    un "Алло, привет, Алён. Персунов Семён, к вам такой не поступал?" with dissolve
    al "Нет, Лен, такого товарища не было. С мужем что случилось?" with dissolve
    un "Да сама не понимаю. Ладно, пока тогда." with dissolve
    $ renpy.pause(1.5)
    un "Надо пойти к нему в депо. Чай потом выпью." with dissolve
    window hide

    $ persistent.sprite_time = "night"
    $ night_time
    scene bg ivlieva_rvp:
    show black:
        alpha 0.8
    with dissolve
    play ambience ambience_cold_wind_loop
    window show
    un "Здравствуйте, а Персунов Семён сегодня на работе был?" with dissolve
    vh "Здрасти, ну конечно. Отработал как обычно. А вы кто?" with dissolve
    un "Меня Елена зовут, я жена его. Он пропал куда-то, домой не пришёл." with dissolve
    vh "Ой, Лена, он ведь с мужиками пошёл. Пить будут, не иначе." with dissolve
    un "А куда они пошли?" with dissolve
    vh "Известно куда, в гаражи рядом с депо. Там они всегда пьянствуют." with dissolve
    vh "И мой тоже там. Я уже милицию вызвала, пусть его в вытрезвитель отвезут. Сил моих нет больше." with dissolve
    un "Мой так никогда не делал!" with dissolve
    vh "Ну, раньше не делал, теперь начнёт." with dissolve
    un "Ладно, я пойду за ним, спасибо вам." with dissolve
    vh "Давайте, спасайте его. Один ведь непьющий на всё депо был." with dissolve
    un "Как же так, он же не киряет обычно. Я не хочу верить в то, что он там с ними." with dissolve
    window hide
    scene bg ext_garage_rvp with dissolve
    window show
    "О боже, его кто-то бьёт." with dissolve
    "Ой, милиция тут, вяжут этого урода." with dissolve
    "Один к Сёме идёт. Его же сейчас тоже повяжут, надо его скорее спасать!" with dissolve
    show mil_rvp at left with dissolve
    un "Товарищ лейтенант, не забирайте его, пожалуйста. Я жена его, он так никогда не гулял. Отдайте мне его, я его заберу домой." with dissolve
    mil "В отделении разберёмся, кто кому муж, кто кому жена. О, Михалыч, ты чего тут делаешь?" with dissolve
    show mh4_rvp at right with dissolve
    mh4 "Алёш, здравствуй. Она правду говорит, это не ваш клиент." with dissolve
    mh4 "Это я его позвал выпить, а оно вот как вышло." with dissolve
    mil2 "Лёха, чё ты с ним лясы точишь, лучше помоги мне повязать второго, он какой-то буйный!" with dissolve
    alex "Сейчас приду!" with dissolve
    alex "Ладно, я сейчас отойду, но чтобы когда я вернулся, вас здесь не было, понятно?!" with dissolve
    window hide
    show mil_rvp at left:
        ease 1 pos(-0.1,0.5)
    window show
    "Надо быстрее поднять Сёму и уходить, пока они заняты." with dissolve
    window hide

    stop music fadeout 2
    stop ambience fadeout 2
    scene bg black
    show prologue_dream
    with fade

    window show
    "Сегодня мы впервые спали раздельно, на расстоянии друг от друга." with dissolve
    "Обычно всегда в обнимку. После трудного дня давали друг другу отдых." with dissolve
    "К этому дню у меня уже сформировался режим сна. Ложусь в десять, встаю в четыре утра, выхожу на смену. Возвращаюсь к трём часам дня, досыпаю пару часов." with dissolve
    "К пяти часам вечера из института приходила Лена." with dissolve
    "Вроде привык, но сегодня мои биологические часы не стали работать." with dissolve
    "Видимо, после алкоголя и стресса организм решил взять тайм-аут на восстановление." with dissolve
    window hide

    scene bg black with dissolve
    scene bg kvartira_rvp
    show unblink
    play ambience ambience_medstation_inside_night
    
    window show
    scene bg kvartira_rvp with dissolve
    $ persistent.sprite_time = "day"
    $ day_time
    "Я встал с кровати в районе девяти." with dissolve
#анимация либо вообще фразу убрать
    "Голова гудела, но скорее от удара об дверь, чем от алкоголя…" with dissolve
    show bg kvartira_rvp with dissolve
    "Лена лежала, отвернувшись от меня. Её лицо я увидел, лишь обойдя кровать." with dissolve
    show int_house_of_un_night:
        alpha 0.7
    with dissolve
    "Помню, как в тот вечер в Совёнке, когда мы остались вдвоём в лагере, я смотрел на неё. Тогда мы помирились, и её личико выражало спокойствие, умиротворение, тихую радость." with dissolve
    scene bg kvartira_rvp:
        align(0.5,0.5) zoom 1.1
    with dissolve
    "Сейчас у неё на лице грусть, будто видит плохой сон." with dissolve
    "И что мне делать в выходной, когда поругался с единственным человеком, с которым хотел провести всё свободное время?" with dissolve
    "Просто собрать молча вещи и уйти навсегда из квартиры или из жизни?" with dissolve
    "Оставить записку с прощальным посланием типа: “Прости, но так будет лучше для всех нас. Я недостоин тебя…” и так далее?" with dissolve
    with hpunch
    "Семён, не твори ерунды." with dissolve
    "Ты был моложе, менее опытным, оказался один в незнакомом месте и времени и смог начать отношения с ней. Вы тогда поругались, а потом помирились." with dissolve
    "Внезапно появились силы не унижать себя, не жалеть себя, а решать проблему как задачу." with dissolve
    "Если вчера преобладали мысли Семёна до Совёнка, то сейчас, наконец, взяла верх новая личность, которая брала ответственность за свои действия." with dissolve
    "Да я в принципе и был таким все эти три года. И всё с Леной было хорошо – мы старались провести вместе каждую свободную минуту." with dissolve
    "Мы не сидели на месте – я её вытаскивал куда-то погулять, а она – меня." with dissolve
    "Но жизнь в этом большом сером городе ослабила нас, мы стали меньше общаться и больше занимать всё своё внимание работой и учёбой. Из-за этого и замкнулись в себе…" with dissolve
    "Однако Лена скоро проснётся." with dissolve
    "Молчание будет убивать наши нервы, мы будем чувствовать себя неловко. С чего начать разговор?" with dissolve
    "Не знаю. Пойду в депо и напрошусь на смену." with dissolve
    "За баранкой троллейбуса придёт и решение, и нужные слова. А вот насчёт того, что со мной происходит, тоже стоит подумать." with dissolve
    "С этими мыслями я оделся, обулся и пошлёпал в депо." with dissolve
    stop ambience fadeout 2
    window hide
    
    scene bg vasyunina_rvp with dissolve
    window show
    "Причём реально пошлёпал, было довольно прилично луж на улице." with dissolve
    scene bg ivlieva_rvp with dissolve
    play ambience ambience_cold_wind_loop
    window show
    nd "Да ты чего, Персунов, какие смены?" with dissolve
    me "Ну, выйти сегодня на рейс хочу. Сегодня же суббота, считай, что я решил устроить себе субботник." with dissolve
    nd "И на чём ты выходить собрался, ударник пятилетки?" with dissolve
    nd "Все, что на ходу, уже в рейсе, других не починили, слесари сам знаешь, как работают. Лучше бы они так пили, как работают, ну или наоборот." with dissolve
    "Слесари вообще были бичом депо. А я с ними пил вчера." with dissolve
    nd "А вообще, что за желание поработать? Ты вроде договаривался всё себе выходные устроить…" with dissolve
    "Секунду было молчание." with dissolve
    nd "Поругались что ли?" with dissolve
    me "Ага." with dissolve
    nd "Да не переживай, помиритесь. Иди домой, не ищи приключений себе." with dissolve
    play music kzd_rvp fadein 2
    "Тоже верные слова. Может не стоит убегать от проблемы в работу, всё равно она так не решится." with dissolve
    "Однако пойду, прогуляюсь. Сразу возвращаться домой как-то скучно. Да и пока я так и не придумал, как извиниться и поговорить с Леной." with dissolve
    "Я ещё ни разу не ходил пешком по моему маршруту. Но в какую сторону пойти? В центр идти долго и утомительно, поэтому пойду в Кузнечиху." with dissolve
    window hide
    scene bg kuzn_rvp with dissolve
    window show
    "Кузнечиха это другой микрорайон, где заканчивался мой маршрут." with dissolve
    "Он мало чем отличается от Нагорного, такие же панельки, разве что новее. В основном девятиэтажки." with dissolve
    window hide

    scene bg ivlieva_rvp with dissolve
    play sound sfx_intro_bus_engine_start

    window show
    "Я пошёл вниз по Ивлиева. Рядом проезжали “коллеги” на троллейбусах и автобусах, везли пассажиров на учёбу и работу." with dissolve
    "Было бы немного иронично, если бы я пошёл работать в автобусный парк. Ведь именно автобус стал проводником сначала в тот загадочный и немного странный пионерлагерь, а затем в райцентр." with dissolve
    "Когда-то меня отвезли, а теперь я вожу." with dissolve
    "Зато электротранспорт меньше загрязняет воздух! – усмехнулся я." with dissolve
    "Будто в этой стране и эпохе кому-то было дело до этого." with dissolve
    "Только если каким-нибудь мудрым партийцам, которые одной рукой составляли директивы о развитии электротранспорта, а другой подписывали приказ о строительстве новой ТЭС." with dissolve
    "Ведь если подумать, откуда берётся электричество для трамваев и троллейбусов?" with dissolve
    "В основном от электростанций, которые работают на энергии сжигания угля." with dissolve
    "Ещё неизвестно, кто больше коптит небо тогда – выхлопы машины или дым от ТЭС." with dissolve
    "Хотя человечество освоило безопасную атомную энергию, а если ещё освоит и термояд…" with dissolve
    "За размышлениями о судьбе энергетики, я прошёл мимо рынка, третьего микрорайона и дошёл до улицы Козицкого." with dissolve
    "Дальше овраг, через который можно перейти по пешеходному мосту. Я дошёл до него и снова погрузился в свои думы." with dissolve
    window hide
    stop music fadeout 2
    scene bg kuzn_most_rvp with dissolve
    window show
    play music music_list["faceless"] fadein 2
    "Так о чём я?" with dissolve
    "Так, стоп!" with dissolve
    "Я опять убегаю от проблемы! Мировая энергетика сама решит, в каком направлении ей развиваться и какие источники использовать!" with dissolve
    "А у меня есть более насущные проблемы, которые не требуют отлагательств." with dissolve
    "Например, вчера я обидел самого дорогого мне человека. Плюнул на своё обещание ей. Так и не извинился." with dissolve
    "И сейчас оставил в одиночестве. Я снова её бросил, как вчера." with dissolve
    "Она, наверное, уже проснулась и не знает, где я. Ей, наверное, страшно за меня." with dissolve
    "Я остановился на середине моста." with dissolve
    "Слева овраг, справа овраг. Впереди дома, позади тоже." with dissolve
    "Мой дом тоже там. Нет смысла куда-то ходить, надо прийти к Лене. Всё-таки я дурную вещь сделал, что ушёл. На обратном пути придумаю, что скажу." with dissolve
    "Обратно я уже шёл не прогулочным шагом, а довольно быстрым." with dissolve
    "Ох, зря я Лену оставил, она надумает себе чего-нибудь не то." with dissolve
    "Впрочем, вещи я не собирал, так что она поймёт, что я не ушёл насовсем." with dissolve
    "Сука, надо было записку оставить в духе: “Ушёл на работу, к вечеру вернусь”." with dissolve
    "Куда я мог пойти, по её мнению? В универсам, в депо, просто погулять." with dissolve
    "Вроде бы ничего такого, но я же не могу залезть ей в голову и понять, что она думает." with dissolve
    window hide
    
    stop music fadeout 2
    scene bg universam_rvp:
        align(.5,.5)
        ease 1 zoom 1.05
    with dissolve
    
    window show
    "Я проходил мимо универсама." with dissolve
    "Может купить ей чего-нибудь вкусного?" with dissolve
    "Полез в карман. Ну да, конечно, деньги-то я не взял. Да и не так у нас их много." with dissolve
    "Всё-таки Лена ранимая и может надумать плохого." with dissolve
    "Вдруг она сидит и рыдает сейчас, расстроившись от того, что я её оставил." with dissolve
    "Или не плачет, а уже с горя…" with dissolve
    stop ambience fadeout 2
    play music music_list["scarytale"] fadein 2
    with hpunch
    "Твою мать!" with dissolve
    "Нужно срочно бежать к ней." with dissolve
    "Чёрт с ними со словами, лишь бы увидеть её живой." with dissolve
    "Пусть она хоть скалкой мне последние мозги вышибет, я заслужил это." with dissolve
    "Я побежал во всю свою прыть к нашему дому." with dissolve
    window hide
    scene bg universam_rvp:
        align(.1,.5)
        ease 1 zoom 1.5
    scene bg dom_rvp with dissolve
    window show
    "Сердце бешено стучало в груди." with dissolve
    "Вот подъезд." with dissolve
    "Сука, почему мы высоко живём, ещё по лестнице бежать наверх!" with dissolve
    "Так, вот квартира." with dissolve
    play sound sfx_unlock_door_campus
    "Дрожащими руками достаю ключ и открываю." with dissolve
    scene bg prih_rvp
    with hpunch
    "Не разуваясь, пробегаю в комнату." with dissolve
    window hide
    
    stop music fadeout 2
    scene bg black with dissolve
    play sound_loop sfx_head_heartbeat fadein 2
    
    window show
    "Люстра." with dissolve
    "Держится на потолке, как обычно." with dissolve
    "На ней…" with dissolve
    window hide

    scene anim prolog_4 with dissolve
    $ renpy.pause(1)
    
    window show
    "...лампочки и хрусталь." with dissolve
    "Я опустил глаза вниз." with dissolve
    window hide

    scene bg kvartira_rvp with dissolve
    show un shy sport with dissolve
    play ambience ambience_medstation_inside_night
    $ renpy.pause(2)
    
    window show
    "Передо мной стояла удивлённая Лена." with dissolve
    me "Привет… Лена…" with dissolve
    "После такого спринта и резкой остановки у меня была сильная одышка." with dissolve
    "После каждого слова я ловил ртом воздух. Я согнулся, упёршись руками в колени, чтобы отдышаться." with dissolve
    "Лена стояла передо мной целая и невредимая." with dissolve
    stop sound_loop fadeout 3
    "Однако я сразу заметил красноту вокруг глаз. Ту самую, которая остаётся, когда человек плакал." with dissolve
    "Самого страшного не произошло, это главное. Дальше пусть хоть режет своим любимым ножом, который когда-то носила с собой." with dissolve
    "Сначала она немного не ожидала моего столь быстрого появления." with dissolve
    window hide
    show un angry2 sport with dspr
    window show
    "Но факт того, что я прошёл в комнату не разувшись не мог не вызвать у неё раздражения." with dissolve
    play music music_list["awakening_power"] fadein 2
    un "Так, а я не поняла, ты чего грязь с улицы в комнату несёшь? Я только пол помыла." with dissolve
    "Мда, вот уж надумал глупостей. Из-за этого только сильнее её обидел. Лена злилась всё больше." with dissolve
    show un angry sport with dspr
    un "Ты меня вообще ни во что не ставишь? Вчера ушёл бухать к своим дружкам, а про меня забыл!" with dissolve
    un "Ну, правда, нахрен эту Лену, мне же эти собутыльники важнее!" with dissolve
    "Лена уже совсем разозлилась." with dissolve
    un "Сегодня утром снова меня оставил, а сейчас так прибежал, что аж разуться забыл. Говори, где был?!" with dissolve
    "Надо что-то отвечать уже." with dissolve
    me "Я в депо пошёл…" with dissolve
    "Ох, зря это сказал. Лену с этого просто вынесло." with dissolve
    show un rage sport with dspr
    un "Куда?!!" with dissolve
    un "Опять к своим дружкам-алкашам! Тебе вчера не хватило, ты ещё хочешь?!" with dissolve
    
    hide un
    show un_rvp ubiu sport
    with dspr

    "Секундная пауза. Лена набрала воздуха в лёгкие для новой очереди слов." with dissolve
    
    hide un_rvp
    show un rage sport
    with dspr
    
    un "Опохмелиться надо, да?! А то непривычно, с утра голова болит от водки!" with dissolve
    "Твою мать, как же я вляпался. Если Лена вышла из себя, то это очень плохо." with dissolve
    un "О, я знаю! Пошёл жаловаться своим товарищам, как его жена молодая пилит." with dissolve
    un "Какая Лена сука. Лучше бы рот закрыла и молча полы мыла, еду готовила." with dissolve
    un "А нам всё по барабану. Хотим – уходим хрен знает куда и бухаем." with dissolve
    un "А потом лежим на холодной земле. Врачи же нас дурят, сказки про пневмонию рассказывают." with dissolve
    un "А я дура, сижу на парах, потом вечером это всё учу." with dissolve
    un "А муж у меня умный, смотри Лена, могу спокойно в ноябре ночью на улице спать." with dissolve
    "Бедная Лена…" with dissolve
    un "А если заболею и умру, ничего страшного. Мне на себя плевать и на других тоже. Жена будет убиваться – да плевать мне!" with dissolve
    "Наконец, Лена уже начала сбавлять громкость. Накопленный негатив нашёл выход, и она была уже больше опустошённая, чем злая." with dissolve
    "Сколько же она надумала." with dissolve
    "Что я хотел сбежать и пожаловаться на неё мужикам." with dissolve
    "Почему она так про меня думает? Я же так не делал. Как будто она на меня примеряла роль другого человека." with dissolve
    "Но это неправильно. Я не злился на неё, я хотел перед ней извиниться. Я хотел лишь отвлечься, чтобы найти правильное решение. А в итоге…" with dissolve
    me "Лена, я не хотел…" with dissolve
    un "Что ты не хотел? Провести дома вечер с женой спокойно? Быть нормальным человеком ты не хотел?" with dissolve
    "Не, ну это уже надо было останавливать." with dissolve
    me "Не хотел я ни с кем опохмеляться с утра. И жаловаться я тоже не хотел никому на тебя!" with dissolve
    show un angry2 sport with dspr
    "Я немного повысил голос. Это помогло успокоить Лену, главное не переборщить." with dissolve
    un "А зачем тогда в депо пошёл?" with dissolve
    me "Хотел взять смену." with dissolve
    un "Семён, ты серьёзно? Ты что у нас, герой соцтруда?" with dissolve
    "Лена замолчала на пару секунд." with dissolve
    un "Всё-таки сбежать хотел от меня." with dissolve
    "Чёрт, а она права. Иначе как бегством не назовёшь." with dissolve
    un "А что же так быстро прибежал, совесть замучила?" with dissolve
    me "Типа того… Я хотел подумать как извиниться, пошёл погулять до Кузнечихи." with dissolve
    me "На мосту понял, что не должен был тебя оставлять. И что надо вернуться скорее и поговорить." with dissolve
    "Всё-таки нужно было дать понять, что я волновался за неё, поэтому прибежал, позабыв про все приличия." with dissolve
    me "От универсама я бежал без остановки. Я испугался, что ты очень расстроишься и…" with dissolve
    un "И что?" with dissolve
    me "Ну, сделаешь с собой что-то плохое…" with dissolve
    "Внезапно Лену снова задели мои слова." with dissolve
    show un angry sport with dspr
    un "Да больно надо! Ещё из-за него я тут буду… нет, вы подумайте, какой он уникальный и важный!" with dissolve
    un "А ты не волнуйся, у нас незаменимых нет." with dissolve
    stop music fadeout 3
    window hide
    scene bg kvartira_rvp:
        parallel:
            zoom 1.0 anchor(0,0)
            ease 5 zoom 2 anchor (800,200)
    show un shy sport at left:
        parallel:
            zoom 1.0 anchor(0,0)
            ease 5 zoom 2 anchor (460,200)
    window show
    "В этот момент она остановилась. Я стоял в шоке от её последних слов." with dissolve
    "Лена поняла, что сказала достаточно или даже слишком много." with dissolve
    "Прежний напор ушёл, его место занимал дискомфорт. Как всегда в тех ситуациях, когда на эмоциях высказываешь человеку всё, что о нём думаешь." with dissolve
    "Но в определённый момент от праведного гнева перегибаешь палку и несправедливо задеваешь человека." with dissolve
    "И уже твоя совесть тебя мучает." with dissolve
    window hide
    scene bg kvartira_rvp:
        parallel:
            zoom 2 anchor (800,200)
            ease 2 zoom 1 anchor (0,0)
    show un normal sport at left:
        parallel:
            zoom 2 anchor (460,200)
            ease 2 zoom 1 anchor (0,0)
    show un normal sport
    window show
    un "Ладно, надоело мне это всё. Иди пол вымой. И дверь закрой нормально, не в лифте родился." with dissolve
    "Начали с грязного пола и закончили им же." with dissolve
    "Больше говорить было не о чем." with dissolve
    "Я развернулся и вышел из комнаты. Разулся, пошёл в ванную, взял швабру и ведро." with dissolve
    window hide

    scene bg black with dissolve
    play sound sfx_open_water_sink
    $ renpy.pause(1)
    play sound_loop sfx_water_sink_stream fadein 1
    
    window show
    "Я сам себе сжёг мосты к лучшему исходу." with dissolve
    "Если бы пошёл домой вчера, вообще этой ссоры бы не случилось." with dissolve
    "Если бы не ушёл утром, а дождался, пока Лена проснётся, сейчас не пришлось ссориться." with dissolve
    "Но уже нет смысла об этом сожалеть, надо обдумать наше с Леной положение." with dissolve
    window hide
    
    stop sound_loop fadeout 1
    play sound sfx_close_water_sink
    scene bg prih_rvp with dissolve
    
    window show
    "Вот уж что точно не надо делать, так это куда-то уходить без нужды и без предупреждения. Хватит с меня уходов." with dissolve
    "Если я хочу решить проблему, надо поговорить с Леной. Но как?" with dissolve
    "За три года отношений мы никогда так не ссорились. Я никогда не бросал Лену, а Лена никогда так на меня не срывалась." with dissolve
    "Лене тоже плохо и это видно. Она пыталась показать, что не переживала от того, что я ушёл, но краснота на лице её выдавала." with dissolve
    "Интересно ещё и то, что Лена верила мне. Она не кричала после моих слов что-то вроде:" with dissolve
    window hide
    
    scene bg kvartira_rvp
    show un angry2 sport
    show prologue_dream
    with fade

    window show
    un "А зачем тогда в депо пошёл?" with dissolve
    me "Хотел взять смену." with dissolve
    show un angry sport with dissolve
    un "Что ты мне врёшь-то? Наверняка хотел им на меня пожаловаться." with dissolve
    window hide
    scene bg prih_rvp with dissolve
    window show
    "Это хороший признак." with dissolve
    "Значит, Лена ещё может меня выслушать, поверить мне." with dissolve
    "И она ещё верит, что я не стал алкашом, который в грош не ставит свою жену ради бутылки." with dissolve
    "Так, а всё-таки, с чего начать разговор?" with dissolve
    "Снова пойти извиниться? Как-то мелко." with dissolve
    "В данной ситуации это скорее формальность." with dissolve
    "Нужно излить друг другу душу, объяснить, почему ты так себя повёл." with dissolve
    "Точнее, я должен объяснить, почему эта каша заварилась." with dissolve
    "Сегодняшний уход уже объяснил более-менее. Но он произошёл из-за вчерашней ситуации." with dissolve
    "Вот тут логика моих действий не так очевидна." with dissolve
    "Я закончил мыть пол." with dissolve
    play sound sfx_stomach_growl
    "Теперь нужно было пообедать, желудок урчал." with dissolve
    "Обычно мы с Леной обедали вместе. Сейчас это наше любимое действие может превратиться в пытку, причём для нас обоих." with dissolve
    "Внезапно, в прихожую зашла Лена." with dissolve
    window hide
    show un normal sport with dissolve
    window show
    un "Закончил? Иди пообедай, там суп есть." with dissolve
    me "А как же ты?" with dissolve
    un "Я уже поела." with dissolve
    window hide
    show un shy sport:
        align(.5,.5)
        ease 1 pos(0.,.5) alpha 0
    window show
    "И с этими словами она резко вышла." with dissolve
    "Даже лица её разглядеть не успел." with dissolve
    "По-моему, она покраснела. Только вот почему она не стала со мной обедать как обычно?" with dissolve
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 1
    "Я помыл руки и пошёл на кухню." with dissolve
    window hide
    
    stop sound_loop fadeout 1
    play sound sfx_close_water_sink
    scene bg kitchen_rvp with dissolve
    play music ya_tebya_lyublyu_rvp fadein 2
    
    window show
    "Я вспомнил, как до этой ссоры старался хотя бы по мелочи помогать на кухне." with dissolve
    "Мастером кулинарии я не был, но порезать продукты и проследить, чтобы не выкипела вода, я все же могу." with dissolve
    "На кухне всё как обычно – холодильник, стол, стулья." with dissolve
    "Плита, на плите кастрюля, в кастрюле супчик." with dissolve
    "Ничего себе… моя любимая солянка. Лена сварила вчера, хотела угостить." with dissolve
    "Тут я всё понял и чуть не разрыдался от этого." with dissolve
    "Лена любит меня, неудачника, который работает за копейки." with dissolve
    "Она хотела порадовать меня после рабочего дня, после тяжёлых недель работы, несмотря на то, что сама устала в тот день от учёбы." with dissolve
    "Рядом со мной есть такой прекрасный человек, я могу жить и быть счастливым." with dissolve
    "Что я делаю вместо этого? Пропадаю, хрен знает где, убиваю себя на морозе." with dissolve
    "Тем самым разбивая ей сердце." with dissolve
    "Воистину, я её недостоин. Я не просто извиниться должен, я на коленях должен перед ней ползать." with dissolve
    "Свой любимый суп я ел с осознанием своей ничтожности." with dissolve
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 1
    "Закончив, я помыл за собой посуду и пошёл в комнату." with dissolve
    window hide
    scene bg kitchen_rvp:
        align(0.1,0.5)
        ease 2 zoom 3
    stop sound_loop fadeout 1
    play sound sfx_close_water_sink
    stop music fadeout 2
    scene bg kvartira_rvp with dissolve
    play ambience ambience_medstation_inside_night
    
    window show
    "Надо поговорить с Леной сейчас. Обнять её, успокоить, объясниться. Пообещать, что больше такого не повторится." with dissolve
    "Лена сидела в комнате и читала книгу." with dissolve
    me "Лена, я хотел…" with dissolve
    play sound disk_ringtone_rvp
    "Внезапно зазвонил телефон, так и не дав мне сказать нужные слова. Я поднял трубку." with dissolve
    stop sound
    play sound trubka_rvp
    voice "Алло, Персунова Елена тут живёт?" #with dissolve
    me "Да, что нужно?" with dissolve
    voice "Позовите её к телефону." #with dissolve
    window hide
    show un normal sport with dissolve
    window show
    "Я обернулся к Лене." with dissolve
    me "Лена, тут тебя просят к телефону." with dissolve
    hide un normal sport with dissolve
    "Лена подошла к телефону." with dissolve
    "Отвечала она коротко и односложно и я не мог понять тему разговора из того, что смогу услышать." with dissolve
    "Она недолго поговорила и положила трубку, а после этого встала и пошла одеваться." with dissolve
    me "Ты куда?" with dissolve
    un "Меня вызвали в институт, там помощь нужна. Срочно нужно плакат к 7 ноября нарисовать." with dissolve
    me "Стой, а без тебя они не могут?" with dissolve
    un "Нет, не могут. У нас в институте только несколько человек рисовать умеют. А Ленина хорошо нарисовать только у меня получится." with dissolve
    me "Подожди, я поговорить хотел." with dissolve
    show un_rvp normal coat with dissolve
    un "Вечером поговорим, не переживай. Закрой за мной дверь, я ухожу." with dissolve
    "После этих слов Лена оделась и вышла." with dissolve
    hide un_rvp normal coat with dissolve
    play sound sfx_close_door_1
    "Я закрыл за ней дверь." with dissolve
    "Вот и поговорили… теперь сиди и жди, Семён. Ты оставил Лену, теперь Лена оставила тебя." with dissolve
    "Ох уж это мучительное ожидание… попробовал все способы занять себя – и телевизор посмотрел, и книгу почитал, и даже конспекты пописал по своей учёбе." with dissolve
    "Лена всё никак не возвращалась. Тишина давила на меня." with dissolve
    stop ambience fadeout 2
    "Я вспомнил про радиолу “Вега”, стоявшую в углу. Такой проигрыватель для виниловых дисков." with dissolve
    play music plastinki_rvp fadein 2
    "Была и коллекция, причём попадались и западные дефицитные исполнители, типа “Divine comedy”, Питера Габриела и Стинга." with dissolve
    scene bg kvartira_rvp
    show black:
        alpha 0.6
    with dissolve
    "Наступал вечер, я сидел у окна, слушал музыку и просто ждал её." with dissolve
    "Ждал увидеть её фиолетовое пальто с зелёным шарфом." with dissolve
    "Ждал её фиолетовые косички волос, плывущие к нашему подъезду." with dissolve
    "Ждал, что она придёт ко мне слушать старые пластинки." with dissolve
    "Я нашёл наш фотоальбом, в котором все наши фото за три года." with dissolve
    "Все сделаны в райцентре и ни одной здесь, в Горьком." with dissolve
    "Все как один эти фотографии навевали воспоминания. А воспоминания разрывали душу." with dissolve
    "Здесь мы такие счастливые были." with dissolve
    "Я не выдержал и закрыл альбом, поставив его на место." with dissolve
    window hide

    scene bg okno_rvp with dissolve
    window show
    "Затем я начал смотреть на окружавший нас пейзаж." with dissolve
    "Зрелище не из приятных." with dissolve
    "Через дорогу недостроенное кирпичное здание рядом с администрацией." with dissolve
    "Недалеко районная поликлиника – потенциальное место работы Лены после института." with dissolve
    window hide

    scene bg universam_rvp
    show black:
        alpha 0.6
    with dissolve
    window show
    "За ними универсам и рынок." with dissolve
    window hide

    scene bg kvartira_rvp
    show black:
        alpha 0.8
    with dissolve
    window show
    "В итоге мне надоели западные песни, и я выключил радиолу." with dissolve
    stop music fadeout 2
    play ambience ambience_medstation_inside_night
    "Наконец, я её увидел." with dissolve
    "Время было около восьми часов вечера. Она приехала на одном из троллейбусов." with dissolve
    "Как только она зашла в подъезд, я пошёл к двери встречать." with dissolve
    scene bg prih_rvp with dissolve
    play sound sfx_open_door_1
    "Когда она поднялась, я уже открыл ей дверь." with dissolve
    show un_rvp shy coat with dissolve
    "Лена была слегка изумлена такой тёплой встречей, но постеснялась что-то сказать." with dissolve
    show un_rvp normal coat with dspr
    un "Слушай, ты поговорить хотел. Подожди немного, я устала." with dissolve
    me "Пойдём, поужинаем. Ты пока раздевайся, я суп погрею." with dissolve
    un "А ты без меня не ел?" with dissolve
    me "Нет, тебя ждал." with dissolve
    show un_rvp shy coat:
        align(.5,.5)
        ease 1 pos(-.1,.5) alpha 0
    with dissolve
    "Было заметно, что Лену тронуло это." with dissolve
    window hide
    
    scene bg kitchen_rvp with dissolve
    
    window show
    "Через несколько минут мы оба ели суп на кухне." with dissolve
    me "Как прошло?" with dissolve
    show un normal sport with dissolve
    un "Нормально, всё успели. Только устала очень." with dissolve
    "Чёрт, опять препоны." with dissolve
    "Наверное, нужно начать разговор сейчас. Только вот опять в нужный момент нет подходящих слов." with dissolve
    $ renpy.pause(1.5)
    "Так мы и доели ужин молча." with dissolve
    window hide
    window show
    un "Пойду{w=0.3} полежу, совсем сил нет." with dissolve
    window hide
    show un normal sport:
        align(.5,.5)
        ease 1 pos(.0,.5) alpha 0
    window show
    "И скрылась в спальне." with dissolve
    "От этих слов я совсем расстроился." with dissolve
    "Опять возможность решить ситуацию ускользает от меня." with dissolve
    "Сейчас она уснёт. Будить её было как-то неприлично, человек работал." with dissolve
    scene bg kitchen_rvp:
        align(0.1,0.5)
        ease 2 zoom 3
    window hide

    $ persistent.sprite_time = "night"
    $ night_time
    scene bg kvartira_rvp
    show black:
        alpha 0.8
    with dissolve
    
    window show
    "От внутреннего беспокойства мне спать не хотелось." with dissolve
    scene bg okno_rvp with dissolve
    "Я пошёл в комнату и сел за стол у окна." with dissolve
    "Вдруг я заметил магнитофон." with dissolve
    "А ведь я давно не слушал музыку на нём." with dissolve
    "Хорошо, что наушники были, а то затея не имела бы смысла." with dissolve
    "А что послушать?" with dissolve
    "В такой момент хорошо подходило что-то лиричное, про ночь." with dissolve
    "Руки сами нашли кассету." with dissolve
    "Кино. Последний герой. Последняя песня альбома." with dissolve
    "Перед тем как нажать на кнопку, немного отвлёкся." with dissolve
    "Помню, как мне подарила эту кассету Алиса ещё в райцентре перед самым отъездом." with dissolve
    "Кинул взгляд на гитару в углу. А ведь музыка много помогала мне, когда было трудно. Может, сейчас поможет?" with dissolve
    "Я нажал кнопку." with dissolve
    stop ambience fadeout 2
    play music sp_noch_rvp fadein 2
    "Песня пошла по проводам мне в уши." with dissolve
    "Надо разобраться в причинах вчерашнего." with dissolve
    "Почему не пошёл после работы домой? Не хотел сидеть дома один." with dissolve
    "Почему не тянуло домой, а хотелось посидеть подольше? Хотелось излить душу, но не видеть Лену." with dissolve
    "Почему хотел излить душу кому-то, но не Лене? Стыдно было говорить с ней." with dissolve
    "Ведь я считаю, что я её недостоин. Если я признаюсь ей в своих проблемах, что рискую быть уволенным, она меня бросит." with dissolve
    "Почему она меня бросит? Она ведь всегда меня поддерживала." with dissolve
    window hide

    $ persistent.sprite_time = "day"
    $ day_time
    show bg kvartira_rvp
    show un smile2 sport
    show prologue_dream
    with fade
    window show
    "Снова вспомнил, как она сказала мне, что не стыдится того, что я работаю простым водителем троллейбуса." with dissolve
    window hide

    $ persistent.sprite_time = "night"
    $ night_time
    scene bg okno_rvp with dissolve
    window show
    "Почему она любит меня? Не знаю."
    "Здесь мои размышления зашли в тупик. Что у Лены в голове, я до конца не представлял." with dissolve
    "Я сменил тему своих мыслей." with dissolve
    "Почему мне не нравится окружающая меня реальность?" with dissolve
    "Жильё, работа, личная жизнь – всё есть. Но у меня было плохое предчувствие." with dissolve
    "Потому что я знал." with dissolve
    "Я знал, что начнётся в ближайшие годы." with dissolve
    "Уже через год Союз распадётся, нужно будет выживать в новой реальности." with dissolve
    "Мне было страшно брать ответственность за нас с Леной перед неизведанным, тяжёлым временем." with dissolve
    "Сначала я думал, этот мир достаточно сильно отличается и история в нём пошла по другому ходу." with dissolve
    "Но всё та же перестройка встретила меня в райцентре. Всё те же невыплаты зарплат на заводе, закрытия производств." with dissolve
    "Союз развалится под возгласы о свободе, а дальше людей будет ждать нищета, бандитизм, несправедливость и потрясения." with dissolve
    "Если это случится, Лена сильно расстроится, а я не хочу её видеть расстроенной." with dissolve
    "А ведь как всё начиналось хорошо. Жизнь казалась такой лёгкой, когда мы были ещё моложе и…" with dissolve
    "Вдруг на моё плечо опустилась рука." with dissolve
    "Я перестал вспоминать, вернулся в реальность." with dissolve
    window hide
    show un normal sport with dissolve
    window show
    "Это была Лена." with dissolve
    stop music fadeout 3
    play music sp_noch_minus_rvp fadein 2
    "Я снял наушники и хотел поставить песню на паузу, но случайно нажал на кнопку перемотки." with dissolve
    "Песня началась сначала. Было тихонько слышно, как Цой желал спокойной ночи всем, кто ложится спать." with dissolve
    un "Чего не спишь?" with dissolve
    me "Что-то не хочется. Задумался о жизни." with dissolve
    un "Да уж, есть над чем подумать. Не против, если я подсяду?" with dissolve
    me "Не против." with dissolve
    "Я выдвинул ей стул. Лена села рядом." with dissolve
    un "Нехорошо получилось сегодня. Ты ведь хотел извиниться за вчерашнее, а я тебя оставила." with dissolve
    "Затем, помолчав несколько секунд, она продолжила." with dissolve
    un "Но я всё же не понимаю, почему ты так поступил? Почему не пошёл домой как обычно?" with dissolve
    "Я решил, что хватит с меня молчать и скрывать свои мысли от Лены. Скажу как есть, а уж дальше она делает, что хочет." with dissolve
    me "Я ж говорю, жизнь заела." with dissolve
    me "Зарплата маленькая, работа непрестижная. Живём в панельной однушке." with dissolve
    "Лене не понравились мои слова." with dissolve
    show un serious sport with dspr
    un "Что значит не престижная? Для меня нет такого понятия. Есть нужная и ненужная обществу." with dissolve
    un "Ты возишь людей на работу и учёбу, меня в том числе. Это нужная обществу работа, значит достойная." with dissolve
    un "Зарплата пусть маленькая, но мы же не голодаем." with dissolve
    un "Тебе только двадцать исполнилось, поработай ещё, повысят зарплату." with dissolve
    un "Закончи институт, в конце концов. Я вот вообще не могу работать, у меня учёба всё время занимает." with dissolve
    un "Мне даёт вуз деньги, чтобы я не умерла с голоду, пока учусь, а ты получаешь зарплату за свой труд, полезный для общества." with dissolve
    show un smile sport with dspr
    un "Это огромная разница и я тебе завидую в этом." with dissolve
    me "Да это понятно. Просто… просто мне стыдно." with dissolve
    show un shy sport with dspr
    "Лена удивилась." with dissolve
    un "Перед кем?" with dissolve
    me "Перед тобой." with dissolve
    un "Я не понимаю. Ты работаешь, деньги в дом приносишь, учишься параллельно с этим." with dissolve
    un "Ты у меня стыда не вызываешь… не считая вчерашнего." with dissolve
    me "Ну как же, ты такая красавица, учишься на одни пятёрки в институте. Спортом занимаешься. А я…" with dissolve
    "Я выдохнул. Затем тяжело продолжил." with dissolve
    me "Давай расстанемся. Я не хочу тебя тяготить." with dissolve
    show un shocked sport with dspr
    "Лена испугалась моих слов. Я продолжил высказывать всё, что таилось в душе." with dissolve
    me "Ты найдёшь себе достойного мужа." with dissolve
    un "Я уже нашла…" with dissolve
    me "У него будет нормальная работа, богатые родители. Он тебя обеспечит." with dissolve
    "Внезапно Лена завелась от этих слов." with dissolve
    show un angry sport with dspr
    un "Я тебе что, шлюха какая-то?! Выйти замуж за деньги предлагаешь?!" with dissolve
    un "Что я этому богатому мужу скажу, когда он штамп в паспорте увидит от нашего брака? “Ой, да сошлась с одним неудачником, он не мог меня рублями засыпать, я его бросила за это”. Да грош мне цена после этого!" with dissolve
    show un normal sport with dspr
    un "Всю жизнь это презирала. Всю жизнь смогла прожить в бедности, это мне не страшно. Лишь бы был человек, с которым я могу быть счастлива." with dissolve
    me "То есть ты не хочешь меня бросить?" with dissolve
    un "Нет, а с чего?" with dissolve
    un "Ты молодец, что хочешь обеспечивать семью, чтобы я не бедствовала. Но не всё сразу же." with dissolve
    un "И не надо так переживать из-за денег, мои чувства к тебе не зависят от того, сколько рублей ты в кассе получаешь." with dissolve
    show un laugh sport with dspr
    un "Это всё остатки твоего мировоззрения от жизни в капиталистическом обществе." with dissolve
    show un grin sport with dspr
    "Лена перестала злиться. Немного улыбнувшись, она продолжила." with dissolve
    un "Видимо, ты даже не представляешь, как изменил мою жизнь в лучшую сторону." with dissolve
    un "Ты столько раз меня выручал. Ты спас меня от той тяжёлой и одинокой жизни." with dissolve
    me "А знаешь, взаимно ведь. Я в тебя смотрю порой как в своё отражение." with dissolve
    me "Моя жизнь до тебя тоже была одинокой. Но благодаря тебе я наконец-то понял, что такое счастье." with dissolve
    me "Жаль только я это ценить не умею." with dissolve
    show un shy sport with dspr
    un "В смысле?" with dissolve
    me "Я про вчерашнее. Я думал, я у тебя сильное отвращение вызвал, ты не захочешь жить с алкашом. Ещё и отца напомнил, прости." with dissolve
    show un normal sport with dspr
    un "А, это… Видно судьба у меня такая." with dissolve
    un "Все мужчины в моей жизни спиваются. Сначала отец, теперь вот муж." with dissolve
    un "Лучшей подруге это тоже одни несчастья принесло. И всё же, надо понять, как ты до такого дошёл." with dissolve
    me "Ну, помнишь, в конце лета мы переехали в Горький. Ты начала учиться, а я работать, ну и тоже учиться… как бы." with dissolve
    un "И за эти месяцы погрязли в рутине. Я должна была тебя как-то отвлечь, но сама загрузилась." with dissolve
    show un sad sport with dspr
    "Лена помолчала и вдруг продолжила очень грустным голосом." with dissolve
    un "Я не думала, что так трудно будет сменить обстановку. Этот город реально не зря Горьким зовётся." with dissolve
    un "Мне порой и страшно и неуютно здесь, всё вместе. Я же всю жизнь в райцентре прожила, не знала, каково это." with dissolve
    un "Мы всё думали, как повезло тебе сесть на автобус и попасть в другое время. Я не знаю, как ты пережил, это же так страшно, наверное, было." with dissolve
    me "Ну да, тяжело мне тогда было. Но главное, что это позади." with dissolve
    window hide
    show un cry sport:
        align(.5,.5)
        ease 2 xpos .25
        ease 2 zoom 2.5 pos(.0,.8)
    window show
    "Я обнял Лену. Она всем видом показывала, что её нужно было поддержать." with dissolve
    me "Хочешь, не буду пить? Вообще." with dissolve
    window hide
    show un smile sport:
        anchor(0.5,0.5) pos(0.0,0.8)
        ease 3 zoom 1.0 pos(0.5,0.5)
    window show
    "Лену обрадовали эти слова." with dissolve
    un "Было бы славно." with dissolve
    un "Но что мужикам скажешь?" with dissolve
    me "Скажу, что перебьются." with dissolve
    "Кто-то бы меня осудил, что я слишком подстраиваюсь под желания Лены. В данном случае это было оправдано." with dissolve
    "Для Лены это было слишком больной темой, я готов был пойти на уступки, чтобы она была счастлива." with dissolve
    me "Слушай, а почему ты мне поверила сегодня, когда я прибежал? Не стала сомневаться в моих словах. Я бы сам не поверил, что кто-то прибежит ради меня." with dissolve
    show un laugh sport with dspr
    un "Да ты врать не умеешь!" with dissolve
    "Лена по-доброму посмеялась." with dissolve
    show un smile sport with dspr
    un "Это всё, что тебя тяготит?" with dissolve
    me "Почти… ещё будущее. Помнишь, я тебе рассказывал, что в моём мире было?" with dissolve
    show un shy sport with dspr
    me "Лена, этот день уже близко. Не будет Союза, понимаешь?" with dissolve
    me "И мне страшно за нас, потому что будет страшное время, я боюсь тебя потерять." with dissolve
    show un serious sport with dspr
    "Лена помрачнела." with dissolve
    un "Честно, не хочу в это верить. Но ведь у нас по-другому история пошла, мы это выяснили." with dissolve
    show un smile sport with dspr
    un "В любом случае, я верю – что бы ни случилось, ты нас защитишь." with dissolve
    "Я немного опешил от такой веры в меня. Лена воспользовалась паузой и сменила тему." with dissolve
    un "Я тут ещё вспомнила, по поводу того, за кого замуж выходить. Смотрел фильм “Москва слезам не верит”?" with dissolve
    un "Там героиня говорила – чтобы стать генеральской женой, нужно пойти замуж за лейтенанта и ездить с ним по воинским частям по всему Союзу." with dissolve
    un "Знаешь, кому принадлежала эта квартира? Моей родственнице, да. У неё муж был генералом. Ну, сам знаешь, почётно быть генеральской женой." with dissolve
    un "Но знала она своего генерала ещё лейтенантом. И замуж пошла за него, когда он ещё лейтенантом был." with dissolve
    un "И жила с ним, деля невзгоды. Они вместе прошли тридцатые годы, прошли всю войну. Она ждала его из походов, поддерживала в трудную минуту." with dissolve
    un "В сорок первом году его рота попала в окружение. Он нашёл в себе силы поднять обескровленных бойцов на прорыв. Они вырвались из вражеского кольца, и он спас ребят." with dissolve
    un "Потому что знал, что она его ждёт. Потом дослужился до генерала." with dissolve
    show un normal sport with dspr
    un "Недолго он генеральские погоны носил, так как вскоре умер. Потом моя тётя переехала в эту однушку. Просторную квартиру вернула государству, сказав, что ей без мужа нет смысла занимать такую площадь." with dissolve
    show un smile sport with dspr
    un "Для неё эти тридцать три квадрата были концом, для нас началом." with dissolve
    me "Я порой корю себя, что не заработал нам на квартиру и, по сути, живу на твоей площади." with dissolve
    show un angry2 sport with dspr
    un "Опять ты начинаешь. Тебе только двадцать исполнилось, как ты мог квартиру получить?" with dissolve
    un "Зачем ты себя гонишь и обременяешь обязательствами, если даже я от тебя этого не требую?" with dissolve
    un "И живёшь ты не в моей, а в нашей квартире. Я всегда поделюсь с тобой всем, что у меня есть." with dissolve
    show un smile sport with dspr
    un "И ты, я уверена, тоже." with dissolve
    "С души будто гора спала. Я такого облегчения не испытывал, наверное, с того времени как помирился с Леной в Совёнке." with dissolve
    me "Тогда прости меня, Лена. Я слишком усложнил жизнь себе и тебе, в итоге не выдержал и повёл себя по дурацки, забыв, что ты меня поддержишь." with dissolve
    un "Ты тоже прости меня, Сёма. Я примерила на тебе воспоминания о другом человеке, хотя ты им и не являлся, и была предвзята по отношению к тебе." with dissolve
    un "Мы с тобой ещё молоды и не застрахованы от ошибок." with dissolve
    show un cry sport with dspr
    "Вдруг Лена погрустнела так сильно, что казалось, готова была заплакать." with dissolve
    un "Только, пожалуйста, не предлагай мне больше расстаться. И не уходи не предупредив. Я… мне было очень больно и грустно." with dissolve
    un "Ты был прав. Я не выдержу, если ты меня оставишь. Я на тебя накричала, не хотела, чтобы ты пользовался моей слабостью." with dissolve
    un "Но сейчас я понимаю, ты хороший человек и не стал бы так поступать. И вообще я такая злая была к тебе, не понимая, какую ношу ты несёшь каждый день без отдыха." with dissolve
    me "Хорошо, не оставлю. Я думаю, эта ситуация послужит для нас уроком. Что нужно лучше прислушиваться друг к другу и не накручивать себя." with dissolve
    show un cry_smile sport with dspr
    un "Ты прав. Вот видишь, ты можешь извлекать уроки из ошибок, значит, ты совсем не безнадёжен." with dissolve
    me "Обещаю, что не буду скрывать от тебя своих переживаний и не брошу тебя в трудную минуту." with dissolve
    un "Хорошо, Сёма. Я тоже обещаю поддерживать и ничего не скрывать от тебя." with dissolve
    show un smile2 sport with dspr
    un "Ой, Сёма, смотри, на улице снег пошёл! Скоро зима и Новый год!" with dissolve
    "Лена светилась от счастья." with dissolve
    show un grin sport with dspr
    un "Повязку уже давно мог снять. Какой ты у меня рассеянный." with dissolve
    "Точно, я про неё совсем забыл с этими думами. Лена сняла бинт и поцеловала меня в лоб." with dissolve
    show un grin sport:
        align(.5,.5)
        ease 2 zoom 2.5 pos(.0,.8) alpha 0
    with dspr
    "Она наклонилась к уху и зашептала." with dissolve
    un "Я горжусь тобой, Сёма." with dissolve
    "Недопонимание между нами ушло, и наши души снова стали близки. Всё начало идти к тому, что не только души." with dissolve
    "Вдруг я вспомнил, что у меня в наушниках до сих пор играет песня." with dissolve
    stop music fadeout 3
    un "А что это играет? Почему сам слушаешь, а мне не даёшь?" with dissolve
    play music sp_noch_solo_rvp
    "Она выдернула штекер из разъёма. И в этот момент как раз начиналось то самое каспаряновское соло на гитаре. Оно громко заиграло на всю квартиру." with dissolve
    "От неожиданности я вскочил из-за стола. Лена резко сначала обняла меня, затем запрыгнула на меня." with dissolve
    "Я хотел было что-то сказать, но она заняла мои губы своими…" with dissolve
    window hide

    scene bg int_house_of_un_night
    show prologue_dream
    with fade
    window show
    "Вспомнился момент из лагеря, как мы слились в экстазе в её домике." with dissolve
    "Тогда я окончательно забыл про поиск ответов, и мне вообще было наплевать на всё, кроме Лены." with dissolve
    "В тот вечер я сидел и любовался ею, когда она спала. Её лицо выражало тихое счастье и спокойствие." with dissolve
    "Так спал человек, которого в душе ничего не беспокоит." with dissolve
    "С того дня мы были крепко связаны на всю оставшуюся жизнь. Я пообещал себе не оставлять её и сделать счастливой." with dissolve
    window hide
    
    scene bg ext_square_night
    show prologue_dream
    with fade
    
    window show
    "Помню, как потом смотрел в окно на ночной лагерь." with dissolve
    "Враждебное прежде место вдруг стало таким уютным." with dissolve
    "Благодаря Лене целый лагерь в тот день принадлежал нам, никто не нарушал эту идиллию." with dissolve
    "И в тот день, казалось, прошлое было абсолютно неважно, важно было лишь то, что мы с Леной нашли друг друга." with dissolve
    "Сейчас так же. Зарплата, троллейбусы, мрачное будущее – всё это перестало что-то значить. Вся жизнь впереди, ещё успею подняться и найти хорошую работу." with dissolve
    "А вообще, счастье не только в приличной зарплате, а в том, чтобы любить и быть любимым. Главное – быть вместе с ней и поддерживать друг друга…" with dissolve
    window hide

    scene bg kvartira_rvp
    show black:
        alpha 0.8
    with dissolve
    window show
    "Минут через десять мы с Леной лежали на кровати и пытались отдышаться." with dissolve
    "Это было прекрасно." with dissolve
    "Это и было счастье." with dissolve
    "Это и был наш рай в панельке." with dissolve
    window hide
    show blink
    
    stop music fadeout 2
    stop ambience fadeout 2
    play sound sp_noch_solo_rvp fadein 2
    scene bg universam_rvp
    show prologue_dream
    with fade
    show credits rvp_credits_a1:
        xalign 0.5
        ypos 1.3
        linear 52.0 ypos -4.0
    $ renpy.pause()
    stop sound fadeout 2
    jump rvp

label b1:
    stop music fadeout 2
    $ renpy.show("black")
    $ renpy.with_statement(fade3)
    $ renpy.pause(2.0, hard=True)
    $ new_chapter(0, u'Рай в панельке: Сторона Б')
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    scene bg int_bus_sunset_rvp with dissolve
    play sound_loop sfx_bus_interior_moving fadein 1

    #Вывод белой полоски
    show white:
        subpixel True
        align (.5,.5)
        easein_expo 1.5 crop (480,3,1440,3)
    #Вывод текста
    show textimg up_b_rvp:
        subpixel True
        crop (0,0,1920,270)
        anchor (0.,1.)
        pos (0.,.5)
        pause 2.
        easein_expo 1.5 crop (0,0,1920,810)#чем больше последняя коорда, тем больше выдвигается
    show textimg dn_b_rvp as textimg2:
        subpixel True
        crop (0,810,1920,270)
        anchor (0.,0.)
        pos (0.,.5)
        pause 2.
        easein_expo 1.5 crop (0,270,1920,810)#чем меньше вторая коорда, тем больше выдвигается
    #Скрытие всего
    $ renpy.pause(5.0)
    hide white
    hide textimg up_b_rvp
    hide textimg dn_b_rvp as textimg2

    "Автобус набирал обороты. Мы с Леной сели на последние места, я уступил ей место у окна." with dissolve
    "Опять я еду в автобусе. Что же всё-таки происходит?" with dissolve
    scene bg int_house_of_un_night with dissolve
    "Проснулись с Леной, пошли собираться, сели в автобус и…" with dissolve
    scene cg epilogue_un with dissolve
    "Снова проснулся на лавочке в Совёнке?" with dissolve

    scene bg int_bus_sunset_rvp with dissolve
    show un_rvp smile pioneer2 with dissolve
    me "Лена, а что было до того, как я проснулся сейчас?" with dissolve
    show un_rvp rock pioneer2 with dspr
    un "У тебя память отшибло?" with dissolve
    me "Если бы ты знала, что я пережил неделю назад, небольшой провал в памяти показался бы тебе мелочью." with dissolve
    me "Пожалуйста, расскажи, а то я уже не могу так, непонятно где, непонятно в каком году." with dissolve
    show un_rvp shy pioneer2 with dspr
    "Лена поняла, что не стоит препираться и нужно помочь." with dissolve
    un "Ну как же. Я проснулась, и мы решили в последний раз погулять по Совёнку, пока ждали автобус. Дошли до площади, затем сели на лавочку полюбоваться лагерем напоследок." with dissolve
    un "Потом ты положил голову мне на колени и задремал." with dissolve
    "Наконец-то воспоминания вернулись ко мне. Всё так и было." with dissolve
    un "Ну как, вспомнил?" with dissolve
    me "Да, спасибо. Долго я так спал?" with dissolve
    show un_rvp smile pioneer2 with dspr
    un "Недолго, минут пятнадцать." with dissolve
    "Видимо мне приснилось, что мы снова в домике. Лена проснулась, и мы пошли на остановку, где нас забрал автобус." with dissolve
    "Затем я проснулся на лавочке снова в Совёнке и услышал, как Ольга Дмитриевна зовёт нас. Мы собираемся и вот я еду… снова…" with dissolve
    "{b}Куда?{/b}" with dissolve
    me "Лен, а куда мы едем?" with dissolve
    un "В райцентр, куда же ещё." with dissolve
    me "А имя у райцентра?" with dissolve
    show un_rvp shy pioneer2 with dspr
    un "Ты не знаешь?" with dissolve
    me "Лена, я вообще ничего не знаю. Ни какая дата на календаре, ни где я нахожусь. У нас есть время, расскажи." with dissolve
    show un_rvp normal pioneer2 with dspr
    un "Ну, смотри, всё я тебе не успею рассказать, но попробую. Город, в который мы сейчас едем, называется Лениноморск. Живёт нас там где-то тысяч сто." with dissolve
    me "Лениноморск? В честь тебя назвали?" with dissolve
    show un_rvp grin pioneer2 with dspr
    un "А ты смешной, ты мне нравишься. Нет, не в честь меня." with dissolve
    show un_rvp smile pioneer2 with dspr
    un "Сейчас июнь 1987-го года. Число… погоди, самой надо вспомнить. Мы сдали годовые экзамены в конце мая, поехали сразу." with dissolve
    un "Смена была две недели. Сегодня суббота, значит… тридцатое… шестое… тринадцатое! Сегодня тринадцатое июня." with dissolve
    me "Надо же, у вас довольно тепло для июня." with dissolve
    un "Ну да, мы же на юге. Что тебе ещё рассказать? Я к твоим услугам." with dissolve
    show un_rvp smile3 pioneer2 with dspr
    "Лена любезно улыбнулась мне." with dissolve
    me "У меня много вопросов. Например…" with dissolve
    scene bg int_bus_sunset_rvp with dissolve
    "Мы разговорились. Лена рассказала про город и про регион, где он находится, про местные достопримечательности." with dissolve
    "Наконец, мы приехали туда. Меня встретили кварталы панельных домов. В этот момент от переизбытка информации меня снова начало клонить в сон." with dissolve
    stop sound_loop fadeout 1
    show blink
    scene bg black with dissolve

    play music raindrops_sandr_rvp fadein 1
    #Вывод белой полоски
    show white:
        subpixel True
        align (.5,.5)
        easein_expo 1.5 crop (480,3,1440,3)

    #Вывод текста
    show textimg kanon2_rvp:
        subpixel True
        crop (0,0,1920,270)
        anchor (0.,1.)
        pos (0.,.5)
        pause 2.
        easein_expo 1.5 crop (0,0,1920,850)#чем больше последняя коорда, тем больше выдвигается
    show textimg epilogue_rvp as textimg2:
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
    hide textimg kanon2_rvp
    hide textimg epilogue_rvp as textimg2
    $ renpy.pause(2.0)

    show unblink
    scene bg int_bus_on_square_rvp with dissolve
    $ persistent.sprite_time = "night"
    $ night_time ()
    play music music_list["no_tresspassing"]

    scene bg int_bus_on_square_rvp:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 15 zoom 3 anchor (1900,900)
        parallel:
            ease 0.20 pos (0, 0)
            ease 0.20 pos (25,25)
            ease 0.20 pos (0, 0)
            ease 0.20 pos (-25,25)
            repeat
#сделать через оффсет
    "Я проснулся посреди пустого Икаруса… опять! Я в шоке рванул по салону, задыхаясь от досады, что всё повторяется снова." with dissolve
#цг - вид из автобуса ночной
    scene bg int_bus_on_square_rvp:
        ease 1 align(.9,.3) zoom 2
    "В отчаянии я повернул голову… и, наконец, заметил, что за окном не утро, а вечер и не ворота лагеря, а незнакомая площадь." with dissolve
#бг - вид в автобусе на задние сиденья
    scene bg int_bus_on_square_rvp:
        align(.9,.3) zoom 2
        ease 1 align(.5,.5) zoom 1
    "Я обернулся и увидел… испуганную Лену."
    show un_rvp scared pioneer2 with dspr
    me "Лена… мы же сейчас не в Совёнке?" with dissolve
    un "Н-нет, Сёма, мы в райцентре. Т-ты в порядке?" with dissolve
    stop music fadeout 2
    me "Да, Лена. Прости, у меня помутнение на секунду произошло. Я просто…" with dissolve 
    show un_rvp normal pioneer2 with dspr
    mt "Ребят, ну вы там долго ещё? Автобусу уезжать надо!" with dissolve
    "Ну наконец-то!" with dissolve
    "Я схватил наши с Леной вещи, взял её за руку и быстро повёл к выходу." with dissolve
    #бег плюс зум
    scene bg int_bus_on_square_rvp:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 15 zoom 3 anchor (1900,900)
        parallel:
            ease 0.20 pos (0, 0)
            ease 0.20 pos (25,25)
            ease 0.20 pos (0, 0)
            ease 0.20 pos (-25,25)
            repeat
    me "Лена, быстрее, на свободу!" with dissolve
    scene black with dissolve
    "И вот пол сменился ступеньками и, наконец, землёй. Из автобуса я не вышел, а буквально выпрыгнул." with dissolve
    scene bg square_lmr_night_rvp with dissolve
    play ambience ambience_camp_center_night
    play sound sfx_bodyfall_1
    "Меня встретила городская площадь… и удивлённая Ольга Дмитриевна." with dissolve
    show un_rvp smile pioneer2 far at right with dissolve
    show mt surprise pioneer far at center with dissolve
    me "Извините, Ольга Дмитриевна, задремали немного в дороге! Вот он я, Семён Персунов, воспитанный вами образцовый пионер, стою перед вами!" with dissolve
    mt "Умеешь ты удивить, Семён. Ладно, вот ребята поезда ждут, иди к ним." with dissolve
    scene bg square_lmr_night_rvp with dissolve
    "На площади было темновато, городской вокзал освещался фонарями. К тому же вечера на юге были не очень тёмными в это время суток." with dissolve
    show sl normal pioneer far:
        anchor(0.5,0.5) pos(0.3,0.5)
    with dissolve
    show sh normal far:
        anchor(0.5,0.5) pos(0.1,0.5)
    with dissolve
    show us smile pioneer far:
        anchor(0.5,0.5) pos(0.9,0.5)
    with dissolve
    show dv normal pioneer2 far:
        anchor(0.5,0.5) pos(0.5,0.5)
    with dissolve
    show mi normal pioneer far:
        anchor(0.5,0.5) pos(0.7,0.5)
    with dissolve
    "Там был весь наш отряд." with dissolve
    play music music_list["reminiscences"] fadein 2
    sh "Ну наконец-то, приехали! Думали, не успеем попрощаться!" with dissolve
    mi "Лена здесь местная, нам Алиса сказала. А ты, Семён, куда поедешь?" with dissolve
    "Действительно, куда я поеду? Да и зачем? Единственный человек, которому я нужен и который нужен мне, живёт здесь." with dissolve
    "Лена сказала, что ей со мной не страшно. Теперь мне не страшно с ней." with dissolve
    me "Ребят, поезд ждёте?" with dissolve
    us "Да, он через два часа только." with dissolve
    me "А куда поезд?" with dissolve
    sl "В Москву, дальше разъедемся кто куда. Садись к нам, последний раз ведь вместе." with dissolve
    "Неужели всё? А я ведь уже привык к ребятам за одну неделю, а они ещё сильнее сдружились между собой за две недели смены." with dissolve
    scene bg square_lmr_night_rvp with dissolve
    "Лена не сидела одна, она общалась со своей соседкой по домику ¬– Мику – и со своей подругой по библиотеке – Женей." with dissolve
    "Меня подозвал Электроник." with dissolve
    show el smile pioneer with dissolve
    el "Слушай, спасибо тебе, что поговорил со мной. У нас с Женей всё-таки получилось." with dissolve
    me "Да ладно, как?" with dissolve
    "Вспомнилось, как он убегал от неё из библиотеки, какая рассвирепевшая была Женя в тот момент." with dissolve
    el "Мы помирились." with dissolve
    el "Женя только с виду такая бука, но так-то добрая, если подход найти. В последнюю ночь мы танцевали среди звёзд." with dissolve
    window hide

    #Приближение Электроника и выдвигание девочек
    show el smile pioneer:
        align(0.5,0.5)
        ease 1.5 pos(0.3,0.7) zoom 1.25
    show mz laugh pioneer far:
        anchor(0.5,0.5) pos(1.1,0.5)
        ease 1.5 pos(0.6,0.5)
    show un_rvp grin pioneer2 far:
        anchor(0.5,0.5) pos(1.3,0.5)
        ease 1.5 pos(0.8,0.5)
    window show
    "Я посмотрел на Женю: она в тот момент о чём-то весело общалась с Леной." with dissolve
    "Видимо, Лена тоже смогла найти подход." with dissolve
    window hide

    #Обратный процесс
    show el smile pioneer:
        anchor(0.5,0.5) pos(0.3,0.7) zoom 1.25
        ease 1.5 pos(0.5,0.5) zoom 1.0
    show mz laugh pioneer far:
        anchor(0.5,0.5) pos(0.6,0.5)
        ease 1.5 pos(1.1,0.5)
    show un_rvp grin pioneer2 far:
        anchor(0.5,0.5) pos(0.8,0.5)
        ease 1.5 pos(1.3,0.5)

    window show
    "Электроник увидел, что я на них смотрю, и развеселился." with dissolve
    show el grin pioneer with dissolve
    el "А ты, я смотрю, тоже нашёл себе подругу? С Леной теперь?" with dissolve
    me "А… как ты догадался?" with dissolve
    el "Ой, да ладно, весь лагерь шептался о вас." with dissolve
    me "Ох, эти сплетники. Слушай, а как вы с Женей теперь? Разъедетесь ведь…" with dissolve
    show el smile pioneer with dspr
    el "А, не переживай, здесь всё схвачено. Оказалось, мы оба из Москвы, сможем видеться там круглый год." with dissolve
    me "Ого, повезло вам." with dissolve
    el "Ладно, бывай, мне ещё надо кое с кем попрощаться." with dissolve
    show el smile pioneer:
        ease 1 pos(0.,.5) alpha 0
    "Ко мне подошёл Шурик." with dissolve
    show sh smile with dissolve
    sh "Семён, спасибо, что помог выйти из подземелья. Непонятно, чем бы это всё закончилось, если бы не ты." with dissolve
    me "Да не за что. Слышал, ты далеко живёшь отсюда." with dissolve
    show sh normal with dspr
    sh "Ага, я вообще из Сибири. В академгородке живу. Там у нас мощный научный центр." with dissolve
    me "А, слышал, Новосибирск. Оставь мне свой адрес, письма будем писать." with dissolve
    sh "Давай, хорошая идея!" with dissolve
    "Шурик дал мне листок из блокнота со своим адресом." with dissolve
    sh "Ручку тоже держи, дарю на память! И в благодарность за спасение!" with dissolve
    me "О, спасибо, а то мне писать нечем." with dissolve
    scene bg square_lmr_night_rvp with dissolve
    "Дальше я подходил к ребятам и записывал их адреса. Эта неделя перевернула мою жизнь, и я хотел сохранить всё, что было с ней связано." with dissolve
    "Лагерь был величиной постоянной, на него я повлиять не мог, да и незачем. А вот дружеские связи, возникшие за эти семь дней, надо было сохранить." with dissolve

    #моргание глазом
    window hide
    show blink
    scene bg black with dissolve
    $ renpy.pause(1.0)
    show unblink

    scene bg square_lmr_night_rvp with dissolve
    show sl smile pioneer with dissolve
    window show
    me "Славя, можно я тут сяду?" with dissolve
    sl "Да, конечно. Скажи, тебе понравилась смена?" with dissolve
    me "Да, безусловно. Спасибо тебе за помощь в начале." with dissolve
    sl "Помнишь, как я тебя у ворот встретила?" with dissolve
    me "О да, ты мне сказала, как пройти к вожатой, а я всё равно перепутал и снова к тебе пришёл." with dissolve
    show sl laugh pioneer with dspr
    "Мы посмеялись над моей неловкостью в первый день. А ведь и недели не прошло…" with dissolve
    show sl smile2 pioneer with dspr
    sl "А потом ты на ужине за Ульяной погнался." with dissolve
    me "Конечно, она мне насекомое под котлету подложила! А потом ты меня в столовой кормила булками с кефиром." with dissolve
    me "Кстати, пока ты к Жене ходила, я у столовой встретил Алису: она тоже хотела закусить ими." with dissolve
    sl "И как бы она это сделала, интересно? Ключи-то у меня и у персонала." with dissolve
    me "А она пыталась взломать замок." with dissolve
    show sl laugh pioneer with dspr
    sl "Вот уж ограбление века!" with dissolve
    "Славя посмеялась над этой выходкой Двачевской." with dissolve
    me "А помнишь, как мы с Леной поплыли за земляникой." with dissolve
    show sl smile pioneer with dspr
    sl "Да… помню вас двоих тогда… Семён, я тебе хочу сказать." with dissolve
    show sl serious pioneer with dspr
    "Славя вдруг стала серьёзной." with dissolve
    sl "Береги то, что имеешь, даже если оно досталось тебе легко." with dissolve
    "Не понял. Допустим, она про Лену. Но я готов беречь её. И досталось мне это счастье не так уж легко, просто Славя не всё знает." with dissolve
    me "Хорошо, Славя, я тебя понял. Не переживай, я отношусь к этому серьёзно, это не игрушки." with dissolve
    show sl normal pioneer with dspr
    "Погодите-ка. Почему эти слова кажутся мне знакомыми? Но ведь никто мне этого не говорил во время смены. Или я что-то забыл?" with dissolve
    me "Слушай, запиши мне свой адрес, мы сможем письма писать." with dissolve
    show sl smile2 pioneer with dissolve
    sl "А зачем тебе мне письма писать?" with dissolve 
    "Она с хитринкой посмотрела на меня. Но вопрос резонный, особенно учитывая, что у меня теперь есть девушка. Нужно убрать возникшую двусмысленность." with dissolve
    me "Да я просто…" with dissolve
    sl "Я Лене оставила адрес свой, у неё запишешь." with dissolve
    me "Хорошо. Знаешь, из тебя хороший руководитель выйдет. Вступай в этот, как его, комсомол!" with dissolve
    show sl laugh pioneer with dspr
    "Славя засмеялась."
    sl "Да я уже там одной ногой, последний раз съездила пионером, разрешили. Ну, бывай, буду рада снова тебя встретить." with dissolve
    me "Ага, как у тех ворот." with dissolve

    #моргание глазом
    window hide
    show blink
    scene bg black with dissolve
    $ renpy.pause(1.0)
    show unblink
    window show

    scene bg square_lmr_night_rvp with dissolve
    show us smile pioneer with dissolve
    me "Ульян, ты не в обиде, что я тебе тогда перца в компот сыпанул?" with dissolve
    us "Конечно в обиде! Но шутка удачная, так что хвалю! Записывай адрес!" with dissolve
    "Я записал её адрес." with dissolve
    show us grin pioneer with dissolve
    us "Ладно, бывай. И удачи с Ленкой!" with dissolve
    "И эта шкода знает…" with dissolve

    #моргание глазом
    window hide
    show blink
    scene bg black with dissolve
    $ renpy.pause(1.0)
    show unblink
    window show

    scene bg square_lmr_night_rvp with dissolve
    show un_rvp smile pioneer2 at right with dissolve
    show mz smile glasses pioneer at left with dissolve
    show mi smile pioneer at center with dissolve
    "Я подошёл к Лене, Мику и Жене. В лагере я хотел сократить эту компанию до одной Лены, но жизнь это сделает сама и надолго, так что надо было с ними поговорить в последний раз." with dissolve
    mi "Семён, привет. Как тебе смена? Мне так понравилось! У вас в Союзе очень красиво, такая природа живописная. Особенно мне понравились сосны около музыкального кружка. Тебе нравятся сосны? Или может ёлки?" with dissolve
    me "Слушай, а тебе не было в своём музклубе одино…?" with dissolve
    dv "Мику, подойди сюда быстрее!" with dissolve
    mi "Ой, извини, ты поговорить хотел, мне ещё к Алисе подойти надо, пойдём со мной. Мы сыграем тебе, послушаешь." with dissolve
    me "А, ну ты иди, я через пару минут подойду, я просто с девочками поговорить хотел." with dissolve
    mi "Хорошо. Приходи к нам, мы тебе сыграем…" with dissolve
    show mi smile pioneer:
        align(0.5,0.5)
        ease 2 pos(1.3,0.5) alpha 0
    "А что она хотела мне сыграть, я уже не услышал."
    show un_rvp smile pioneer2:
        anchor(0.5,0.5) pos (0.7,0.5)
        ease 1 pos(0.6,0.5)
    show mz smile glasses pioneer:
        anchor(0.5,0.5) pos (0.3,0.5)
        ease 1 pos(0.4,0.5)
    "Остались Лена и Женя. Я повернулся к ним."
    mz "Ну что, Семён, понравилось в лагере?" with dissolve
    "Женя выглядела нетипично весело для своего мрачного образа." with dissolve
    me "Какая-то ты весёлая для отъезда… да и вообще." with dissolve
    mz "А чего грустить? Смена рано или поздно закончится, главное – то, как она тебя поменяет. А также люди, которых ты там встретил и они изменили твою жизнь к лучшему." with dissolve
    mz "Мне очень многое дала эта смена и я постараюсь это сохранить и не потерять. Мы с Леной обменялись адресами, чтобы писать друг другу." with dissolve
    mz "С Серёжей будем видеться, он тебе, наверное, говорил, что мы из одного города. Тебе тоже спасибо за то, что притащил меня в карты играть." with dissolve
    $ persistent.sprite_time = "sunset"
    $ sunset_time
    show mz smile glasses pioneer:
        anchor(0.5,0.5) pos (0.4,0.5)
        ease 1 pos(0.5,0.5)
    show ext_square_sunset behind mz
    "Ох, вспомнила. Тот самый турнир на втором дне. А ведь момент, когда я уговаривал Женю играть, был одним из самых приятных… после всех моментов с Леной, конечно." with dissolve
    "Не в Жене дело. Просто это был приятный и беззаботный, ничем не омрачённый день. Даже обходной для меня обернулся приятной прогулкой и знакомством с ребятами." with dissolve
    "И когда я уговаривал Женю, я примерил на себе совершенно нетипичную для себя, даже противоположную моему естеству роль." with dissolve
    "Будто сам себя вытягивал из кокона затворничества к людям, к обществу." with dissolve
    mz "Эй, ты чего там задумался. Семёёён?" with dissolve
    scene bg square_lmr_night_rvp with dissolve
    $ persistent.sprite_time = "night"
    $ night_time
    show mz angry glasses pioneer:
        anchor(0.5,0.5) pos(0.4,0.5)
    show un_rvp smile2 pioneer2:
        anchor(0.5,0.5) pos(0.6,0.5)
    "Я мысленно вернулся из лучшего дня смены в “здесь и сейчас”." with dissolve
    mz "Ну вот, замечтался и совсем меня не слушает." with dissolve
    #блять сука какого хуя оно само не исчезает. Если вы читаете это, то знайте - при написании этого перехода ренпу себя повёл странно.
    hide un_rvp smile pioneer2
    $ persistent.sprite_time = "day"
    $ day_time
    show mz normal glasses pioneer:
        anchor(0.5,0.5) pos (0.4,0.5)
        ease 1 pos(0.5,0.5)
    show int_dining_hall_day behind mz
    "Ага, как тогда в столовой, когда она мне что-то тараторила." with dissolve
    hide mz normal glasses pioneer
    show un smile2 pioneer with dissolve
    "Хотя стоп, я же с Леной тогда решил сесть. Да что же не так с моей памятью…" with dissolve
    #по центру кусок бг площади вырван и под ним бг столовой и спрайт Жени и Лены 
    scene bg square_lmr_night_rvp with dissolve
    $ persistent.sprite_time = "night"
    $ night_time
    show mz angry glasses pioneer:
        anchor(0.5,0.5) pos(0.4,0.5)
    show un_rvp smile pioneer2:
        anchor(0.5,0.5) pos(0.6,0.5)
    "Снова вижу перед собой ту самую недовольную Женю." with dissolve
    me "Да просто воспоминания накрыли. Ладно, я пойду. Спасибо за смену, Жень." with dissolve
    show mz normal glasses pioneer:
        anchor(0.5,0.5) pos(0.4,0.5)
    mz "Бывай. Может быть, свидимся. Ладно, Лен, каких тебе книг прислать?" with dissolve
    un "Сейчас, подожди, Жень. Сёма, а ты куда?" with dissolve
    me "Мику позвала, она на гитаре играет." with dissolve
    show un_rvp serious pioneer2 with dspr 
    un "С Алисой?" with dissolve
    me "Ну да." with dissolve
#запятая после ну, а лучше троеточие
    "Лена, прежде беззаботно сидевшая и слушавшая наш разговор, вдруг стала серьёзной." with dissolve
    show un_rvp normal pioneer2 with dspr
    un "Ну, иди. Так о чем это мы, Жень… ах да, книги. Мне нужно…" with dissolve
    
    scene bg square_lmr_night_rvp with dissolve
    "Учитывая всё произошедшее, можно было понять, почему она так напряглась. Но прочитать её мысли я не мог." with dissolve
    show mi smile pioneer at cright with dissolve
    show dv normal pioneer at cleft with dissolve
    "Вот и наши гитаристки." with dissolve
    mi "Вот так это играется, запиши." with dissolve
    "Алиса старательно заносила ценную информацию в блокнот. Вся страница была исписана табами, строчками, аккордами, даже схемами и комментариями." with dissolve
    mi "Ой, Семён, наконец-то ты пришёл. Что хочешь послушать?" with dissolve
    me "Эм, ну…" with dissolve
    show dv angry pioneer2 at cleft with dissolve
    dv "Семён, не до тебя сейчас. Уйди куда-нибудь." with dissolve
    "Понимаю её. Интернета нет и ещё не будет лет десять, а тут такое везение – встреча с девочкой с другой стороны железного занавеса. Да что там, другой культуры!" with dissolve
    me "А, ну если мешаю…" with dissolve
    mi "Нет, не мешаешь!" with dissolve
    mi "Алис, я тебе всё описала, теперь давай попрактикуемся! Сёма, будешь слушать?" with dissolve
    me "Не откажусь. Что играете?" with dissolve
    mi "Новую песню из Японии." with dissolve
    dv "А мне его присутствие мешает. Я ещё не тренировалась, и если он будет сбивать меня, ничего не выйдет." with dissolve
    me "А ты закрой глаза и представь, что меня нет." with dissolve
    show dv grin pioneer2 at cleft with dissolve
    dv "Как я буду пальцы видеть, если глаза закрою, умник?" with dissolve
    me "Ладно, не буду мешать." with dissolve
    "Они начали играть. Мику задавала темп и играла громче, Алиса старалась подыгрывать ей в такт." with dissolve
    window hide

    #Музыкальная пауза
    $ renpy.notify("Щёлкните для продолжения")
    $ renpy.pause()
    
    #моргание глазом
    show blink
    scene bg black with dissolve
    $ renpy.pause(1.0)
    show unblink

    scene bg square_lmr_night_rvp with dissolve
    show mi smile pioneer at cright with dissolve
    show dv normal pioneer at cleft with dissolve
    window show
    dv "Сколько у нас ещё времени?" with dissolve
    mi "Около часа." with dissolve
    dv "Я бы не отказалась в картишки перекинуться напоследок, вы как?" with dissolve
    show mi smile pioneer at cright:
        align(.5,.5)
        ease 1 pos(0.5,0.5)
    show dv normal pioneer at cleft:
        align(.5,.5)
        ease 1 pos(0.7,0.5)
    show sh normal:
        anchor(0.5,0.5) pos(0.3,0.5)
    with dissolve 
    show sl normal pioneer:
        anchor(0.5,0.5) pos(0.1,0.5)
    with dissolve
    "Мы нашли ещё ребят, колоду карт и через несколько минут уже раздавали карты на чемодане."
    show un_rvp smile pioneer2:
        anchor(0.5,0.5) pos(0.9,0.5)
    "Подошла и Лена, и тоже играла с нами." with dissolve
    "Время прошло очень весело, беззаботно и приятно." with dissolve
    "Всё закончено. Песни сыграны, адреса записаны, слёзы выплаканы. Я просто играл в карты с ребятами, шутил свои шутки и смеялся с чужих." with dissolve
    "И чувствовал себя счастливым." with dissolve
    "Но всё хорошее когда-нибудь заканчивается." with dissolve
    mt "Ребята, собираемся! Поезд подходит к платформе!" with dissolve
    "Мы дошли с ребятами до платформы, помогли девочкам донести вещи. Видел, как Электроник старался для Жени." with dissolve
    window hide
    stop music fadeout 1

    scene bg black with dissolve
    $ renpy.pause(1.0)
    play sound wagon_rvp fadein 1
    window show
    "Поезд тронулся и поехал."
    "Уезжали по разным концам Союза, даже мира, ставшие дорогими мне меньше чем за одну неделю ребята. И встретимся ли мы когда-то ещё?" with dissolve
    "Одно точно можно было сказать – они оставили след в моём сердце. И воспоминания на всю жизнь." with dissolve
    "Но не все меня покинули." with dissolve
    window hide

    scene bg perron_rvp with dissolve
    show dv normal pioneer2:
        anchor(0.5,0.5) pos (0.3,0.5)
    with dissolve
    show un_rvp normal pioneer2:
        anchor(0.5,0.5) pos (0.7,0.5)
    with dissolve
    window show
    "Остались… Алиса и Лена." with dissolve
    "Честно говоря, даже страшно немного. Как бы всё не закончилось, как вчера." with dissolve
    window hide

    window show
    dv "Ну что, Лен, пойдём." with dissolve
    show dv surprise pioneer2:
        anchor(0.5,0.5) pos (0.3,0.5)
    with dissolve
    dv "А ты чего тут стоишь? Почему с ребятами не поехал?" with dissolve
    un "У него сложная ситуация. Ему надо тут остаться." with dissolve
    me "А вы куда сейчас?" with dissolve
    un "К себе домой." with dissolve
    me "Пойдем, провожу тебя." with dissolve
    show un_rvp smile pioneer2:
        anchor(0.5,0.5) pos (0.7,0.5)
    with dissolve
    un "Давай!" with dissolve
    show dv normal pioneer2:
        anchor(0.5,0.5) pos (0.3,0.5)
    with dissolve
    dv "Ладно, пойдём, проводишь нас, время позднее уже." with dissolve
    stop sound fadeout 2
    play ambience ambience_camp_center_night
    scene bg square_lmr_night_rvp with dissolve
    window show
    "Мы вышли с перрона на площадь." with dissolve
    show dv normal pioneer2:
        anchor(0.5,0.5) pos (0.3,0.5)
    with dissolve
    show un_rvp smile3 pioneer2:
        anchor(0.5,0.5) pos (0.7,0.5)
    with dissolve
    "Лена радостно заговорила со мной." with dissolve
    un "Ну что, Сёма, как тебе город?" with dissolve
    me "Да ничего, мне нравится." with dissolve
    show dv scared pioneer2:
        anchor(0.5,0.5) pos (0.3,0.5)
    with dissolve
    "Я успел заметить, что Алиса напряглась." with dissolve
    dv "Стойте, мне надо отойти кое-куда. Лена, пойдём со мной." with dissolve
    show un_rvp normal pioneer2:
        anchor(0.5,0.5) pos (0.7,0.5)
    with dissolve
    un "Ох, ну ладно. Подожди нас здесь, мы скоро." with dissolve
    window hide
    stop ambience fadeout 2

    scene bg int_vokzal_rvp with dissolve
    play music music_list["drown"]
    $ persistent.sprite_time = "day"
    $ day_time
    show un_rvp angry2 pioneer2:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    un "Алис, а до дома дотерпеть никак?" with dissolve
    window hide
    show un_rvp angry2 pioneer2:
        ease 1 pos(-0.3,0.5)
    show dv scared pioneer2:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    dv "Лен, надо поговорить." with dissolve
    dv "Слушай, ты всё-таки с ним?" with dissolve
    window hide
    show dv scared pioneer2:
        ease 1 pos(-0.3,0.5)
    show un_rvp angry2 pioneer2:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    un "Да, Алиса, и не нужно больше вмешиваться!" with dissolve
    window hide
    show un_rvp angry2 pioneer2:
        ease 1 pos(-0.3,0.5)
    show dv angry pioneer2:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    dv "Лена, ну как же ты не понимаешь, не с тем ты связалась! Я тебе говорила об этом ещё в походе, но ты мне не веришь." with dissolve
    window hide
    show dv angry pioneer2:
        ease 1 pos(-0.3,0.5)
    show un_rvp angry pioneer2:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    un "Да, Алиса, я тебе не поверила и не верю сейчас. Ты просто хочешь разрушить наши отношения." with dissolve
    window hide
    show un_rvp angry pioneer2:
        ease 1 pos(-0.3,0.5)
    show dv guilty pioneer2:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    dv "Лена, я лишь хотела предупредить тебя." with dissolve
    dv "Ты так уверена в нём? Я же правду говорю, он за мной подглядывал." with dissolve
    window hide
    show dv guilty pioneer2:
        ease 1 pos(-0.3,0.5)
    show un_rvp angry2 pioneer2:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    un "Знаю я твои штучки. Наверняка ты его шантажировала." with dissolve
    window hide
    show un_rvp angry2 pioneer2:
        ease 1 pos(-0.3,0.5)
    show dv scared pioneer2:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    dv "Лена, ты не понимаешь, это другое." with dissolve
    window hide
    show dv scared pioneer2:
        ease 1 pos(-0.3,0.5)
    show un_rvp laugh pioneer2:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    un "Ладно, давай спросим у него прямо. Я думаю, он не будет отпираться и скажет правду." with dissolve
    window hide
    stop music fadeout 2

    scene bg square_lmr_night_rvp:
        align(.5,.5)
        ease 1 zoom 1.05
    with dissolve
    play ambience ambience_camp_center_night
    window show
    $ persistent.sprite_time = "night"
    $ night_time
    show dv normal pioneer2 far:
        anchor(0.5,0.5) pos(0.3,0.5)
    with dissolve
    show un_rvp angry2 pioneer2 far:
        anchor(0.5,0.5) pos(0.7,0.5)
    with dissolve
    "Спустя несколько минут девочки вернулись, но их лица были серьёзными." with dissolve
    play music music_list["sunny_day"] fadein 2
    un "Семён, есть разговор." with dissolve
    show un_rvp angry2 pioneer2 with dissolve
    un "Ты, правда, подглядывал за Алисой?" with dissolve
    "Да вы серьёзно, опять это. Один мой легкомысленный поступок, а столько последствий." with dissolve
    "И ведь целых два дня уже эта канитель длится. Впрочем, я сам смалодушничал и соврал Лене тогда в лесу. Нужно исправить ошибку." with dissolve
    "Теперь остаётся только сказать правду. Я не могу строить отношения на лжи, скрывая что-то от неё." with dissolve
    "Я тяжело вздохнул." with dissolve
    me "Да, Лена, это правда." with dissolve
    show un_rvp ubiu pioneer2:
        align(.5,.5) zoom 1.25
    with dissolve
    play sound sfx_face_slap
    $ renpy.pause(0.5)
    with hpunch
    show dv shocked pioneer2 far:
        anchor(0.5,0.5) pos(0.3,0.5)
    "Взмах руки Лены. Секунда. Чёткий удар ладонью прямо по щеке. Заслуженно." with dissolve
    show un_rvp rage pioneer2 close with dissolve
    un "Ну почему, Сёма, почему?!" with dissolve
    show un_rvp ubiu pioneer2:
        align(.5,.5) zoom 1.25
    with dissolve
    me "Потому что был легкомысленен. Потому что не понимал, что мне нужна только ты." with dissolve
    me "Прости меня, если сможешь." with dissolve
    show un_rvp angry2 pioneer2 close with dissolve
    "Лена сверлила меня взглядом и молчала." with dissolve
    show un_rvp normal pioneer2 with dissolve
    un "Всё ясно с тобой. Пойдём, проводишь нас, а то время позднее." with dissolve
    show un_rvp normal pioneer2:
        ease 1 pos(-0.3,0.5)
    with dissolve
    scene bg square_lmr_night_rvp with dissolve
    show un_rvp normal pioneer2 at left
    show pi normal at right
    "Черт возьми, а он всё-таки признался. Я думала, будет до последнего отрицать. И что теперь? Ленка в слезах, он тоже понурый идёт." with dissolve
    "Да, я вроде как поступила правильно. Я предупредила её. Я не хотела, чтобы он ей изменял, а она потом лила слёзы." with dissolve
    "В порыве справедливого гнева я хотела, чтобы он получил по заслугам. Ну получил, и что дальше с этого?" with dissolve
    "Всё же я что-то не так сделала. Может, он и вправду полюбил её уже после." with dissolve
    "Надо с ним поговорить. Проверить, искренен ли он." with dissolve
    scene bg street_lmr_night_rvp:
        parallel:
            zoom 1.05 anchor (48,27)
        parallel:
            ease 0.50 pos (0, 0)
            ease 0.50 pos (25,25)
            ease 0.50 pos (0, 0)
            ease 0.50 pos (-25,25)
        repeat
    show dv shy pioneer2 far at left:
        parallel:
            zoom 1.05 anchor (48,27)
        parallel:
            ease 0.50 pos (0, 0)
            ease 0.50 pos (0,15)
        repeat
#подумать над ходьбой
    "Мы шли вдвоём, Лена в нескольких метрах позади нас. Было слышно, как она иногда всхлипывала." with dissolve
    "Ситуация просто хуже некуда. Один в незнакомом городе, без средств, в другом времени." with dissolve
    "Опозорился перед единственным человеком, которому я дорог. И который бесконечно дорог мне." with dissolve
    "К глазам подступали слёзы, внутри всё сжалось в комок." with dissolve
    show dv guilty pioneer2 with dissolve
    "Вдруг со мной заговорила Алиса." with dissolve
    dv "Знаешь, Семён. Ты молодец, что признался." with dissolve
    me "Алиса, чего тебе надо?" with dissolve
    dv "Скажи, пожалуйста, так же честно – ты любишь Лену?" with dissolve
    me "Да." with dissolve
    show dv angry pioneer2 with dspr
    dv "Тогда зачем подглядывал за мной?" with dissolve
    me "Говорю же, бес попутал. Пошёл утром мыться, услышал вас, испугался, запрыгнул в кусты." with dissolve
    me "Потом вся эта круговерть с походом и вами. После этого я уже понял, что мне не нужен никто, кроме Лены." with dissolve
    show dv guilty pioneer2 with dspr
    dv "Знаешь… а я тебе верю." with dissolve
    me "Алиса, зачем ты вообще про это решила вспомнить?" with dissolve
    dv "Пойми, мне нет смысла делать больно тебе или Лене." with dissolve
    dv "Но Лена моя лучшая подруга, я не могу позволить, чтобы с ней был человек, который будет засматриваться на других девушек." with dissolve
    dv "Вот я и сказала ей об этом." with dissolve
    dv "Но всё-таки ты не такой, как я о тебе думала. Ты конечно дурак, но всё-таки не подлец." with dissolve
    "Подруги, ничего себе." with dissolve
    me "Твоя лучшая подруга тебе апперкот прописала в челюсть вчера." with dissolve
    dv "До сих пор больно. Это неправильно с её стороны, и я, конечно, в обиде на неё." with dissolve
    dv "Но я знаю Лену уже давно. Она очень хорошая, просто её лучше не злить." with dissolve
    me "Ты меня извини, Алис. Но, по-моему, тогда, на костре, всё это выглядело, как будто ты нас рассорить хотела." with dissolve
    dv "Возможно, я не совсем правильно сказала, что хотела." with dissolve
    dv "Но кто тебе сказал, где искать Лену?" with dissolve
    "А ведь действительно. Получается, Алиса в тот момент пыталась помочь." with dissolve
    dv "Сейчас её лучше не трогать, потом спокойно поговорите. Сейчас до дома дойдём." with dissolve
    stop music fadeout 2
    "Вдруг Лена ускорила шаг и сама подошла к нам." with dissolve
    un "Ребят, стойте." with dissolve
    play music music_list["waltz_of_doubts"] fadein 2
    scene cg un_dv_rvp with dissolve
    "Мы остановились в круге света под фонарём." with dissolve
    un "Я тут подумала. В общем… каждый из нас в этой ситуации в чём-то виноват." with dissolve
    un "Алиса, прости, что вчера ударила тебя и не верила до этого момента." with dissolve
    dv "Хорошо, Лен." with dissolve
    dv "Да и как бы ты меня не била, другой подруги у меня нет." with dissolve

    scene cg un_dv_2_rvp with dissolve
    un "Что же до тебя, Семён…" with dissolve
    "Лена тяжело вздохнула. Я снова почувствовал на себе её взгляд." with dissolve
    un "Ты совершил глупость, но ты хотя бы признался." with dissolve
    un "Мы все иногда совершаем ошибки." with dissolve
    un "Ты, конечно, меня очень расстроил… Но так уж и быть, прощу тебя. На первый раз." with dissolve
    me "Спасибо!" with dissolve
    un "Но знай, если будешь вести себя как кобель, не удивляйся, что я стану сукой." with dissolve
    me "Я тебя понял, Лена." with dissolve

    scene cg sproot_rvp with dissolve
    "Лена улыбнулась нам." with dissolve
    un "Ладно, это всё позади. На самом деле, я вас так люблю!" with dissolve
    dv "И я тебя тоже, Лена." with dissolve
    me "И я." with dissolve
    "Мы обняли Лену. Фонарь освещал нас сверху." with dissolve
    window hide

    play ambience ambience_camp_center_evening fadein 1
    scene bg ext_internat_rvp with dissolve
    show un_rvp smile pioneer2 at left with dissolve
    show dv normal pioneer2 at right with dissolve
    "Через пару минут мы подошли к какому-то жилому зданию." with dissolve
    un "Вот и пришли." with dissolve
    show un_rvp shy pioneer2 with dspr
    un "Ой, а где тебе ночевать? Алис, ему переночевать надо, может, проведём его?" with dissolve 
    me "А вы… вместе живёте?"
    show dv guilty pioneer2 with dspr
    dv "Нет, Лен, не позволят. У нас сейчас жёстко с этим. Надо переночевать – пусть идёт на вокзал. Тут по улице прямо как сейчас шли, и до площади." with dissolve
    "На двери была табличка, но за Леной я не смог увидеть, что там написано." with dissolve
    un "Да, вот ещё." with dissolve
    "Вдруг Лена открыла сумку и достала какой-то кулёк." with dissolve
    un "Вот, возьми на еду, завтра столовая откроется." with dissolve
    show dv shy pioneer2 with dspr
    dv "Лена, мы вообще-то с тобой эти деньги откладывали..." with dissolve
    show un_rvp normal pioneer2 with dissolve
    un "Алиса, ему сейчас нужнее." with dissolve
    show dv sad pioneer2 with dissolve
    "Алиса не стала возражать, но была недовольна этим решением Лены. Я взял деньги и положил в пакет с вещами." with dissolve
    show un_rvp smile3 pioneer2 close with dspr
    un "Ладно, Сём, завтра увидимся тогда." with dissolve
    window hide
    show un_rvp grin pioneer2 close:
        anchor(0.5,0.5) pos(0.3,0.5)
        ease 2 zoom 1.5
    show un_rvp grin pioneer2 close:
        anchor(0.5,0.5) pos(0.3,0.5) zoom 1.5
        ease 1 zoom 1.0
    window show
    "Она поцеловала меня в ту самую щёку, по которой ударила." with dissolve

    scene bg street_lmr_night_rvp with dissolve
    $ set_mode_nvl()
    play music larek_rvp fadein 2
    window show
    nvl clear
    "Я пошёл обратно. События давали пищу для размышлений." with dissolve
    "Неужели Лена с Алисой действительно дружат? Они же полные противоположности друг другу. Одна дерзкая, но пугается, если на неё надавить." with dissolve
    "Другая стеснительная, но в экстремальных ситуациях сохраняет спокойствие." with dissolve
    "Да и не видел я их вместе. Наоборот, они вроде враждовали." with dissolve
    "Где живут Лена с Алисой? Непохоже на обычную панельку, скорее на общагу. Но было что-то от школы." with dissolve
    "Они живут в одном доме. Видимо, так и познакомились." with dissolve
    "У них есть родители. Значит, мне ещё предстоит знакомство с мамой и папой Лены. Мда, чувствую, что скандала не избежать – дочь полюбила странного подростка, появившегося из ниоткуда." with dissolve
    "Да и не подростка, на самом деле…" with dissolve
    "Я шёл по улице быстрым шагом и думал об этом всём. Редкие прохожие встречались мне." with dissolve
    window hide
    $ set_mode_adv()
    $ renpy.pause(1.0)
    scene bg square_lmr_night_rvp with dissolve
    window show
    "Вот и площадь. Пройдя её, добрался до вокзала." with dissolve
    stop ambience fadeout 1
    scene bg int_vokzal_rvp with dissolve
    "Зашёл в зал ожидания. Ничего необычного, помещение с типичной советской плиткой и мозаикой соцреализма на стене." with dissolve
    window hide
    
    show blink
    scene bg black
    "Я сел на лавочку и закрыл глаза." with dissolve
    $ set_mode_nvl()
    window show
    nvl clear
    "Только сейчас я почувствовал, как сильно я устал. День был слишком насыщенный и контрастный. Заснуть мешало чувство голода, сегодня я поел лишь печенья." with dissolve
    "Зато с кем…" with dissolve
    "Спать не хотелось, нужно было выстроить план на будущее." with dissolve
    "Подведём итоги. Из лагеря я всё-таки выбрался. Это действительно прошлое, поздний Советский Союз, провинция. Панельки, серость, дефицит. Перестройка, а потом девяностые." with dissolve
    "Ладно, до них ещё дожить надо." with dissolve
    "Гораздо важнее то, что здесь и сейчас. Мне надо что-то поесть. Коммунизм тут, наверное, также не построили, а значит, нужны деньги. Конечно, нужны, Лена же мне их дала." with dissolve
    "Всё же Лена опрометчиво поступила, что так сразу отдала их с Алисой “общак”. Неужели она так меня любит сильно, что готова отдать всё, чтобы я хорошо себя чувствовал?" with dissolve
    "Надо обязательно вернуть эти деньги, хотя бы Алисе её долю, а то она расстроилась. Однако мне на что-то тут тоже жить надо, нужны деньги на первое время." with dissolve
    "Значит, нужно работать, чтобы эти деньги получить." with dissolve
    "Чтобы взяли на работу, нужны документы." with dissolve
    "Со мной были вещи, в которых я сел в четыреста десятый автобус в тот судьбоносный вечер. Джинсы, рубашка, пальто. Я накрылся пальто, как одеялом." with dissolve
    "А джинсы, наверное, здесь будут последним писком моды." with dissolve
    nvl clear
    window hide

    $ set_mode_adv()
    window show
    "В конце концов, от всех этих размышлений я задремал." with dissolve
    stop music fadeout 2
    window hide
    $renpy.pause(1.0)
    $ persistent.sprite_time = "sunset"
    $ sunset_time
    play music music_list["glimmering_coals"] fadein 3 
    scene bg ext_washstand_day with dissolve
    "Семён, сверкая пятками и не только ими, удалялся от умывальников. Догонять его в лесу не было смысла." with dissolve
    th "Вот ведь кобель! Ведь уже какой день он с Ленкой шашни крутит, а сам!" with dissolve
    th "Нет, он у меня не отделается так просто! Я всё расскажу Лене! Пусть знает, какой он на самом деле!" with dissolve
    window hide

    scene bg ext_polyana_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 1
    window show
    show dv guilty pioneer:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    dv "Лена, надо поговорить." with dissolve
    window hide
    show dv guilty pioneer:
        ease 1 pos(-0.3,0.5)
    show un shy pioneer:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    un "Ой, а что такое? Ты такая серьёзная." with dissolve
    window hide
    show un shy pioneer:
        ease 1 pos(-0.3,0.5)
    show dv guilty pioneer:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    dv "Мне нужно кое-что рассказать тебе про Семёна." with dissolve
    window hide
    show dv guilty pioneer:
        ease 1 pos(-0.3,0.5)
    show un angry2 pioneer:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    un "Да? Ну и что же такое ты хочешь мне сказать?" with dissolve
    window hide
    show un angry2 pioneer:
        ease 1 pos(-0.3,0.5)
    show dv guilty pioneer:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    dv "Лена, он не такой хороший, как ты думаешь." with dissolve
    window hide
    show dv guilty pioneer:
        ease 1 pos(-0.3,0.5)
    show un angry2 pioneer:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    un "Если честно, не хочу от тебя ничего слушать." with dissolve
    window hide
    show un angry2 pioneer:
        ease 1 pos(-0.3,0.5)
    show dv angry pioneer:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    dv "Ну Лена, я сейчас хочу тебе сказать правду." with dissolve
    window hide
    show dv angry pioneer:
        ease 1 pos(-0.3,0.5)
    show un angry pioneer:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    un "Послушай, Алиса!" with dissolve
    window hide
    show un angry pioneer:
        ease 1 pos(-0.3,0.5)
    show dv angry pioneer:
        anchor(0.5,0.5) pos (1.3,0.5)
        ease 1 pos(0.5,0.5)
    window show
    dv "Нет, это ты меня послушай!" with dissolve
    window hide
    stop music fadeout 2
    stop ambience fadeout 1

    scene black with dissolve
    play music bomzh_rvp fadein 1
    window show
    voice "Просыпаемся, молодой человек."
    show unblink
    scene bg int_vokzal_rvp
    show mil_rvp at cleft with dissolve
    show mil2_rvp at cright with dissolve
    "Я открыл глаза. Этого ещё не хватало. Передо мной стоял патруль местной милиции." with dissolve
    mil "Так, кто тут у нас? Пионер, несовершеннолетний. Парень, ты что тут делаешь?" with dissolve
    me "Да мне переночевать надо." with dissolve
    mil2 "Все дома ночуют, а не здесь. Детям ночью на вокзале не место." with dissolve
    "Ага, тоже мне ребёнка нашли." with dissolve
    mil "На местного ты не похож, первый раз тебя вижу здесь." with dissolve
    mil2 "Пойдём с нами, пионер. Будем выяснять, кто ты и откуда."
    window hide
    
    scene bg lenie_rvp with dissolve
    show mil_rvp at cleft with dissolve
    show mil2_rvp at cright with dissolve
    window show
    "Дальше началось неприятное."
    mil "Фамилия, имя, отчество."
    me "Персунов Семён Николаевич."
    mil "Год рождения."
    "Я назвал свой год рождения. Он совпадал с текущим."
    mil "Издеваешься? Тебя спрашивают не какой год сейчас, а в каком году родился."
    me "Я в этом году и родился."
    mil "Ты у меня сейчас за такие шутки на пятнадцать суток пойдёшь сразу. Что у него там в вещах?"
    mil2 "Я вообще не понял: почти ничего нет, какая-то коробка с кнопками и паспорт, причем не наш. А вот ещё деньги."
    mil "Сколько тут? Значит, при досмотре найдены деньги двадцать два рубля, паспорт серия-номер. Дай-ка сюда, надо записать." with dissolve
    mil "Не понял, что за страна такая, СССР же у нас. Выдан… когда??? Это что за шутки, Персунов?" with dissolve
    "И что делать? Притвориться человеком из их времени не получилось, паспорт выдал меня с головой. Красиво врать я не умею. Милиционеры люди опытные, раскусят меня." with dissolve
    me "Мужики, ну как бы объяснить… я из будущего." with dissolve
    mil "Чего? Слышь ты, Алиса Селезнёва, кончай бред нести." with dissolve
    "Я рассказал милиционерам, как было. А что делать?" with dissolve #фразы не хватает
    window hide
    stop music fadeout 1
        
    scene bg lenie_rvp with dissolve
    play music music_list["drown"] fadein 2
    $ set_mode_nvl()
    window show
    nvl clear
    "Какое-то время я просидел в КПЗ, затем пришёл начальник отделения с каким-то офицером. Меня повезли в областное управление КГБ." with dissolve
    "Там меня сфотографировали, сняли отпечатки пальцев и долго допрашивали. Я им рассказал всю историю моей жизни, историю своего мира, которую помнил." with dissolve
    "И, конечно же, неделю в лагере." with dissolve
    "Из-за паспорта несуществующего в их мире государства и моих показаний, меня подозревали в том, что я засланный диверсант, который должен убеждать людей, что СССР скоро развалится." with dissolve
    "Вот ведь бред, специально подготовить человека, чтобы он такой ерундой занимался. Но им это казалось единственным разумным объяснением." with dissolve
    "Да и телефон выглядел как шпионское устройство для связи с руководством." with dissolve
    "Неужели всё закончится вот так? Меня отправят в тюрьму, а Лена с ума сойдёт от своего горя.…" with dissolve 
    "Прости меня, Лена. Я снова ошибся и наше счастье снова рушится." with dissolve
    "Казалось, что судьба моя была предрешена, как вдруг…" with dissolve
    window hide
    $ set_mode_adv()
    
    scene bg kgb_rvp with dissolve
    show genda_rvp with dissolve
    window show
    play sound sfx_carousel_squeak
    "В мою камеру зашёл мужчина. Его лицо показалось мне знакомым." with dissolve
    muj "Семён Персунов?" with dissolve
    me "Да. А вы кто?" with dissolve
    muj "Меня тут все знают. Если ты был в Совёнке, то мог меня видеть." with dissolve
    "И тут я вспомнил. Тот самый бронзовый человек в центре лагеря." with dissolve
    me "Погодите, вы – тот самый Генда?" with dissolve
    gn "Да. У нас мало времени, поэтому сразу перейдём к делу. Ты говоришь, что приехал на автобусе неделю назад из будущего, верно?" with dissolve
    me "Говорил, но мне никто не верит." with dissolve
    gn "Я верю." with dissolve
    "Я был в шоке." with dissolve
    me "Как? Вы знаете, как это произошло? Как это могло быть? Кто это устроил?" with dissolve
    gn "Не знаю. Из надёжного источника мы лишь знали, что это произойдёт." with dissolve
    gn "Больше я тебе ничего не смогу сказать." with dissolve
    "Я понял, что вновь не дождусь ответов." with dissolve
    gn "Ты вчера вечером приехал в Лениноморск. У тебя там никого нет?" with dissolve
    me "Разве что Лена." with dissolve
    gn "Какая Лена?" with dissolve
    me "Мы познакомились с ней в Совёнке. Ну, такая с фиолетовыми волосами, глаза зелёные ещё." with dissolve
    "Черт возьми, я ведь даже её фамилию не знаю." with dissolve
    gn "Я, кажется, понял о ком ты. Ты бы хотел с ней снова встретиться?" with dissolve
    me "Да, я люблю её, а она меня." with dissolve
    "И с чего я так откровенничаю с ним? Он вроде не настроен против меня, но явно знает больше моего. Лицо Генды не выражало никаких эмоций." with dissolve
    gn "Что ж, время нашего общения подошло к концу. Я постараюсь помочь тебе. До встречи." with dissolve
    me "Извините, можно?" with dissolve
    gn "Что?" with dissolve
    me "Попросить кое о чём. У меня в вещах деньги были, двадцать два рубля. Как-то можно проконтролировать, чтобы они не пропали и мне их вернули?" with dissolve
    me "Или пусть Лене отправят. Это все её сбережения, она мне их отдала, чтобы были деньги на первое время." with dissolve
    gn "Хорошо, проконтролирую." with dissolve
    me "Спасибо, товарищ Генда!" with dissolve
    show genda_rvp:
        align(.5,.5)
        ease 1 pos(1.,.5) alpha 0
    play sound sfx_metal_door_large_close_basement
    "Он вышел из камеры. Генда произвёл на меня впечатление местного босса. Он что-то хочет от меня? Я буду пешкой в его игре?" with dissolve
    "Повлияет ли моё откровение на Лену? Могут ли у неё начаться проблемы?" with dissolve
    "В моей ситуации остаётся только ждать." with dissolve
    "Спустя несколько часов ко мне снова пришли." with dissolve
    voice "Персунов, на выход!"
    window hide

    $ set_mode_nvl()
    window show
    nvl clear
    play sound sfx_carousel_squeak
    "Меня выпустили из камеры и повели по коридору в допросную. Я уже не знал, что им ещё рассказать, но они не стали меня допрашивать." with dissolve
    "Мне объявили, что у них нет ко мне вопросов, и они освобождают меня. А если вопросы появятся, со мной свяжутся." with dissolve
    "Мне вернули все мои вещи, запаковав их в вещмешок, отдельно вручили те самые деньги и повезли обратно в Лениноморск." with dissolve
    "Во время дороги два сотрудника КГБ разговорились." with dissolve
    sot "Слушай, а как там Ирина?" with dissolve
    sot2 "Какая Ирина?" with dissolve
    sot "Ну, которая с тобой училась." with dissolve
    sot2 "А, вспомнил. А что, она за границей сейчас, в одной капстране. Больше ничего не знаю." with dissolve
    sot "Эх, завидую ей даже. Не то, что я сижу тут, тухну. Никакой интересной жизни." with dissolve
    "Странно, что они при мне это рассказывают. Впрочем, что мне эта информация даёт? Да и они видимо поняли, что не шпион я никакой." with dissolve
    window hide
    $ set_mode_adv()
    stop music fadeout 1 

    $ persistent.sprite_time="day"
    $ day_time
    scene bg square_lmr_day_rvp with dissolve 
    play ambience ambience_camp_center_day fadein 1
    window show
    "Через час меня высадили на той же самой площади, куда я приехал из лагеря." with dissolve
    "В городе наступило утро. Люди шли по своим делам, на работу. Один я стоял и не понимал, что мне делать." with dissolve
    "За спиной у меня был вещмешок со всем моим скромным инвентарём. Ну, я хотя бы здесь уже был." with dissolve
    "Надо найти Лену. Я обернулся в сторону и вдруг увидел её. Она сидела и читала книгу на лавочке. Как знакомо." with dissolve
    "Я пошёл к ней. Она увидела меня, вскочила и побежала." with dissolve
#сделать Лене футболку с юбкой
    show un_rvp sad pioneer2 far at left with dissolve
    un "Сёма, привет!" with dissolve
    show un_rvp sad pioneer2 at cleft with dissolve
    un "Куда ты пропал? Я тебя вчера весь день ждала! Я так волновалась." with dissolve
    me "Лен, такое случилось. Просто чудо какое-то, что я снова с тобой." with dissolve
    me "Я в милиции был." with dissolve
    show un_rvp scared pioneer2 close at cleft with dissolve
    un "Какой ужас! Тебя били? С тобой сейчас всё в порядке?" with dissolve
    show un_rvp sad pioneer2 close at cleft with dissolve
    un "Пойдём, расскажешь нам с Алисой." with dissolve
    scene bg square_lmr_day_rvp with dissolve
    "Пока мы с Леной дошли до их дома, я рассказал, что произошло. Как меня задержала милиция, как допрашивали, как меня посетил Генда." with dissolve
    window hide
    
    scene bg ext_internat_rvp with dissolve
    show un_rvp smile pioneer2 at left with dissolve
    window show
    un "Подожди здесь, я сейчас." with dissolve
    show un_rvp smile pioneer2:
        anchor(.5,.5) pos(.3,.5)
        ease 1 pos(.8,.5) alpha 0
    "Лена скрылась за дверью."
    "Я остался ждать."
    scene bg ext_internat_rvp:
        align(.5,.5)
        ease 3 zoom 3 align(.9,.9)
    "Вскоре я начал смотреть на место её жительства. Не похоже на обычный дом, ограждено забором."
    "Наконец, я прочитал название на табличке." with dissolve
    "МИНИСТЕРСТВО ПРОСВЕЩЕНИЯ СССР" with dissolve
    "ОТДЕЛ НАРОДНОГО ОБРАЗОВАНИЯ" with dissolve
    "ИСПОЛКОМА ЛЕНИНОМОРСКОГО РАЙОННОГО СОВЕТА ДЕПУТАТОВ" with dissolve 
    "ШКОЛА-ИНТЕРНАТ №2" with dissolve
    "Что такое интернат? Это там, где дети и учатся и живут? Почему Лена и Алиса живут здесь, а не с родителями?" with dissolve
    scene bg ext_internat_rvp:
        align(.9,.9) zoom 3
        ease 3 zoom 1 align(.5,.5)
    "Мне пришлось прервать свои размышления, так как пришла Алиса."
    play music music_list["that_s_our_madhouse"]
    show dv angry pioneer2 far with dissolve
    "Лицо её не было приветливым." with dissolve
    dv "Опять ты пришёл!" with dissolve
    "Что за перемена с ней произошла?" with dissolve
    show dv angry pioneer2 with dissolve
    dv "Ты что творишь? Я думала, ты нормальный парень, а ты…" with dissolve
    dv "Что за лапшу ты Ленке на уши навешал! Какое ещё попадание из будущего?!" with dissolve
    me "Алис, я правда…" with dissolve 
    dv "Ты чё, Булычёва обчитался?!" with dissolve
    dv "Ведь ещё как убедительно напел ей про это! Лена умная девочка, а ты смог ей такую чушь внушить!" with dissolve
    dv "Со мной такое не пройдёт. Я в такие сказки не верю." with dissolve
    me "А вот следует поверить…" with dissolve
    dv "Он ещё мне тут указывать будет!" with dissolve
    dv "Ты лучше скажи, где пропадал вчера весь день! И где деньги, которые тебе Лена отдала?" with dissolve
    show dv rage pioneer2 with dissolve
    dv "Пропил, да?! Гулял на наши деньги?! Ах ты скоти…" with dissolve
    show dv rage pioneer2 close with dissolve
    "Алиса замахнулась рукой для удара, но я успел схватить её." with dissolve
    show dv angry pioneer2 close with dissolve
    dv "Эй, отпусти!" with dissolve 
    show un_rvp shy pioneer2 at left with dissolve
    "В этот момент вернулась Лена. Алиса её не заметила." with dissolve
    dv "У тебя ничего не получится! Ты не уведёшь у меня подругу!" with dissolve
    un "Алис, ты чего?" with dissolve
#добавить эмоцию из 2 копейки
    show dv surprise pioneer2 close with dissolve
    "Лена снова подкралась бесшумно и напугала Алису." with dissolve
    dv "Лена! А я тут… Вот с ним разбираюсь!" with dissolve
    show un_rvp angry pioneer2 at left with dissolve
    un "Алиса, отстань от Сёмы! Он в милиции весь день провёл, намучался!" with dissolve
    show dv angry pioneer2 close with dissolve
    dv "Так ему и надо! Небось нажрался и его забрали!" with dissolve
    show un_rvp angry pioneer2 at left with dissolve
    un "Хватит на него наговаривать!" with dissolve
    me "Вот твои деньги!" with dissolve 
    show un_rvp normal pioneer2 at left with dissolve
    show dv angry pioneer2 close with dissolve
    "Я достал и вложил Алисе в руку, которую держал." with dissolve 
    me "И ерунду всякую про меня придумывать не надо!" with dissolve 
    un "Ребят, хватит ссориться! Алиса, никто меня у тебя не уводит!" with dissolve
    dv "А что он за ерунду он тебе нёс про то, что в Совёнок из будущего попал!" with dissolve
    un "Не хочешь – не верь. Я верю. Всё, пойдемте, позавтракаем." with dissolve
    window hide
    stop ambience fadeout 1
    stop music fadeout 1

    scene int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_full fadein 1
    show un_rvp smile pioneer2 at left with dissolve
    show dv normal pioneer2 at right with dissolve
    window show
    "Мы пошли в столовую. Там я снова рассказал, через что мне пришлось пройти с нашей прошлой встречи." with dissolve
    dv "Ничего себе тебе внимание оказали, сам Генда приходил." with dissolve
    me "А кто это?" with dissolve
    show dv laugh pioneer2 at right with dissolve
    dv "Герой Донбасса и Кузбасса…" with dissolve
    "Пошутила Алиса." with dissolve
    show un_rvp smile3 pioneer2 at left with dissolve
    un "Первый секретарь нашего обкома. Уроженец нашего города и настоящий коммунист! Мой папа с ним работал." with dissolve
    "Надо бы про родителей спросить." with dissolve
    me "Можно вопрос?" with dissolve
    un "Да, конечно." with dissolve
    me "А вы тут без родителей живёте, где они?" with dissolve
    show un_rvp normal pioneer2 at left with dspr
    show dv angry pioneer2 at right with dspr
    "Девочкам не понравился мой вопрос." with dissolve
    dv "Не твоё дело." with dissolve
    "А затем добавила с иронией." with dissolve
    show dv grin pioneer2 at right with dspr
    dv "Скажем так, они устали от нас и решили уехать. Но мы тут и без них справляемся." with dissolve
    "Лена ничего не ответила, лишь нахмурилась. И решила резко сменить тему." with dissolve
    un "Слушай, а я вспомнила, почему захотела тебя ударить." with dissolve
    show dv surprise pioneer2 at right with dspr
    dv "И почему же?" with dissolve
    show un_rvp angry pioneer2 at left with dspr
    un "Да ты булки лопала!" with dissolve
    "Неожиданное заявление. Действительно, Алиса тогда жевала булочку. Но бить-то зачем?" with dissolve
    un "Алис, ты мне мозги вынесла на тему, как бы не потолстеть. Я решила поддержать тебя, сама терпела и не ела, а ты!" with dissolve
    me "Но это же не повод бить её!" with dissolve
    show un_rvp grin pioneer2 at left with dspr
    "Лена ласково улыбнулась." with dissolve
    un "Да, не повод! Просто кое-кто мне все нервы поднял, и это стало спусковым крючком." with dissolve
    show un_rvp normal pioneer2 at left with dspr
    "Лена призадумалась." with dissolve
    show un_rvp sad pioneer2 at left with dspr
    un "Но вообще я неправильно поступила. Не злитесь на меня, пожалуйста, я так больше не буду." with dissolve
    me "Я-то не злюсь. А вот Алиса… не знаю." with dissolve
    show dv guilty pioneer2 at right with dspr
    dv "Лен, я тебе всё вчера сказала. Другой подруги у меня всё равно нет." with dissolve
    "Странный ответ. Наверное, причина в другом, просто Алиса не хочет говорить." with dissolve
    "Мы доели свой завтрак, и пошли на улицу." with dissolve
    window hide
    stop ambience fadeout 1
    scene bg ext_internat_rvp with dissolve
    play ambience ambience_camp_center_day fadein 1
    show un_rvp smile pioneer2 at right with dissolve
    show dv normal pioneer2 at left with dissolve
    window show
    dv "Ну что, гость из будущего, чем займёшься теперь?" with dissolve 
    dv "Мы тебя содержать не будем, у нас у самих денег не так много!" with dissolve
    un "Тебе надо найти работу. Что ты умеешь?" with dissolve
    play music music_list["torture"] fadein 2
    "И тут на меня накатил ужас. Весь мой мозг подавал сигнал тревоги, как сознательная, так и бессознательная часть." with dissolve
    "Нигде не было опыта работы, подходящей в это время." with dissolve
    "Эникейщик? Тут нет компьютеров, с которыми я умею работать." with dissolve
    "Оператор колл-центра? В это время их тут даже не было. Не уверен, что тут даже есть АТС." with dissolve
    me "Да… особо-то и ничего." with dissolve
    show dv grin pioneer2 at left with dissolve 
    dv "Мдаа, нашла ты себе жениха, Лен, ничего не скажешь." with dissolve
    stop music fadeout 2
    un "Алис, перестань. Не волнуйся, Сёма, в нашей стране тебе не дадут с голоду помереть! На заводе, думаю, найдётся и работа, и крыша над головой." with dissolve
    un "Сегодня как раз понедельник, рабочая неделя началась!" with dissolve
    "Делать нечего, пойду на неквалифицированную физическую работу." with dissolve
    me "Пойду на завод тогда. А вы где работаете?" with dissolve
    show un_rvp laugh pioneer2 at right with dspr
    show dv laugh pioneer2 at left with dspr
    dvun "А нигде, у нас каникулы!" with dissolve
    "Сказали девочки очень радостным голосом." with dissolve
    me "Везёт же вам." with dissolve
    show un_rvp smile pioneer2 at right with dissolve
    show dv normal pioneer2 at left with dspr
    un "Да ладно, Семён. Я уверена, что у тебя всё получится!" with dissolve
    me "Ладно, где завод-то хоть?" with dissolve
    un "Как идёшь до площади, так и иди прямо по улице. Там дойдёшь до него. Сразу узнаешь, не ошибёшься." with dissolve
    scene bg ext_internat_rvp with dissolve
    "Я пошёл в указанном направлении." with dissolve
    window hide
    
    scene bg square_lmr_day_rvp with dissolve
    $renpy.pause(1.0)

    scene bg zavod_rvp with dissolve
    window show
    play music music_list["tried_to_bring_it_back"] fadein 2
    "Спустя полчаса я действительно увидел громаду завода." with dissolve #поправил опечатку
    "Перед отделом кадров я остановился. А документы? Я открыл мешок с вещами. Там я нашёл конверт, которого раньше не было." with dissolve
    "Внутри было временное удостоверение личности. Дата рождения была странной. Число и месяц это день моего попадания в лагерь." with dissolve
    "Год рождения не мой. С другой стороны, как раз сходилось с тем, что мне примерно столько лет биологически." with dissolve
    "Хотя бы ФИО не изменили, на том спасибо." with dissolve 
    "Видимо, уполномоченные сотрудники посчитали день моего попадания моим вторым днём рождения, в этом мире. Что-то в этом есть…" with dissolve 
    "Впрочем, какая разница! Я же не верю в какие-то там гороскопы, что дата рождения влияет на судьбу." with dissolve
    "И вообще, надо дела делать!" with dissolve
    "Я постучался в дверь отдела кадров, а затем вошёл." with dissolve
    play sound sfx_knock_door7_polite
    stop ambience fadeout 1

    play ambience ambience_int_cabin_evening fadein 1
    $ set_mode_rvp(mode=nvl)
    window show
    nvl clear
    me "Здравствуйте, у вас есть работа?" with dissolve
    "На меня подняла глаза сотрудница отдела кадров бальзаковского возраста." with dissolve
    kd "Нет работы!" with dissolve
    me "Прям никакой? Ну, мне очень надо, а то с голоду помру!" with dissolve
    kd "Ладно, давай документы." with dissolve
    "Я протянул бумагу." with dissolve
    kd "И что это? Где паспорт?" with dissolve
    kd "Может быть ещё это поможет?" with dissolve
    "Я протянул бумагу с надписью “Ходатайство”." with dissolve
    "Лицо кадровика изменилось, когда она увидела, кем оно было подписано. Оказалось, товарищ Генда позаботился и о моём трудоустройстве." with dissolve
    "Нужно было лишь дописать в верхнем правом углу, что ходатайство на имя директора завода." with dissolve
    "Прошло несколько часов бюрократических мучений. Меня отправляли из одного кабинета в другой, долго выясняли, откуда у меня бумага от столь высокопоставленного партийца." with dissolve
    "Несмотря на её наличие, мною не хотели заниматься. В конце концов, меня попросили ждать в коридоре, а затем попросту забыли." with dissolve
    window hide
    $ set_mode_rvp(mode=adv)
    window show
    "Я уже отчаялся и сам пошёл на территорию завода, но на проходной меня не хотели пускать без пропуска." with dissolve
    show mh_rvp with dissolve
    "Вдруг один рабочий заинтересовался мною." with dissolve
    rb "Парень, ты чего тут стоишь?" with dissolve
    me "Да я ищу, кому помощник нужен. Мне работа нужна." with dissolve
    rb "Ну-ка, пойдём со мной." with dissolve
    "Мы пошли обратно в заводоуправление." with dissolve
    rb "Как зовут-то тебя хоть?" with dissolve
    me "Семён." with dissolve
    rb "Меня Михаил зовут. А чего на завод пришёл, решил подзаработать?" with dissolve
    me "Ага. Да я в город приехал недавно, у меня ничего вообще нет. Даже жить негде." with dissolve
    mh "Ну ты даёшь. Ладно, а что умеешь?" with dissolve
    me "А что нужно?" with dissolve
    mh "Много чего. Ладно, не можешь – научим, не хочешь – заставим. Я тут токарем работаю." with dissolve
    $renpy.pause(1.0)
    "Мы снова пришли в отдел кадров. Токарь начал за меня договариваться." with dissolve
    mh "Люд, ну мне нужен помощник. Вы меня обделили тогда." with dissolve
    scene bg zavod_rvp with dissolve
    $renpy.pause(2.0)
    "После нескольких минут словесных баталий вопрос с моим трудоустройством был решён. Заодно и выдали временный пропуск." with dissolve
    show mh_rvp with dissolve
    mh "Пошли в цех. Только бога ради, сними галстук, а то подумают, экскурсию вожу из школы." with dissolve
    me "Слушайте, тут такая незадача. Мне жить негде." with dissolve 
    mh "В смысле?" with dissolve
    me "Ну, негде." with dissolve
    mh "Ну, попробуй в общагу нашу заселиться. Даю тебе час времени, пока я на обеде." with dissolve
    "Я выпросил в отделе кадров обратно то самое ходатайство от Генды." with dissolve

    scene bg obschaga_rvp with dissolve
    "Общежитие было рядом. Комендант, посмотрев на документы и особенно на ходатайство, решила всё-таки заселить меня." with dissolve 
    "Уже скоро я получал постельное бельё." with dissolve 
    me "А куда тут одеяло вставлять?" with dissolve
    "Спросил я про пододеяльник." with dissolve
    ks "Ну как, берёшь и вот так." with dissolve
    "Кастелянша взяла и просто разорвала пододеяльник по шву. Я был поражён простотой решения…" with dissolve
    stop ambience fadeout 1
    "Я поднялся на второй этаж, нашёл комнату. Внутри никого не было. Комната в тот момент хорошо освещалась солнцем и показалась уютной." with dissolve
    "Я скинул бельё с вещами на кровать и побежал обратно на завод, там меня ждали." with dissolve
    stop music fadeout 2

    scene bg tsekh_rvp with dissolve
    play ambience ambience_clubs_inside_day fadein 1
    "Мне выдали рабочую одежду – халат и штаны. С белой рубашкой такое сочеталось, честно говоря, не очень, но выбора у меня не было." with dissolve
    show mh_rvp with dissolve
    mh "Ну вот, смотри, здесь мы работаем." with dissolve
    "Моему взору открылся просторный цех завода."
    mh "Работы много. Сегодня надо убрать мусор и разложить детали." with dissolve
    mh "Ещё надо инструменты в порядок привести. И постоянно приносить мне заготовки, я замахался ходить за ними." with dissolve
    mh "Так что вперёд и с песней!" with dissolve
    scene bg tsekh_rvp with dissolve
    "Работа шла тяжело. Михаил в довольно жёстком и приказном тоне объяснял, что и куда относить, требуя от меня запоминания его инструкций с первого раза." with dissolve
    "При этом нужно было не забывать вовремя приносить ему заготовки, которые он точил." with dissolve
    "Всю вторую половину рабочего дня от обеда до конца смены я был занят физической работой. За проходную завода я вышел ужасно уставшим." with dissolve
    "Нужно поужинать. Но денег у меня не было." with dissolve
    "Я снова пошёл к Лене." with dissolve
    window hide
    stop ambience fadeout 1

    $ persistent.sprite_time = "night"
    $ night_time
    scene bg square_lmr_night_rvp with dissolve
    play ambience ambience_camp_center_night
    window show
    "Я уже дошёл до площади, как вдруг встретил там Алису." with dissolve
    show dv normal pioneer2 with dissolve
    dv "Куда идём? Неужто снова к нам?" with dissolve
    me "К вам, куда же ещё? А ты откуда?" with dissolve
    show dv angry pioneer2 with dissolve
    dv "Не твоё дело." with dissolve
    dv "Так, ты нашёл работу? Тебя заселили куда-нибудь? Мы тебя к себе не возьмём, не думай." with dissolve
    me "Не волнуйся, на заводе нашлась работа. В общаге теперь живу." with dissolve 
    show dv surprise pioneer2:
        align(.5,.5)
        ease 6 zoom 1.25
    show bg square_lmr_night_rvp behind dv:
        align(.5,.5)
        ease 6 zoom 1.25
    "Неужели он действительно не врал? И ему негде было жить. И он как-то попал сюда…" with dissolve
    "Однако, это сильно с его стороны, он не растерялся и нашёл себя здесь. И Лена правильно сделала, что поверила ему." with dissolve
    show dv surprise pioneer2:
        align(.5,.5) zoom 1.25
        ease 1 zoom 1
    show bg square_lmr_night_rvp:
        align(.5,.5) zoom 1.25
        ease 1 zoom 1
    dv "Семён… а ты, правда, остаёшься?"
    me "Да, а куда мне деваться?" with dissolve
    show dv guilty pioneer2 with dspr
    dv "Слушай… извини тогда за то, что наехала на тебя с утра. Ну не каждый день приезжают вот так, из ниоткуда!" with dissolve
    me "Ладно, проехали. Я сам должен извиниться, что подглядывал за тобой." with dissolve
    show dv normal pioneer2 with dspr
    dv "Да ладно, забавная ситуация была. И у тебя всё равно выхода не было." with dissolve
    me "Рад, что ты это понимаешь. А что это у тебя?" with dissolve
    dv "Да в библиотеку ходила, книгу новую взяла." with dissolve
    #добавить книгу в руку Алисе
    window hide
    
    scene bg ext_internat_rvp with dissolve
    show dv normal pioneer2 with dissolve
    window show
    "Мы дошли до интерната." with dissolve
    dv "Ладно, я пойду Лене скажу, что ты пришёл." with dissolve
    show dv normal pioneer2:
        align(.5,.5)
        ease 1 pos(1.,.5) alpha 0
    "Алиса пошла за Леной." with dissolve
    "А всё-таки я не думаю, что она это затеяла только из благородных чувств. Ведь так у Алисы снова был шанс начать со мной…" with dissolve
    "Впрочем, больно я ей нужен. Смешно, однако, я воображаю, что две таких прекрасных девушки будут биться за меня, никчёмного безработного."
    "Впрочем, уже и не безработного." with dissolve
    "Через пять минут она уже пришла ко мне." with dissolve
    show un_rvp smile2 pioneer2 with dissolve
    un "Сёма, привет. Алиса сказала, что ты работу нашёл." with dissolve
    me "Да, токарь помощником взял. Комнату в общежитии дали." with dissolve
    me "Слушай, есть что поесть? Я не обедал сегодня." with dissolve
    un "Ой, пойдем, поужинаем." with dissolve
    window hide
    stop ambience fadeout 1

    scene bg int_dining_hall_night with dissolve
    play ambience ambience_dining_hall_empty fadein 1
    show un_rvp smile pioneer2 with dissolve
    window show
    "За ужином я рассказал Лене, как прошёл мой день. Про удачную встречу с токарем, про общагу." with dissolve
    un "Ну, вот видишь, на заводе нашлась для тебя работа." with dissolve
    me "Это да. Теперь целый день буду спину гнуть, а вы отдыхать." with dissolve
    "Отшутился я." with dissolve
    un "Я тоже хочу поработать летом в городе. В больницу попрошусь, вдруг помощь будет нужна. Да даже полы мыть готова." with dissolve
    me "А почему туда?" with dissolve
    un "Хочу врачом стать. Хочу понять, как изнутри это устроено. Полезный опыт будет." with dissolve
    me "Пожалуй."with dissolve
    window hide
    stop ambience fadeout 1

    scene bg ext_internat_rvp with dissolve
    play ambience ambience_camp_center_evening fadein 1
    play music zapomnyu_rvp fadein 1
    show un_rvp smile pioneer2 with dissolve
    window show
    "Мы вышли из столовой." with dissolve
    me "Ладно, мне пора. В общагу надо до одиннадцати вернуться." with dissolve
    show un_rvp serious pioneer2 with dspr
    un "Ну вот, а я хотела погулять."
    "Лена надула губки. Хотелось её порадовать. В принципе, времени не так много." with dissolve
    me "Ну, пойдём до площади." with dissolve
    show un_rvp smile pioneer2 with dissolve
    un "Давай!" with dissolve
    window hide
    
    scene bg square_lmr_night_rvp with dissolve
    window show
    "Мы дошли до площади и сели на лавочке." with dissolve
    show un_rvp smile pioneer2 with dissolve
    un "Сёма, ты молодец. Со всеми трудностями справился. Находишь себя в этом мире." with dissolve
    un "Я думаю, у тебя всё получится!" with dissolve
    me "Ты, правда, так считаешь?" with dissolve
    un "Ну конечно! Ладно, уже поздно. Тебе выспаться надо, мне тоже домой пора." with dissolve
    me "Да уж, завтра на смену. Спокойной ночи!" with dissolve
    show un_rvp smile2 pioneer2 close with dissolve
    un "Спокойной ночи!" with dissolve
    window hide
    show un_rvp grin pioneer2 close:
        anchor(0.5,0.5) pos(0.5,0.5)
        ease 1 zoom 1.5
    show un_rvp grin pioneer2 close:
        anchor(0.5,0.5) pos(0.5,0.5) zoom 1.5
        ease 1 zoom 1.0
    window show
    "Лена поцеловала меня на прощание, и мы разошлись. Завтра трудный день." with dissolve
    window hide
    stop ambience fadeout 1  
    scene bg square_lmr_night_rvp with dissolve    
    show credits rvp_credits_b1:
        xalign 0.5
        ypos 1.3
        linear 52.0 ypos -4.0
    $ renpy.pause()
    stop music fadeout 2

    scene bg black with dissolve
    $ renpy.pause(1.5)

    scene bg obkom_rvp with dissolve
    play ambience ambience_int_cabin_day fadein 1
    play music music_list["drown"] fadein 1
    window show
    "В областной комитет поступил звонок." with dissolve
    gn "Генда, слушаю." with dissolve
    ktoto "Говорит Алекс." with dissolve
    alx "Он появился." with dissolve
    gn "Неужели? Где он сейчас?" with dissolve
    alx "У нас задержали странного гражданина. Заявляет, что он из будущего. Передали вашим, даёт показания." with dissolve
    gn "Понял. Скоро буду." with dissolve
    window hide
    stop ambience fadeout 1

    scene bg lenie_rvp with dissolve
    show genda_rvp with dissolve
    ktoto "Зачем нам его отпускать?" with dissolve
    gn "Всё нормально. Никакой он не диверсант, как вы тут думаете." with dissolve
    gn "Меня предупреждали о том, что он появится." with dissolve
    gn "Сейчас он должен жить у нас, в Лениноморске. Посмотрим, к чему это приведёт." with dissolve
    gn "Пишите пока ходатайство." with dissolve
    gn "Прошу посодействовать гражданину Персунову С.Н. в трудоустройстве и предоставлении временного жилья в связи с трудным материальным положением." with dissolve
    ktoto "А на чьё имя-то?" with dissolve
    gn "Хм. Ну, пусть он сам допишет. Место оставь под это." with dissolve
    "Подпись – первый секретарь областного комитета КПСС тов. Генда." with dissolve
    "Генда взял бумагу, подписал её и поставил печать." with dissolve
    gn "Отлично. Теперь оформите ему временное удостоверение личности, паспорт потом сам сделает. Фотографии у вас есть, я смотрю." with dissolve
    gn "Что у него с вещами?" with dissolve
    ktoto "Пальто, джинсы, рубашка. Какое-то устройство. Мы думали, для связи с кураторами." with dissolve
    gn "Устройство отдать нашим спецам, ему оно тут действительно ни к чему."
    gn "Пока рано что-то говорить, возможно это просто бытовая вещь, которую используют в будущем." with dissolve
    gn "Он ещё что-то про деньги говорил." with dissolve
    ktoto "Да вроде не было никаких денег." with dissolve
    gn "В протоколе написано, двадцать два советских рубля." with dissolve
    gn "Нехорошо чужое себе присваивать. Персунов говорил, это деньги дочери моего друга. Если это правда, ты у меня завтра будешь сторожем работать." with dissolve
    ktoto "Виноват, товарищ первый секретарь! Деньги будут возвращены с точностью до рубля!" with dissolve
    gn "То-то же. Мда, распустились вы с тех пор, как я в обком ушёл." with dissolve
    gn "И вещмешок ему нормальный дайте, чтобы было, куда вещи положить." with dissolve
    "Меньше чем через час все документы на гражданина Персунова были готовы." with dissolve
    "Сотрудники отдельного подразделения КГБ под кодовым названием “СЦП” изъяли все записи, связанные с загадочным появлением гражданина Семёна Персунова в городе Лениноморск." with dissolve
    window hide
    jump rvp
    
label b2:
    stop music fadeout 2
    $ renpy.show("black")
    $ renpy.with_statement(fade3)
    $ renpy.pause(2.0, hard=True)
    $ new_chapter(0, u'Рай в панельке: Часть 2Б')
    $ persistent.sprite_time = "day"
    $ day_time
#  call showtext_rvp("textimg up_a_rvp","textimg dn_a_rvp")

#    $ s="""26 июня 1987 года, г. Лениноморск."""
    play ambience ambience_camp_center_day fadein 1
    scene bg ext_internat_rvp with dissolve
    show un_rvp shy pioneer2:
        align(.3,.5)
    un "Алис, я не знаю. Он какой-то грустный в последнее время. Боюсь, я ему надоела." with dissolve
    dv "С чего ты взяла?" with dissolve
    un "Ну просто… в лагере я лезла к нему. Под руку его взяла один раз. На острове когда были, голову на плечо положила и мы заснули." with dissolve
    un "А потом я в последний день затеяла историю, что нам надо остаться вдвоём с ним. Проявляла инициативу, одним словом." with dissolve
    un "Мне кажется, это из-за меня он остался у нас. Если говорит, что приехал из другого времени." with dissolve
    show un_rvp sad pioneer2:
        align(.3,.5)
    un "Неужели я его обрекла на несчастье жить здесь со мной, лишила того, что он имел?" with dissolve
    un "У него же там наверняка родители были, а я… своих не имею, да ещё у Сёмы их забрала!" with dissolve
    show un_rvp sad pioneer2:
        ease 1 xpos -.2
    show dv_rvp nenrav pioneer2:
        align(.5,.5) xpos 1.2
        ease 1 xpos .8
    dv "Ну, хватит, Лен. Не накручивай себя. Во-первых, это он не из-за тебя грустный ходит, возможно. Во-вторых, а зачем ты его рассказы о прошлом слушаешь?"
    dv "Как ты вообще поверила в эту историю с попаданием из будущего, непонятно." with dissolve
    show dv normal pioneer2:
        align(.5,.5) xpos .8
    dv "Ладно. Кажется, я могу помочь. Добавить немного романтики, так сказать." with dissolve

    play ambience ambience_clubs_inside_day fadein 1
    play music pesnyabezslov_rvp fadein 2
    scene bg tsekh_rvp with dissolve
    mh "Тьфу-ты! А говорил – нормально выточишь!" with dissolve
    mh "Семыч, это никуда не годится. Мне надоело за тобой брак забирать. Давай дуй в путягу. Там научат работать." with dissolve
    me "Да я же и так работаю!" with dissolve
    mh "Надо, чтобы тебя нормально научили! У меня нет времени возиться с тобой особо. У нас план горит, мне премия нужна." with dissolve
    me "Да мне немного попрактиковаться надо и…" with dissolve
    mh "Ты уже какую деталь испортил, практикант херов! У меня нет уже для тебя лишних, остальные надо выточить… идеально, блин. Задал мне задачку." with dissolve
    mh "Вот что я тебе скажу. Не надо тут строить из себя тут токаря хрен знает какого разряда. Приходи с документами на Горького, пять. Все мы через неё, родимую, прошли." with dissolve
    mh "Всё, разговор окончен." with dissolve
    me "Смена, кстати, тоже." with dissolve
    mh "Так чего стоишь? Давай в раздевалку и домой. Я тебя ждать не собираюсь. Просто в цеху закрою и будешь ночевать тут, хехе." with dissolve
    "Сказал Михаил и засмеялся при этом так неприятно." with dissolve
    scene bg tsekh_rvp with dissolve
    $ set_mode_rvp(mode=nvl)
    "Прошло две недели с моего появления в этом городе. После всех злоключений мне удалось быстро найти кров и работу, как-то устроиться на первое время."
    "Однако появилась какая-то тоска. Несмотря на то, что тут у меня появился шанс начать новую жизнь с Леной, я начинал скучать по своему родному миру."
    "Там можно было спать до обеда и сидеть дома. А здесь нужно вставать утром и идти на завод."
    "Но, конечно, если бы не Лена, совсем от тоски загнулся. Встречи с ней были поводом не унывать."
    "Но здесь не лагерь, где можно было под каким-либо предлогом сбежать от вожатой. Здесь с утра до вечера работа, потом ненадолго увидимся с ней."
    "Пару раз в неделю ходим играть в бадминтон, Лена увлеклась им после смены."
    "Ещё и денежный вопрос. В лагере он вообще не стоял! Пошёл в столовую, поел, что тебе дали, и идёшь себе дальше по своим делам."
    "А тут… нужна одежда, нужны бытовые принадлежности. Зубы почистить, привести себя в порядок, чтобы не стыдно было к Лене идти."
    "В общем, девяносто девять проблем, которые меня занимали и из-за которых я ходил хмурый."
    "Так было и в тот июньский день, когда я в очередной раз пошёл к Лене."
    $ set_mode_rvp(mode=adv)
    scene bg zavod_rvp:
        align(.5,.5) zoom 1.05
        ease .5 offset(25,25)
        ease .5 offset(0,0)
        ease .5 offset(-25,25)
        ease .5 offset(0,0)
        repeat
    "Ну вот опять! Моя попытка доказать моему наставнику, что я чего-то стою, провалилась." with dissolve
    "Нет, я понимаю, я новичок в токарном деле, со станком на «вы». Но идти в ПТУ?! Да помилуйте! Там же контингент - оторви и выбрось. Ещё ведь знакомиться с ними." with dissolve
    scene bg square_lmr_day_rvp:
        align(.5,.5) zoom 1.05
        ease .5 offset(25,25)
        ease .5 offset(0,0)
        ease .5 offset(-25,25)
        ease .5 offset(0,0)
        repeat   
    "Зачем мне кто-то ещё? Есть мой учитель токарного дела Михаил, есть моя любовь Лена и её подруга Алиса. Всё, мне больше никого не надо." with dissolve
    "Настрой портила и простая усталость, идти до Лены приходится полчаса по жаре." with dissolve
    "Ох, не стоило мне тогда быть таким брюзгой." with dissolve
    scene bg ext_internat_rvp:
        align(.5,.5) zoom 1.05
        ease .5 offset(25,25)
        ease .5 offset(0,0)
        ease .5 offset(-25,25)
        ease .5 offset(0,0)
    "Пройдя знакомый мне маршрут, я пришёл к интернату. И снова меня встретила Лена." with dissolve
    show un_rvp smile2 pioneer2 with dissolve
    un "Сёма, привет. Как дела?" with dissolve
    me "Да так, пойдёт." with dissolve
    "Позитив Лены действовал мне на нервы." with dissolve
    show un_rvp shy pioneer2 with dspr
    un "Что-то случилось?" with dissolve
    me "Да ничего не случилось. Всё нормально." with dissolve
    show un_rvp smile pioneer2 with dspr
    un "Ну ладно. Пойдём за мной, покажу кое-что." with dissolve
    scene bg new_rayon_rvp:
        align(.5,.5) zoom 1.05
        ease .5 offset(25,25)
        ease .5 offset(0,0)
        ease .5 offset(-25,25)
        ease .5 offset(0,0)
        repeat
    "Мы пошли в какой-то незнакомый район. Дорога была недолгой, но от усталости ногам было тяжело. Подошли к многоэтажке. Я ещё не видел здесь таких новых домов." with dissolve
    show un_rvp smile pioneer2:
        ease .5 yoffset 0
        ease .5 yoffset 15
        repeat
    with dissolve
    me "Лена, куда мы идём?" with dissolve
    show un_rvp hitr pioneer2:
        ease .5 yoffset 0
        ease .5 yoffset 15
        repeat
    with dspr
    un "Сейчас узнаешь." with dissolve
    "Загадочно улыбнувшись, сказала она." with dissolve
    scene bg staircase_rvp with dissolve
    "Мы зашли и поднялись на лифте на самый высокий этаж. Спасибо хоть, что не по лестнице." with dissolve
    "Опять какой-то сюрприз от Лены. Нет, я как бы не против, но сейчас я немного не в духе после смены." with dissolve
    "Интересно, зачем она меня сюда привела? Знакомство с её загадочными родителями? Я сейчас не готов к такой ответственной миссии." with dissolve
    show un_rvp smile pioneer2 with dissolve
    me "Не нравится мне всё это." with dissolve
    un "Ну, подожди немного." with dissolve
    show un_rvp smile pioneer2:
        align(.5,.5)
        ease 1 pos(1.,.5) alpha 0
    "Мы вышли на девятом этаже. Чуть замешкавшись, Лена подошла к лестнице и стала подниматься."
    me "Что ты делаешь?" with dissolve
    un "Сейчас узнаешь." with dissolve
    "Лена становилась всё взволнованнее. Я не придал этому значения, а зря." with dissolve
    stop music fadeout 2
    play ambience ambience_cold_wind_loop fadein 1
    scene bg roof_rvp:
        align(.0,.0)
        ease 1 zoom 1.05
    show un_rvp smile pioneer2:
        anchor(.5,.5) pos(.1,.5) zoom 1.25 alpha 0
        ease 1.5 xpos(.25) alpha 1
    "Она достала ключ и стала открывать люк. Мы поднялись на крышу." with dissolve
#    "Нам открылся вид на город." with dissolve
#а где этот ваш вид??
    show un_rvp smile pioneer2:
        anchor(.5,.5) pos(.25,.5) zoom 1.25
        ease 1 xpos .5
    with dspr
    un "Ну, как тебе?" with dissolve
    "Мне это всё надоело окончательно. Ещё сейчас нас с Леной увидит кто-нибудь. Проблемы начнутся." with dissolve
    me "Ну и зачем это всё?" with dissolve
    show un_rvp shy pioneer2:
        align(.5,.5) zoom 1.25
    with dspr
    un "Тебе не нравится?" with dissolve
    "Лена часто дышала от подъёма, но больше от волнения." with dissolve
    me "Вообще не нравится, если честно." with dissolve
#'не нравится' заменить на 'нет'
    me "Я весь день работал, потом ты меня тащишь куда-то на крышу!" with dissolve
    show un_rvp normal pioneer2:
        align(.5,.5) zoom 1.25
    with dspr
    un "Ну да, наверное, зря это всё было." with dissolve
    me "Да уж." with dissolve
    un "Я такая дура." with dissolve
    me "В смысле?" with dissolve
    play music music_list["doomed_to_be_defeated"] fadein 1
    show un_rvp angry pioneer2:
        align(.5,.5) zoom 1.25
    with dspr
    un "Да ладно, не молчи уж!" with dissolve
    "Лена повысила голос." with dissolve
    me "Ты о чём?" with dissolve
    show un_rvp ubiu pioneer2:
        align(.5,.5) zoom 1.25
    with dspr
    "Она окончательно разозлилась." with dissolve
    show un_rvp rage pioneer2:
        align(.5,.5) zoom 1.25
    with dspr
    un "Да не скрывай!" with dissolve
    me "Чего я скрываю?" with dissolve
    un "Совсем меня за дуру держишь?! Думаешь, я не замечаю?!" with dissolve
    un "Я тебе надоела, да?! Разонравилась?!" with dissolve
    un "Привязалась в лагере ненормальная и никак от неё не избавишься!" with dissolve
    me "Чего..." with dissolve
    un "А ты не переживай, Сём. Я тебя избавлю от этого груза!" with dissolve
    un "Сейчас прыгну! И будешь свободен!" with dissolve
    show un_rvp normal pioneer2:
        align(.5,.5) zoom 1.25
        ease .7 xpos 1.2
    "Лена резко дернулась к краю!"
#дёр
    scene bg roof_rvp:
        align(.5,.5) zoom 1.05
        ease .3 offset(25,25)
        ease .3 offset(0,0)
        ease .3 offset(-25,25)
        ease .3 offset(0,0)
    "Я бросился за ней. Вроде бы мы и не стояли близко к краю, но всё решали секунды. Перехватить Лену удалось в паре метров." with dissolve
    "Я схватил её со спины." with dissolve
    "Ещё немного, и было бы поздно." with dissolve
    scene bg roof_rvp:
        align(.5,.5) zoom 1.05
        ease .1 xoffset 25
        ease .1 xoffset 0
        ease .1 xoffset -25
        ease .1 xoffset 0
        pause .5
        repeat
    me "Ты что творишь?!" with dissolve
    un "Пусти! Я не хочу тебе мешать жить!" with dissolve
    me "Да никому ты не мешаешь!" with dissolve
    un "Но ты же несчастный! Я тебе надоела!" with dissolve
    me "Да ты чего, блин?! Я же тебя люблю!" with dissolve
    un "Правда?" with dissolve
    me "ДА ПРАВДА!" with dissolve
    stop music fadeout 1
    scene bg roof_rvp with dissolve
    "Крикнул я ей в ухо." with dissolve
    "Лена перестала вырываться из объятий." with dissolve
    un "Отпусти меня." with dissolve
    me "Не будешь с крыши прыгать, пущу." with dissolve
    un "Не буду." with dissolve
    "Но я не отпустил Лену. Слишком уж боялся за неё в тот момент. Развернул к себе и прижал." with dissolve

    play music namstoboy_rvp fadein 1
#цгшка
    me "Лен, ты чего творишь?" with dissolve
    un "Не знаю, просто… я думала, что мучаю тебя своей привязанностью." with dissolve
    me "Да ну нет, конечно! С чего ты взяла?" with dissolve
    un "А чего ты хмурый такой в последнее время?" with dissolve
    "Сказала она с некоторой горечью в голосе." with dissolve
    me "Да это не из-за тебя." with dissolve
    un "А из-за чего?" with dissolve
    me "Ну…" with dissolve
    un "Давай говори!" with dissolve
    me "Ну, работа… денег нет." with dissolve
    un "Пон-я-я-я-тно." with dissolve
    un "Что-то ещё?" with dissolve
    me "С Мишей поругался, токарем своим на заводе. Деталь хотел выточить, запорол." with dissolve
    "Лена помолчала." with dissolve
    un "А я думала, я тебе навязываюсь." with dissolve
    me "С чего ты взяла?" with dissolve
    un "Ну, лезла к тебе в лагере." with dissolve
    me "Лезла и ладно. Я не против." with dissolve
    un "Это хорошо." with dissolve
    un "Сём, мне что-то плохо." with dissolve
    me "Тебе помочь? Может в больницу отвести?" with dissolve
    un "Давай просто сядем." with dissolve
    
    "Мы с Леной сели на крышу. Лена устало опёрлась на меня и закрыла глаза." with dissolve
    "Прямо как тогда, на острове, когда пошли за земляникой." with dissolve
    "Так мы сидели какое-то время. Я задумался." with dissolve
    "Опять Лена выкинула какой-то сюрприз. А я её неправильно понял и это чуть не случилось страшное. Понимаю, я её задел. Но прыгать с крыши…" with dissolve
    "Надо будет поговорить с ней." with dissolve
    "Сейчас всё, что мне оставалось делать – смотреть на закат, красящий город золотым цветом." with dissolve
    $ renpy.pause(2.0)
    "Лена очнулась от дрёмы." with dissolve
    show un_rvp normal pioneer2 with dissolve
    me "Как себя чувствуешь? Может, пойдём отсюда?" with dissolve
    show un_rvp shy pioneer2 with dissolve
    un "Да, давай." with dissolve
    me "Лен, а зачем мы вообще сюда пришли?" with dissolve
    un "Полюбоваться." with dissolve
    me "Давай в другой раз как-нибудь, хорошо?" with dissolve
    show un_rvp smile pioneer2 with dissolve
    un "Хорошо." with dissolve

    stop ambience fadeout 1
    scene bg podezd_lmr_sunset_rvp with dissolve
    show un_rvp smile pioneer2:
        anchor(.5,.5) pos(.1,.5) zoom 1.25 alpha 0
        ease 1.5 xpos(.25) alpha 1
    "Мы спустились обратно. Я решил спросить." with dissolve
    me "А откуда у тебя ключ?" with dissolve
    un "Алиса дала." with dissolve
    me "А у неё он откуда?" with dissolve
    show un_rvp hitr pioneer2:
        anchor(.5,.5) pos(.25,.5) zoom 1.25
        ease 1 xpos .5
    with dspr
    un "Ты Алису не знаешь?" with dissolve
    "К Лене наконец вернулся прежний весёлый вид." with dissolve
    me "Я с вами не так давно знаком." with dissolve
    un "Она и не такое может." with dissolve
    me "Впрочем, это в её репертуаре." with dissolve
    play ambience ambience_camp_center_evening fadein 1
    stop music fadeout 1
    scene bg ext_internat_rvp with dissolve
    "До интерната мы шли молча." with dissolve
    show un_rvp normal pioneer2 with dissolve
    un "Сёма." with dissolve
    me "Да, Лен?" with dissolve
    show un_rvp sad pioneer2 with dspr
    un "Прости меня за всё это." with dissolve
    me "Я сам виноват." with dissolve
    un "Нет, правда. Мне стыдно, что я такую истерику устроила на ровном месте." with dissolve
    me "Давай завтра сходим куда-нибудь? Только без перепадов высоты." with dissolve
    show un_rvp smile pioneer2 with dspr
    un "Хорошо! Мы завтра с Алисой в библиотеку собирались." with dissolve
    me "Пойдёт." with dissolve
    show un_rvp laugh pioneer2 with dspr
    un "А теперь, иди домой и отдыхай! И чтобы больше на усталость не жаловался!" with dissolve
    show un_rvp laugh pioneer2:
        align(.5,.5)
        ease 1 pos(1.,.5) alpha 0
    "Весело сказала Лена и убежала к себе. Я проводил её взглядом." with dissolve
    "Обдумывая произошедшее, на ум приходило одно." with dissolve
    "Я совершенно не понимаю Лену." with dissolve
    stop ambience fadeout 1
    jump rvp