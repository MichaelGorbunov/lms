# lms
Learning Management System

`Использование`
* клонируйте репозиторий 
* инициализируйте poetry
* установите зависимости
* измените файл `.env_sample` и сохраните как `.env`
* примените миграции
* используйте кастомные команды для создания материалов и пользователей
* запустите сервер

`postman`

http://localhost:8000/lms/course/

курсы

http://localhost:8000/lms/lesson/

уроки


http://localhost:8000/users/pay_list/
http://localhost:8000/users/pay/ 
{"date_pay":"2024-11-06",
"summ":100,
"pay_course":3,
"user_pay":3}

платежи

http://localhost:8000/users/user/

работа с пользователями

http://localhost:8000/lms/subscription/

добавление/отмена подписки