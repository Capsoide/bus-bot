# Bus Ticket Booking Bot

This project is a Python-based automation bot that books bus tickets on the "MarcheRoma" website using Selenium WebDriver.

## Features
- Automatically fills in the departure and destination fields.
- Selects travel dates and passenger details.
- Searches for available trips and selects a booking option.
- Completes the booking form with user details.
- Handles cookies and confirmation prompts.

## Prerequisites

Before running the bot, ensure you have the following installed:

- **Python 3.x**
- **Google Chrome** (latest version)
- **ChromeDriver** (compatible with your Chrome version)
- Required Python packages:
  ```bash
  pip install selenium
  ```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/bus-booking-bot.git
   cd bus-booking-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and install ChromeDriver from [here](https://chromedriver.chromium.org/downloads) and add it to your system path.

## Usage

1. Update the script with your travel details, such as departure, destination, and date.
2. Run the script:
   ```bash
   python bot.py
   ```
3. The bot will automatically open the browser, navigate to the site, and proceed with booking.

## Configuration

Modify the following sections of `bot.py` to customize the booking details:

- **Departure:** `partenza.send_keys("Camerino")`
- **Destination:** `destinazione.send_keys("Porto San Giorgio")`
- **Travel date:** `data.send_keys("17/01/2025")`
- **Personal details:** Email, name, surname, phone number.

## Error Handling

- The bot implements basic error handling and retries in case of failure.
- If elements are not found, the script will wait and attempt to retry.

## Disclaimer

This project is intended for educational purposes only. Use it responsibly and ensure compliance with the website's terms of service.

## License

This project is licensed under the MIT License.

## Author

Nicola Capancioni

