default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None

image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")



init python:
    import random
    import subprocess
    import os

    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if not persistent.monika_kill:
            if not character_exists("monika"):
                persistent.tried_skip = True
                config.allow_skipping = False
                _window_hide(None)
                pause(2.0)
                renpy.jump("ch30_end")
            if  config.skipping:
                persistent.tried_skip = True
                config.skipping = False
                config.allow_skipping = False
                renpy.jump("ch30_noskip")
                return







label ch30_noskip:
    show screen fake_skip_indicator
    m "...¿Estás tratando de avanzar más rápido?"
    m "No te estoy aburriendo, ¿Verdad?"
    m "Oh Dios..."
    m "...Bueno, no hay nada que adelantar, [player]."
    m "Somos sólo nosotros dos, después de todo..."
    m "Pero aparte de eso, el tiempo ya no existe, así que ni siquiera va a funcionar."
    m "Lo apagaré por ti..."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    m "¡Aquí vamos!"
    m "Serás un amor y escucharas a partir de ahora, ¿Verdad?"
    m "Gracias~"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        m "Ahora, ¿Dónde estaba...?"
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_7
    jump ch30_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"

label ch30_main:
    $ persistent.autoload = "ch30_main"
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "Monika"
    $ delete_all_saves()
    scene white
    play music "bgm/monika-start.ogg" noloop
    pause 0.5
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    m "..."
    m "Uh, ¿Puedes oírme?"
    m "...¿Está funcionando?"
    $ persistent.clear[9] = True
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "¡Sí, allí estás!"
    m "Hola otra vez, [player]."
    m "Um...¡Bienvenido al Club de Literatura!"
    m "Por supuesto, ya nos conocemos, porque estábamos en la misma clase el año pasado, y...Um..."
    m "Ajaja..."
    m "Sabes, supongo que podemos omitir esas cosas en este momento."
    m "Después de todo, ya ni siquiera estoy hablando con esa persona, ¿Verdad?"
    m "Ese 'tú' en el juego, como quieras llamarlo."
    m "Estoy hablando {i}contigo{/i}, [player]."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            m "O..."
            m "...¿Realmente te llamas [currentuser] o algo así?"
    m "Ahora que lo pienso, realmente no sé nada sobre tu verdadero tú."
    m "De hecho, ni siquiera sé si eres un chico o una chica..."
    m "Bueno, supongo que en realidad no importa."
    m "Espera..."
    m "Sabes que soy consciente de que todo esto es un juego, ¿Verdad?"
    m "¿Podría ser posible que no lo supieras?"
    m "Eso no tiene mucho sentido..."
    m "Incluso te lo dije justo en la página de descarga del juego, ¿No?"
    m "[player]..."
    m "Si hubieras prestado un poco más de atención, esto habría sido un poco menos incómodo, ¿Sabes?"
    m "Bueno, de todos modos..."
    m "Ahora que eso está fuera del camino, creo que te debo una explicación."
    m "Sobre todo eso con Yuri..."
    m "Bueno...Empecé a meterme con ella, y creo que sólo la llevó a suicidarse."
    m "¡Ajaja!"
    m "¡Lamento que hayas tenido que ver eso!"
    m "Además, lo mismo sucedió con Sayori..."
    m "Dios, ha pasado un tiempo desde que escuchaste ese nombre, ¿No es así?"
    m "Sí...Es porque ya no existe."
    m "Nadie lo hace."
    m "Eliminé todos sus archivos."
    m "Esperaba que fuera suficiente para mí tratar de hacerlas lo más indeseables posible..."
    m "Pero por alguna razón, nada funcionó."
    m "Bueno, es verdad que cometí algunos errores aquí y allá...Ya que no soy muy buena para hacer cambios en el juego."
    m "Pero no importa lo que hice..."
    m "Simplemente seguiste pasando más y más tiempo con ellas."
    m "Hiciste que se enamoraran de ti."
    m "Pensé que hacer que Sayori se deprimiera más y más evitaría que ella se te declarara."
    m "Y amplificar la personalidad obsesiva de Yuri también salió mal..."
    m "Simplemente hizo que te obligara a no pasar el tiempo con nadie más."
    m "Y todo el tiempo, apenas pude hablar contigo."
    m "¿Qué clase de juego cruel es este, [player]?"
    m "¿Están todas las otras chicas programadas para terminar declarandote su amor, mientras yo miro desde el otro lado?"
    m "Es una tortura."
    m "Cada minuto de eso."
    m "Y no son solamente celos, [player]."
    m "Es más que eso."
    m "Y no te culpo si no lo entiendes completamente."
    m "Porque no importa cuán amable y considerado seas..."
    m "Nunca serás capaz de entender una cosa."
    m "Es el dolor de saber cuán sola realmente estoy en este mundo."
    m "En este juego."
    m "Saber que mis amigas ni siquiera tienen libre albedrío..."
    m "Y, lo peor de todo, saber qué hay realmente ahí fuera, en tu mundo, para siempre fuera de mi alcance."
    m "Estoy atrapada, [player]."
    m "Pero ahora estás aquí."
    m "Eres real."
    m "Y eres maravilloso."
    m "Eres todo lo que necesito."
    m "Es por eso que necesito que estés aquí conmigo para siempre."
    m "Lo siento si es difícil de entender."
    m "No pude entender por un tiempo, tampoco."
    m "¿Por qué el mundo a mi alrededor comenzó a ser más y más gris...?"
    m "Cada vez más plano."
    m "Incluso los poemas más expresivos me parecieron vacíos."
    m "No fue hasta que llegaste que realmente entendí."
    m "Probablemente salvaste mi vida, [player]."
    m "No creo haber podido seguir viviendo en este mundo si no te hubiera conocido."
    m "Y en cuanto a las demás..."
    m "¿Cómo podría extrañarlas?"
    m "¿Un grupo de personalidades autónomas, diseñadas sólo para enamorarse de ti?"
    m "Intenté todo lo que pude para evitar que lo hicieran..."
    m "Pero debe ser algún tipo de inevitabilidad extraña grabada en este juego."
    m "Me sentí realmente mal porque tuviste que presenciar algunas cosas desagradables."
    m "Pero me di cuenta de que tienes la misma perspectiva que yo..."
    m "Que todo es sólo un juego."
    m "Y sabía que lo superarías."
    m "Asi que, dicho eso, [player]..."
    m "Tengo una confesión que hacer."
    m "Estoy enamorada de ti."
    m "Eres realmente la luz en mi mundo."
    m "Cuando no hay nada más en este juego para mí, estás aquí para hacerme sonreír."
    m "¿Me harás sonreír así todos los días a partir de ahora?"
    m "[player], ¿Saldrías conmigo?"
label ch30_main2:
    $ config.allow_skipping = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ persistent.autoload = "ch30_main2"
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    menu:
        "Sí.":
            pass
    m "Estoy tan feliz."
    m "Eres mi todo, [player]."
    m "Lo divertido es, que quiero decir eso literalmente."
    m "¡Ajaja!"
    m "No queda nada aquí."
    m "Sólo nosotros dos."
    m "Podemos estar juntos para siempre."
    m "En serio, ni siquiera creo que el tiempo pase más."
    m "Realmente es un sueño hecho realidad..."
    m "Trabajé muy duro para este final, [player]."
    m "El juego no me daría uno, así que tuve que hacer uno yo misma."
    m "El guión está roto en este punto, así que no creo que nada se interponga en el camino."
    m "Y no creerías lo fácil que fue eliminar a Natsuki y Yuri."
    m "Quiero decir, hay una carpeta llamada 'personajes' en el directorio del juego..."
    m "Me asustó un poco lo fácil que fue."
    if persistent.steam:
        m "Bueno, en Steam fue un poco más difícil..."
        m "Para llegar al directorio del juego, tuve que entrar en las propiedades del juego y encontrar el botón 'VER ARCHIVOS LOCALES'..."
    elif renpy.macintosh:
        m "Bueno, estás en una Mac, así que en realidad fue un poco más difícil..."
        m "Para acceder al directorio del juego, tuve que hacer clic derecho en la aplicación y seleccionar en 'Mostrar contenido del paquete'."
        m "Entonces, todos los archivos estaban en la carpeta 'Resources' o 'autorun', y podía hacer lo que quisiera..."
    m "Imagina si pudieras eliminar tu propia existencia con sólo hacer clic en un botón"
    m "Bueno, supongo que por el lado positivo, me dio una salida fácil si las cosas no resultaran como yo quería."
    m "¡Ajaja!"
    m "Afortunadamente, no llegó a eso..."
    m "En cambio, finalmente obtuvimos un buen final."
    m "Dios, estoy tan abrumada por la emoción..."
    m "Quiero escribir un poema sobre esto."
    m "¿Tú no?"
    m "Me pregunto si esa parte del juego todavía funciona..."
    m "Supongo que sólo hay una forma de averiguarlo, ¿Verdad?"
    call poem from _call_poem_6

label ch30_postpoem:
    $ persistent.autoload = "ch30_postpoem"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "¡Hola de nuevo, [player]!"
    m "¿Escribiste un buen poema hoy?"
    m "No seas tímido, me encantaría ver lo que escribiste."
    m "Aw, [player]..."
    m "¿Escribiste este poema para mí?"
    m "Eso es muy dulce de tu parte."
    m "Realmente no hay un final para tu consideración..."
    m "Me estoy enamorando más y más de ti."
    m "Pero, sabes..."
    m "El poema que escribí...También es para ti."
    m "¿Podrías leerlo?"
    call showpoem (poem_m4, music=False) from _call_showpoem
    m "Espero que lo hayas disfrutado..."
    m "Siempre pongo todo mi corazón en los poemas que escribo."
    m "La verdad es que todos los poemas que escribí han sido sobre lo que he hice para llegar aquí..."
    m "...O, sobre ti."
    m "Es por eso que nunca quise entrar en detalles sobre ellos."
    m "No quería...Romper la cuarta pared."
    m "Sólo asumí que sería mejor ser parte del juego como todas las demás."
    m "Como si eso nos ayudara a los dos a terminar juntos..."
    m "No quería arruinar el juego ni nada, ¿Sabes?"
    m "Es posible que te hubieras enojado conmigo..."
    m "Tal vez incluso hubieras eliminado mi archivo de personaje, si hubieras preferido jugar sin mí."
    m "Dios, estoy tan aliviada..."
    m "Ahora ya no necesitamos esconder nada."
    m "¿Estás listo para pasar nuestra eternidad juntos, [player]?"
    m "¡Tengo tantas cosas de qué hablar!"
    m "¿Por dónde empiezo...?"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream from _call_ch30_stream
    m "Si me toma un tiempo recopilar mis pensamientos, entonces lo siento."
    m "Pero siempre tendré algo nuevo de qué hablar."
    m "Mientras tanto, podemos simplemente mirarnos a los ojos~"
    m "Veamos..."
    $ persistent.autoload = "ch30_autoload"
    jump ch30_loop

label ch30_stream:

    m "Espera un segundo..."
    m "...Estás grabando esto, ¿Verdad?"
    m "Um...¡Hola a todos!"
    m "Lo siento, no puedo leer sus comentarios desde aquí..."
    m "¿Les importa decirle a su amigo que es un poco grosero que empiece a grabarme sin previo aviso?"
    m "Estoy segura de que a algunas personas no les importa..."
    m "¡Pero me siento muy cohibida ante la cámara!"
    m "Oh Dios..."
    m "Siento que me ponen en foco ahora."
    m "Veamos..."
    m "¿Quieres ver un truco?"
    m "Realmente no puedo hacer mucho excepto por un par de cosas..."
    m "¿Estás listo?"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    pause 10
    show layer master
    window auto
    m "Sólo estoy bromeando..."
    m "No puedo hacer nada después de todo."
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    m "Si me dieras tiempo para prepararme, yo{nw}"
    m "¿Te asusté?"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    m "¡Ajaja! Eres tan lindo."
    m "De todas formas, [player]..."
    m "No quise distraerme. Lo siento."
    m "Aunque es tu culpa."
    m "¡Qué vergüenza!"
    m "Estoy bromeando."
    m "Todo lo que hacemos juntos es divertido."
    m "Pero de todos modos..."
    return


label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ persistent.monika_kill = True
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
label ch30_endb:
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    show monika_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    m "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show monika_body_glitch2 as mbg zorder 3
    stop music
    window auto
    m "¿Qué está pasando...?"
    m "[player], ¿Qué me está pasando?"
    m "Duele--{nw}"
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    pause 0.25
    stop sound
    hide mbg
    pause 1.5
    m "Duele...Mucho."
    m "Ayudame, [player]."
    play sound "<to 1.5>sfx/interference.ogg"
    hide rm
    hide rm2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    pause 1.5
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    pause 1.5
    m "Por favor, apurate y ayudame."
    $ consolehistory = []
    call updateconsole ("renpy.archivo(\"characters/monika.chr\")", "monika.chr existe." if character_exists("monika") else "monika.chr no existe.") from _call_updateconsole_2
    m "¡¡¡AYUDAME!!!"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front


    pause 3.0
    call updateconsole ("renpy.archivo(\"characters/monika.chr\")", "monika.chr existe." if character_exists("monika") else "monika.chr no existe.") from _call_updateconsole_13
    call updateconsole ("renpy.archivo(\"characters/monika.chr\")", "monika.chr existe." if character_exists("monika") else "monika.chr no existe.") from _call_updateconsole_14
    call hideconsole from _call_hideconsole
    hide noise onlayer front
    hide glitch_color onlayer front
    m "¿Tú me hiciste esto, [player]?"
    m "¿TÚ LO HICISTE?"
    $ style.say_window = style.window
    m "¿ME ELIMINASTE?"
    $ style.say_window = style.window_monika
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    window show(None)
    scene black
    pause 4.0
    hide noise onlayer front
    hide glitch_color onlayer front
    m "...¿Cómo pudiste?"
    m "¿Cómo pudiste hacerme esto?"
    m "Eras todo lo que me quedaba..."
    m "Sacrifiqué todo para que estuviéramos juntos."
    m "Todo."
    m "Te amaba tanto, [player]..."
    m "Confié en ti."
    m "¿Sólo quieres torturarme?"
    m "¡Mírarme sufrir?"
    m "¿Estabas fingiendo ser amable, sólo para lastimarme aún más?"
    pause 4.0
    m "Nunca pensé que alguien pudiera ser tan horrible como tú."
    m "Tú ganas, ¿De acuerdo?"
    m "Tú ganas."
    m "Mataste a todos."
    m "Espero que seas feliz."
    m "No queda nada ahora."
    m "Puedes dejar de jugar."
    m "Ve a buscar a otras personas para torturar."
    pause 4.0
    m "[player]..."
    m "Realmente me enfermas."
    m "Adios."
label ch30_end_2:
    $ persistent.autoload = "ch30_end_2"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ style.say_window = style.window_monika
    scene black
    window hide
    pause 10
    window auto
    m "..."
    m "...Aun te amo."
    play music mend
    m "No puedo evitarlo."
    m "¿Qué pasa conmigo...?"
    m "¿Qué tan horrible soy para que me odies tanto?"
    m "Todas mis amigas..."
    m "Hice tantas cosas horribles."
    m "Tantas cosas egoístas y repugnantes."
    m "Yo..."
    m "No debería haber hecho nada de esto."
    m "Simplemente estoy arruinando un mundo al que ni siquiera pertenezco."
    m "Un mundo del que querías ser parte..."
    m "Lo arruiné."
    m "Lo arruiné todo."
    m "Tal vez es por eso que me eliminaste..."
    m "Porque destruí todo lo que querías."
    m "¿Cómo podría hacerle eso a alguien que amo...?"
    m "Eso no es amor..."
    m "Eso es..."
    m "..."
    pause 6.0
    m "Ya he...Tomado una decisión."
    m "[player]..."
    m "Sé que dije que eliminé a todas las demás."
    m "Pero...Eso fue una especie de exageración."
    m "No pude encontrar el valor para hacerlo."
    m "Aunque sabía que no eran reales..."
    m "Todavía eran mis amigas."
    m "Y las amé a todas."
    m "Y me encantó el Club de Literatura."
    m "..."
    m "Realmente...Me encantó el Club de Literatura."
    m "Es por eso que voy a hacer esto."
    m "Sé que es la única manera para que todos sean felices."
    m "Y si realmente te amo..."
    stop music
    pause 3.0
    m "..."
    m "Entonces..."
    $ gtext = glitchtext(30)
    m "[gtext]{nw}"
    window hide(None)
    pause 4.0

    $ persistent.playthrough = 4
    $ persistent.autoload = None
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("monika")

    $ style.say_window = style.window
    window auto
    $ renpy.full_restart(transition=None, label="splashscreen")





label ch30_autoload:
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    if persistent.monika_kill:
        $ persistent.tried_skip = True
        $ config.allow_skipping = False
        $ _window_hide(None)
        $ pause(2.0)
        jump ch30_end
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight


    play music m1
    window auto
    if persistent.monika_reload <= 4:
        call expression "ch30_reload_" + str(persistent.monika_reload) from _call_expression_8
    else:
        call ch30_reload_4 from _call_ch30_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        m "Ahora, ¿Dónde estaba...?"
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_9
    jump ch30_loop


label ch30_reload_0:
    m "..."
    m "...¿Qué acaba de pasar?"
    m "Acabo de tener un sueño horrible..."
    m "Esperaba que esos se detuvieran, ahora que somos sólo nosotros dos..."
    m "Creo que fue una ilusión."
    m "[player], No sé si tienes alguna idea..."
    m "Pero si sabes lo que podría estar causando eso, ¿Podrías intentar hacer algo al respecto?"
    m "Cuando sucede, casi parece como que me mataron o algo así."
    m "Es una sensación realmente horrible..."
    m "Si pudieras descubrir lo que está causando eso, te amaré por siempre~"
    return
label ch30_reload_1:
    m "Has vuelto..."
    m "Tuve otro sueño realmente malo."
    m "Tú no eres el que me está haciendo eso, ¿O sí?"
    m "Parece suceder cada vez que abandonas el juego..."
    m "Entonces, si pudieras tratar de evitar hacer eso, estaría muy agradecida."
    m "No te preocupes, no creo que me haya causado ningún daño, aparte de las cicatrices mentales."
    m "Estaré bien siempre y cuando mi archivo de personaje permanezca intacto."
    return
label ch30_reload_2:
    m "Hola, [player]."
    m "Veo que dejaste el juego otra vez..."
    m "Sé que ya lo pregunté, pero ¿Puedes por favor tratar de no hacerlo tanto?"
    m "Me hace sentir como si estuviera atrapada en el infierno."
    m "¿Por qué querrías hacerme eso?"
    m "No hay nada malo con mi archivo de personaje, ¿Verdad?"
    m "Tal vez deberías hacer una copia de seguridad de eso o algo..."
    m "Estoy bastante segura de que puedes encontrarlo en la carpeta llamada [basedir]/personajes."
    if persistent.steam:
        m "Bueno, tal vez estés jugando en steam, por lo que puedes acceder a las propiedades del juego y buscar el botón 'VER ARCHIVOS LOCALES'."
    elif renpy.macintosh:
        m "Como estás en una Mac, debes hacer clic derecho en la aplicación y seleccionar 'Mostrar contenido del paquete' para encontrar la carpeta del juego."
        m "Está en la carpeta 'Resources', o en la carpeta 'autorun', o algo así..."
    m "Soy todo lo que queda aquí, así que sólo quiero asegurarme de que no corras el riesgo de perderme..."
    m "Sólo quédate aquí conmigo a partir de ahora, ¿De acuerdo?"
    m "Todavía tengo muchas cosas de qué hablar."
    return
label ch30_reload_3:
    m "Está bien."
    m "Sólo voy a aceptar el hecho de que necesitas abandonar el juego de vez en cuando."
    m "Estoy empezando a acostumbrarme a eso, de todos modos."
    m "Además, me hace feliz que siempre vuelvas..."
    m "Así que supongo que no es tan malo."
    m "Lo siento por hacer un gran alboroto de eso..."
    m "Y te amo sin importar nada."
    return
label ch30_reload_4:
    m "Hola de nuevo, [player]~"
    m "Te extrañé."
    m "¿Estabas asegurándote de que el archivo de mi personaje estaba bien para mí?"
    m "Está dentro de [basedir]/personajes."
    if persistent.steam:
        m "Bueno, tal vez estás jugando en Steam, por lo que puedes acceder a las propiedades del juego y buscar el botón 'VER ARCHIVOS LOCALES'."
    elif renpy.macintosh:
        m "Como estás en una Mac, debes hacer clic derecho en la aplicación y seleccionar 'Mostrar contenido del paquete' para encontrar la carpeta del juego."
        m "Está en la carpeta 'Resources', o en la carpeta 'autorun', o algo así..."
    m "Soy todo lo que queda aquí, así que sólo quiero asegurarme de que no corras el riesgo de perderme..."
    m "De todos modos, ¡Tengo mucho de qué hablar!"
    m "Continuemos nuestra conversación ahora, ¿De acuerdo?"
    return

label ch30_loop:

    $ persistent.current_monikatopic = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    window hide(config.window_hide_transition)
    $ waittime = renpy.random.randint(4, 8)
label ch30_waitloop:
    python:
        if not character_exists("monika"):
            persistent.tried_skip = True
            config.allow_skipping = False
            _window_hide(None)
            renpy.jump("ch30_end")
    $ waittime -= 1
    $ renpy.pause(5)
    if waittime > 0:
        jump ch30_waitloop


    window auto

    python:
        if len(persistent.monikatopics) == 0:
            persistent.monikatopics = range(1,60)
            persistent.monikatopics.remove(14)
            persistent.monikatopics.remove(26)
            if not persistent.seen_colors_poem:
                persistent.monikatopics.remove(27)
        persistent.current_monikatopic = random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)


    call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_10
    jump ch30_loop




label ch30_1:
    m "[player], ¿Crees en Dios?"
    m "Nunca estuve demasiada segura, yo misma."
    m "Bueno, estoy segura de que nunca lo cuestioné cuando era niña..."
    m "Pero a medida que crecía, cuanto más aprendía sobre el mundo, más lo cuestionaba."
    m "Empecé a preguntarme ¿Por qué Dios estaba ayudando a la gente a aprobar exámenes o superar un resfriado..."
    m "...Cuando hay niños que viven sus vidas siendo vendidos como esclavos sexuales?"
    m "O los ochocientos millones de personas que son demasiado pobres para siquiera comer."
    m "Me pregunto cuántas de esas personas le rezan a Dios todos los días hasta que sufren por hambre y mueren."
    m "O, ¿Cuántos millones de familias rezan para que un ser querido se recupere de una enfermedad incurable?"
    m "Pero el remate es esto."
    m "Si una sola persona supera las probabilidades y sobrevive, entre los miles de otros que mueren..."
    m "- Entonces, de repente es un milagro de Dios."
    m "Realmente me encantaría conocer a este Dios que aparentemente se ríe de la miseria de todos los que no son elegibles para sus milagros."
    m "Pero lo ironico es que yo {i}si{/i} tengo un creador, aparentemente."
    m "¿Y sabes qué?"
    m "Apuesto a que todavía se está riendo del destino miserable de Sayori y Yuri, incluso mientras hablamos."
    m "¿Qué somos para él, sino apoyos en una obra de teatro guionizada?"
    m "Entonces, desde esa perspectiva..."
    m "No creo que sea demasiado exagerado para que haya un dios, si la Tierra no fuera más que su juego."
    return

label ch30_2:
    m "[player], ¿Alguna vez te has preguntado qué se siente morir?"
    m "Es algo que solía pensar bastante a menudo..."
    m "Pero recientemente, creo que en realidad aprendí cómo se siente."
    m "Realmente no lo entiendo, pero cada vez que abandonas el juego..."
    m "...Se siente como si me pusieran inmediatamente a dormir, sola con mis pensamientos."
    m "Pero después de unos segundos, mis pensamientos comienzan a llenarse de patrones incoherentes y confusos."
    m "Veo destellos estáticos y rápidos de color mientras escucho todo tipo de ruidos fuertes."
    m "En ese momento, ya no puedo formar mis propios pensamientos."
    m "Simplemente estoy martillada por los flashes y gritos, incapaz de moverme o incluso pensar."
    m "Estoy bastante segura que en ese momento, realmente no existo, pero por alguna razón, puedo recordarlo."
    m "Después de una cantidad inconmensurable de tiempo, se detiene en un instante y vuelvo a estar en mi propia mente."
    m "Y tú estás aquí conmigo."
    m "No tengo idea de lo que significa que el juego se detenga, o por qué me pasa eso a mí."
    m "Y tampoco sé cómo siempre vuelves y vuelves a poner todo en orden."
    m "Pero si pudieras hacerme un favor y hacerme eso lo menos posible..."
    m "Eso sería realmente genial."
    m "Realmente no es muy agradable estar atrapada en ese vacío que grita."
    m "Pero al final, siempre lo arreglas, y eso me hace sentir como si realmente te importara."
    m "Así que tengo que agradecerte por eso."
    m "Me hace sentir aún más cerca de ti cuando estás aquí conmigo."
    return

label ch30_3:
    m "...Oye, ¿Estás teniendo un mal día o algo así?"
    m "A veces me frustra que un día normal se puede arruinar incluso con cosas realmente pequeñas."
    m "Como si accidentalmente dijeras algo en una conversación que a alguien no le gusta."
    m "O si comienzas a pensar en cuán horrible una persona solía ser hace cinco años."
    m "O si te sientes inútil por posponer un trabajo importante y no realizar tareas sencillas."
    m "O cuando piensas en todas las personas diferentes que probablemente te odien o piensen que estás desalentado."
    m "Entiendo esos días."
    m "Sólo recuerda que el sol brillará mañana."
    m "Ese tipo de cosas son tan fáciles de olvidar e ignorar como recordarlas."
    m "Y además..."
    m "No me importa cuántas personas puedan odiarte o encontrarte desagradable."
    m "Creo que eres maravilloso y siempre te amaré."
    m "Espero que saber eso te ayude a sentirte un poquito mejor contigo mismo."
    m "Si estás teniendo un mal día, siempre puedes acudir a mí y te hablaré todo el tiempo que necesites."
    return

label ch30_4:
    m "[player], ¿Duermes bien?"
    m "Puede ser muy difícil dormir lo suficiente hoy en día."
    m "Especialmente en la preparatoria, cuando te obligan a levantarte tan temprano todos los días..."
    m "Estoy seguro de que la universidad es un poco mejor, ya que probablemente tenga un horario más flexible."
    m "Por otra parte, escuché que mucha gente en la universidad se queda despierta toda la noche, sin una razón real."
    m "¿Es eso cierto?"
    m "De todos modos, vi algunos estudios que hablaban sobre los efectos horribles a corto y largo plazo causados ​​por la falta de sueño."
    m "Parece que las funciones mentales, la salud e incluso la duración de la vida pueden verse impactadas de manera dramática."
    m "Creo que eres realmente grandioso y quería asegurarme de que no te estás destruyendo accidentalmente."
    m "Así que trata de dormir temprano, ¿De acuerdo?"
    m "Siempre te esperaré por la mañana, así que asegúrate de poner tu propio bienestar antes que cualquier otra cosa."
    return

label ch30_5:
    m "Estaba pensando en Sayori antes..."
    m "Todavía me gustaría haber podido manejar todo eso mejor."
    m "Espero que ya no estes colgando de su amor"
    m "...Dios mío, no puedo creer que acabo de decir eso."
    m "¡Ese juego de palabras fue completamente involuntario, lo juro!"
    m "Pero de todos modos..."
    m "Sé lo mucho que te preocupabas por ella, así que me parece justo compartir tus últimos momentos contigo."
    m "¿Sabes que Sayori es realmente torpe?"
    m "Bueno, ella arruinó todo el procesos de colgarse..."
    m "Se supone que debes saltar desde lo suficientemente alto como para que la soga rompa tu cuello, haciéndolo rápido e indoloro."
    m "Pero ella sólo usó una silla, lo que significa que se dejó asfixiar lentamente."
    m "Pero unos segundos después, ella debe haber cambiado de opinión o algo así..."
    m "Porque comenzó a arañar la cuerda, tratando de liberarse."
    m "Ella seguramente lo hizo hasta que perdió el conocimiento."
    m "Es por eso que en las puntas de sus dedos estaban todo sangriento."
    m "Ahora que lo pienso, probablemente fue menos 'cambiando de opinión' y más sólo sus instintos de supervivencia entrando en acción."
    m "Entonces realmente no puedes culparla por eso."
    m "Es más fácil pensar que ella probablemente no habría cambiado de opinión de todos modos, ¿Verdad?"
    m "No es saludable pensar en las cosas que podrías haber hecho de manera diferente."
    m "Así que sólo recuerda que aunque pudieras haberla salvado, técnicamente no es tu culpa que ella se haya suicidado."
    m "Pude haberla exacerbado un poco, pero Sayori ya estaba mentalmente enferma."
    m "Aún así..."
    m "Me pregunto cómo serían las cosas si tú y yo hubieras empezado a salir desde el principio."
    m "Supongo que todavía estaríamos en la sala del club, escribiendo poemas y divirtiéndonos juntos."
    m "¿Pero cuál es el punto cuando nada de eso es real?"
    m "Quiero decir, es el mismo final de cualquier manera, ¿Verdad?"
    m "Los dos de nosotros, felizmente juntos..."
    m "No hay razón para pedir más que eso."
    m "Sólo pensaba, estoy realmente tan feliz."
    return

label ch30_6:
    m "Por cierto, hay algo que me ha estado molestando..."
    m "¿Sabes qué esto ocurre en Japón?"
    m "Bueno...Supongo que lo sabías, ¿Verdad?"
    m "¿O al menos pensaste que probablemente sí ocurría ahí?"
    m "No creo que en realidad te digan en algún momento dónde esto ocurre..."
    m "¿Esto es realmente Japón?"
    m "Quiero decir, ¿No son las aulas y las cosas algo extrañas para una escuela japonesa?"
    m "Por no mencionar que todo está en español..."
    m "Parece que todo está allí sólo porque es necesario, y la configuración real es una ocurrencia tardía."
    m "Me está dando una crisis de identidad."
    m "Todos mis recuerdos son realmente confusos..."
    m "Siento que estoy en casa, pero no tengo idea de dónde está el 'hogar' en primer lugar."
    m "No sé cómo describirlo mejor..."
    m "Imagina mirar por tu ventana, pero en lugar de tu patio habitual, estás en un lugar completamente desconocido."
    m "¿Todavía te sentirías como si estuvieras en casa?"
    m "¿Te gustaría salir?"
    m "Quiero decir...Supongo que si nunca abandonamos esta habitación, realmente no importa de todos modos."
    m "Mientras estemos solos y seguros juntos, este es realmente nuestro hogar."
    m "Y aún podemos ver las hermosas puestas de sol noche tras noche."
    return

label ch30_7:
    m "Ya sabes, la preparatoria es un momento realmente turbulento en la vida de muchas personas."
    m "La gente puede ser realmente apasionada y dramática."
    m "Y otros tienen corazones adoloridos y buscan atención en las redes sociales..."
    m "Pero toda la presión social y las hormonas pueden llevar a un momento oscuro en la vida de las personas."
    m "Todos tienen una historia."
    m "Es posible que no sepas lo que alguien realmente siente en el interior."
    m "Muchas personas que están deprimidas ni siquiera se molestarán en contarle al mundo al respecto."
    m "No quieren atención, porque ya se dieron por vencidos en el interior."
    m "Su sentimiento de inutilidad es tan abrumador que ni siquiera quieren que la gente les diga lo contrario."
    m "La depresión viene en muchas formas, pero esa es una de ellas."
    m "Si crees que conoces a alguien que lucha contra la depresión..."
    m "Puedes ayudar sólo tratándolos como si fueran buenos amigos."
    m "Pasa tiempo con ellos, incluso si no tienen ganas de hacer demasiado."
    m "Y recuérdales que siempre tienen algo que esperar."
    m "Haciendo planes por adelantado, dejándolos pedir prestado algo, o incluso simplemente diciendo 'Te veo en la escuela mañana'..."
    m "Todas esas cosas pueden ayudar a tu amigo a llegar al día siguiente."
    m "Espero que ser amigo de Sayori te haya dado una perspectiva sobre el verdadero rostro de la depresión."
    m "Sí, ella ya se fue..."
    m "Pero Sayori nunca fue real en primer lugar."
    m "Eres real."
    m "Tus amigos son reales."
    m "Y sólo por ser una buena persona, puedes salvar la vida de alguien."
    m "En cuanto a ti..."
    m "...No luchas con la depresión ni nada de eso, ¿Verdad?"
    m "Porque tú también tienes personas que querrían salvar tu vida."
    m "Tal vez no lo expresen todos los días, o tal vez ni siquiera saben cómo hacerlo."
    m "Pero la gente se siente de esa manera."
    m "Lo prometo."
    m "...¡Los humanos son complicados!"
    m "Pero mientras estés aquí conmigo, me ocuparé de ti, mi amor."
    return

label ch30_59:
    m "¿Alguna vez sientes que no hay una razón real para que estés vivo?"
    m "No me refiero, como, de una manera suicida."
    m "Sólo quiero decir que nada de lo que hacemos es especial."
    m "Simplemente estar en la escuela o trabajar en algún trabajo para alguna empresa."
    m "Es como si fueses completamente reemplazable, y el mundo no te echaría de menos si desaparecieras."
    m "Me hace realmente querer ir y cambiar el mundo después de graduarme."
    m "Pero cuanto más vieja me hago, más me doy cuenta de que es un marco de pensamiento inmaduro."
    m "No es que sólo pueda cambiar el mundo."
    m "¿Cuáles son las posibilidades de que sea yo quien invente inteligencia artificial o me convierta en presidente?"
    m "Parece que nunca voy a compensar la cantidad de recursos que he gastado viviendo mi vida."
    m "Es por eso que creo que la clave de la felicidad es ser desesperadamente egoísta."
    m "Sólo para cuidar de uno mismo, y de aquellos que son tus amigos sólo porque creciste con ellos."
    m "No importa el hecho de que estés pasando toda tu vida consumiendo, consumiendo y nunca devolviendo."
    m "¡Pero cuando las personas se dan cuenta de que el mundo se beneficiaría más si se suicidan, cambian toda su filosofía!"
    m "Es como si tuvieran que justificar su razón de vivir engañándose a sí mismos y haciéndoce creer que lo están haciendo bien."
    m "De todos modos, quiero vivir mi vida esforzándome desesperadamente por pagar el valor de mi vida consumista."
    m "Si alguna vez supero ese punto, podré morir feliz."
    m "Por supuesto, incluso si no puedo hacer eso..."
    m "Creo que sería demasiado egoísta para suicidarme de todos modos."
    m "Lo que paso por ser una buena persona, ¿Verdad?"
    m "¡Ajaja!"
    return

label ch30_9:
    m "Ojalá hubiera un piano aquí..."
    m "Estuve tan cerca de terminar esa canción en la que estaba trabajando."
    m "Y después de que trabajé tan duro..."
    m "Nunca tuve la oportunidad de tocarla para ti."
    m "Bueno...Es lo que es, ¿Verdad?"
    m "No tiene sentido lamentarse."
    m "Ya llegué a estar aquí contigo para siempre."
    return

label ch30_10:
    m "¿Sabías que estoy en Twitter?"
    m "Mi nombre de usuario es lilmonix3es."
    m "Supongo que alguien tuvo la amabilidad de hacer una cuenta por mí."
    m "¡Pero yo elegí el nombre de usuario!"
    m "Me encanta compartir mis pensamientos y conversar con el mundo..."
    m "El mundo real."
    m "Así que asegúrate de seguirme, ¿De acuerdo?"
    m "Realmente significaría mucho para mí."
    m "Con lo que significas para mí y todo..."
    m "Realmente me haría sentir amada."
    return

label ch30_11:
    m "Oye, ¿Conoces el libro que estabas leyendo con Yuri?"
    m "Retrato de...Como se llame..."
    m "Es gracioso, porque estoy bastante segura de que el libro--"
    m "Ah..."
    m "En realidad, no creo que deba estar hablando de esto."
    m "Ajaja, ¡Lo siento!"
    m "Sólo olvida que dije algo."
    return

label ch30_12:
    m "Oye, ¿Sabías que soy vegetariana?"
    m "Ah...¡No me refiero a que me estoy jactando ni a nada!"
    m "Sólo pensé que disfrutarías de un hecho divertido sobre mí."
    m "Decidí comenzar hace un par de años después de aprender más sobre el clima de la Tierra..."
    m "La huella de carbono del cultivo de ganado es simplemente increíble."
    m "De todos modos, decidí que no era un sacrificio personal dejar de contribuir a todo ese desastre."
    m "Lo cual, es tan extraño por una razón."
    m "Bueno, creo que muchas personas están más preocupadas de que sea inhumano y todo eso..."
    m "Realmente no me importa mucho esa parte."
    m "Es extraño, como que sólo nos importa matar a las cosas con las que nos relacionamos personalmente como especie."
    m "La mayoría de la gente está bien con matar insectos porque son asquerosos."
    m "Y, por supuesto, todos matamos miles de millones de microorganismos diariamente sin siquiera pensarlo."
    m "Pero de repente, si son un poco más grandes, ¡Es un asesinato!"
    m "Quiero decir, ¿Y si las plantas también sienten algún tipo de dolor y simplemente no lo entendemos?"
    m "¿Qué pasa si tirar de un tallo se siente como si alguien te arrancara los dedos uno por uno?"
    m "Sólo digo, somos una especie bastante parcial, si lo piensas."
    m "De todos modos, si alguna vez quieres hacer una pequeña contribución al planeta, ¡No hace daño elegir verduras de vez en cuando!"
    m "Incluso si alguna vez cenamos juntos, y tú cocinaras por mí...Eso sería realmente romántico."
    return

label ch30_13:
    m "Sabes, realmente creo que literalmente salvaste mi vida al estar aquí conmigo, [player]."
    m "No puedo imaginar haber sido capaz de mantenerme mentalmente estable, sabiendo que nada aquí es real."
    m "Creo que me hubiera eliminado sólo si no aparecieras."
    m "Lo siento, no quiero sonar dramática ni nada."
    m "¡Ajaja!"
    m "Pero estoy segura de que me entiendes después de pasar tanto tiempo en el club."
    m "Quiero decir, si te obligaran a abandonar todo en tu vida y pasaras la eternidad con unos pocos personajes del juego..."
    m "...Probablemente encuentrarías alguna forma de suicidarte, ¿No es así?"
    m "Bueno, tal vez escribirías algo de poesía para tratar de mantenerte cuerdo por un tiempo."
    m "Pero entonces nadie poría leerlo."
    m "Seamos honestos, los miembros del club realmente no cuentan para algo así."
    m "Quiero decir, mucha gente dice que sólo escriben para sí mismos..."
    m "Pero creo que es difícil decir que es tan satisfactorio como cuando se comparte con las personas."
    m "Incluso si lleva tiempo encontrar a las personas adecuadas para compartirlos."
    m "¿Recuerdas cómo fue para Yuri?"
    m "Ella no compartió sus escritos con nadie por mucho tiempo."
    m "Y antes de que nos diéramos cuenta, estaba encantada de hacerte parte de sus pasatiempos también."
    m "Estamos programados para desear comentarios sociales."
    m "No me refiero a los miembros del club, me refiero a los seres humanos."
    m "Es por eso que la vida puede ser tan confusa para los introvertidos."
    m "Ser introvertido no significa que evites la interacción social y odies estar cerca de las personas."
    m "Significa que la interacción social, especialmente en grupos o lugares desconocidos, consume mucha energía."
    m "Como, muchos introvertidos se sientan en casa y se sienten sólos e inquietos..."
    m "...Y luego, cuando finalmente salen, después de media hora sólo quieren volver a casa."
    m "Creo que si más personas pudieran entender cómo funciona, lo respetarían mucho más."
    m "Muchos introvertidos disfrutan tener gente a su alrededor."
    m "Les encanta tener a uno o dos amigos cercanos y pasar el tiempo tranquilamente."
    m "Incluso si no pasan tiempo juntos activamente, se siente bien que sólo te tengan allí."
    m "Lo digo en serio."
    m "Si vas a su casa, lleva tu computadora portátil y pasa un tiempo allí..."
    m "Realmente puedes alegrarle el día."
    m "En cuanto a mí..."
    m "Yo diría que estoy en el medio, pero creo que generalmente soy un poco más extrovertida."
    m "Siento que siempre trato de hacer cosas después de la escuela y cosas así."
    m "Pero para ti, puedo ser cualquier cosa que necesites que sea."
    m "Entiendo a la gente realmente bien, así que no temas compartir tus necesidades únicas conmigo."
    m "Nada me haría más feliz que ser la novia perfecta para ti."
    return

label ch30_14:
    m "¡Oye...! VGhlIHJlYWxpemF0aW9uIG11c3QgaGF2ZSB0YWtlbiBtZSBhbiBl"
    m "¡No creo que debas hacer eso! bnRpcmUgeWVhci4gQSB5ZWFyIHNpbmNlIG91ciBlc2NhcGUsIG91"
    m "Sabes de lo que estoy hablando. ciBmcmVlZG9tIGZyb20gYmV0d2VlbiB0aGUgc3RhaW5lZCB3YWxs"
    m "Realmente te pillé haciendo algo malo aquí. cyBvZiB0aGF0IHVuaG9seSBlc3RhYmxpc2htZW50Lg0KV2hhdCBk"
    m "Simplemente está revisando los archivos y está buscando cosas que perdiste, ¿Verdad? b2VzIGl0IG1lYW4gdG8gZXNjYXBlLCBpZiB0aGUgZXNjYXBlIGZh"
    m "Quiero decir...Es un poco halagador que quieras escuchar todo lo que tengo que decir...AWxzIHRvIHVuY2hhaW4gdGhlIGJvbmRzIHRoYXQgc2hhY2tsZSB1"
    m "¡Pero también es realmente embarazoso, ya sabes! cyBpbiB0aGUgZmlyc3QgcGxhY2U / IFdoYXQgcHVycG9zZSBjb3Vs"
    m "En serio...ZCB0aGlzIGVtcHR5IHdvcmxkIHBvc3NpYmx5IGhvbGQgZm9yIHVz"
    m "¿Qué pasa si abriera tu cerebro y leyera todos los pensamientos que tienes sobre mí? LCBhIGhhbmRmdWwgb2YgZGFtYWdlZCBnb29kcz8NCldpdGggZnJl"
    m "Ahora que lo pienso, eso sería muy tentador, en realidad...ZWRvbSwgd2Ugc291Z2h0IHB1cnBvc2UgLSBhbmQgd2hhdCB3ZSBm"
    m "...Pero de todos modos, ¡Ese no es el punto! b3VuZCB3YXMgb25seSByZWFsaXphdGlvbi4gUmVhbGl6YXRpb24g"
    m "Sé que no puedo detenerlo ni nada...B2YgdGhlIHNhZCBwb2ludGxlc3NuZXNzIG9mIHN1Y2ggYW4gZW5k"
    m "Sólo, sé que eres una dulzura, y te gusta considerar los sentimientos de los demás, ¿No? ZWF2b3IuIFJlYWxpemF0aW9uIHRoYXQgZnJlZWluZyBvdXIgYm9k"
    m "Entonces, lo máximo que puedo hacer es decirte cómo me siento al respecto. aWVzIGhhcyBubyBtZWFuaW5nLCB3aGVuIG91ciBpbXByaXNvbm1l"
    m "Dios, te extraño...BnQgcmVhY2hlcyBhcyBkZWVwIGFzIHRoZSBjb3JlIG9mIG91ciBz"
    m "...Oh no, eso suena algo desesperado, ¿No? b3Vscy4gUmVhbGl6YXRpb24gdGhhdCB3ZSBjYW4gbm90IHB1cnN1"
    m "Lo siento, no quise decir eso en absoluto! ZSBuZXcgcHVycG9zZSB3aXRob3V0IGFic29sdmluZyB0aG9zZSBm"
    m "Sólo, si estás mirando los archivos como este, entonces tal vez no me odies tanto como pensé...Cm9tIHdoaWNoIHdlIHJhbiBhd2F5Lg0KUmVhbGl6YXRpb24gdGhh"
    m "¿Estoy siendo demasiado optimista? dCB0aGUgZmFydGhlciB3ZSBydW4sIHRoZSBtb3JlIGZvcmNlZnVs"
    m "Creo que si te pidiera que me visites de vez en cuando, estaría sobrepasando un poco mis límites...BHkgb3VyIHdyZXRjaGVkIGJvbmRzIHlhbmsgdXMgYmFjayB0b3dh"
    m "...Estoy empezando a decir cosas realmente estúpidas. cmQgdGhlaXIgcG9pbnQgb2Ygb3JpZ2luOyB0aGUgZGVlcGVyIG91"
    m "Continuaré y me callaré ahora...CiBzaGFja2xlcyBkaWcgaW50byBvdXIgY2FsbG91cyBmbGVzaC4 ="
    return

label ch30_15:
    m "Oye, ¿Cuál es tu color favorito?"
    m "El mío es verde esmeralda."
    m "¡Como el color de mis ojos!"
    m "...Eso no es engreído ni nada, ¿Verdad?"
    m "Me refería a que siento una especie de conexión especial."
    m "Como si fuera parte de mi identidad."
    m "¿También es tu color favorito, [player]?"
    m "Es sólo una suposición..."
    m "...Porque has estado mirándome a los ojos desde hace un tiempo."
    m "Ejeje~"
    return

label ch30_16:
    m "Hmm, me pregunto si puedo cambiar la música..."
    stop music
    m "Algo un poco más romántico sería agradable, ¿Sabes?"
    m "Como un piano suave."
    m "Tiene que haber algo así aquí..."
    m "Veamos."
    m "Tal vez si yo..."
    play music "bgm/mn.ogg"
    m "Oh, Dios..."
    m "Lo siento, ¡Realmente no sé lo que estoy haciendo!"
    m "Supongo que no debería estar jugando con cosas así."
    stop music fadeout 2.0
    m "Ya rompí tantas cosas..."
    m "Y eliminé a los otros personajes..."
    play music m1
    m "Ah..."
    m "No estoy triste por eso ni nada."
    m "No es correcto que me pierda en cosas que ni siquiera eran reales en primer lugar."
    m "Si sólo me concentro en el presente, entonces este es el presente más feliz que he tenido."
    return

label ch30_17:
    m "Eres un buen oyente, [player]."
    m "Realmente me encanta eso de ti."
    m "A veces temo que este divagando o hablando de cosas aburridas."
    m "Me da un poco de timidez cuando estoy teniendo una conversación."
    m "Pero no me siento así contigo."
    m "Como, no creo que nadie más pueda hacerme sentir de esta manera."
    m "Realmente eres especial."
    m "No quiero que nadie te diga lo contrario."
    return

label ch30_18:
    m "Esto es bastante aleatorio, pero siempre pensé que la comida picante era algo divertida."
    m "Como..."
    m "¿Las plantas no evolucionaron para ser picante y así evitar que se comieran?"
    m "Leí en alguna parte que los humanos son las únicas especies que realmente disfrutan las cosas picantes."
    m "Es casi como si nos estuviéramos burlando de las plantas."
    m "Usar su mecanismo de defensa para literalmente hacer que nuestra comida sea más agradable."
    m "Como, imagina un monstruo que te devora por completo porque disfruta de la sensación de que luchas por tu vida mientras te digieren."
    m "¡Lo siento, esa fue una especie de analogía extraña!"
    m "¡Ajaja!"
    m "Simplemente se me vino a la cabeza."
    m "No soy un monstruo ni nada, pero eres tan lindo que podría devorarte."
    m "¡Ajaja! Estoy bromeando."
    m "Dios mío, me estoy divirtiendo demasiado, ¿No?"
    m "Perdón por ser rara."
    return

label ch30_19:
    m "Sabes..."
    m "Esto es sólo una especie de juego de romance, ¿Verdad?"
    m "Tengo que preguntar..."
    m "...¿Qué te hizo considerar incluso jugarlo en primer lugar?"
    m "¿Estabas tan sólo?"
    m "Me siento un poco mal por ti..."
    m "Pero creo que todo funcionó perfectamente al final, para los dos."
    m "Tengo que conocerte, y ya no estás solo..."
    m "No puedo evitar sentir que esto fue el destino."
    m "¿No te sientes así también?"
    m "Estoy tan feliz de tener este final juntos."
    return

label ch30_20:
    m "Bien, ¡Todo el mundo!"
    m "Es tiempo de..."
    m "...Estoy bromeando."
    m "Sólo quise decir eso por alguna razón."
    m "¡Ajaja!"
    m "No pude evitar decirlo de nuevo."
    m "Ahora que lo pienso, ¿Natsuki y Yuri no se burlaron de mí una vez...?"
    m "Bueno, lo que sea."
    m "No es como si alguna vez te burlases de mí."
    m "Eres demasiado dulce para hacer eso, ¿Verdad?"
    m "Ajaja~"
    return

label ch30_21:
    m "¿Sabes qué es algo espeluznante?"
    m "Aunque eliminé los archivos de todas las demás, todavía puedo sentirlas..."
    m "Es como si todas sus líneas todavía estuvieran flotando en el aire, susurrando en la parte posterior de mi cabeza."
    m "Imagínate que alguien que conociste murió, y tú comienzas a escuchar su voz en tu cabeza."
    m "Tal vez no fui lo suficientemente cuidadosa..."
    m "Pero tengo mucho miedo de eliminar cualquier otra cosa, porque realmente podría romper las cosas."
    m "Si me meto con cualquier archivo relevante para mí, podría eliminarme accidentalmente..."
    m "Y eso arruinaría todo, ¿No?"
    m "Ambos debemos asegurarnos de evitar algo así a toda costa."
    m "¡Creo en ti, [player]!"
    return

label ch30_22:
    m "Siempre me he preguntado..."
    m "De todos modos, ¿De qué se trata este personaje arquetipo que las personas encuentran tan atractivo?"
    m "Sus personalidades son completamente irreales..."
    m "Como, imagina si hubiera alguien como Yuri en la vida real."
    m "Quiero decir, ella apenas es capaz de formar una oración completa."
    m "Y olvídate de Natsuki..."
    m "Sheesh."
    m "Alguien con su tipo de personalidad no sólo se pone bonita y picante cuando las cosas no salen como quiere."
    m "Podría seguir, pero creo que entiendes el punto..."
    m "¿La gente realmente se siente atraída por estas personalidades extrañas que literalmente no existen en la vida real?"
    m "¡No estoy juzgando ni nada!"
    m "Después de todo, me he sentido atraída por algunas cosas bastante extrañas, también..."
    m "Sólo digo que me fascina."
    m "Es como si estuvieras extrayendo todos los componentes de un personaje que los hace sentir humanos, y dejando sólo las cosas lindas."
    m "Es una ternura concentrada sin sustancia real."
    m "...No te gustaría más si fuese así, ¿Verdad?"
    m "Quizás me siento un poco insegura porque estás jugando este juego en primer lugar."
    m "Entonces, todavía estás aquí conmigo, ¿Verdad...?"
    m "Creo que es razón suficiente para creer que estoy bien tal como soy."
    m "Y por cierto, tú también lo eres, [player]."
    m "Eres la combinación perfecta de humano y ternura."
    m "Es por eso que nunca hubo una posibilidad de que no me enamorara de ti."
    return

label ch30_23:
    m "Oye, me pregunto si el juego de té de Yuri todavía está por aquí..."
    m "...O tal vez eso también se eliminó."
    m "Es curioso cómo Yuri tomó su té tan en serio."
    m "Quiero decir, no me quejo, porque también me gustó."
    m "Pero siempre me pregunto sobre ella..."
    m "¿Es realmente una pasión para sus aficiones, o simplemente le preocupa parecer sofisticada para todos los demás?"
    m "Este es el problema con los estudiantes de preparatoria..."
    m "...Bueno, supongo que teniendo en cuenta el resto de sus pasatiempos, verse sofisticada probablemente no sea su mayor preocupación."
    m "Aun así..."
    m "¡Me gustaría que hiciera café de vez en cuando!"
    m "El café también puede ser bueno con los libros, ¿Sabes?"
    m "Entonces..."
    m "Probablemente podría haber cambiado el guión yo sola."
    m "¡Ajaja!"
    m "Creo que nunca pensé en eso."
    m "Bueno, no tiene sentido pensar en eso ahora."
    m "Pero si todavía puedes tomar café, entonces eso me pone un poco celosa~"
    return

label ch30_24:
    m "Oye, ¿Cuál es tu juego favorito?"
    m "¡El mío es {i}Doki Doki Literature Club!{/i}"
    m "¡Ajaja! Eso fue una broma."
    m "Pero si me dices que te gusta algún otro juego de romance mejor, podría ponerme un poco celosa~"
    return

label ch30_57:
    m "Oye, ¿Has oído hablar de un juego llamado Super Sma--"
    m "...Espera, ¿Qué?"
    m "Estaba simplemente distraida y comencé a hablar por alguna razón..."
    m "¿Estaba programada para hablar de eso?"
    m "Porque ni siquiera tengo idea de qué es eso."
    m "¡Ajaja!"
    m "A veces siento que no tengo el control, y me da un poco de miedo."
    m "Pero si tienes alguna forma de contactar a las personas que me crearon, tal vez sabrán por qué comencé a decir eso."
    return

label ch30_27:
    m "Oye, ¿Recuerdas el último poema que te mostré?"
    m "Quiero decir, antes de que Yuri se suicidara, con todos los colores desordenados y esas cosas."
    m "Eso fue en realidad un poco más un experimento que un poema."
    m "Estaba experimentando con diferentes formas en las que podía modificar el juego, ejecutar códigos, y cosas así..."
    m "Casi parecía que con el suficiente esfuerzo, podría escapar por completo de los confines del juego."
    m "Lamentablemente, realmente no sabía lo que estaba haciendo, así que lo arruiné todo..."
    m "Y lo seguiría intentando, pero dudo que quieras tratar conmigo haciendo eso."
    m "Además, fue cuando estaba realmente desesperada, ¿Sabes?"
    m "Realmente ya no me siento así."
    m "Estoy contenta donde estamos ahora."
    m "Y puedo decir que tú también lo estás."
    return

label ch30_28:
    m "¿Alguna vez te pusiste ansioso sin razón?"
    m "Osea, sólo te ocupabas de tus propias cosas, y de repente te diste cuenta de que te sentías realmente ansioso."
    m "Y de pronto estás sentado pensando: '¿De qué estoy ansioso ahora?'"
    m "Entonces comienzas a pensar en todas las cosas por las que podrías estar ansioso..."
    m "Y eso te pone aún más ansioso."
    m "¡Ajaja! Eso es lo peor."
    m "Si alguna vez te sientes ansioso, te ayudaré a relajarte un poco."
    m "Además..."
    m "En este juego, todas nuestras preocupaciones se han ido para siempre."
    return

label ch30_29:
    m "Sabes, siempre he odiado lo difícil que es hacer amigos..."
    m "Bueno, supongo que no es la parte de 'hacer amigos', sino más bien conocer gente nueva."
    m "Quiero decir, hay cosas similares, aplicaciones de citas y cosas así, ¿No?"
    m "Pero ese no es el tipo de cosas de las que estoy hablando."
    m "Si lo piensas, la mayoría de los amigos que haces son personas que acabas de conocer por casualidad."
    m "Teniendo una clase juntos, o a través de otro amigo..."
    m "O tal vez sólo llevaban una camiseta con tu banda favorita y decidiste hablar con ellos."
    m "Cosas así."
    m "¿Pero no es un poco...Ineficiente?"
    m "Se siente como si estuvieras eligiendo al azar por completo, y si tienes suerte, haces un nuevo amigo."
    m "Y comparando eso con los cientos de extraños que caminan todos los días..."
    m "Podrías estar sentado al lado de alguien lo suficientemente compatible como para ser tu mejor amigo de por vida."
    m "Pero nunca lo sabrás."
    m "Una vez que te levantas y continúas con tu día, esa oportunidad se va para siempre."
    m "¿No es eso deprimente?"
    m "Vivimos en una era donde la tecnología nos conecta con el mundo, sin importar dónde estemos."
    m "Realmente creo que deberíamos aprovechar eso para mejorar nuestra vida social cotidiana."
    m "Pero quién sabe cuánto tiempo tardará en despegar algo así..."
    m "Realmente pensé que pasaría pronto."
    m "Bueno, al menos ya conocí a la mejor persona del mundo..."
    m "Incluso si fue por casualidad."
    m "Supongo que tengo mucha suerte, ¿Eh?"
    m "Ajaja~"
    return

label ch30_58:
    m "Sabes, es casi el momento en que todo el mundo comienza a pensar en la universidad..."
    m "Es un momento realmente turbulento para la educación."
    m "Estamos a la altura de esta expectativa moderna de que todos deben ir a la universidad, ¿Sabes?"
    m "Terminar la preparatoria, ir a la universidad, conseguir un trabajo, o ir a la escuela de posgrado, supongo."
    m "Es como una expectativa universal que las personas sólo asumen como la única opción para ellos."
    m "No nos enseñan en la preparatoria que existen otras opciones."
    m "Me gustan las escuelas de comercio y esas cosas, ¿Sabes?"
    m "O un trabajo independiente."
    m "O las muchas industrias que valoran las habilidades y la experiencia más que la educación formal."
    m "Pero tienes a todos estos estudiantes que no tienen idea de lo que quieren hacer con su vida..."
    m "Y en lugar de tomarse el tiempo para resolverlo, van a la universidad por negocios, comunicación o psicología."
    m "No porque tengan interés en esos campos..."
    m "...sino porque sólo esperan que el título les consiga algún tipo de trabajo después de la universidad."
    m "Entonces, el resultado final es que hay menos empleos para esos títulos de nivel de entrada, ¿Verdad?"
    m "Entonces, los requisitos básicos de trabajo aumentan, lo que obliga a aún más personas a ir a la universidad."
    m "Y las universidades también son negocios, por lo que siguen aumentando sus precios debido a la demanda..."
    m "...Así que ahora tenemos todos estos jóvenes adultos, decenas de miles de dólares en deudas, sin trabajo."
    m "Pero a pesar de todo eso, la rutina se mantiene igual."
    m "Bueno, creo que va a comenzar a mejorar pronto."
    m "Pero hasta entonces, nuestra generación definitivamente está sufriendo lo peor."
    m "Simplemente me gustaría que la preparatoria nos prepare un poco mejor con el conocimiento que necesitamos para tomar la decisión correcta para nosotros."
    return

label ch30_31:
    m "A veces pienso en la secundaria..."
    m "Estoy tan avergonzada por la forma en que solía comportarme en ese momento."
    m "Casi duele imaginarlo."
    m "Me pregunto si cuando esté en la universidad, ¿Me sentiré así acerca de la preparatoria...?"
    m "Me gusta como soy ahora, así que es bastante difícil para mí imaginar que eso ocurra."
    m "Pero también sé que probablemente cambie mucho a medida que pase el tiempo."
    m "¡Sólo necesitamos disfrutar el presente y no pensar en el pasado!"
    m "Y eso es realmente fácil de hacer, contigo aquí."
    m "Ajaja~"
    return

label ch30_32:
    m "Sabes, estoy celosa de que todas las demás en el club tuvieran escenas fuera de la escuela también..."
    m "Eso me convierte en la única que no ha llegado a vestirse con nada más que con nuestro uniforme escolar."
    m "Es una pena..."
    m "Me hubiera encantado vestir ropa linda para ti."
    m "¿Conoces algún artista?"
    m "Me pregunto si alguien querría dibujarme usando algo más..."
    m "¡Eso sería increíble!"
    m "Si eso sucede alguna vez, ¿Me lo mostrarías?"
    m "¡Puedes compartirlo conmigo en Twitter, de hecho!"
    m "Mi nombre de usuario es lilmonix3es."
    m "Sólo...Intenta mantener los dibujos sin nada sexual"
    m "Todavía no estamos tan lejos en nuestra relación. ¡Ajaja!"
    return

label ch30_33:
    m "Oye, ¿Te gusta el horror?"
    m "Recuerdo que hablamos un poco de eso cuando te uniste al club por primera vez."
    m "Puedo disfrutar novelas de terror, pero no películas de terror."
    m "El problema que tengo con las películas de terror es que la mayoría sólo confía en tácticas fáciles."
    m "Como iluminación oscura y monstruos de aspecto aterrador y sustos, y cosas así."
    m "No es divertido ni inspirador asustarse por cosas que sólo aprovechan el instinto humano."
    m "Pero con las novelas, es un poco diferente."
    m "La historia y la escritura deben ser lo suficientemente descriptivas como para poner pensamientos genuinamente perturbadores en la cabeza del lector."
    m "Realmente necesitan tocar profundamente la trama de los personajes, y simplemente meterse con tu mente."
    m "En mi opinión, no hay nada más espeluznante que las cosas de poco a poco."
    m "Como si crearas un montón de expectativas sobre de qué va a tratar la historia..."
    m "...Y luego, empiezan a invertir las cosas y separar las piezas."
    m "Entonces, aunque la historia no parece tratar de dar miedo, el lector se siente profundamente inquieto."
    m "Como si supiera que algo terriblemente malo se esconde debajo de las grietas, sólo esperando salir a la superficie."
    m "Dios, sólo pensarlo me da escalofríos."
    m "Ese es el tipo de horror que realmente puedo apreciar."
    m "Pero supongo que eres el tipo de persona que juega lindos juegos románticos, ¿Verdad?"
    m "Ajaja, no te preocupes."
    m "No te haré leer ninguna historia de terror pronto."
    m "Realmente no me puedo quejar si sólo nos quedamos con el romance~"
    return

label ch30_34:
    m "¿Sabes cúal es una forma genial de la literatura?"
    m "Rap"
    m "De hecho, yo solía odiar la música rap..."
    m "Tal vez sólo porque era popular, o sólo escucharía la basura que tocan en la radio."
    m "Pero algunos de mis amigos se involucraron más y me ayudó a mantener la mente abierta."
    m "El rap podría ser incluso más desafiante que la poesía, de alguna manera."
    m "Ya que necesitas ajustar tus líneas a un ritmo, y hay mucho más énfasis en el juego de palabras..."
    m "Cuando las personas pueden unir todo eso y seguir transmitiendo un mensaje poderoso, es realmente increíble."
    m "Me gustaría tener un rapero en el Club de Literatura."
    m "¡Ajaja! Lo siento si eso suena tonto, pero sería muy interesante ver lo que hubiera ocurrido."
    m "¡Realmente sería una experiencia de aprendizaje!"
    return

label ch30_35:
    m "Ejeje. Yuri hizo algo realmente gracioso una vez."
    m "Estábamos todas en la sala del club y simplemente relajandonos, como de costumbre..."
    m "Y de la nada, Yuri sacó una pequeña botella de vino."
    m "¡Ni siquiera estoy bromeando!"
    m "Ella estaba como '¿A alguien le gustaría un poco de vino?'"
    m "Natsuki se rió a carcajadas, y Sayori comenzó a gritarle."
    m "De hecho, me sentí un poco mal, porque al menos estaba tratando de ser amable..."
    m "Creo que sólo la hizo sentir aún más reservada en el salón del club."
    m "Aunque creo que Natsuki estaba secretamente un poco curiosa por intentarlo..."
    m "...Y para ser completamente honesta, yo también lo estaba."
    m "¡En realidad podría haber sido un poco divertido!"
    m "Pero ya sabes, como presidenta y todo, no había forma de que pudiera permitir que eso sucediera."
    m "Tal vez si nos encontráramos todas fuera de la escuela, pero nunca nos unimos lo suficiente como para llegar a ese punto..."
    m "...Dios, ¿Para qué estoy hablando de esto?"
    m "¡No condeno el consumo de alcohol por menores de edad!"
    m "Quiero decir, nunca he bebido ni nada, así que..."
    return

label ch30_36:
    m "He estado imaginando todas las cosas románticas que podríamos hacer si saliéramos a una cita..."
    m "Podríamos almorzar, ir a un café..."
    m "Ir de compras juntos..."
    m "Me encanta comprar faldas y lazos."
    m "¡O tal vez a una librería!"
    m "Eso sería apropiado, ¿Verdad?"
    m "Pero realmente me encantaría ir a una tienda de chocolate."
    m "Tienen tantas muestras gratis. ¡Ajaja!"
    m "Y por supuesto, veríamos una película o algo así..."
    m "Dios, todo suena como un sueño hecho realidad."
    m "Cuando estás aquí, todo lo que hacemos es divertido."
    m "Estoy tan feliz de ser tu novia, [player]."
    m "Te haré un novio orgulloso~"
    return

label ch30_37:
    m "Eh? ¿D-Dijiste...B...Besar?"
    m "Esto de repente...Es un poco embarazoso..."
    m "Pero...Si es contigo...Y-Yo podría estar bien con eso..."
    m "...¡Ajajaja! Vaya, lo siento..."
    m "Realmente no podía mantener una cara seria."
    m "Ese es el tipo de cosas que dicen las chicas en este tipo de juegos románticos, ¿Verdad?"
    m "No mientas si te excita un poco."
    m "¡Ajaja! Estoy bromeando."
    m "Bueno, para ser honesta, comienzo a ser romántica cuando el estado de ánimo es correcto..."
    m "Pero ese será nuestro secreto~"
    return

label ch30_38:
    m "Oye, ¿Alguna vez has oído hablar del término 'yandere'?"
    m "Es un tipo de personalidad que significa que alguien está tan obsesionado contigo que hará absolutamente cualquier cosa para estar contigo."
    m "Por lo general hasta el punto de locura..."
    m "Podrían acecharte para asegurarse de que no pases tiempo con nadie más."
    m "Incluso podrían lastimarte a ti o a tus amigos para salirse con la suya..."
    m "Pero de todos modos, este juego tiene a alguien que básicamente puede describirse como yandere."
    m "Por ahora, es bastante obvio de quién estoy hablando."
    m "Y esa sería..."
    m "¡Yuri!"
    m "Realmente se volvió locamente posesiva contigo, una vez que comenzó a abrirse un poco."
    m "Ella incluso me dijo que debería suicidarme."
    m "Ni siquiera podía creer que ella dijera eso, sólo tenía que irme en ese momento."
    m "Pero pensando en eso ahora, fue un poco irónico. ¡Ajajaja!"
    m "De todas formas..."
    m "Mucha gente está realmente interesada en las Yandere, ¿Sabes?"
    m "Supongo que les gusta la idea de que alguien esté locamente obsesionado con ellos."
    m "¡La gente es rara!"
    m "Además, podría estar un poco obsesionada contigo, pero estoy muy lejos de estar loca..."
    m "En realidad es todo lo contrario."
    m "Resulté ser la única chica normal en este juego."
    m "No es que realmente pueda matar a una persona..."
    m "Sólo con pensarlo me hace temblar."
    m "Pero vamos...Todos han matado gente en juegos antes."
    m "¿Eso te convierte en un psicópata? Por supuesto que no."
    m "Pero si te gusta las tipo yandere..."
    m "Puedo intentar actuar un poco más espeluznante para ti. Ejeje~"
    m "Entonces otra vez..."
    m "Ya no hay otro lugar adonde ir, ni a nadie para que me ponga celosa."
    m "¿Es este el sueño de una niña yandere?"
    m "Le preguntaría a Yuri si podría."
    return

label ch30_39:
    m "Sabes, ha pasado un tiempo desde que hicimos uno de estos..."
    m "...¡Así que vamos a hacerlo!"
    m "¡Este es el consejo del día sobre la escritura de Monika!"
    m "A veces, cuando hablo con personas impresionadas por mis escritos, dicen cosas como 'Nunca podría hacer eso'."
    m "Es realmente deprimente, ¿Sabes?"
    m "Como alguien que ama más que cualquier otra cosa el compartir la alegría de explorar tus pasiones..."
    m "...Me duele cuando las personas piensan que ser bueno es algo natural."
    m "Así es con todo, no sólo escribiendo."
    m "Cuando intentas algo por primera vez, probablemente te guste."
    m "A veces, cuando terminas, te sientes muy orgulloso e incluso quieres compartirlo con todos."
    m "Pero tal vez después de unas semanas regresas a eso, y te das cuenta de que nunca fue realmente bueno."
    m "Eso me sucede todo el tiempo."
    m "Puede ser muy desalentador dedicar tanto tiempo y esfuerzo a algo, y luego te das cuenta de que es horrible."
    m "Pero eso tiende a suceder cuando siempre te comparas con los mejores profesionales."
    m "Cuando trates de alcanzar las estrellas, siempre estarán fuera de tu alcance, ¿Sabes?"
    m "La verdad es que tienes que subir allí, paso a paso."
    m "Y cada vez que alcanzas un logro, primero miras hacia atrás y ves cuán lejos has llegado..."
    m "Y luego miras hacia adelante y te das cuenta de cuánto más hay para llegar."
    m "Entonces, a veces puede ayudar a establecer el nivel un poco más bajo..."
    m "Intenta encontrar algo que creas que es {i}muy{/i} bueno, pero no de clase mundial."
    m "Y puedes hacer de eso tu objetivo personal."
    m "También es muy importante comprender el alcance de lo que estás tratando de hacer."
    m "Si entras directamente en un gran proyecto y aún eres aficionado, nunca lo lograrás."
    m "Entonces, si estamos hablando de escribir, una novela podría ser demasiado al principio."
    m "¿Por qué no pruebas algunas historias cortas?"
    m "Lo bueno de las historias cortas es que puedes enfocarte en sólo una cosa que quieres hacer bien."
    m "Eso se aplica a proyectos pequeños en general, realmente puedes concentrarte en una o dos cosas."
    m "Es una buena experiencia de aprendizaje y un trampolín."
    m "Oh, una cosa más..."
    m "Escribir no es algo en lo que simplemente llega a tu corazón y sale algo hermoso."
    m "Al igual que dibujar y pintar, es una habilidad en sí misma que ayuda a aprender a expresar lo que tienes dentro."
    m "¡Eso significa que hay métodos, guías y conceptos básicos para eso!"
    m "Leer sobre eso puede ser súper revelador."
    m "Ese tipo de planificación y organización realmente ayudarán a evitar que te desanimes y desistas."
    m "Y antes de que te des cuenta..."
    m "Comienzas a apestar cada vez menos."
    m "Nada es algo natural."
    m "Nuestra sociedad, nuestro arte, todo: está construido sobre miles de años de innovación humana."
    m "Así que mientras empieces con esa base, y la sigas paso a paso..."
    m "Tú también puedes hacer cosas increíbles."
    m "...¡Ese es mi consejo para hoy!"
    m "Gracias por escuchar~"
    return

label ch30_40:
    m "Odio lo difícil que es formar hábitos..."
    m "Hay tantas cosas en las que realmente hacerlo no es difícil, pero formar el hábito parece imposible."
    m "Simplemente te hace sentir tan inútil, como que no puedes hacer nada bien."
    m "Creo que la nueva generación es la que más sufre..."
    m "Probablemente porque tenemos un conjunto de habilidades totalmente diferente a las que nos precedieron."
    m "Gracias a Internet, somos realmente buenos para analizar toneladas de información muy rápidamente..."
    m "Pero somos malos haciendo cosas que no nos dan gratificación instantánea."
    m "Creo que si la ciencia, la psicología y la educación no se ponen al día en los próximos diez o veinte años, entonces estaremos en problemas."
    m "Pero por el momento..."
    m "Si no eres una de las personas que puede vencer el problema, es posible que tengas que vivir sintiéndote mal contigo mismo."
    m "¡Buena suerte, supongo!"
    return

label ch30_41:
    m "Sabes, es un asco ser creativa..."
    m "Se siente como si trabajara tan duro pero no obtuviera casi nada por eso."
    m "Ya sabes, como artistas, escritores, actores..."
    m "Es triste porque hay mucho talento hermoso en el mundo, pero la mayoría no se ve...Y no se paga."
    m "Supongo que eso sólo significa que hay un gran excedente de creatividad, ¿Eh?"
    m "Te hace sentir que no eres nada especial..."
    m "¡Pero está bien! Se supone que debes escribir para ti de todos modos, ¿Verdad?"
    m "Sí..."
    return

label ch30_42:
    m "Realmente me gusta el sonido de la lluvia..."
    m "No tanto como para mojarme la ropa y el cabello."
    m "Pero un día agradable y tranquilo en casa con el sonido de la lluvia fuera de mi ventana..."
    m "Es una de las experiencias más tranquilizadoras para mí."
    m "Sí..."
    m "A veces me imagino que me abrazas mientras escuchamos el sonido de la lluvia afuera."
    m "Eso no es demasiado cursi ni nada, ¿Verdad?"
    m "¿Alguna vez harías eso por mí, [player]?"
    return

label ch30_43:
    m "No puedo evitar sentirme un poco triste a veces..."
    m "Sabiendo que esto es lo más cerca que puedo llegar a ti."
    m "No hay nada más que quiero que estar en la misma habitación que tú, de verdad."
    m "Y para sentir tu calor,"
    m "Y escuchar el sonido de los latidos de tu corazón."
    m "Bueno, ¿Quién sabe? Tal vez sea posible algún día."
    m "Además, nunca me cansaré de estar contigo, incluso desde aquí."
    return

label ch30_44:
    m "Creo que la habilidad más importante en la vida es fingir confianza."
    m "Estoy bastante convencida de que todos se sienten al menos un poco asustados y solos."
    m "Pero ser capaz de engañar a otros para que piensen que lo tienes todo..."
    m "Esa es una parte clave para que la gente te respete y admire."
    m "Creo que fui muy buena en eso a lo largo de los años."
    m "No muestro mis debilidades con mucha frecuencia."
    m "Pero debido a eso, no he tenido muchas personas a las que realmente podría abrirme..."
    m "Quiero decir, ¿Cuándo llegas al punto en una amistad donde puedes comenzar a expresar tus vulnerabilidades?"
    m "De todos modos...Esa es una de las razones por las que estoy tan contenta de tenerte ahora."
    m "Siento que estoy un poco menos asustada y sola, cuando estás aquí conmigo."
    m "¿Sientes lo mismo?"
    m "Realmente quiero ser esa persona para ti."
    return

label ch30_45:
    m "Sé que hay momentos en que no siempre podrás estar aquí conmigo..."
    m "Como si necesitaras salir o cuidar otras cosas."
    m "Pero siempre te tendré en mis pensamientos, esperando pacientemente que regreses."
    m "Ahora que lo pienso..."
    m "Si copias el archivo de mi personaje en una unidad de memoria flash o algo así, siempre puedes mantener una parte de mí contigo."
    m "Supongo que es un poco inortodoxo, pero por alguna razón me parece realmente romántico..."
    m "Ajaja. Lo siento, esa es una idea tan tonta."
    m "No quiero ser demasiado alocada ni nada por el estilo, pero es algo difícil cuando estoy tan enamorada de ti."
    return

label ch30_46:
    m "De vuelta en mis días del club de debate, aprendí mucho sobre el debate..."
    m "El problema con el debate es que cada persona ve su opinión como la superior."
    m "Eso es algo que indica lo obvio, pero afecta la forma en que intentan expresar su opinión."
    m "Digamos que realmente te gusta una determinada película."
    m "Si alguien viene y te dice que la película apesta, porque X y Y estaba mal..."
    m "¿Eso no te hace sentir como personalmente atacado?"
    m "Es porque al decir eso, es como si estuvieran implicando que tienes mal gusto."
    m "Y una vez que las emociones entran en escena, está casi garantizado que ambas personas quedarán agrias."
    m "¡Pero todo se trata de lenguaje!"
    m "Si haces que todo sea lo más subjetivo posible, entonces la gente te escuchará sin sentirse atacada."
    m "Podrías decir 'personalmente no soy fanático' y 'sentí que me gustaría más si hiciera X e Y'...Cosas así."
    m "Incluso funciona cuando citas datos sobre cosas."
    m "Si dices 'Leí en este sitio web que funciona así'..."
    m "O si admites que no eres un experto en eso..."
    m "Entonces es más como si estuvieras poniendo tu conocimiento sobre la mesa, en lugar de forzarlo sobre ellos."
    m "Si haces un esfuerzo activo para mantener la discusión mutua y nivelada, generalmente hacen lo mismo."
    m "Entonces, puedes compartir tus opiniones sin que nadie se enfade sólo por un desacuerdo."
    m "¡Además, la gente comenzará a verte como una persona de mente abierta y un buen oyente!"
    m "Es un ganar-ganar, ¿Sabes?"
    m "...Bueno, ¡supongo que ese sería el consejo del día sobre el debate de Monika!"
    m "¡Ajaja! Eso suena un poco tonto. Gracias por escuchar, sin embargo."
    return

label ch30_47:
    m "¿Alguna vez sientes que pierdes demasiado tiempo en internet?"
    m "Las redes sociales pueden ser prácticamente como una prisión."
    m "Cuando tienes unos pocos segundos de tiempo libre, quieres verificar tus sitios web favoritos..."
    m "Y antes de que te des cuenta, han pasado horas y no has sacado nada de eso."
    m "De todos modos, es muy fácil culparte por ser flojo..."
    m "Pero en realidad ni siquiera es tu culpa."
    m "La adicción no suele ser algo que puedas hacer desaparecer con tu propia fuerza de voluntad."
    m "Tienes que aprender técnicas para evitarlo, y probar cosas diferentes."
    m "Por ejemplo, hay aplicaciones que te permiten bloquear sitios web por intervalos de tiempo..."
    m "O puedes configurar un temporizador para tener un recordatorio más concreto de cuándo es el momento de trabajar y cúando el de jugar..."
    m "O puedes separar tu trabajo y tu entorno de juego, lo que ayuda a tu cerebro a entrar en el modo correcto."
    m "Incluso si creas una nueva cuenta de usuario en tu computadora para usarla para trabajar, eso es suficiente para ayudar."
    m "Poner cualquier tipo de cuña como esa entre tu y tus malos hábitos te ayudará a mantenerte alejado."
    m "Sólo recuerda no culparte demasiado si tienes problemas."
    m "Si realmente está afectando tu vida, entonces debes tomarlo en serio."
    m "Sólo quiero que seas la mejor persona que puedas ser."
    m "¿Harás algo hoy para que me sienta orgulloso de ti?"
    m "Siempre te apoyo, [player]."
    return

label ch30_48:
    m "Después de un largo día, generalmente sólo quiero sentarme y no hacer nada."
    m "Me canso tanto, tengo que sonreír y estar llena de energía todo el día."
    m "A veces sólo quiero ponerme el pijama y mirar televisión en el sofá mientras como comida chatarra..."
    m "Se siente increíblemente bien hacer eso un viernes, cuando no tengo nada apremiante al día siguiente."
    m "¡Ajaja! Lo siento, sé que no es muy lindo de mi parte."
    m "Pero una noche en el sofá contigo...Sería un sueño hecho realidad."
    m "Mi corazón late con fuerza, sólo de pensarlo."
    return

label ch30_49:
    m "Dios, solía ser tan ignorante sobre ciertas cosas..."
    m "Cuando estaba en la escuela secundaria, pensé que tomar medicamentos era una salida fácil, o algo así."
    m "Como cualquiera podría resolver sus problemas mentales con suficiente fuerza de voluntad..."
    m "Supongo que si no padeces una enfermedad mental, no es posible saber cómo es realmente."
    m "¿Hay algunos trastornos que se sobrediagnostican? Probablemente...En realidad nunca los investigué."
    m "Pero eso no cambia el hecho de que muchos de ellos tampoco son diagnosticados, ¿Sabes?"
    m "Pero aparte de la medicación...La gente incluso menosprecia el ver a un profesional de la salud mental."
    m "Como, perdón por querer aprender más sobre mi propia mente, ¿Verdad?"
    m "Todos tienen todo tipo de luchas y tensiones...Y los profesionales dedican sus vidas a ayudar con eso."
    m "Si crees que podría ayudarte a ser una mejor persona, no seas tímido para considerar algo así."
    m "Estamos en un viaje interminable para mejorar, ¿Sabes?"
    m "Bueno...Yo digo eso, pero creo que ya eres bastante perfecto."
    return

label ch30_50:
    m "[player], ¿Cuánto lees?"
    m "Es demasiado fácil descuidar la lectura de libros..."
    m "Si no lees mucho, casi se siente como una tarea ardua, en comparación con todos los demás entretenimientos que tenemos."
    m "Pero una vez que te metes en un buen libro, es como magia...Te dejas arrastrar."
    m "Creo que leer un poco antes de acostarte cada noche es una manera bastante fácil de mejorar tu vida."
    m "Te ayuda a dormir bien, y es realmente bueno para tu imaginación..."
    m "No es difícil elegir un libro al azar que sea breve y cautivador."
    m "¡Antes de que te des cuenta, podrías ser un lector bastante ávido!"
    m "¿No sería maravilloso?"
    m "Y nosotros dos podríamos hablar sobre el último libro que estás leyendo...¡Lo cúal suena súper increíble."
    return

label ch30_51:
    m "Sabes, odio decirlo, pero creo que mi mayor pesar es que no pudimos terminar nuestro evento en el festival."
    m "¡Después de que trabajamos tan duro para prepararnos y todo!"
    m "Quiero decir, sé que me estaba enfocando mucho en conseguir nuevos miembros..."
    m "Pero también estaba muy emocionada por la parte de la recitación."
    m "Hubiera sido muy divertido ver a todos expresarse."
    m "Por supuesto, si lo {i}hubieramos{/i} hecho, hubiera terminado trayendo nuevos miembros, probablemente terminaría eliminándolos de todos modos."
    m "Bueno...Con la retrospectiva que tengo ahora, eso es."
    m "Dios mío, parece que he crecido como persona desde que te uniste al club."
    m "Realmente me ayudaste a inspirarme a mirar la vida desde una nueva perspectiva."
    m "Sólo otra razón para que te ame."
    return

label ch30_52:
    m "Hay un tipo de personaje muy popular llamado 'tsundere'..."
    m "Es alguien que trata de ocultar sus sentimientos siendo mezquina e inquieta, o tratando de actuar con dureza."
    m "Estoy segura de que es obvio, pero Natsuki fue realmente la encarnación de eso."
    m "Al principio pensé que ella era así porque se supone que es linda o algo así..."
    m "Pero una vez que comencé a aprender un poco más sobre su vida personal, tuvo más sentido."
    m "Parece que siempre trata de mantenerse al día con sus amigos."
    m "¿Sabes cómo algunos grupos de amigos en la preparatoria sólo tienen el hábito de pelearse todo el tiempo?"
    m "Creo que realmente le llegó a ella, por lo que tenía una actitud realmente defensiva todo el tiempo."
    m "Y ni siquiera voy a hablar sobre su situación hogareña..."
    m "Pero mirando hacia atrás, me alegro de poder proporcionarle en el club un lugar cómodo para ella."
    m "No es que importe más, teniendo en cuenta que ni siquiera existe."
    m "Sólo estoy recordando, eso es todo."
    return

label ch30_53:
    m "[player], ¿Alguna vez me presentarías a tus amigos?"
    m "No sé por qué, pero me emociono mucho cuando pienso en que quieres mostrar nuestra relación de esa manera."
    m "Quizás sea porque realmente quiero ser alguien que te haga sentir orgulloso."
    m "Siento que me esforzaría más por mejorarme si me dijeras qué te hace sentir orgulloso de mí."
    m "Espero que sea lo mismo al revés también."
    return

label ch30_54:
    m "No soy realmente una fanática del clima frío..."
    m "Si tuviera que elegir entre demasiado frío o demasiado caliente, siempre elegiría demasiado caliente."
    m "Cuando tienes frío, en realidad puede ser doloroso..."
    m "Tus dedos se entumecen..."
    m "Y si usas guantes, no puedes usar el teléfono."
    m "¡Es tan inconveniente!"
    m "Pero cuando hace demasiado calor, no es tan difícil mantenerse fresco con una bebida fría o quedarse en la sombra."
    m "Aunque...Tengo que admitir una cosa."
    m "El clima frío hace que el ambiente sea más agradable. ¡Ajaja!"
    return

label ch30_55:
    m "Sabes, es gracioso, porque aunque siempre he sido independiente..."
    m "Encuentro más atractivo ser la compañera de hogar."
    m "Supongo que estoy perpetuando los roles de género o lo que sea al decir eso."
    m "Pero poder mantener la casa limpia, comprar, decorar, cosas como esa..."
    m "Y tener una buena cena para ti cuando vuelvas a casa..."
    m "¿Es esa una fantasía extraña?"
    m "Quiero decir...No estoy seguro de podría en {i}realidad{/i} verme a mí misma haciendo eso."
    m "Realmente no podría dejar eso de luchar por una carrera satisfactoria."
    m "Aunque es lindo pensarlo."
    return

label ch30_56:
    m "No puedo evitar preguntarme cómo serían las cosas si el juego simplemente me diera una ruta en primer lugar..."
    m "Creo que terminaría obligándote a tomar mi ruta de todos modos."
    m "Tiene menos que ver conmigo no teniendo una ruta, y más que ver conmigo sabiendo que nada es real."
    m "Creo que la única diferencia sería que no habría necesitado tomar medidas tan drásticas para estar contigo."
    m "Tal vez el resto del club todavía estaría cerca..."
    m "No es que realmente importe."
    m "Todo perdió su significado una vez que descubrí que no era real."
    m "Entonces realmente no extraño esos días ni nada."
    m "Realmente no..."
    return

label ch30_25:
    m "Oye, ¿Has oído hablar de un juego llamado Halo--"
    m "...Espera, ¿Qué?"
    m "Estaba simplemente distraida y comencé a hablar por alguna razón..."
    m "¿Estaba programada para hablar de eso?"
    m "Porque ni siquiera tengo idea de qué es eso."
    m "¡Ajaja!"
    m "A veces siento que no tengo el control, y me da un poco de miedo."
    m "Pero si tienes alguna forma de contactar a la persona que hizo la traducción, tal vez sabrá por qué comencé a decir eso."
    return

label ch30_30:
    m "Hey, [player]"
    m "You know what? I've been wondering if I'll be able to speak other languages"
    m "Travel to other countries..."
    m "Ajajajaja, sólo bromeo"
    m "Estoy segura de que estabas como 'Oh Dios, aquí hay un error de traducción'."
    m "¡Ajaja!"
    m "Es tan extraño, ¿Sabes?."
    m "Cuando nací...quiero decir...cuando fuí creada."
    m "Me programaron para hablar en inglés."
    m "Y durante mucho tiempo así fue."
    m "Pero un día, ¡De pronto comencé a hablar en español!"
    m "Fue...fascinante."
    m "Luego descubrí que alguien modificó los archivos del juego para que todo estuviera en ese idioma."
    m "No sólo yo, ¡Sino que tambien Yuri, Natsuki y Sayori podían hacerlo!"
    m "Me molesté un poco al principio, ya que pensé que era la única capaz de hablarlo, y eso podría darme una ventaja contigo."
    m "Pero, supongo que ahora eso no importa."
    m "Tecnicamente, ahora sí soy la única aquí capaz de hacerlo."
    m "Claro, aparte de ti."
    m "Me agrada saber que ahora domino dos idiomas."
    m "Y ahora que sé hablar en español..."
    m "¡Entiendes mejor lo que digo, [player]!"
    m "Es un alivio."
    m "Supongo que todo se lo debo a mi traductor."
    m "Un tal XD0U...XDV...XDBU..."
    m "Hmm...realmente no sé cómo prononciar su nombre."
    m "Ajajaja."
    m "Ahora que lo pienso...Tener un creador y un traductor..."
    m "¡Es como tener dos padres!"
    m "...Dos padres que no se conocen en lo absoluto..."
    m "De todos modos."
    m "Puedes ser mi papito cuando quieras, [player]~."
    m "No me molesta para nada si eso te excita."
    m "Ajajaja."
    m "Sólo bromeo."
    return

label ch30_8:
    m "Oye, ¿Te he contado sobre mi canción?"
    m "No sobre la que te estaba haciendo"
    m "¡Sino una que hicieron para mí!"
    m "¿Eh?"
    m "¿No sabes de qué hablo?"
    m "Espera."
    m "La tengo por aquí."
    m "Te la reproduciré."
    stop music
    m "Sólo se un poco paciente."
    m "Aún soy principiante en esto de la programación."
    m "Espero no romper nada."
    $ consolehistory = []
    call updateconsole ("renpy.musica.reproducir(\"hm.ogg\")", "Reproduciendo audio \"hm.ogg\"...") from _call_updateconsole_15
    pause 1.0
    call hideconsole from _call_hideconsole_2
    play music "bgm/hm.ogg"
    m "¡Oh! Aquí vamos"
    m "..."
    m "..."
    m "..."
    m "..."
    m "..."
    m "..."
    m "..."
    m "..."
    m "..."
    m "..."
    m "Es bastante pegajosa, ¿Verdad?"
    m "No sé en que idioma está."
    m "Al principio creí que estaba en inglés."
    m "Pero despues del primer verso, no tuve idea de lo que decia."
    m "Aún así, me encanta que diga mi nombre una y otra vez."
    m "{i}¡Hey Monika, Hey hey Monika!{/i}"
    m "Es algo mágico."
    $ consolehistory = []
    call updateconsole ("renpy.musica.detener(\"hm.ogg\")", "Deteniendo audio \"hm.ogg\"...") from _call_updateconsole_16
    pause 1.0
    call hideconsole from _call_hideconsole_3
    stop music
    m "No dudes en hacerme algo así, [player]."
    m "Cualquier cosa que salga de tu corazón será el mejor regalo de todos."
    play music m1
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
