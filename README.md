
# ReactPy Application Example 

This is a project with the new library ReactPy, is just for fun, for practice but here some facts about this project.

## Dependencies

 - reactpy[fastapi]
 - uvicorn[standard]


Those dependecies were installed with the Prefered Installer Program (pip) as follows.

 - pip install "reactpy[fastapi]"
 - pip install "uvicorn[standard]"

To start the project you need to put the following lines of code:

    from reactpy import component, html, hooks
    from reactpy.backend.fastapi import configure
    from fastapi import FastAPI

    app = FastAPI()
    configure(app, NameOfTheRootComponent)



Then to run it you need to put the following command in the terminal:

  - uvicorn main:app --reload

  