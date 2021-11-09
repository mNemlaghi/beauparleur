# beauparleur
A simple GPT2 model based generative application on streamlit, thanks to french pretrained model on Hugging Face

## Dependencies
Python 3.7 framework, with : 

- [Hugging Face](https://huggingface.co/) 🤗 
- [Streamlit](https://streamlit.io/)

You might want to execute the following command : 

```
pip install -r src/requirements.txt
```

After install, you can run the app by running the following command.

```
streamlit run src/app.py --server.port $YOURLOCALPORT
```

Alternatively (__RECOMMENDED__), you might want to use Docker, in a three-step process:
1. Building the image

```
docker build -f deploy/Dockerfile -t beauparleur .
```

2. Running the container : __it is a best practice to chose ports when running the application__ 

```
docker run -itd --rm -p $YOURLOCALPORT:$REMOTEPORT -e REMOTEPORT=$REMOTEPORT --name bouche beauparleur 
```

3. Now, you can open your browser at your local port, and enjoy the app ! 


## Model & generation methods.

Model used is  [Belgian GPT-2](https://github.com/antoiloui/belgpt2), an attempt on pre-training GPT-2 like model on French data. 
Three methods are currently experimented thanks to Hugging Face : 

- Greedy generation
- Beam search generation
- Sampling (Top-K and/or Top-P)

