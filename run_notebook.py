
# simple runner to execute notebook locally (requires nbconvert)
# python run_notebook.py
from nbformat import read, write, NO_CONVERT
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat

with open('notebooks/pricing_model_notebook.ipynb') as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': './'}})

with open('notebooks/executed.ipynb', 'w') as f:
    nbformat.write(nb, f)
print('Executed notebook produced at notebooks/executed.ipynb')
