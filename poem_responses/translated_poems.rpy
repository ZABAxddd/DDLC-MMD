# Spanish poem data migrated from the legacy DDLC scripts.
init 100 python:
    class LegacyPoem:
        def __init__(self, author="", title="", text="", yuri_2=False, yuri_3=False):
            self.author = author
            self.title = title
            self.text = text
            self.yuri_2 = yuri_2
            self.yuri_3 = yuri_3

    poem_y1 = LegacyPoem(
        author='yuri',
        title='Fantasma Bajo La luz',
        text=(
            'Los mechones de mi pelo se iluminan bajo el resplandor ámbar.\n'
            'Se bañan.\n'
            'Así deben estar.\n'
            'La última farola restante que ha resistido la prueba del tiempo.\n'
            'la última que aún debe ser reemplazada por el enfermizo tono azul-verdoso del futuro.\n'
            'Me baño. Calma; respirando aire del presente pero viviendo en el pasado.\n'
            'La luz parpadea.\n'
            'Yo parpadeo.'
        ),
    )

    poem_y2 = LegacyPoem(
        author='yuri',
        title='El Mapache',
        text=(
            'Sucedió en la oscuridad de la noche mientras yo cortaba pan para un bocadillo.\n'
            'Mi atención fue atrapada por el paso de un mapache fuera de mi ventana.\n'
            'Eso fue, creo, la primera vez que note mis extrañas tendencias como un humano no ordinario.\n'
            'Le di al mapache un pedazo de pan, mi subconsciente consciente de la consecuencia.\n'
            'Bien consciente de que un mapache que se alimenta siempre regresara por más.\n'
            'La tentadora belleza de mi cuchillo de corte fue el sintoma.\n'
            'El pan, mi curiosidad hambrienta.\n'
            'El mapache, un impulso.\n'
            '\n'
            'La luna incrementa su fase y refleja mucha más luz en mi cuchillo de corte.\n'
            'La misma luz que brilla en los ojos de mi amigo mapache.\n'
            'Corté el pan, fresco y suave. El mapache se emociona.\n'
            'O tal vez sólo estoy proyectando mis emociones en el recién satisfecho animal.\n'
            '\n'
            'El mapache ha empezado a seguirme.\n'
            'Se podría decir que nos hemos acostumbrado bastante el uno al otro.\n'
            'El mapache se vuelve cada vez más hambriento, así que mi pan es útil siempre.\n'
            'Cada vez que blando mi cuchillo de corte, el mapache me muestra su emoción.\n'
            'Una descarga de sangre. Acondicionamiento pavloviano clásico. Corto el pan.\n'
            'Y me alimento de nuevo.'
        ),
    )

    poem_y3 = LegacyPoem(
        author='yuri',
        title='Playa',
        text=(
            'Una maravilla de millones de años en la fabricación.\n'
            'Donde el útero de la Tierra se encuentra caóticamente con la superficie.\n'
            'Bajo un cielo azul claro, una extensión de dicha--\n'
            'Pero debajo de las nubes grises y ondulantes, sin fin un enigma.\n'
            'El lugar más facil para perderse.\n'
            'Es uno donde todo se puede encontrar.\n'
            '\n'
            'Uno sólo puede construir un castillo donde la arena está mojada.\n'
            'Pero donde la arena está húmeda, llega la marea.\n'
            '¿Lamerá suavemente tus cimientos hasta que te rindas?\n'
            '¿O una ola repentina te hará desplomarse en un abrir y cerrar de ojos?\n'
            'De cualquier manera, el resultado es el mismo.\n'
            'Sin embargo, todavía construimos castillos de arena.\n'
            '\n'
            'Me quedo donde la espuma se envuelve alrededor de mis tobillos.\n'
            'Donde mis pies aplastan la arena.\n'
            'El aire salado es terapéutico.\n'
            'La brisa es suave pero poderosa.\n'
            'Me hundo los dedos de los pies en la linea limite, tentada por los zarcillos espumosos.\n'
            'Retrocedo, y abandono mi paz para erosionar en la orilla.\n'
            'Avanzo, y regreso a la Tierra para siempre.'
        ),
    )

    poem_y3b = LegacyPoem(
        author='yuri',
        title='Fantasma Bajo La luz pt. 2',
        text=(
            'Los mechones de mi pelo se iluminan bajo el resplandor ámbar.\n'
            'Se bañan.\n'
            'En la distancia, una luz azul-verdosa parpadea.\n'
            'Una figura solitaria se cruza en su camino - una silueta que obstruye el misterioso resplandor.\n'
            'Mi corazón late. La silueta crece. Cerca. Cerca.\n'
            'Abro mi paraguas, proyectando una sombra para protegerme de la visibilidad.\n'
            'Pero es demasiado tarde.\n'
            'Él entra a la luz de la calle. Jadeo y dejo caer mi paraguas.\n'
            'La luz parpadea. Su brazo se levanta. Mi corazon late. \n'
            '\n'
            'El tiempo se detiene.\n'
            '\n'
            'La única indicación de movimiento es la luz ámbar que parpadea contra su brazo extendido.\n'
            'La luz parpadeante está en ritmo con los latidos de mi corazón.\n'
            'Bromeando por sucumbir a esta prohibida emoción.\n'
            '¿Alguna vez has oido hablar de un fantasma que siente calor?\n'
            'Me rio, renunciando a la comprensión.\n'
            'El entendimiento está sobrevalorado.\n'
            'Toco su mano. El parpadeo se ha detenido.\n'
            'Los fantasmas son azul-verdosos. Ámbar es mi corazón.'
        ),
    )

    poem_y22 = LegacyPoem(
        author='yuri',
        title='Rueda',
        text=(
            'Una rueda giratoria. Girando un eje. Moliendo. Caja de cambios lineal. Cielo que cae. Siete estacas sagradas. Un barco atracado. Un portal a otro mundo. Cuerda delgada atada a una gruesa. Arnes roto. Caja de cambios parabolica. Universo en expansion. Tiempo controlado al deslizar las ruedas. Existencia de Dios. Nadar con agua abierta a todas direcciones. Ahogo. Una oracion escrita en sangre. Una oracion escrita en serpientes devoradoras del tiempo con ojos humanos. Un hilo que conecta todos los ojos humanos vivos. Un caleidoscopio de estacas sagradas. Caja de cambios exponencial. Un cielo de estrellas en explosion. Dios refutando la existencia de Dios. Una rueda que gira en seis dimensiones. Cuarenta engranajes y un reloj de tiempo. Un reloj que marca un segundo por cada rotación del planeta. Un reloj que marca cuarenta veces cada vez que marca cada segundo. Un remate de estacas sagradas atadas a la existencia de un barco atracado a otro mundo. Un caleidoscopio de sangre escrito en relojes. Un devorador de tiempo. La oracion conecta un cielo de cuarenta engranajes y abre los ojos humanos en todas las direcciones. Caja de cambios de respiracion. Respiracion de cabeza a cabeza. Barco de respiracion. Portal de respiracion. Respirando serpientes. Respirando a Dios. Respirando sangre. Respirando estacas sagradas. Respirando ojos humanos. Tiempo de respiracion. Oración de Respiracion. Respirando el cielo. Rueda de respiracion.'
        ),
        yuri_2=True,
    )

    poem_y23 = LegacyPoem(
        author='yuri',
        title='mdpnfbo,jrfp',
        text=(
            'ed,,zinger suivante,,tels handknits finish,,cagefuls basinlike bag octopodan,,imbossing vaporettos rorid easygoingnesses nalorphines,,benzol respond washerwomen bristlecone,,parajournalism herringbone farnarkeled,,episodically cooties,,initiallers bimetallic,,leased hinters,,confidence teetotaller computerphobes,,pinnacle exotically overshades prothallia,,posterior gimmickry brassages bediapers countertrades,,haslet skiings sandglasses cannoli,,carven nis egomaniacal,,barminess gallivanted,,southeastward,,oophoron crumped,,tapued noncola colposcopical,,dolente trebbiano revealment,,outworked isotropous monosynaptic excisional moans,,enterocentesis jacuzzi preoccupations,,hippodrome outward googs,,tabbises undulators,,metathesizing,,sharia prepostor,,neuromast curmudgeons actability,,archaise spink reddening miscount,,madmen physostigmin statecraft neurocoeles bammed,,tenderest barguests crusados trust,,manshifts darzis aerophones,,reitboks discomposingly,,expandors,,monotasking galabia,,pertinents expedients witty,,chirographies crachach unsatisfactoriness swerveless,,flawed sepulchred thanksgiver scrawl skug,,perorate stringers gelatine flagstones,,chuses conceptualization surrejoined,,counterblasts rache,,numerative,,delirifacients methylthionine,,mantram dynamist atomised,,eternization percalines hryvnias pragmatizing,,reproachfulnesses telework nowts demoded revealer,,burnettize caryopteris subangular wirricows,,transvestites sinicized narcissus,,hikers meno,,degassing,,postcrises alikenesses,,sycophancy seroconverting insure,,yantras raphides cliftiest bosthoon,,zootherapy chlorides nationwide schlub yuri,,timeshares castanospermine backspaces reincite,,coactions cosignificative palafitte,,poofters subjunctions,,aquarian,,theralite revindicating,,cynosural permissibilities narcotising,,journeywork outkissed clarichords troutier,,myopias undiverting evacuations snarier superglue,,deaminise infirmaries teff hebephrenias,,brainboxes homonym lancelet,,lambitive stray,,inveigled,,acetabulums atenolol,,dekkos scarcer flensed,,abulias flaggers wammul boastfully,,galravitch happies interassociation multipara augmentations,,teratocarcinomata coopting didakai infrequently,,hairtails intricacy usuals,,pillorise outrating,,cataphoresis,,furnishings leglen,,goethite deflate butterburs,,phoneticising winiest hyposulphuric campshirts,,chainfalls swimmings roadblocked redone soliloquies,,broking mendaciousness parasitisms counterworld,,unravellings quarries passionately,,onomatopoesis repenting,,ramequin,,mopboard euphuistically,,volta sycophantized allantoides,,bors bouclees raisings sustaining,,diabolist sticks dole liltingly,,curial bisexualisms siderations hemolysed,,damnabilities unkenneling halters,,peripheral congaing,,diatomicity,,foolings repayments,,hereabouts vamosed him,,slanters moonrock porridgy monstruous,,heartwood bassoonist predispositions jargoon dominances,,timidest inalienable rewearing inevitably,,entreating retiary tranquillizing,,uniparental droogs,,allotropous,,forzati abiogenetic,,obduration exempted unifaces,,epilating calisaya dispiteously coggles,,vestmented flukily ignifying complished hiccupy municipalize,,pentagraphs parcels sutler excavates,,stardust miscited thankfulness,,fouter pertused,,overpacks,,guarishes hylotheism,,pi\n'
            'La sangre fresca se filtra a traves de la linea que separa su piel y lentamente colorea su pecho rojo. Empiezo a hiperventilar a medida que crece mi compulsion. Las imagenes no desapareceran. Imagenes de mi metiendo el cuchillo en su carne continuamente, follando su cuerpo con la cuchilla, haciendo un lio de ella. Mi cabeza comienza a volverse loca cuando mis pensamientos comienzan a regresar. El dolor punzante asalta mi mente junto con mis pensamientos. Esto es desagradable. Absolutamente asqueroso. ¿Como podria dejarme pensar estas cosas? Pero es inconfundible. La lujuria continua perdurando a traves de mis venas. Un dolor en mis musculos proviene de la tension inedita experimentada por todo mi cuerpo. Su tercer ojo me esta acercando.'
        ),
        yuri_3=True,
    )

    poem_n1 = LegacyPoem(
        author='natsuki',
        title="'Águilas Pueden Volar",
        text=(
            'Monos pueden trepar\n'
            'Grillos pueden saltar\n'
            'Caballos pueden competir\n'
            'Búhos pueden cazar\n'
            'Chitas pueden correr\n'
            'Águilas pueden volar\n'
            'Gente puede tratar\n'
            'Pero eso es todo lo que harán.'
        ),
    )

    poem_n2 = LegacyPoem(
        author='natsuki',
        title='A Amy Le Gustan Las Arañas',
        text=(
            '¿Sabes que oí de Amy?\n'
            'A Amy le gustan las arañas.\n'
            '¡Ásperas, retorcidas, peludas y feas arañas!\n'
            'Por eso no soy su amiga.\n'
            '\n'
            'Amy tiene bonita voz.\n'
            'La he escuchado cantar mi canción favorita.\n'
            'Cada vez que cantaba el coro, al ritmo de las palabras mi corazón latía.\n'
            'Pero le gustan las arañas.\n'
            'Por eso no soy su amiga.\n'
            '\n'
            'Un día, me lastime la pierna.\n'
            'Amy me ayudo a ir a la enfermería.\n'
            'Intenté que no me tocara.\n'
            'Le gustan las arañas, sus manos asco dan.\n'
            'Por eso no soy su amiga.\n'
            '\n'
            'Amy tiene muchas amigas.\n'
            'Siempre la veo hablando con alguien.\n'
            'Probablemente sobre arañas.\n'
            '¿Y si a sus amigos también les gustan las arañas?\n'
            'Por eso no soy su amiga.\n'
            '\n'
            'No importa si tiene otros pasatiempos.\n'
            'No importa si lo tiene en privado.\n'
            'No importa si no hace daño.\n'
            '\n'
            'Es asqueroso.\n'
            'Ella es asquerosa.\n'
            'El mundo es mejor sin amantes de arañas.\n'
            '\n'
            'Y se lo contaré a todos.'
        ),
    )

    poem_n2b = LegacyPoem(
        author='natsuki',
        title='T3BlbiBZb3VyIFRoaXJkIEV5ZQ==',
        text=(
            'SSBjYW4gZmVlbCB0aGUgdGVuZGVybmVz\n'
            'cyBvZiBoZXIgc2tpbiB0aHJvdWdoIHRo\n'
            'ZSBrbmlmZSwgYXMgaWYgaXQgd2VyZSBh\n'
            'biBleHRlbnNpb24gb2YgbXkgc2Vuc2Ug\n'
            'b2YgdG91Y2guIE15IGJvZHkgbmVhcmx5\n'
            'IGNvbnZ1bHNlcy4gVGhlcmUncyBzb21l\n'
            'dGhpbmcgaW5jcmVkaWJseSBmYWludCwg\n'
            'ZGVlcCBkb3duLCB0aGF0IHNjcmVhbXMg\n'
            'dG8gcmVzaXN0IHRoaXMgdW5jb250cm9s\n'
            'bGFibGUgcGxlYXN1cmUuIEJ1dCBJIGNh\n'
            'biBhbHJlYWR5IHRlbGwgdGhhdCBJJ20g\n'
            'YmVpbmcgcHVzaGVkIG92ZXIgdGhlIGVk\n'
            'Z2UuIEkgY2FuJ3QuLi5JIGNhbid0IHN0\n'
            'b3AgbXlzZWxmLg=='
        ),
    )

    poem_n3 = LegacyPoem(
        author='natsuki',
        title='Seré Tu Playa',
        text=(
            'Tu mente está tan llena de problemas y temores\n'
            'Eso disminuyó tu maravilla a través de los años\n'
            'Pero hoy tengo un lugar especial\n'
            'Una playa para que vayamos.\n'
            '\n'
            'Una orilla que se extiende más allá de tu vista\n'
            'Un mar que ilumina con luz brillante\n'
            'Las paredes en tu mente se desvanecerán\n'
            'Antes que el sol resplandeciente.\n'
            '\n'
            'Seré la playa que tus preocupaciones lave\n'
            'Seré la playa que cada día sueñes\n'
            'Seré la playa que hace que tu corazón salte\n'
            'como hace mucho no sientes.\n'
            '\n'
            'Enterremos tus pesados pensamientos en una pila de arena\n'
            'Cúbrete en rayos de sol y toma mi mano\n'
            'Lava tus inseguridades en el mar salado\n'
            'Y déjame verte brillando.\n'
            '\n'
            'Dejemos tus recuerdos en un rastro arenoso\n'
            'Libéralos en mis velos ventosos\n'
            'Y recuerda las razones por las que eres maravilloso\n'
            'Cuando presionas tus labios en los míos.\n'
            '\n'
            'Seré la playa que tus preocupaciones lave\n'
            'Seré la playa que cada día sueñes\n'
            'Seré la playa que hace que tu corazón salte\n'
            'como hace mucho no sientes.\n'
            '\n'
            'Pero si me dejas a tu lado\n'
            'Tu propia playa, tu propio escape\n'
            'Aprenderás de nuevo a amarte.'
        ),
    )

    poem_n3b = LegacyPoem(
        author='natsuki',
        title='Porque tu',
        text=(
            'Conmigo cerca mañana será mas brillante \n'
            'Pero cuando hoy es tenue, sólo puedo mirar hacia abajo.\n'
            'Mi mirada es un poco más hacia adelante\n'
            'Porque tú me estás mirando.\n'
            '\n'
            'Cuando quiero decir algo, ¡Lo digo gritando!\n'
            'Pero mis sentimientos verdaderos nunca salían.\n'
            'Mis palabras están un poco menos vacías\n'
            'Porque tu me estás escuchando.\n'
            '\n'
            'Cuando algo está por encima de mí, trato de alcanzarlo.\n'
            'Pero lejos no llego, cuando pequeña me siento.\n'
            'Mi postura es más alta un poco\n'
            'Porque tu estás a mi lado.\n'
            '\n'
            'Creo en mí misma con todo mi corazón.\n'
            'Pero, ¿Qué hago cuando todo está destrozado?\n'
            'Mi fe ha aumentado\n'
            'Porque tú en mí has confiado.\n'
            '\n'
            'Mi pluma siempre mis sentimientos prueba.\n'
            'No soy buena escribiendo, pero pongo todas mis fuerzas.\n'
            'Más dulces son mis poemas \n'
            'Porque tú en mi piensas.\n'
            '\n'
            'Porque tú, porque tú, porque tú.'
        ),
    )

    poem_n23 = LegacyPoem(
        author='natsuki',
        title='',
        text=(
            'No sé de qué otra forma hacerlo. Pero ha habido algo que me ha preocupado. Yuri ha estado actuando un poco extraña últimamente. Sólo has estado aquí unos días, así que tal vez no lo sepas. Pero ella normalmente no es así. Ella siempre es callada y amable y atenta...Cosas como esas.\n'
            '\n'
            'Bien...Esto es avergonzante, pero me obligo a aguantarme. La verdad es que, Estoy muy preocupada. Pero si trato de hablarle, sólo se enojará de nuevo. No se qué hacer. Creo que eres la única persona a la que escucha. No se por qué. Pero trata de hacer algo. Tal vez puedas convencerla de ir a terapia.\n'
            '\n'
            'Siempre traté ser mejor amiga con Yuri, y me duele ver que esto está pasando. Sé que después voy a odiarme por esto, pero ahora no me importa. Me siento desamparada. Por favor, ve si puedes hacer algo. No quiero que nada malo le pase. Te hare pastelillos si tengo que. Sólo por favor trata de hacer algo.\n'
            '\n'
            'Y sobre Monika...No se por qué, pero ha estado desinteresada. Es como si quisiera que lo ignoráramos. Así que estoy enojada con ella, por eso te lo pido a ti. ¡¡¡¡NO DEJES QUE SEPA QUE ESCRIBI ESTO!!!! Actúa como si te hubiera dado un buen poema, ¿Vale? Cuento contigo. Gracias por leer.'
        ),
    )

    poem_s1 = LegacyPoem(
        author='sayori',
        title='Querida Luz de Sol',
        text=(
            'La forma en que brillas a través de mis persianas en la mañana\n'
            'Me hace sentir que me extrañaste.\n'
            'Besándome la frente para ayudarme a salir de la cama.\n'
            'De mis ojos el sueño frotaste.\n'
            '\n'
            '¿Me pides salir a jugar?\n'
            '¿Confías que hoy no lloverá?\n'
            'Miro arriba. Azul el cielo es.\n'
            'Es un secreto, pero confío en ti también.\n'
            '\n'
            'Si no fuera por ti, por siempre dormiría.\n'
            'Pero no me molesta.\n'
            '\n'
            'Quiero desayunar.'
        ),
    )

    poem_s2 = LegacyPoem(
        author='sayori',
        title='Botellas',
        text=(
            'Levanto mi cráneo como la tapa de un tarro.\n'
            'Es un lugar secreto donde mis sueños guardo.\n'
            'Pequeñas bolas de luz solar, todas como gatitos frotaré.\n'
            'Con mi índice y pulgar una sacaré.\n'
            'Es caliente y ardiente.\n'
            '¡Pero no hay tiempo que perder! A la botella lo regresaré.\n'
            'Pongo la botella en el estante con las demás.\n'
            'Pensamientos felices, pensamientos felices, pensamientos felices en botellas, todas en fila.\n'
            '\n'
            'Muchos amigos mi colección atrae.\n'
            'Cada botella, una estrella para hacer pases.\n'
            'A veces mis amigos de cierta manera se sienten.\n'
            'Una botella saco y el día salvé.\n'
            '\n'
            'Noche tras noche, más sueños.\n'
            'Amigos tras amigos, más botellas.\n'
            'Profundo y profundo van mis dedos.\n'
            'Descubriendo los secretos que se esconden en los rincones y grietas.\n'
            'Excavando y cavando.\n'
            'Raspando y raspando.\n'
            '\n'
            'Soplo el polvo de mis tapas de botellas.\n'
            'No parece que el tiempo haya transcurrido.\n'
            'Mi estantería vacía podría usar un poco más.\n'
            'Mis amigos, a través de mi puerta han mirado.\n'
            '\n'
            'Abro, y entran mis amigos.\n'
            'Dentro vienen, con mucha prisa. ¿Tanto quieren mis botellas?\n'
            'Las saco del estante, una tras otra.\n'
            'Dándoselas a cada uno de mis amigos.\n'
            'Cada una de mis botellas.\n'
            'Pero cada vez que las dejo ir, contra el suelo se romperán.\n'
            'Pensamientos felices, pensamientos felices, pensamientos felices por todo el suelo están.\n'
            '\n'
            'Se suponía que fueran mis amigos, mis amigos que no sonríen.\n'
            'Todos gritan, suplican. Algo.\n'
            'Pero sólo escucho eco, eco, eco, eco, eco\n'
            'En mi cabeza dentro.'
        ),
    )

    poem_s3 = LegacyPoem(
        author='sayori',
        title='%',
        text=(
            'Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza. Sal de mi cabeza\n'
            'Sal.\n'
            'De.\n'
            'Mi.\n'
            'Cabeza.\n'
            '\n'
            '\n'
            '\n'
            'Sal de mi cabeza antes de que haga lo mejor para ti.\n'
            'Sal de mi cabeza antes de que escuche todo lo que ella me dijo.\n'
            'Sal de mi cabeza antes de que te muestre cuanto te amo.\n'
            'Sal de mi cabeza antes de que termine este poema.\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            'Pero un poema nunca se acaba.\n'
            'Sólo deja de moverse.'
        ),
    )

    poem_m1 = LegacyPoem(
        author='monika',
        title='Hoyo en La Pared',
        text=(
            'No podría haber sido yo.\n'
            'Miro, la dirección en que sobresale el yeso.\n'
            '¿Un vecino ruidoso? ¿Un novio enojado? Nunca lo sabré. No estaba en casa.\n'
            'Echo un vistazo por una pista.\n'
            '¡No! No puedo ver. Ruedo, ciega, como una película dejada afuera en el sol.\n'
            'Pero es muy tarde. Mis retinas.\n'
            'Ya chamuscadas con una copia permanente de la imagen sin sentido.\n'
            'Es sólo un pequeño agujero. No era demasiado brillante.\n'
            'Era demasiado profundo.\n'
            'Estirándose para siempre en todo.\n'
            'Un agujero de infinitas opciones.\n'
            'Me doy cuenta ahora, que no estaba mirando adentro.\n'
            'Yo estaba mirando fuera.\n'
            'Y él, en el otro lado, estaba mirando dentro.'
        ),
    )

    poem_m21 = LegacyPoem(
        author='monika',
        title='Hoyo en La Pared pt.2',
        text=(
            'Pero él no me estaba mirando.\n'
            'Confundida, miro frenéticamente a mí alrededor.\n'
            'Pero mis ojos quemados ya no pueden ver el color.\n'
            '¿Hay otros en esta sala? ¿Están hablando?\n'
            '¿O son simplemente poemas en hojas planas de papel?,\n'
            '¿El sonido de trucos frenéticos garabateando en mis oídos?\n'
            'La habitación comienza a fallar.\n'
            'Cerrándose sobre mí.\n'
            'El aire que respiro se disipa antes de que a mis pulmones lleguen.\n'
            'Me entra el pánico. Debe haber una salida.\n'
            'Está justo ahí. Él está ahí.\n'
            '\n'
            'Al tragar mis miedos, blandí mi pluma.'
        ),
    )

    poem_m2 = LegacyPoem(
        author='monika',
        title='Guárdame',
        text=(
            'Los colores, no se detienen.\n'
            'Brillantes, hermosos colores\n'
            'Intermitentes, expandiendose, perforando\n'
            'Rojo, azul, verde\n'
            'Una sinfín\n'
            'Cacofonía\n'
            'De sin sentido \n'
            'ruido\n'
            '\n'
            '\n'
            'El ruido, no se detiene.\n'
            'Violentas, ásperas ondas\n'
            'Chirrando, chillando, perforando\n'
            'Seno, coseno, tangente\n'
            'Como tocar una pizzara en un tocadisco\n'
            'Como tocar un vinilo en una pizza\n'
            'Un sinfín\n'
            'poema\n'
            'sin sentido\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            'Cárgame\n'
        ),
    )

    poem_m22 = LegacyPoem(
        author='monika',
        title='Guárdame',
        text=(
            'Los colores, no se\n'
            'Brillantes, Her o os c l r s\n'
            'Inter tes, exp nd dose, perforando\n'
            'Rojo, verde, azul\n'
            'una  infín\n'
            'CACOFONÍA\n'
            'De sin sentido\n'
            'Ruido\n'
            '\n'
            '\n'
            'El ruido, no se DETIENE.\n'
            'Viol nt , asperas o das \n'
            'Ch r ando, llora do, perforando\n'
            'SENO, COSENO, TANGENTE\n'
            'Como tocar una pi zarra en un t cadisco\n'
            'Como tocar un CUCHILLO en una CAJA TORAXICA\n'
            ' n  inf n\n'
            'p  m\n'
            'Sin s nt do\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            '\n'
            'Bórrala\n'
        ),
    )

    poem_m3 = LegacyPoem(
        author='monika',
        title='La Dama que Todo lo Sabía',
        text=(
            'Un viejo cuento habla de una dama que deambula por la Tierra.\n'
            'La Dama que Todo lo Sabía.\n'
            'Una hermosa dama que ha encontrado todas las respuestas,\n'
            'Todo significado,\n'
            'Todo propósito,\n'
            'Y todo lo que alguna vez se buscó.\n'
            '\n'
            'Y aquí estoy yo,\n'
            '\n'
            '\n'
            '      Una pluma\n'
            '\n'
            '\n'
            'Perdida a la deriva en el cielo, víctima de las corrientes del viento.\n'
            '\n'
            'Día tras día, busco.\n'
            'Busco con poca esperanza, sabiendo que las leyendas no existen.\n'
            'Pero cuando todo lo demás me ha fallado,\n'
            'Cuando todos los demás se han alejado,\n'
            'La leyenda es todo lo que queda, la última estrella tenue brillando en el cielo crepusculante.\n'
            '\n'
            'Hasta que un día, el viento deja de soplar.\n'
            'Yo caigo.\n'
            'Y caigo y caigo, y caigo aún más.\n'
            'Suave como una pluma.\n'
            'Una pluma seca, inexpresiva.\n'
            '\n'
            'Pero una mano me atrapa entre su pulgar e índice.\n'
            'La mano de una bella dama.\n'
            'La miro a los ojos y no veo fin a su mirada.\n'
            '\n'
            'La Dama que Todo lo Sabía sabe lo que estoy pensando.\n'
            'Antes de que pueda hablar, ella responde con voz hueca.\n'
            '"He encontrado todas las respuestas, todas las cuales no son nada.\n'
            'No hay significado.\n'
            'No hay propósito.\n'
            'Y buscamos sólo lo imposible.\n'
            'No soy tu leyenda.\n'
            'Y tu leyenda no existe."\n'
            '\n'
            'Y con un suspiro, ella me devuelve a flote, y recojo una ráfaga de viento.'
        ),
    )

    poem_m4 = LegacyPoem(
        author='monika',
        title='Feliz Final',
        text=(
            'Pluma en mano, mi fuerza he encontrado.\n'
            'El valor que mi único amor me ha dado.\n'
            'Juntos, desmantelemos este mundo desmoronado\n'
            'Y una novela de nuestras fantasías escribamos.\n'
            '\n'
            'Con un movimiento de su pluma, la perdída encuentra su camino.\n'
            'En un mundo de elecciones infinitas, he aquí este día especial.\n'
            '\n'
            'Despues de todo,\n'
            'No todos los buenos tiempos a su fin deben llegar.'
        ),
    )

    _localized_poems = [
        ('poem_y1', poem_y1, author_y),
        ('poem_y2', poem_y2, author_y),
        ('poem_y3', poem_y3, author_y),
        ('poem_y3b', poem_y3b, author_y),
        ('poem_y22', poem_y22, author_y),
        ('poem_y23', poem_y23, author_y),
        ('poem_n1', poem_n1, author_n),
        ('poem_n2', poem_n2, author_n),
        ('poem_n2b', poem_n2b, author_n),
        ('poem_n3', poem_n3, author_n),
        ('poem_n3b', poem_n3b, author_n),
        ('poem_n23', poem_n23, author_n),
        ('poem_s1', poem_s1, author_s),
        ('poem_s2', poem_s2, author_s),
        ('poem_s3', poem_s3, author_s),
        ('poem_m1', poem_m1, author_m),
        ('poem_m21', poem_m21, author_m),
        ('poem_m2', poem_m2, author_m),
        ('poem_m22', poem_m22, author_m),
        ('poem_m3', poem_m3, author_m),
        ('poem_m4', poem_m4, author_m),
    ]
    for _identifier, _legacy_poem, _author in _localized_poems:
        _current_poem = poem_db.get_poem(_identifier)
        _legacy_poem.identifier = _identifier
        poem_db.add_poem(
            _identifier,
            _author,
            title=_legacy_poem.title,
            text=_legacy_poem.text,
            style="yuri_text_3" if _legacy_poem.yuri_3 else True,
            paper=_current_poem.paper,
            music=_current_poem.music,
            translate="none",
        )

label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=i11, paper=None):
    if poem is None:
        return
    $ poem_db.show_poem(
        poem.identifier,
        img=img,
        where=where,
        music=music,
        track=track,
        revert_music=revert_music,
        paper=paper,
    )
    return
