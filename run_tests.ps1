# Clean previous results
Remove-Item -Recurse -Force allure-results -ErrorAction SilentlyContinue

# Run tests
pytest -v

# Preserve history
Copy-Item -Path allure-report\history -Destination allure-results\history -Recurse -Force -ErrorAction SilentlyContinue

# Copy allure properties
Copy-Item -Path allure.properties -Destination allure-results\allure.properties -ErrorAction SilentlyContinue

# Copy categories
Copy-Item -Path categories.json -Destination allure-results\categories.json -ErrorAction SilentlyContinue

# Generate report
allure generate allure-results --clean -o allure-report

# Open report
allure open allure-report