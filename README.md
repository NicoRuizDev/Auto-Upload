# <div id="top"></div>
<!--
*** Hi
--> 



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  
  <h3 align="center">Auto-Upload</h3>

  <p align="center">
      An auto upload addon for NicoRuizDev/DiscordCDN!
    <br />
    <a href="https://discord.gg/JRVPjPe3d8"><strong>Join Discord »</strong></a>
    <br />
    <br />
    <a href="https://discord.gg/JRVPjPe3d8">View Demo</a>
    ·
    <a href="https://github.com/NicoRuizDev/Auto-Upload/issues">Report Bug</a>
    ·
    <a href="https://github.com/NicoRuizDev/Auto-Upload/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This addon allows you to quickly and easily upload screenshots to the DiscordCDN service by pressing a keyboard shortcut.

Once installed, pressing "Ctrl + PrtScn" will take a screenshot of your screen and copy the link in your clipboard automatically, you can paste it anywhere. The resulting file link, file size, and file name will be printed to the console and the file link will also be copied to your clipboard for easy sharing.

The addon makes use of the popular libraries pyautogui and keyboard to handle screenshotting and hotkey functionality, as well as the requests library to interact with the API and the pyperclip library to manage the clipboard.

This addon is a convenient and efficient solution for sharing screenshots, making it an ideal tool for anyone who frequently needs to share screenshots on Discord or other online platforms.


<div align="center">
<img src="https://raw.githubusercontent.com/NicoRuizDev/DiscordCDN/main/assets/home.gif" alt="Demo" width="880" height="532">
</div>

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python 3.7.9](https://www.python.org)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- DOCUMENTATION -->
## Documentation

Auto-Upload Addon Installation Guide
This guide will help you install the Auto-Upload Addon on your machine. The following steps assume that you have already installed Python and pip.

# Step 1: Install the Required Libraries
To use the addon, you must first install the required libraries. You can do this by running the following command in your terminal:
```sh
pip install pyautogui keyboard requests pyperclip
```
# Step 2: Clone or Download the Repository
Next, you need to obtain a copy of the addon code. You can either clone the repository using Git or download by clicking [here](https://github.com/NicoRuizDev/Auto-Upload/archive/refs/heads/main.zip).
# Step 3: Enter your APP Link in the url variable on `main.py`.
# Step 4: Run the Code
Once you have a copy of the code, navigate to the directory in your terminal and run the following command: 
```sh
python main.py
```
# Step 5: Use the Addon
You can now use the addon by pressing "ctrl + prtscn" on your keyboard. A screenshot of your screen will be taken and sent to the DiscordCDN API. The resulting file link, file size, and file name will be printed to the console and the file link will also be copied to your clipboard for easy sharing.

And that's it! You should now have the Auto-Upload Addon up and running on your machine. Happy screenshotting!

Warning: You must have DiscordCDN installed on your server, to setup click [here](https://github.com/NicoRuizDev/DiscordCDN)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b NicoRuizDev/Auto-Upload`)
3. Commit your Changes (`git commit -m 'Add some Auto-Upload'`)
4. Push to the Branch (`git push origin NicoRuizDev/Auto-Upload`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/NicoRuizDev/Auto-Upload](https://github.com/NicoRuizDev/Auto-Upload)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [Python 3.7.9](https://www.python.org)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/NicoRuizDev/Auto-Upload.svg?style=for-the-badge
[contributors-url]: https://github.com/NicoRuizDev/Auto-Upload/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/NicoRuizDev/Auto-Upload.svg?style=for-the-badge
[forks-url]: https://github.com/NicoRuizDev/Auto-Upload/network/members
[stars-shield]: https://img.shields.io/github/stars/NicoRuizDev/Auto-Upload.svg?style=for-the-badge
[stars-url]: https://github.com/NicoRuizDev/Auto-Upload/stargazers
[issues-shield]: https://img.shields.io/github/issues/NicoRuizDev/Auto-Upload.svg?style=for-the-badge
[issues-url]: https://github.com/NicoRuizDev/Auto-Upload/issues
[license-shield]: https://img.shields.io/github/license/NicoRuizDev/Auto-Upload.svg?style=for-the-badge
[license-url]: https://github.com/NicoRuizDev/Auto-Upload/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
