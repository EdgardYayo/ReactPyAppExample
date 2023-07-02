from reactpy import component, html, hooks


@component
def Form():
   

    
    return html.form({
        "style": {
            "display": "flex",
            "flex_direction": "column",
            "align_items":"center",
            "justify_content":"center",
            "gap":"10px",
            "border": "2px black solid",
            "width":"500px",
            "margin":"auto"
            
        }
    },  html.h1("Formulario de Registro"),
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
        html.button({"style": { "margin_bottom":"10px" } },{
            "type":"submit"
        }, "Submit")
    )