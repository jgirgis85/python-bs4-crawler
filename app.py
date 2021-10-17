import requests
from bs4 import BeautifulSoup
response = requests.get("https://jgirgis85.github.io/employee-list/")
page = BeautifulSoup(response.content, "html.parser")

employees_html_list = page.find_all("div", class_="employee")
employees_data = []
for employee_html_div in employees_html_list:
    employee_name = employee_html_div.find(
        "p", class_="full-name").getText().strip()
    employee_avatar = employee_html_div.find(
        "figure", class_="image").find("img")['src']
    employee_job = employee_html_div.find("h2", class_="job").getText().strip()
    employee_department = employee_html_div.find(
        "h3", class_="department").getText().strip()

    employees_data.append({
        'name': employee_name,
        'avatar': employee_avatar,
        'job': employee_job,
        'department': employee_department
    })

print(employees_data)
