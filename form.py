from reactpy import component, html, hooks


@component
def Form():
    face, set_face = hooks.use_state(False)
    facing = "😊" if face else "Submit"

    
    return html.form(
        html.label(
            html.input({
                "type":"text",
                "placeholder":"Name"
            })
        ),
        html.label(
            html.input({
                "type":"number",
                "placeholder":"Age"
            })
        ),
        html.label(
            html.input({
                "type":"date",
                "placeholder":"Birthday"
            })
        ),
        html.button({
            "type":"submit"
        }, facing)
    )