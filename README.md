# Star Wars UI & API Automation Assessment

This repository contains the automated UI and API tests for a Star Wars movie app as part of DigiCert's technical assessment.

## UI Test Scenarios (Selenium + Pytest)

- Sort movies by Title and assert the last movie is **The Phantom Menace**
- Check if **Wookie** is present in the Species list for **The Empire Strikes Back**
- Assert that **Kamino** is not part of Planets list for **The Phantom Menace**

## API Test Scenarios (requests + Pytest)

- Total number of movies is 6
- Director of the 3rd movie is **Richard Marquand**
- 5th movie’s producers are NOT **Gary Kurtz, George Lucas**

## Screenshots

Located in the `screenshots/` and `tests/screenshots/` folders.

## Tools Used

- Python
- Pytest
- Selenium
- Requests
- GitHub Actions (CI ready)
