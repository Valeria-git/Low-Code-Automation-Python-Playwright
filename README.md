# Low-Code Automation – Python + Playwright

**Low-Code Automation – Python + Playwright** is a demo project (`part1`, `part2`) built with [Playwright for Python](https://playwright.dev/python).  
It demonstrates how to quickly create automated browser tests with minimal setup.

## Project structure
- `part1/` — first part of training: basic test scenarios
- `part2/` — second part: more advanced exercises
- `.gitignore` — ignored files and folders
- `README.md` — project documentation

## Project goals
- Learn the basics of test automation with Playwright and Python;  
- Write reliable UI tests with minimal effort;  
- Build a reproducible structure for future scaling (CI, reports, Page Object Model, etc.).  

## How to run

1. **Clone the repo and navigate to it:**
    ```bash
    git clone https://github.com/Valeria-git/Low-Code-Automation-Python-Playwright.git
    cd Low-Code-Automation-Python-Playwright
    ```

2. **Install dependencies:**
    ```bash
    playwright install
    ```

3. **Run tests:**
    ```bash
    pytest
    ```

4. **Generate HTML report (if `pytest-html` plugin is installed):**
    ```bash
    pytest --html=report.html
    ```

## Next steps
- Add more tests (using Page Object Model, fixtures, etc.);  
- Integrate reporting (Allure, HTML reports, screenshots, videos);  
- Set up CI (GitHub Actions, GitLab CI, etc.) to run tests automatically on push;  
- Extend coverage with cross-browser and cross-device testing.  

## Useful links
- [Playwright for Python: official docs](https://playwright.dev/python/docs/intro)  
- [Playwright Python on GitHub](https://github.com/microsoft/playwright-python)  
- [Best practices for Playwright tests](https://playwright.dev/docs/best-practices)  

---
 
