from bs4 import BeautifulSoup
import requests
import time

print("Put Keyword, job title, or company")
key = input(">")
print("Put Area, city, or town")
area = input(">")
keyword = key.replace(' ','-')
areas = area.replace(' ','-')
print('')

def find_jobs():
    if area == "":
        html_text = requests.get(f'https://www.jobstreet.co.id/en/job-search/{keyword}-jobs/?sort=createdAt').text
    else:
        html_text = requests.get(f'https://www.jobstreet.co.id/en/job-search/{keyword}-jobs-in-{area}/?sort=createdAt').text
    soup = BeautifulSoup(html_text, 'lxml')
    list_of_jobs = soup.find_all('article', class_='sx2jih0 sx2jih1 zcydq88 zcydq83c zcydq81q _58veS_0')
    for index, jobs in enumerate(list_of_jobs):
        company_name = jobs.find('span', class_='sx2jih0 zcydq82c _18qlyvc0 _18qlyvcv _18qlyvc1 _18qlyvc8')
        if type(company_name)==type(None):
            company_name = jobs.find('span', class_='sx2jih0 zcydq83 zcydq82g').text
        else:
            company_name = jobs.find('span', class_='sx2jih0 zcydq82c _18qlyvc0 _18qlyvcv _18qlyvc1 _18qlyvc8').text
        job_name = jobs.find('h1', class_='sx2jih0 zcydq82c _18qlyvc0 _18qlyvcv _18qlyvc3 _18qlyvc8').text
        link = jobs.h1.a['href']
        location_and_salary = jobs.find_all('span',class_='sx2jih0 zcydq82c _18qlyvc0 _18qlyvcv _18qlyvc3 _18qlyvc6')
        location = location_and_salary[0].text
        salary = "not defined"
        if len(location_and_salary)>1:
            salary = location_and_salary[1].text
        with open(f'Output/{index}.text', 'w') as f:
            f.write(f"Position: {job_name} \n")
            f.write(f"Company: {company_name} \n")
            f.write(f"Location: {location} \n")
            f.write(f"Salary: {salary} \n")
            f.write(f"More Info: https://www.jobstreet.co.id{link}")


if __name__ == '__main__':
    while True:
        find_jobs()
        minutes=1
        time.sleep(minutes * 60)

