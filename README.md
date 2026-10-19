# Phys_probl_F34567

Code and solutions for problems from the [Physics 101 course](https://dl.tntu.edu.ua/bounce.php?course=124&p=/content.php?cid=332703) at TNTU.

## Quick start (for non‑GitHub users)

You do NOT need a GitHub account or to become a contributor to use these materials. Choose one of the options below:

- Download the whole repository as a ZIP
  1. Open the repository in a web browser: https://github.com/TNTU-Cyber-Physical-Systems-Laboratory/Phys_probl_F34567
  2. Click the green "Code" button and choose "Download ZIP".
  3. Extract the ZIP on your computer and open the extracted folder.

- Download a single file
  1. Open the file in the repository on GitHub.
  2. Click "Raw" to view the raw file contents, then save the page (File → Save) or right‑click → "Save link as..." to download the file.

- Use Jupyter notebooks online (if notebooks are included)
  - Open a notebook directly in Google Colab without a GitHub account:
    1. Go to https://colab.research.google.com
    2. Choose "GitHub" and paste the repository URL or a direct link to the notebook file (or use the file picker).
    3. Colab will open the notebook and allow you to run cells in the cloud.
  - Alternatively, use Binder (if a Binder configuration is provided) or run notebooks locally with Jupyter.

## Requirements and running code locally

Most scripts and notebooks in this repository use Python. Recommended steps to run code locally:

1. Install Python (3.8 or newer recommended) from https://python.org or use Anaconda/Miniconda.
2. Open a terminal (or Anaconda Prompt) and change into the repository folder you downloaded.
3. If this repository contains a `requirements.txt` file, install dependencies with:

   pip install -r requirements.txt

   If there is no `requirements.txt`, inspect the top of the script or the notebook for required packages (e.g., numpy, scipy, matplotlib) and install them individually, for example:

   pip install numpy scipy matplotlib jupyter

4. To run a Python script:

   python path/to/script.py

   To run a Jupyter notebook locally:

   jupyter notebook

   then open the notebook file in your browser and run the cells.

5. To execute a notebook from the command line and produce output (useful for batch runs):

   jupyter nbconvert --to notebook --execute --inplace path/to/notebook.ipynb


## How the code is organized

- Files are grouped by problem or topic. Look for folder or file names that include the problem number or title from the course materials.
- Each problem folder (when present) may include:
  - one or more scripts or notebooks that implement the solution,
  - input or data files the scripts use,
  - a short README or notes describing how to run those files.

If you are unsure which file to run for a particular course problem, browse the repository in your file explorer (after downloading) or view files on GitHub and look for filenames or folder names containing the problem number.

## Using the code without being a developer

- You are not required to know Git to use the code. Download files or the ZIP and run them using the instructions above.
- If you want to reproduce figures or results exactly, use the same package versions where possible (pin versions in a virtual environment or conda environment).
- If a script expects data files, place those files in the same folder as the script or adjust paths as indicated in the script's documentation/comments.

## Troubleshooting

- Missing modules: install the required Python packages (see "Requirements").
- Python version errors: try a newer Python 3.x release (3.8+).
- Path or file not found: make sure you downloaded the repository contents and are running the script from the correct folder or adjust file paths in the script.
- If a notebook fails in Colab due to missing packages, install them in a Colab cell using `!pip install package_name`.

## Contributing

If you would like to contribute (submit fixes, new solutions, or improvements), instructions for contributing are provided in the separate CONTRIBUTING.md file in this repository. Please read that file for the contribution process, coding style, and how to create pull requests.


---

If something in these instructions does not work for you, tell us which file or problem you're trying to run and what error you see; we can add more specific guidance.
