from transformers import GPT2LMHeadModel, GPT2Tokenizer

def analyze_with_gpt2(logs):
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    inputs = tokenizer.encode(logs, return_tensors="pt")
    outputs = model.generate(inputs, max_length=1000, num_return_sequences=1)

    analysis = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return analysis

def main():
    logs = "Esempio di log di sistema per l'analisi con GPT-2..."
    analysis = analyze_with_gpt2(logs)
    print(analysis)

if __name__ == "__main__":
    main()