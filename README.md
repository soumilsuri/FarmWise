# FarmWise

FarmWise is a project that utilizes Convolutional Neural Networks (CNN) implemented in TensorFlow to classify crop diseases. This tool aids in the identification and diagnosis of crop diseases, enabling farmers to take timely actions to mitigate crop damage.

## Requirements

To run FarmWise, ensure you have the following dependencies installed:

- Python 3.x
- TensorFlow 2.10.0
- streamlit 1.15.1
- numpy 1.23.5
- Pillow 9.3.0

You can install these dependencies using pip and the provided `requirements.txt` file:

```bash
pip install -r requirements.txt

# Setup
FarmWise can be set up in a Python environment using Anaconda. Follow these steps to set up the environment:

Install Anaconda from Anaconda's website.
Create a new Anaconda environment using the provided environment.yml file:
bash
Copy code
conda env create -f environment.yml
Activate the Anaconda environment:
bash
Copy code
conda activate farmwise
Usage
Once the dependencies are installed and the environment is set up, you can run FarmWise using Streamlit:

bash
Copy code
streamlit run farmwise.py
This command will launch a local server, and you can access FarmWise by opening the provided URL in your web browser.

Contributing
If you'd like to contribute to FarmWise, please fork the repository, make your changes, and submit a pull request. We welcome any contributions that improve the accuracy, efficiency, or usability of the tool.

License
FarmWise is licensed under the MIT License.
