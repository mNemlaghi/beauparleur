# beauparleur
A simple GPT2 model based generative application on streamlit, thanks to french pretrained model on Hugging Face

# Dependencies
Python 3.7 framework, with : 

- Hugging Face
- StreamLit

Alternatively, you might want to use Docker, in a two-step process:
1. Building the image

```
docker build -f deploy/Dockerfile -t beauparleur .
```

2. Running the container : __it is a best practice to chose ports when running the application__ 

```
docker run --rm -p $YOURLOCALPORT:$REMOTEPORT -e REMOTEPORT=$REMOTEPORT --name bouche beauparleur 
```

