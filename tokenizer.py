from tokenizers import Tokenizer, models, pre_tokenizers, decoders, normalizers, trainers
import json

# Initialize a tokenizer with the BPE model
tokenizer = Tokenizer(models.BPE())

# Set the normalizer
tokenizer.normalizer = normalizers.NFKC()

# Set the pre-tokenizer
tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel()

# Set the decoder
tokenizer.decoder = decoders.ByteLevel()

# Train the tokenizer using the BPE trainer
trainer = trainers.BpeTrainer(
    vocab_size=60000,
    min_frequency=2,
    special_tokens=["<PAD>", "<BOS>", "<EOS>"],
)

# Train the tokenizer on your dataset
files = ["quran-simple-clean.txt"]  # Replace this with the path to your dataset
tokenizer.train(files, trainer)

# Save the trained tokenizer
tokenizer.save("arabic_bpe_tokenizer.json")

# Load the trained tokenizer from the saved file
tokenizer = Tokenizer.from_file("arabic_bpe_tokenizer.json")

# Save the vocab.json file
with open("vocab.json", "w", encoding="utf-8") as vocab_file:
    vocab = tokenizer.get_vocab()
    json.dump(vocab, vocab_file, ensure_ascii=False)

# Load the tokenizer configuration from the arabic_bpe_tokenizer.json file
with open("arabic_bpe_tokenizer.json", "r", encoding="utf-8") as config_file:
    tokenizer_config = json.load(config_file)

# Extract the merges from the tokenizer configuration
merges = tokenizer_config["model"]["merges"]

# Save the merges to the merges.txt file
with open("merges.txt", "w", encoding="utf-8") as merges_file:
    for merge in merges:
        merges_file.write(f"{merge[0]} {merge[1]}\n")
