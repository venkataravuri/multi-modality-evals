from typing import List
from multi_modality_evals.models.model import TransformerModel
from transformers import AutoModelForCausalLM, AutoTokenizer

class PhiModel(TransformerModel):

    def __init__(self) -> None:
        super.__init__()
        self.model =  AutoModelForCausalLM.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
    
    def generate(self, messages) -> str:

        inputs = self.tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")

        outputs = self.model.generate(inputs, max_new_tokens=32)
        text = self.tokenizer.batch_decode(outputs)[0]

        return text