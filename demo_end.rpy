screen demo_end():
    add "menu_bg"

    add "bg/splash3.png":
        xsize 200
        fit "contain"
        align (0.0, 0.0)

    vbox:
        align (0.5, 0.5)
        spacing 20

        text "Fin de la demo":
            color "#000000"
            size 40
            xalign 0.5

        null height 10

        text "Voces:":
            color "#000000"
            size 30
            xalign 0.5

        text "Sayori: Miki Geeky\n\nYuri: Yumi\n\nNatsuki: Alhura Driftveil\n\nMonika: Zulyand Céspedes":
            style "navigation_button_text"
            color "#000000"
            size 25
            xalign 0.5
            text_align 0.5

        text "mod programado: sontse":
            style "navigation_button_text"
            color "#000000"
            size 15
            xalign 1.8

        null height 30

        textbutton "Continuar sin voz":
            action Return()
            text_style "navigation_button_text"
            text_color "#000000"
            text_outlines []
            text_hover_color "#555555"
            xalign 0.5

        textbutton "Salir":
            action Function(renpy.quit)
            text_style "navigation_button_text"
            text_color "#000000"
            text_outlines []
            text_hover_color "#555555"
            xalign 0.5

label demo_end_label:
    call screen demo_end
    return
