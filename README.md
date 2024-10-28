# Lead generation through Web Scraping Project

## Overview
This project is designed to generate business leads through scraping data about property management companies in London using Python and Selenium. 
The objective is to extract relevant information such as company names, contact details, website links. 
The data is then saved into a structured format like CSV.

## Technologies Used
- **Python**: The core programming language used for the project.
- **Selenium**: A web scraping tool to interact with and extract data from Google Maps.
- **Pandas**: For data manipulation and saving the scraped data into a CSV file.
- **ChromeDriver**: To automate and control the Chrome browser.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/EugeneMakanga/Leadgen.git

2. Install the required Python packages:
   ```bash
   pip install selenium pandas
   ```
3. Download and set up [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) and make sure it’s in your system’s PATH.

## How to Run the Project

1. Open the project in VS Code.
2. Update the search term in the script (e.g., "property management services in London").
3. Run the script:
   ```bash
   python main.py
   ```
4. The script will open Chrome, perform a search on Google Maps, and scrape the data into a CSV file (`output.csv`).

## Project Structure

```
project-directory/
│
├── main.py                        # The main script for scraping data
├── README.md                      # Project documentation
└── output.csv                     # Output file containing the scraped data
```

## Data Collected
- Company Name
- Website Link
- Contact Information (if available)

## Notes
- Make sure you have the latest version of Chrome and ChromeDriver installed.
- Be mindful of Google Maps’ terms of service when scraping data.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the open-source community for providing the tools used in this project.