import torch
import multiprocessing

torch.set_num_threads(multiprocessing.cpu_count())

def get_device():
    if torch.cuda.is_available(): return "cuda"
    if torch.backends.mps.is_available(): return "mps"
    return "cpu"