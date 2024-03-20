import nbformat
from nbconvert import PDFExporter
from nbconvert.preprocessors import ExecutePreprocessor
from coloringAlgForStudents import STUDENTS_ID

# Load your notebook
path2Dir = fr'C:\Users\Simon\PycharmProjects\GraphColoringTest'
path2NB = path2Dir + '\Tests.ipynb'
with open(path2NB) as f:
    nb = nbformat.read(f, as_version=4)

# Execute all the cells
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': path2Dir}})

# Convert to PDF
pdf_exporter = PDFExporter()
# pdf_exporter.template_file = 'article'  # You can choose different templates

# Save as PDF
outputFileName = fr'C:\Users\Simon\PycharmProjects\GraphColoringTest\PDFs\{STUDENTS_ID}'
with open(outputFileName, "wb") as f:
    f.write(pdf_exporter.from_notebook_node(nb)[0])
