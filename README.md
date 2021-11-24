# Kevin Kelly Sample Django App

The following routes are available (assuming the server is local and the port is 8000):
1. A JSON reponse. This will return {"Message": Hello World!"} in JSON format
```localhost:8000/kevinkelly/json_response```
and
2. This will use a template that is defined at templates/hello_world.html to render 'Hello World' in bold using the template.
```localhost:8000/kevinkelly/html_template_response```

## Misc Files
/.vscode folder contains vscode specific files including
- launch.json (This is the configuration used to launch the application in debug mode)
- workspace.code-workspace (This is just a file that contains the location of the base of the project)
