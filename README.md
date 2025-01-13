# lms
Learning Management System

`Использование`

###### клонируйте репозиторий 

git clone --branch deploy --single-branch https://github.com/MichaelGorbunov/lms

###### инициализируйте poetry или venv

###### установите зависимости

###### измените файл `.env_sample` и сохраните как `.env`

###### настройте удаленный сервер 

###### установите redis

apt install redis-server 


###### установите postgresql

apt-get install postgresql postgresql-contrib

настройте  postgresql для локального подключения  без пароля

создайте базу данных(например 'lms')

настройте gunicorn

пример файла настройки в директории data

установите nginx

пример файла настройки в директории data



в репозитории на github установите следующие секреты

_DEPLOY_DIR_
	
директория для развертывания
	
_POSTGRES_DB_
	
название вашей базы(например 'lms') 
	
_SECRET_KEY_
	
ключ django
	
_SSH_KEY_
	
значение приватного ключа ssh
	
_SSH_USER_

пользователь(например root) 



при внесении изменений в проект при помощи github actions

происходит тестирование проекта и развертывание его на подготовленнном сервере




`postman`

http://<ip сервера>/lms/course/

курсы

http://<ip сервера>/lms/lesson/

уроки


http://<ip сервера>/users/pay_list/
http://<ip сервера>/users/pay/ 
{"date_pay":"2024-11-06",
"summ":100,
"pay_course":3,
"user_pay":3}

платежи

http://<ip сервера>/users/user/

работа с пользователями

http://<ip сервера>/lms/subscription/

добавление/отмена подписки