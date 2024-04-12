# PythonSharedModules

To Run the Module Locally in VSCode set the PYTHONPATH to the absoulte path of the folder
````
export PYTHONPATH="${PYTHONPATH}:/<absolute_path>/PythonSharedModules"
````

To Build First Module
```commandline
docker build -f FirstModule/Dockerfile -t firstmodules .

docker run -it --rm --name firstmodules firstmodules /app/FirstModule/run_main.sh /bin/bash
```

To Build and Run Second Module
```commandline
docker build -f SecondModule/Dockerfile -t secondmodules .

docker run -it --rm --name secondmodules secondmodules /app/SecondModule/run_main.sh /bin/bash
```
