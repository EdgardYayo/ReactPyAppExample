from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from form import Form


@component
def Item(text, initial_done=False):
    done, set_done = hooks.use_state(initial_done)

    def handle_click(event):
        set_done(not done)

    attrs = { "style": { "color":"green" } } if done else {}

    if done:
        return html.li(attrs, text)
    else:
        return html.li(
            html.span(attrs, text),
            html.button({ "on_click": handle_click }, "Hecho")
        )


@component
def HelloWorld():
    return html.div(
        html._("Lista de tareas"),
        html.ul(
            Item("Hacer tareas"),
            Item("Revisar Tareas"),
            Item("Reactpy")
        ),
        Form()
    )


app = FastAPI()
configure(app, HelloWorld)