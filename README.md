# PythonSharedModules

To Build First Module
```commandline
docker build -f FirstModule/Dockerfile -t firstmodules .

docker run -it --rm --name firstmodules firstmodules /app/FirstModule/run_main.sh /bin/bash
```

To Build Second Module
```commandline
docker build -f SecondModule/Dockerfile -t secondmodules .

docker run -it --rm --name secondmodules secondmodules /app/SecondModule/run_main.sh /bin/bash
```