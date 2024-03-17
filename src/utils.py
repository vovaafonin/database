def print_vacancies(vacancies_list):
    """Функция вывода вакансий"""
    for vacancy in vacancies_list:
        if vacancy['Salary_from'] != 0 and vacancy['Salary_to'] != 0:
            print(f'Наименование компании: {vacancy['Company_name']}\n'
                  f'Наименование вакансии: {vacancy['Vacancy_name']}\n'
                  f'Предлагаемая З/П: от {vacancy['Salary_from']} {vacancy['Currency']} '
                  f'до {vacancy['Salary_to']} {vacancy['Currency']}\n'
                  f'Ссылка на вакансию: {vacancy['Vacancy_url']}\n'
                  )
        elif vacancy['Salary_from'] != 0 and vacancy['Salary_to'] == 0:
            print(f'Наименование компании: {vacancy['Company_name']}\n'
                  f'Наименование вакансии: {vacancy['Vacancy_name']}\n'
                  f'Предлагаемая З/П: от {vacancy['Salary_from']} {vacancy['Currency']}\n'
                  f'Ссылка на вакансию: {vacancy['Vacancy_url']}\n'
                  )
        elif vacancy['Salary_from'] == 0 and vacancy['Salary_to'] != 0:
            print(f'Наименование компании: {vacancy['Company_name']}\n'
                  f'Наименование вакансии: {vacancy['Vacancy_name']}\n'
                  f'Предлагаемая З/П: до {vacancy['Salary_to']} {vacancy['Currency']}\n'
                  f'Ссылка на вакансию: {vacancy['Vacancy_url']}\n'
                  )
        elif vacancy['Salary_from'] == 0 and vacancy['Salary_to'] == 0:
            print(f'Наименование компании: {vacancy['Company_name']}\n'
                  f'Наименование вакансии: {vacancy['Vacancy_name']}\n'
                  f'Предлагаемая З/П не указана\n'
                  f'Ссылка на вакансию: {vacancy['Vacancy_url']}\n'
                  )