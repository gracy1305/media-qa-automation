# Media QA Automation Demo

Built a Selenium-based automation script to validate media playback behavior in a web application.

--- 

## Demo
This project simulates a real-world QA automation flow by launching a browser, loading a media page, and programmatically validating video playback (play and pause actions) using Selenium.

---

## Features
- Browser automation with Selenium WebDriver
- DOM-based element detection
- JavaScript-driven media control (play/pause)
- Basic test validation and logging

---

## Tech Stack
- Python
- Selenium
- Chrome WebDriver
- HTML (for test page)

---

## How to Run

1. Install dependencies:
```pip install selenium```
2. Open your project in VS Code and start Live Server for `index.html`
3. Run the script:
```python test_media.py```
4. The browser will open and automatically:
  - Load the page
  - Play the video
  - Pause the video
  - Print test results in terminal

---

## Use Case
Simulates real-world QA testing for media-heavy applications such as:
- Streaming platforms
- Video-based web applications
- Media playback validation systems

---

## Future Improvements
- Add automated test cases (pass/fail conditions)
- Integrate with testing frameworks like PyTest
- Add CI/CD pipeline for automated testing
- Support multiple browsers (Firefox, Edge)

---

