<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h1 align="center">U.S. House Price index Forecasting</h1>
  <p>Problem Statement: What are all the factors that could influence residential home prices across the United States over the next decade</p>
  <p align="center">
    A deep learning project using tensorflow package with EDA and interactive web-app
    <br />
    <a href="https://github.com/cpt-John/us_hpi_forecastingus_hpi_forecasting/blob/master/model.ipynb"><strong><h2>Go EDA and modeling »</h2></strong></a>
    <br />
    <a href="https://cpt-john-us-hpi-forecasting-streamlit-y33hzf.streamlitapp.com/"><strong><h2>Go to deployed web app »</h2></strong></a>
    <br />
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This project goes over the wrangling, EDA, and deployment of U.S. house price index forecasting

Here's what is covered:

- Basic loading wrangling of the data set
- Useful plots and EDA
- A LSTM deep learning model
- A web app complete with front end and back end ready for deployment

Use the `model.ipynb` to get started.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Python 3](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Scikit Learn](https://scikit-learn.org/stable/)
- ['TensoeFlow'](https://www.tensorflow.org/)
- [Streamlit](https://share.streamlit.io/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

Find instructions to install the following software if you are not using web-based interactive computing platform like [Jupyter Notebook](https://jupyter.org/) / [Google Colab](https://colab.research.google.com/?)

- Instructions to install [python](https://wiki.python.org/moin/BeginnersGuide/Download)
- Instructions to install [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/cpt-John/us_hpi_forecasting
   ```
2. Install python packages

   ```
   pip install -r requirements_all.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

The `model.ipynb` file discusses the main ideas of data wrangling, plotting and EDA. Towards the end you will find the process of modelling. Once you have understood the idea behind the modeling you can checkout the `web_app`; The `streamlit*` files are used for streamlit webapp.

### Note :

The `serialized` directory will contain files which are serialized to save the time fitting the model during deployment . These files are serialized in the `model.ipynb`

### Steps to start local development server

1. Start server
   ```
   streamlit run streamlit.py
   ```

### You can view the deployment on live server here <a href="https://cpt-john-us-hpi-forecasting-streamlit-y33hzf.streamlitapp.com/"><strong>Go to web app »</strong></a>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

John Francis - johnfrancis95815@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/cpt-John/us_hpi_forecasting?style=for-the-badge
[contributors-url]: https://github.com/cpt-John
[license-shield]: https://img.shields.io/github/license/cpt-John/us_hpi_forecasting?style=for-the-badge
[license-url]: https://github.com/cpt-John/us_hpi_forecasting/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/john-francis-526999148/
