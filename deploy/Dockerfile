FROM python:3.7-slim-buster

ENV REMOTEPORT 1091
RUN pip install --upgrade pip

RUN   useradd --create-home server

USER server

ENV PATH="/home/server/.local/bin:${PATH}"

COPY --chown=server:server src src

RUN pip install --user -r src/requirements.txt

## Downloading Belgian GPT2 Model, in order to accelerate startup time
RUN python -c "from transformers import GPT2Tokenizer; _ = GPT2Tokenizer.from_pretrained('antoiloui/belgpt2')"
RUN python -c "from transformers import GPT2LMHeadModel; _ = GPT2LMHeadModel.from_pretrained('antoiloui/belgpt2')"

## Running streamlit
CMD streamlit run src/app.py --server.port $REMOTEPORT
