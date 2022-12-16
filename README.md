<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-software">About The Software</a>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#cite">Cite</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Software


A ready to use Python package (scripts) with a trained ML model to classify Sentinel-2 L1C image. The Python package takes the L1C product path and produces an RGB image with six classes (Water, Shadow, Cirrus, Cloud, Snow, and Other) at 20m resolution. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.


### Installation

Below is an example of how you can instruct on installing and setting up.

1. Clone the repo
   ```sh
   git clone https://github.com/kraiyani/Sentinel_2_image_scene_classifier.git
   ```

2. Goto Sentinel_2_image_scene_classifier directory and unzip
    ```
    cd Sentinel_2_image_scene_classifier
    ```

3. Install dependency
    ```sh
    pip3 install -r requirements.txt
    ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used.

Sample Sentinel 2 L1C images can be found under _sample_L1C_ folder.

1. Goto Project-Name directory
    ```
    cd Sentinel_2_image_scene_classifier
    ```
2. Run main.py as
    ```
    python3 main.py -i <inputdirectory> -o <outputdirectory>
    ```
3. Example
    ```
    python3 main.py -i sample_L1C/S2B_MSIL1C_20180115T112419_N0206_R037_T29SNC_20180115T133323.SAFE -o output/
    ```
4. Find classified file in output folder
    ```
    classified_S2B_MSIL1C_20180115T112419_N0206_R037_T29SNC_20180115T133323.SAFE.png

    post_processed_classified_S2B_MSIL1C_20180115T112419_N0206_R037_T29SNC_20180115T133323.SAFE.png

    ```

_Classified image color codes are: Water as Blue, Shadow as
Brown, Cirrus as light Purple, Cloud as White, Snow as Cyan and Other as Green_.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Kashyap Raiyani- k.raiyani@uninova.pt

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Cite

This work can be cited as:


1. MDPI and ACS Style
  ```
  Raiyani, K.; Gonçalves, T.; Rato, L.; Salgueiro, P.; Marques da Silva, J.R. Sentinel-2 Image Scene Classification: A Comparison between Sen2Cor and a Machine Learning Approach. Remote Sens. 2021, 13, 300. https://doi.org/10.3390/rs13020300
  ```

2. AMA Style
  ```
  Raiyani K, Gonçalves T, Rato L, Salgueiro P, Marques da Silva JR. Sentinel-2 Image Scene Classification: A Comparison between Sen2Cor and a Machine Learning Approach. Remote Sensing. 2021; 13(2):300. https://doi.org/10.3390/rs13020300
  ```

3. Chicago/Turabian Style
  ```
  Raiyani, Kashyap, Teresa Gonçalves, Luís Rato, Pedro Salgueiro, and José R. Marques da Silva. 2021. "Sentinel-2 Image Scene Classification: A Comparison between Sen2Cor and a Machine Learning Approach" Remote Sensing 13, no. 2: 300. https://doi.org/10.3390/rs13020300
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

