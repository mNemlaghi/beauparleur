# -*- coding: utf-8 -*-
import argparse
from transformers import CamembertTokenizerFast
from transformers import  GPT2Config, GPT2LMHeadModel, GPT2Tokenizer
from abc import abstractmethod
from typing import List

class GPT2SentencesGenerator():
    """Abstract sentences GPT2 class, taking two inputs directly from Huffing Face directory: tokenizer and model"""
    def __init__(self, model_dir):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
        self.model = GPT2LMHeadModel.from_pretrained(model_dir)

    @abstractmethod
    def generate(self):
        """Abstract generative method""" 
        pass

    def decode(self, generated: List[int])-> List[str]:
        """ Decode model output """
        res = []
        for v in generated:
            res.append(self.tokenizer.decode(v, skip_special_tokens = True))
        return res

    def encode_context(self, contexte:str)->List[int]: 
        """encodes prompt input with UTF8 handling""" 
        utf8_contexte = contexte.encode("utf8").decode("utf8")
        input_ids = self.tokenizer.encode(utf8_contexte, return_tensors = "pt")
        return input_ids

class GreedySentencesGenerator(GPT2SentencesGenerator):
    def generate(self,  contexte:str)->List[str]:
        """ Greedy output generation method """
        input_ids = self.encode_context(contexte)
        generated = self.model.generate(input_ids, do_sample = False)
        return self.decode(generated)

class BeamSentencesGenerator(GPT2SentencesGenerator):
    def generate(self,  contexte:str, nsamples:int, num_beams:int)->List[str]:
        """  """
        input_ids = self.encode_context(contexte)
        generated = self.model.generate(input_ids, do_sample = False, num_beams= num_beams, num_return_sequences = nsamples, early_stopping=True)
        return self.decode(generated)

class SamplingSentencesGenerator(GPT2SentencesGenerator):
    def generate(self,  contexte:str, nsamples : int =10, temperature : int = 0.7,  top_p: float = 0.9, top_k : float =0)-> List[str]:
        input_ids = self.encode_context(contexte)
        generated = self.model.generate(
        input_ids,
        do_sample=True,
        top_p = top_p,
        top_k = top_k,
        temperature =temperature,
        num_return_sequences=nsamples,
        repetition_penalty = 1.2, 
        early_stopping = True)
        return self.decode(generated)

if __name__=='__main__':
    parser = argparse.ArgumentParser()    
    parser.add_argument("--contexte")
    parser.add_argument("--model_dir")
    parser.add_argument("--temperature", type = float, default = 0.7)
    parser.add_argument("--tensors_type",  default = "pt")
    parser.add_argument("--samples_output", default = "generated_sample.txt")
    args = parser.parse_args()
    g = SamplingSentencesGenerator(args.model_dir)
    res = g.generate(args.contexte, nsamples = 5, temperature = args.temperature)
    for v in res:
        print(v)
