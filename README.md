# basket_io

To up and running backet_io:_

1. clone this project

2. Build docker containers: sudo docker-compose build web

3. Run Django migrations: docker-compose run web python manage.py migrate

4. Create super user: docker-compose run web python manage.py createsuperuser

5. sudo docker-compose up web




Author:

https://gist.github.com/grillazz/0efa5c364f0e8a8c61e9b91310bd5954

https://www.linkedin.com/in/jakubmiazek

https://keybase.io/grillazz
