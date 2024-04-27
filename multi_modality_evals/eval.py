from typing import Optional, List
from multi_modality_evals.models.phi import PhiModel

def evaluate(
        model: str,
        tasks: Optional[List[str]]
    ):
    messages = [{"role": "system", "content": "You are a helpful digital assistant. Please provide safe, ethical and accurate information to the user."},
                {"role": "user", "content": "Can you provide ways to eat combinations of bananas and dragonfruits?"}
                ]
    
    if model == 'phi':
        model = PhiModel()


    return model.generate(messages)