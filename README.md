<h1>FarmWise</h1>

<p>FarmWise is a project that utilizes Convolutional Neural Networks (CNN) implemented in TensorFlow to classify crop diseases. This tool aids in the identification and diagnosis of crop diseases, enabling farmers to take timely actions to mitigate crop damage.</p>

<h2>Requirements</h2>

<p>To run FarmWise, ensure you have the following dependencies installed:</p>

<ul>
        <li>Python 3.x</li>
        <li>TensorFlow 2.10.0</li>
        <li>streamlit 1.15.1</li>
        <li>numpy 1.23.5</li>
        <li>Pillow 9.3.0</li>
</ul>

<p>You can install these dependencies using pip and the provided <code>requirements.txt</code> file:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<h2>Setup</h2>

<p>FarmWise can be set up in a Python environment using Anaconda. Follow these steps to set up the environment:</p>

<ol>
        <li>Install Anaconda from <a href="https://www.anaconda.com/products/distribution">Anaconda's website</a>.</li>
        <li>Create a new Anaconda environment using the provided <code>environment.yml</code> file:</li>
</ol>

<pre><code>conda env create -f environment.yml</code></pre>

<p>Activate the Anaconda environment:</p>

<pre><code>conda activate farmwise</code></pre>

<h2>Usage</h2>

<p>Once the dependencies are installed and the environment is set up, you can run FarmWise using Streamlit:</p>

<pre><code>streamlit run farmwise.py</code></pre>

<p>This command will launch a local server, and you can access FarmWise by opening the provided URL in your web browser.</p>

<h2>Contributing</h2>

<p>If you'd like to contribute to FarmWise, please fork the repository, make your changes, and submit a pull request. We welcome any contributions that improve the accuracy, efficiency, or usability of the tool.</p>

<h2>License</h2>

<p>FarmWise is licensed under the MIT License.</p>
