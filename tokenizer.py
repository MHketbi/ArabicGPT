from tokenizers import Tokenizer, trainers, normalizers, pre_tokenizers, processors
from tokenizers.models import BPE

# Create a BPE tokenizer model
tokenizer = Tokenizer(BPE(unk_token="[UNK]"))

# Add a normalizer that handles Arabic text
tokenizer.normalizer = normalizers.Sequence([
    normalizers.NFKC(),
    normalizers.Arabic()
])

# Add a pre-tokenizer that splits the input into words
tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

# Train the tokenizer on the Arabic corpus
trainer = trainers.BpeTrainer(vocab_size=30000, min_frequency=2, special_tokens=["[UNK]", "[CLS]", "[SEP]", "[MASK]", "[PAD]"])
tokenizer.train(files=["arabic_corpus.txt"], trainer=trainer)

# Save the tokenizer to a file
tokenizer.save("MegatronReady.json")
