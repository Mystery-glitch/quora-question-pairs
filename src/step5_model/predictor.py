import torch
from sentence_transformers import SentenceTransformer,util

class SBERTPredictor:
    def __init__(self,path):
        self.model=SentenceTransformer(path)
    
    def predict(self,sentence1,sentence2):
        emb1=self.model.encode(sentence1,convert_to_tensor=True)
        emb2=self.model.encode(sentence2,convert_to_tensor=True)

        return util.cos_sim(emb1,emb2).item()

    def predict_batch(self,sentences1,sentences2,batch_size=32):
        emb1=self.model.encode(sentences1,batch_size=batch_size,convert_to_tensor=True)
        emb2=self.model.encode(sentences2,batch_size=batch_size,convert_to_tensor=True)

        scores=torch.nn.functional.cosine_similarity(emb1,emb2,dim=1)
        return scores.cpu().numpy()