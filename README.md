# Selenium Testing Project

This project demonstrates how to use Selenium to automate web testing using Python. Selenium is a powerful tool for automating web browsers, and it's commonly used for testing web applications, scraping data, and automating repetitive tasks.

In this project, you'll find a simple example script that uses Selenium to perform automated testing on the Compozent website. The script opens a Chrome web browser, navigates to the Compozent website, and checks if the title of the page matches the expected title.

## Getting Started

### Prerequisites

- Python 3.x
- Chrome browser
- ChromeDriver (compatible with your Chrome browser version)
- Selenium library

### Installation

1. Clone this repository to your local machine:

    ```bash
      git clone https://github.com/AKSH2002/Simple_Selenium_Test.git
    ```


2. Install the required Python packages using pip:

    ```bash
      pip install -r requirements.txt
    ```


3. Download ChromeDriver:

- Visit the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/)
- Download the version compatible with your Chrome browser
- Extract and move `chromedriver` to a directory in your `PATH`

## Usage

1. Open the script `simple_selenium_test.py` in a text editor.

2. Replace `/usr/lib/bin/chromedriver` with the actual path to the ChromeDriver executable on your machine.

3. Run the script:

    ```bash
      python3 simple_selenium_test.py
    ```


4. The script will open the Chrome browser, navigate to "https://compozent.com", and verify if the title matches the expected title.

## Troubleshooting

- If you encounter issues with ChromeDriver or browser compatibility, consider using Chrome browser for testing as it's often easier to set up.
- Make sure to keep your Chrome browser and ChromeDriver updated to avoid compatibility problems.
- Refer to the official documentation of Selenium and related tools for further troubleshooting and support.