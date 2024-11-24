"""
The following example takes pre-trained MiniLM v2 from
huggingface models repository and executes against STS benchmark dataset
on CPU and GroqChip1 through GroqFlow.
"""
import os
from transformers import AutoTokenizer, AutoModel
import torch
from demo_helpers.compute_performance import compute_performance
from demo_helpers.args import parse_args

from groqflow import groqit


def evaluate_minilm(rebuild_policy=None, should_execute=True):
    # set seed for consistency
    torch.manual_seed(0)
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    # load pre-trained torch model
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

    # Custom input text
    custom_text = [
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step."
    ]

    # Tokenize custom input
    max_seq_length = 128
    tokenized_inputs = tokenizer(
        custom_text,
        max_length=max_seq_length,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )

    # Prepare custom inputs
    custom_inputs = {
        "input_ids": tokenized_inputs["input_ids"].to(torch.long),
        "token_type_ids": tokenized_inputs["token_type_ids"].to(torch.long),
        "attention_mask": tokenized_inputs["attention_mask"].to(torch.bool),
    }

    # Generate Groq model with custom inputs
    groq_model = groqit(model, custom_inputs, rebuild=rebuild_policy)

    # compute performance on CPU and GroqChip
    if should_execute:
        compute_performance(
            groq_model,
            model,
            dataset="stsb_multi_mt",
            tokenizer=tokenizer,
            max_seq_length=max_seq_length,
            task="sentence_similarity",
        )

    print(f"Proof point {__file__} finished!")


if __name__ == "__main__":
    evaluate_minilm(**parse_args())
