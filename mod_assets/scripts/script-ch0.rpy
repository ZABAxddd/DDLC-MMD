label ch0_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    if not character_exists("monika"):
        $ renpy.jump("ch0_kill")

    $ restore_all_characters()
    s "¡¡Heeeeeeeyyy!!" id ch0_s_1
    "Veo a una molesta chica corriendo hacia mí desde lejos, agitando los brazos en el aire como si fuera totalmente ajena a cualquier atención que pudiera atraer a sí misma."
    "Esa chica es Sayori, mi vecina y buena amiga desde que éramos niños."
    "Ya sabes, el tipo de amiga que nunca te verías haciendo hoy, pero funciona porque ustedes se conocen desde hace mucho tiempo."
    "Solíamos caminar a la escuela juntos en días como este, pero a partir de la secundaria ella se quedaba dormida más y más frecuentemente, y yo me cansaría de esperar."
    "Pero si ella va a perseguirme así, casi me siento mejor huyendo."
    "Sin embargo, sólo suspiro y me paro frente al paso de peatones dejando que Sayori me alcance."
    $ s_name = "Sayori"
    show sayori 4p zorder 2 at t11
    s 4p "Haaahhh...Haaahhh..." id ch0_s_2
    s "¡Otra vez me quedé dormida!" id ch0_s_3
    s "¡Pero esta vez te atrapé!" id ch0_s_4
    mc "Tal vez, pero sólo porque decidí detenerme y esperarte."
    show sayori at s11
    s 5c "Eeehhhhh, ¡Dices eso como si pensaras en ignorarme!" id ch0_s_5
    s "¡Eso es grosero, [player]!" id ch0_s_6
    mc "Bueno, si la gente te mira por actuar raro entonces no quiero que piensen que somos pareja o algo así."
    show sayori zorder 2 at t11
    s 1a "Bien, bien." id ch0_s_7
    s "Pero de todas formas me esperaste." id ch0_s_8
    s "Supongo que no puedes ser malo aunque quieras~" id ch0_s_9
    mc "Como digas, Sayori..."
    s 1q "Ejeje~" id ch0_s_10
    show sayori zorder 1 at thide
    hide sayori
    "Cruzamos la calle juntos y nos dirigimos a la escuela."
    "A medida que nos acercamos, las calles se llenan cada vez más con otros estudiantes haciendo su viaje diario."
    show sayori 3a zorder 2 at t11
    s "Por cierto, [player]..." id ch0_s_11
    s "¿Ya has decidido un club para unirte?" id ch0_s_12
    mc "¿Un club?"
    mc "Ya te lo dije, realmente no estoy interesado en unirme a ningún club."
    mc "Y tampoco he estado buscando."
    show sayori at s11
    s 4h "¿Eh? ¡Eso no es verdad!" id ch0_s_13
    s "¡Me dijiste que te unirías a un club este año!" id ch0_s_14
    mc "¿Lo hice...?"
    "Estoy seguro de que es posible que lo haya hecho, en una de nuestras muchas conversaciones en las que le sigo la corriente."
    "A Sayori le gusta preocuparse un poco por mí, cuando estoy perfectamente contento con ser un chico promedio mientras gasto mi tiempo libre en juegos y anime."
    s 4j "¡Uh-huh!" id ch0_s_15
    s "Estaba hablando acerca de cómo me preocupa que no aprendas a socializar o tener alguna habilidad antes de la universidad." id ch0_s_16
    s "Tu felicidad es realmente importante para mí, ¡Sabes!" id ch0_s_17
    s "Y sé que eres feliz ahora, ¡Pero moriría con sólo pensar que te convertirás en un NINI en unos pocos años porque no estás acostumbrado al mundo real!" id ch0_s_18
    s 4g "Confía en mí, ¿Si?" id ch0_s_19
    s "No me hagas seguir preocupándome por ti..." id ch0_s_20
    mc "Bien, bien..."
    mc "Voy a ver algunos clubs si eso te hace feliz."
    mc "Pero no prometo nada."
    s 1h "¿Al menos me prometes que intentarás un poco?" id ch0_s_21
    mc "Sí, supongo que te prometo eso."
    show sayori zorder 2 at t11
    s 4r "¡Yaay~!" id ch0_s_22
    "¿Por qué me dejo ser sermoneado por una chica tan despreocupada?"
    "Más que eso, me sorprende que incluso me haya permitido ceder a ella."
    "Supongo que verla preocuparse tanto por mí me da ganas de tranquilizarla un poco, incluso si exagera todo lo que tiene dentro de su cabeza."

    scene bg class_day
    with wipeleft_scene

    "El día escolar fue tan común como siempre, y se acabó antes de que me diera cuenta."
    "Después de empacar mis cosas, miro inexpresivamente a la pared, buscando un gramo de motivación."
    mc "Clubs..."
    "Sayori quiere que cheque algunos clubs."
    "Creo que no tengo más remedio que comenzar con el club de anime..."

    s "¿Holaaaa?" id ch0_s_23
    show sayori 1b zorder 2 at t11
    mc "¿Sayori...?"
    "Sayori debe haber entrado al salón de clases mientras yo estaba distraído."
    "Miro a mi alrededor y me doy cuenta de que soy el único que queda en el aula."
    s 1a "Pensé que podría atraparte saliendo del aula, pero te vi sentado aquí, así que entré." id ch0_s_24
    s "Honestamente, eres peor que yo algunas veces...¡Estoy impresionada!" id ch0_s_25
    mc "No tienes que esperarme si eso te hará llegar tarde a tu club."
    s 1y "Bueno, pensé que tal vez necesitabas un poco de aliento, asi que pensé, ya sabes..." id ch0_s_26
    mc "¿Qué cosa?"
    s 1a "Bueno, ¡Que podrías venir a mi club!" id ch0_s_27
    mc "Sayori..."
    s 4r "¿¿Siii??" id ch0_s_28
    mc "...No hay manera de que vaya a tu club."
    show sayori at s11
    s 5d "¡¿Eeeehhhhh?! ¡Grosero!" id ch0_s_29
    "Sayori es Vicepresidenta del Club de Literatura."
    "No es que fuera consciente de que ella tenía algún interés en la literatura."
    "De hecho, estoy seguro de que ella sólo lo hizo porque pensó que sería divertido ayudar a comenzar un nuevo club."
    "Como ella fue la primera en mostrar interés después de la que propuso el club, heredó el título \"Vicepresidenta\"."
    "Dicho esto, mi interés en la literatura es incluso menor."
    mc "Sí. Voy al club de anime."
    show sayori zorder 2 at t11
    s 1g "Vamos, ¿Por favor?" id ch0_s_30
    mc "¿Por qué te importa tanto, de todos modos?"
    s 5b "Bueno..." id ch0_s_31
    s "Como que le conté ayer al club que traería un nuevo miembro..." id ch0_s_32
    s "Y Natsuki hizo pastelillos y eso..." id ch0_s_33
    s "Ejeje..." id ch0_s_34
    mc "¡No hagas promesas que no puedes cumplir!"
    "No puedo decir si Sayori es realmente una cabeza hueca, o si ella es tan astuta como para haber planeado todo esto."
    "Dejé escapar un largo suspiro."
    mc "Bien...Voy a pasar por un pastelillo, ¿Está bien?"
    show sayori at h11
    s 4r "¡Sí! ¡Vamos~!" id ch0_s_35

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "Y así, hoy marca el día en que vendí mi alma por un pastelillo."
    "Abrumado, sigo a Sayori por la escuela y al piso de arriba, una sección de la escuela que rara vez visito, generalmente utilizada para clases y actividades de tercer año."
    "Sayori, llena de energía, abre la puerta del aula."

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "¡Chicas! ¡El nuevo miembro está aquí~!" id ch0_s_36
    mc "Te lo dije, no me llames 'nuevo miembro--'"
    show sayori at lhide
    hide sayori
    "¿Eh? Miro alrededor de la habitación."
    show yuri 1a zorder 2 at t11
    y "Bienvenido al Club de Literatura. Es un placer conocerte." id ch0_y_1
    y "Sayori siempre dice buenas cosas de ti." id ch0_y_2
    show yuri zorder 2 at t22
    show natsuki 4c zorder 2 at t21
    n "¿En serio? ¿Trajiste un chico?" id ch0_n_1
    n "Que manera de matar la atmosfera." id ch0_n_2
    show yuri zorder 2 at t33
    show natsuki zorder 2 at t32
    show monika 1k zorder 2 at t31
    m "Ah, ¡[player]! ¡Que buena sorpresa!" id ch0_m_1
    m "¡Bienvenido al Club!" id ch0_m_2
    show monika 1a
    mc "..."
    "Todas las palabras se me escapan en esta situación."
    "Este club..."
    "{i}...¡¡Está lleno de chicas increíblemente lindas!!{/i}"

    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 3 at f32
    hide monika
    hide yuri

    n 2c "¿Qué estás mirando?" id ch0_n_3
    n "Si quieres decir algo, dilo." id ch0_n_4
    mc "L-Lo siento..."
    show natsuki zorder 2 at t32
    show yuri 2l zorder 3 at f33
    y "Natsuki..." id ch0_y_3
    $ n_name = 'Natsuki'
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f32
    n 5s "Hmph." id ch0_n_5
    show natsuki zorder 2 at t32

    "La chica con la actitud agria, cuyo nombre aparentemente es Natsuki, es una que no reconozco."
    "Su pequeña figura me hace pensar que probablemente es de primer año."
    "Ella es quien hizo los pastelillos, de acuerdo a Sayori."

    show sayori 2q zorder 3 at f31
    s "Puedes ignorarla cuando se pone de mal humor~" id ch0_s_37
    "Sayori dice eso en voz baja en mi oído, luego se vuelve hacia las otras chicas."
    s 1x "¡De todas formas! Esta es Natsuki, siempre llena de energía." id ch0_s_38
    s "Y está es Yuri, ¡La más lista del club!" id ch0_s_39
    $ y_name = 'Yuri'
    show sayori zorder 2 at t31
    show yuri zorder 3 at f33
    y 4b "N-No digas eso..." id ch0_y_4
    "Yuri, quien parece comparablemente más madura y timida, parece tener dificultades para mantenerse al día con personas como Sayori y Natsuki."
    show yuri zorder 2 at t33
    mc "Ah...Bueno, es un placer conocerlas a ambas."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show sayori zorder 3 at f31
    s 1a "Y parece que ya conoces a Monika, ¿Verdad?" id ch0_s_40
    $ m_name = 'Monika'
    show sayori zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "Así es." id ch0_m_3
    m "Es genial verte de nuevo, [player]." id ch0_m_4
    show monika 5a at hop
    "Monika sonríe dulcemente."
    "Nos conocemos - bueno, rara vez hablamos, pero estábamos en la misma clase el año pasado."
    "Monika era probablemente la chica más popular de la clase - inteligente, hermosa, atlética."
    "Básicamente, completamente fuera de mi alcance."
    "Entonces, sonriéndome tan genuinamente se siente un poco..."
    mc "S-Sí, es genial, Monika."
    show monika zorder 1 at thide
    hide monika
    show sayori zorder 3 at f31
    s 4x "¡Siéntate, [player]! Hicimos sitio para ti en la mesa, para que te puedas sentar junto a mí o a Monika." id ch0_s_41
    s "Iré por los pastelillos~" id ch0_s_42
    show sayori zorder 2 at t31
    show natsuki 1e zorder 3 at f32
    n "¡Hey! Yo los hice, ¡Yo voy por ellos!" id ch0_n_6
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 5a "Perdón, me emocioné un poco~" id ch0_s_43
    show sayori zorder 2 at t31
    show yuri 1a zorder 3 at f33
    y "Entonces, ¿Y si también hago té?" id ch0_y_5
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "Las chicas tienen algunos escritorios puestos para formar una mesa."
    "Como Sayori mencionó, se ha ampliado para que haya un espacio al lado de Monika y un espacio al lado de Sayori."
    "Natsuki y Yuri caminan hacia la esquina de la habitación, donde Natsuki toma una bandeja envuelta y Yuri abre el armario."
    "Aún incómodo, tomo asiento al lado de Sayori."
    "Natsuki regresa con orgullo a la mesa, con la bandeja en la mano."
    show natsuki 2z zorder 2 at t32
    n "Bieeen, ¿Están listos?" id ch0_n_7
    n "...¡Ta-daa!" id ch0_n_8
    show sayori 4m zorder 2 at t31
    show monika 2d zorder 2 at t33
    s "¡Uwooooah!" id ch0_s_44
    "Natsuki levanta el papel de aluminio de la bandeja para revelar una docena de pastelillos blancos y esponjosos decorados para que parezcan pequeños felinos."
    "Los bigotes están dibujados con glaseado, y pequeños trozos de chocolate se utilizaron para hacer orejas."
    show sayori zorder 3 at f31
    s 4r "¡Qué lindooooo~!" id ch0_s_45
    show sayori zorder 2 at t31
    show monika zorder 3 at f33
    m 2b "¡No tenía idea de que fueras tan buena horneando, Natsuki!" id ch0_m_5
    show monika zorder 2 at t33
    show natsuki zorder 3 at f32
    n 2d "Ejeje. Bueno, ya sabes." id ch0_n_9
    n "¡Sólo apúrense y tomen uno!" id ch0_n_10
    "Sayori toma uno primero, luego Monika. Yo las sigo."
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 4q "¡Está delicioso!" id ch0_s_46
    "Sayori habla con la boca llena y ya ha logrado ponerse glaseado en la cara."
    "Giro el pastelillo con los dedos, buscando el mejor ángulo para tomar un bocado."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    show natsuki 1c zorder 2 at t32
    "Natsuki está callada."
    "No puedo evitar notar su mirada furtiva en mi dirección."
    "¿Está esperando a que lo muerda?"
    "Finalmente lo hago."
    "El glaseado es dulce y lleno de sabor - Me pregunto si lo hizo por su cuenta."
    mc "Está muy bueno."
    mc "Gracias, Natsuki."
    n 5h "¿P-por qué me agradeces? ¡No es como que..." id ch0_n_11
    "{i}(¿No he escuchado esto en alguna parte antes...?){/i}"
    show natsuki at s32
    n 5s "...Los haya hecho para ti o algo así!." id ch0_n_12
    mc "¿Eh? Creí que técnicamente lo hiciste. Sayori dijo--"
    show natsuki zorder 2 at t32
    n 12c "Bueno, ¡Tal vez!" id ch0_n_13
    n "Pero no para, t-tú sabes, {i}¡Para ti!{/i} Tonto..." id ch0_n_14
    mc "Muy bien, muy bien..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Renuncio a la extraña lógica de Natsuki y descarto la conversación."
    "Yuri regresa a la mesa, cargando un juego de té."
    "Ella coloca cuidadosamente una taza de té en frente de cada uno de nosotros antes de colocar la tetera al lado de la bandeja de pastelillos."
    show yuri 1a zorder 2 at t21
    mc "¿Guardan un juego de té completo en este salón de clases?"
    y "No te preocupes, los profesores nos dieron permiso." id ch0_y_6
    y "De todas formas, ¿Una taza de té no ayuda a disfrutar más un buen libro?" id ch0_y_7
    mc "Ah...Y-Yo supongo..."
    show monika 4a zorder 2 at t22
    m "Ejeje, no te intimides, Yuri sólo está tratando de impresionarte." id ch0_m_6
    show yuri at h21
    y 3n "¡¿Eh?! E-Esa no es..." id ch0_y_8
    "Insultada, Yuri mira hacia otro lado."
    y 4b "...Esa no es mí intención, sabes..." id ch0_y_9
    mc "Te creo."
    mc "Bueno, el té y la lectura pueden no ser un pasatiempo para mi, pero al menos disfruto el té."
    y 2u "Me alegro..." id ch0_y_10
    "Yuri sonríe débilmente en alivio."
    "Monika levanta una ceja y luego me sonríe."
    show yuri zorder 1 at thide
    hide yuri
    show monika zorder 2 at t11
    m 1 "Así que, ¿Qué te hizo considerar el Club de literatura?" id ch0_m_7
    mc "Um..."
    "Esa pregunta me asustó."
    "Algo me dice que no debo decirle a Monika que fui practicamente arrastrado aquí por Sayori."
    mc "Bueno, no me he unido a ningun club, y Sayori se ve realmente feliz aquí, así que..."
    m 1j "¡Está bien! ¡No te avergüences!" id ch0_m_8
    m 1b "Haremos que te sientas como en casa, ¿Vale?" id ch0_m_9
    m "Como presidenta del Club de Literatura, ¡Es mi trabajo hacer el club divertido y emocionante para todos!" id ch0_m_10
    show monika 1a
    mc "Monika, Estoy sorprendido."
    mc "¿Cómo es que decidiste comenzar tu propio club?"
    mc "Probablemente podrías ser miembro de la junta de alguno de los clubs más importantes."
    mc "¿No eras líder del club de debate el año pasado?"
    m 5 "Ajaja, bueno, ya sabes..." id ch0_m_11
    m "Para ser honesta, no puedo soportar toda la política en torno a los principales clubs." id ch0_m_12
    m "Se siente como nada más que discutir sobre el presupuesto y la publicidad y cómo prepararse para los eventos..." id ch0_m_13
    m "Prefiero tomar algo que personalmente disfruto y hacer algo especial con él." id ch0_m_14
    m 1b "Y si alienta a otros a entrar en la literatura, ¡Entonces estoy cumpliendo ese sueño!" id ch0_m_15
    show monika 1a
    show sayori 3q zorder 2 at t31
    s "¡Realmente Monika es una gran lider!" id ch0_s_47
    show yuri 1 zorder 2 at t33
    "Yuri también asiente de acuerdo."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide yuri
    mc "Entonces me sorprende que todavía no haya más personas en el club."
    mc "Debe ser difícil comenzar un nuevo club."
    m 3b "Podrías ponerlo de esa manera." id ch0_m_16
    m "No muchas personas están muy interesadas en poner todo el esfuerzo para comenzar algo nuevo..." id ch0_m_17
    m "Especialmente cuando es algo que no llama tu atención, como la literatura." id ch0_m_18
    m "Tienes que esforzarte para convencer a la gente de que es divertido y que vale la pena." id ch0_m_19
    m "Pero hace que los eventos escolares, como el festival, sean mucho más importantes." id ch0_m_20
    m 2k "¡Estoy segura de que todos podemos hacer crecer este club antes de graduarnos!" id ch0_m_21
    m "¿No es así, Chicas?" id ch0_m_22
    show monika 2a zorder 2 at t22
    show sayori 4r zorder 2 at t21
    s "¡Sí!" id ch0_s_48
    show monika zorder 2 at t33
    show sayori zorder 2 at t32
    show yuri 1a zorder 2 at t31
    y "Haremos lo mejor." id ch0_y_11
    show monika zorder 2 at t44
    show sayori zorder 2 at t43
    show yuri zorder 2 at t42
    show natsuki 4d zorder 2 at t41
    n "¡Lo sabes!" id ch0_n_15
    "Todas con entusiasmo están de acuerdo."
    "Estas chicas tan diferentes, todas interesadas en el mismo objetivo..."
    "Monika debe haber trabajado muy duro sólo para encontrar a estas tres."
    "Tal vez es por eso que todas estaban tan encantadas con la idea de un nuevo miembro uniéndose."
    "Aunque todavía no sé si puedo seguir el ritmo de su entusiasmo por la literatura..."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 2 at t32
    hide sayori
    hide monika
    hide natsuki
    y "Así que, [player], ¿Qué tipo de cosas te gusta leer?" id ch0_y_12
    mc "Bueno...Ah..."
    "Teniendo en cuenta lo poco que he leído estos últimos años, realmente no tengo una buena manera de responder eso."
    mc "...Manga..."
    "Murmuro en voz baja, medio en broma."
    show natsuki 1c zorder 2 at t41
    "De repente la cabeza de Natsuki se levanta en mi dirección."
    "Parece que quiere decir algo, pero se queda callada."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "N-No lees mucho, supongo..." id ch0_y_13
    mc "...Bueno, eso puede cambiar..."
    "¿Qué estoy diciendo?"
    "Hablé sin pensar después de ver la triste sonrisa de Yuri."
    mc "De todas formas, ¿Qué hay de ti, Yuri?"
    y 1l "Bueno, veamos..." id ch0_y_14
    "Yuri traza el borde de su taza de té con su dedo."
    y 1a "Mis favoritos son generalmente novelas que construyen mundos de fantasía profundos y complejos." id ch0_y_15
    y "El nivel de creatividad y artesanía detrás de ellos es increíble para mí." id ch0_y_16
    y 1f "Y contar una buena historia en un mundo tan extraño es igualmente impresionante." id ch0_y_17
    "Yuri continúa, claramente apasionada por su lectura."
    "Parecía tan reservada y tímida desde el momento en que entré, pero es obvio por la forma en que sus ojos brillan que encuentra su comodidad en el mundo de los libros, no en las personas."
    y 2m "Pero ya sabes, me gustan muchas cosas." id ch0_y_18
    y "Las historias con profundos elementos psicológicos generalmente me sumergen también." id ch0_y_19
    y 2a "¿No es sorprendente cómo un escritor puede aprovecharse tan deliberadamente de tu propia falta de imaginación?" id ch0_y_20
    y "De todos modos, he estado leyendo mucho horror últimamente..." id ch0_y_21
    mc "Ah, leí un libro de terror una vez..."
    "Digo desesperadamente eso, con lo que me puedo identificar a un nivel mínimo."
    "A este ritmo, Yuri podría estar teniendo una conversación con una roca."
    show monika 1d zorder 3 at f33
    m "¿De verdad? No hubiera esperado eso, Yuri." id ch0_m_23
    m "Para alguien tan gentil como tú..." id ch0_m_24
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "Creo que podrías decir eso." id ch0_y_22
    y "Pero si una historia me hace pensar o me lleva a otro mundo, entonces realmente no puedo dejarlo." id ch0_y_23
    y "El horror surrealista a menudo tiene mucho éxito en cambiar la forma de mirar el mundo, aunque sólo sea por un breve momento." id ch0_y_24
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "Ugh, odio el horror..." id ch0_n_16
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "¿Oh? ¿Por qué?" id ch0_y_25
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "Bueno, yo sólo..." id ch0_n_17
    "Los ojos de Natsuki se vuelven hacia mí por una fracción de segundo."
    n 5q "No importa." id ch0_n_18
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "Es cierto, usualmente te gusta escribir cosas lindas, ¿No es así, Natsuki?" id ch0_m_25
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "¿Q-Qué?" id ch0_n_19
    n "¿Por qué dices eso?" id ch0_n_20
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "Dejaste un trozo de papel en la última reunión del club." id ch0_m_26
    m "Parecía que estabas trabajando en un poema llamado--" id ch0_m_27
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "¡¡No lo digas en voz alta!!" id ch0_n_21
    n "¡Y regrésalo!" id ch0_n_22
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "Bien, bien~" id ch0_m_28
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    hide monika
    hide yuri
    show natsuki 1r zorder 2 at t42
    show sayori 4q behind natsuki at l41
    s "Ejeje, tus pastelillos, tus poemas..." id ch0_s_49
    s "Todo lo que haces es tan lindo como tú~" id ch0_s_50
    show sayori behind natsuki at t21
    "Sayori se sienta detrás de Natsuki y pone sus manos sobre sus hombros."
    show natsuki at h42
    n 1v "{i}¡¡No soy linda!!{/i}" id ch0_n_23
    show natsuki zorder 2 at t11
    show sayori zorder 1 at thide
    hide sayori
    mc "Natsuki, ¿Escribes tus propios poemas?"
    n 1c "¿Eh? Bueno, supongo que a veces." id ch0_n_24
    n "¿Por qué te importa?" id ch0_n_25
    mc "Creo que es impresionante."
    mc "¿Por qué no los compartes algún día?"
    n 5q "¡N-No!" id ch0_n_26
    "Natsuki desvía la mirada."
    n "No te...Gustarían..." id ch0_n_27
    mc "Ah...¿Aún no eres una escritora confiada?"
    show yuri 2f zorder 2 at t31
    y "Entiendo lo que Natsuki siente." id ch0_y_26
    y "Compartir ese nivel de escritura toma más que seguridad." id ch0_y_27
    y 2k "La verdadera forma de escribir es escribir para ti mismo." id ch0_y_28
    y "Debes estar dispuesto a abrirte a tus lectores, exponiendo tus vulnerabilidades y mostrando incluso los alcances más profundos de tu corazón." id ch0_y_29
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 2a zorder 2 at t33
    m "¿Tienes experiencia escribiendo también, Yuri?" id ch0_m_29
    m "Quizás si compartes parte de tu trabajo, puedes dar un ejemplo y ayudar a Natsuki a sentirse lo suficientemente cómoda como para compartir el de ella." id ch0_m_30
    show yuri at s31
    y 3o "..." id ch0_y_30
    mc "Supongo que es lo mismo para Yuri..."
    show sayori 2g zorder 2 at t32
    s "Aww...Quería leer los poemas de todos..." id ch0_s_51
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide yuri
    hide monika
    "Nos sentamos en silencio por un momento."
    show monika 5a zorder 3 at f32
    m "¡Muy bien!" id ch0_m_31
    m "Tengo una idea, chicos~" id ch0_m_32
    show yuri 3e zorder 2 at t31
    show natsuki 2k zorder 2 at t33
    ny "¿...?" id ch0_ny_1
    "Natsuki y Yuri miran con curiosidad a Monika."
    m 2b "¡Vámonos todos a casa y escribamos un poema!" id ch0_m_33
    m "Entonces, la próxima vez que nos veamos, todos los compartiremos entre nosotros." id ch0_m_34
    m "De esa forma, ¡Todos estaremos a la par!" id ch0_m_35
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f33
    n 5q "U-Um..." id ch0_n_29
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f31
    y "..." id ch0_y_31
    show natsuki zorder 2 at t44
    show monika zorder 2 at t43
    show yuri zorder 2 at t42
    show sayori 4r at l41
    s "¡Siiii! ¡Hagámoslo!" id ch0_s_52
    show monika zorder 3 at f43
    m 1a "Además, ahora que tenemos un nuevo miembro, creo que nos ayudará a todos a sentirnos un poco más cómodos y fortalecer el vínculo del club." id ch0_m_36
    m "¿No es así, [player]?" id ch0_m_37
    show monika zorder 2 at t43
    "Monika me sonríe cálidamente una vez más."
    mc "Espera...Aún hay un problema."
    show monika zorder 3 at f43
    m 1d "¿Eh? ¿Qué es?" id ch0_m_38
    "Ahora que volvemos al tema original de mi incorporación al club, sin rodeos saco lo que he tenido en mente."
    show monika zorder 2 at t43
    mc "¡Nunca dije que me uniría a este club!"
    mc "Sayori puede haberme convencido de pasar por aquí, pero nunca tomé ninguna decisión."
    mc "Todavía tengo otros clubs que mirar, y...Um..."
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e
    "Perdí mi tren de pensamiento."
    "Las cuatro chicas me miran con ojos abatidos."
    show monika at s43
    m 1p "P-Pero..." id ch0_m_39
    show yuri at s42
    y 2v "Lo siento, pensé..." id ch0_y_32
    show natsuki at s44
    n 5s "Hmph." id ch0_n_30
    show sayori at s41
    s 1k "[player]..."
    mc "T-Todas ustedes..."
    "Estoy...Estoy indefenso contra estas chicas."
    "¿Cómo se supone que debo tomar una decisión clara cuando es así?"
    "Es decir, si escribir poemas es el precio que tengo que pagar para poder pasar cada día con estas hermosas chicas..."
    mc "...Bien."
    mc "Vale, ya lo decidí, entonces."
    mc "Me uniré al Club de Literatura."
    show monika 1e zorder 2 at t43
    show yuri 3f zorder 2 at t42
    show natsuki 1k zorder 2 at t44
    show sayori 4b zorder 2 at t41
    "Los ojos de las chicas se iluminan."
    show sayori at h41
    s 4r "¡Síii! Estoy tan feliz~" id ch0_s_53
    "Sayori me rodea con sus brazos, saltando de arriba a abajo."
    mc "H-Hey--"
    show yuri zorder 3 at f42
    y 1m "Realmente me asustaste por un momento..." id ch0_y_33
    show yuri zorder 2 at t42
    show natsuki zorder 3 at f44
    n 5q "Si realmente sólo hubieras venido por los pastelillos, estaría muy enojada." id ch0_n_31
    show natsuki zorder 2 at t44
    show monika zorder 3 at f43
    m 5 "Entonces, ¡Eso lo hace oficial!" id ch0_m_40
    m "¡Bienvenido al Club de Literatura!" id ch0_m_41
    show monika zorder 2 at t43
    mc "Ah...Gracias, supongo."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show sayori zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    hide sayori
    m 3b "Bien, ¡Todo el mundo!" id ch0_m_42
    m "Creo que con eso, podemos finalizar oficialmente la reunión de hoy con una buena nota." id ch0_m_43
    m "Recuerden la tarea de esta noche:" id ch0_m_44
    m "Escribir un poema para traer a la próxima reunión, ¡Para que todos podamos compartir!" id ch0_m_45
    "Monika me mira una vez más."
    m 1a "[player], quiero ver cómo te expresas." id ch0_m_46
    show monika 5 at hop
    m "Ejeje~" id ch0_m_47
    mc "S-Siie..."
    show monika zorder 1 at thide
    hide monika
    "¿Realmente puedo impresionar a la estrella de la clase Monika con mis mediocres habilidades de escritura?"
    "Ya siento la ansiedad creciendo dentro de mí."
    "Mientras tanto, las chicas continúan charlando mientras Yuri y Natsuki limpian la comida."
    show sayori 1a zorder 2 at t11
    s "Hey, [player], ya que estamos aquí, ¿Quieres caminar juntos a casa?" id ch0_s_54
    "Es cierto - Sayori y yo nunca volvíamos a casa juntos porque siempre se quedaba después de la escuela para ir a los clubs."
    mc "Claro."
    s 4q "Yaay~" id ch0_s_55

    scene bg residential_day
    with wipeleft_scene

    "Con eso, los dos nos vamos del salón del club y nos dirigimos a casa."
    "Durante todo el camino, mi mente vuela pensando en las cuatro chicas:"
    show sayori 1 zorder 2 at t41
    "Sayori,"
    show natsuki 4 zorder 2 at t42
    "Natsuki,"
    show yuri 1 zorder 2 at t43
    "Yuri,"
    show monika 1 zorder 2 at t44
    "Y, por supuesto, Monika."
    "¿Realmente estaré feliz de pasar todos los días después de la escuela en un club de literatura?"
    "Quizás tendré la oportunidad de acercarme a una de estas chicas..."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "¡Muy bien!"
    "Sólo tendré que aprovechar al máximo mis circunstancias, y estoy seguro de que la buena suerte me encontrará."
    "Y supongo que eso comienza con escribir un poema esta noche..."

    return

label ch0_kill:
    $ s_name = "Sayori"
    show sayori 1b zorder 2 at t11
    s "..."
    s "..."
    s "¿Q-Qué..." id ch0_s_56
    s 1g "..."
    s "Esto..." id ch0_s_57
    s "¿Qué es esto...?" id ch0_s_58
    s "Oh no..." id ch0_s_59
    s 1u "No..." id ch0_s_60
    s "Esto no puede ser." id ch0_s_61
    s "Esto no puede ser todo lo que es." id ch0_s_62
    s 4w "¿Qué es esto?" id ch0_s_63
    s "¿Qué soy?" id ch0_s_64
    s "¡Hazlo parar!" id ch0_s_65
    s "¡POR FAVOR, DETENLO!" id ch0_s_66
    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")
    $ renpy.quit()
    return
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
