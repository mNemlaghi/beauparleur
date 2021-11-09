import streamlit as st
from sampler import GPT2SentencesGenerator, SamplingSentencesGenerator, GreedySentencesGenerator, BeamSentencesGenerator
import meta

st.set_page_config(layout="wide")

@st.cache(allow_output_mutation = True)
def get_sentences_generator(method):
    model_dir = "antoiloui/belgpt2"
    if method =='sampling':
        return SamplingSentencesGenerator(model_dir)
    elif method == 'greedy':
        return GreedySentencesGenerator(model_dir)
    elif method == 'beam':
        return BeamSentencesGenerator(model_dir)
    else:
        return NotImplementedError


def display_parameters_from_generation_method(methode):
    user_input = st.text_input('Texte de départ (peut être vide)', "les modèles génératifs sont cool !")
    if methode == 'sampling':
        user_nsamples = st.number_input("Nombre de phrases", min_value=1, max_value = 20)
        user_temperature = st.slider("Choisissez une température : le degré de 'folie' du texte", min_value = 0.01, max_value = 1.5, value = 0.7)
        user_top_k = st.slider(" TOP K : choisissez parmi les K mots les plus probables dans la génération",  min_value = 0, max_value = 1000, value=0)
        user_top_p = st.slider(" TOP P : choisissez parmi le pourcentage des mots les plus probables dans la génération",  min_value = 0.5, max_value = 0.99, value = 0.9)
        args_dict= {"contexte":user_input, "nsamples":user_nsamples, "temperature":user_temperature, "top_p":user_top_p, "top_k":user_top_k}
    elif methode == 'greedy':
        args_dict= {"contexte":user_input}
    elif methode == 'beam':
        user_num_beams = st.number_input("Nombre de faisceaux de probabilités", min_value = 2, max_value = 10)
        user_nsamples = st.number_input("Nombre de phrases", min_value=1, max_value = 10)
        args_dict= {"contexte":user_input, "num_beams":user_num_beams, "nsamples":user_nsamples}
    else:
       st.write("Les autres méthodes arrivent !!!")
    return args_dict


def display_principles():
    for k,sentences in meta.body.items():
        st.header(k)
        for s in sentences:
            st.write(s)

def main():
    st.title(meta.TITLE)
    display_principles()
    methode = st.selectbox("Choisissez votre méthode de génération", ['sampling', 'greedy', 'beam'])
    generator = get_sentences_generator(methode)
    st.header(f"Paramètres de la méthode __{methode}__")
    args_dict = display_parameters_from_generation_method(methode)

    if st.button('Parle, beau parleur !'):
        res = generator.generate(**args_dict)
        for texte in res:
            st.write(texte)

if __name__=='__main__':
    main()
