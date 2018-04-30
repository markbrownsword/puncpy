## Python Punctuation Library (using NLTK)

### Prerequisites
[Install Miniconda](https://conda.io/miniconda.html)  

### Setup
```bash
# Install source from Github
mkdir PuncPy  
cd PuncPy  
git clone <https://github.com/markbrownsword/punc-py.git> .  

# Create Python 3.5 environment
conda create --name python35 --file requirements.txt

```

### Dev and Test

```bash
# Activate environment
conda activate python35

# Install (required one time only with pip option --editable used)
./install.sh

# Run (in Python Console)
```bash
>>> from puncpy.tagger import Tagger
>>> from puncpy.common import process_tagged_text
>>> tagger = Tagger('This is my own invention')
>>> result = tagger.tag_text()
>>> process_tagged_text(result)
```

# Test
python -m unittest discover -v

# Create Requirements File
conda list --export > requirements.txt 

# Deactivate environment
conda deactivate
```
