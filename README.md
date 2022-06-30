<div id="top"></div>
<!--
*** Thanks for checking out the MXISOAGENT webscraping bot. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br /> 
<div align="center">
  <a href="https://github.com/dgustave/MXISOAGENT">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">MXISOAGENT Datapump Simulator</h3>

  <p align="center">
    Automated bot for MXISOAGENT website that simulates resaving accounts not available on Mxconnect. 
    <br />
    <a href="https://github.com/dgustave/MXISOAGENT"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dgustave/MXISOAGENT">View Demo</a>
    ·
    <a href="https://github.com/dgustave/MXISOAGENT/issues">Report Bug</a>
    ·
    <a href="https://github.com/dgustave/MXISOAGENT/issues">Request Feature</a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://mxisoagent.com/mx/login.aspx)

There are many tools associated to MXA datapump and the Applications Solutions Team wanted an easy solution to resave accounts to reduce the load. Currently our other systems do not retry to save accounts on Mxconnect. These systems act independeently causing issues like loading notes before accounts are updated on MXConnect causing massive amounts of lag in our system. 

Use the `README.md` to get started.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python](https://www.python.org/)
* [Selenium](https://selenium-python.readthedocs.io/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to to use the software for initial setup. This can replace the installation process.
* mxisoagent
  ```sh
  sh mxisoagent/setup.sh
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._


1. Clone the repo
   ```sh
   git clone https://github.com/dgustave/MXISOAGENT
   ```
2. Install Anaconda (MAC)
   ```sh
   brew install --cask anaconda 
   ```
3. Install pip
   ```py
   python3 -m pip install --upgrade pip
   ```
 4. Install pipenv
   ```py
   pip install pipenv
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This space is used to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For examples, please refer to the [Documentation]("https://github.com/dgustave/MXISOAGENT". After completing installations. 
   
   Store MXISOAgent credentials
   ```py
   python  mxisoagent -i
   ```
   
   Store MXISOAgent csv's from partners/portfolios in this directory and label appropiately for later use. 
   ```
   mxisoagent/data/external/ 
   ```

   Run MXISOAgent to start simulated datapump process
   ```py
   python  mxisoagent
   ```



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelogs
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" for other related MXA to MXC datapump issues until the product is sunsetted. 


See the [open issues](https://github.com/dgustave/MXAISOAGENT/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/{your_feature_name}`)
3. Commit your Changes (`git commit -m 'Add some {your_feature_name}'`)
4. Push to the Branch (`git push origin {your_feature_name}`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/dgustave/MXISOAGENT](https://github.com/dgustave/MXISOAGENT)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this link to get a list resources you might find helpful. It also contains a list of resources I would like to give credit to. 

* [REFRENCES](https://github.com/dgustave/MXISOAGENT/references/references.txt)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/dgustave/MXISOAGENT.svg?style=for-the-badge
[contributors-url]: https://github.com/dgustave/MXISOAGENTgraphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dgustave/MXISOAGENT.svg?style=for-the-badge
[forks-url]: https://github.com/dgustave/MXISOAGENT/network/members
[stars-shield]: https://img.shields.io/github/stars/dgustave/MXISOAGENT.svg?style=for-the-badge
[stars-url]: https://github.com/dgustave/MXISOAGENT/stargazers
[issues-shield]: https://img.shields.io/github/issues/dgustave/MXISOAGENT.svg?style=for-the-badge
[issues-url]: https://github.com/dgustave/MXISOAGENT/issues
[license-shield]: https://img.shields.io/github/license/dgustave/MXISOAGENT.svg?style=for-the-badge
[license-url]: https://github.com/dgustave/MXISOAGENT/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: [https://linkedin.com/in/othneildrew](https://www.linkedin.com/in/donleygustave/)
[product-screenshot]: references/imgs/mxisoagent.png
