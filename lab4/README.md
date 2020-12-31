# lab 4
***
**1.** Ознайомився з Docker, запустив перевірку версії, виведення допомоги та тестовий імедж і перенаправив все у одни файл "my_work.log."  
**2.** Створив файл з іменем "Dockerfile",заповнив його, у ньому змінив посилання на свій репозиторій.  
**3.** Створив власний репозиторій на Docker Hub - https://hub.docker.com/repository/docker/denysitis/labpy4  
**4.** Виконав білд та завантажив його до репозиторію.  Django Images - https://hub.docker.com/layers/denysitis/labpy4/django/images/sha256-de4ec413327d3796593685709f0fb0f44c9ac11e968887842d724c11e7fc625f?context=repo  
**5.** Виконав команду для запуску веб-сервера "sudo docker run -it --name=django --rm -p 8000:8000 denysitis/labpy4:django"  
**6.** Переконався, веб-сайт працює.  
**7.** Створив Dockerfile.site  
**8.** Виконав команди імеджа:  
sudo docker build -t denysitis/labpy4:monitoring . --file Dockerfile.site  
sudo docker images  
sudo docker push denysitis/labpy4:monitoring  
Monitoring Image - https://hub.docker.com/layers/denysitis/labpy4/monitoring/images/sha256-38c6fd69bc6a730abcdefa547ff83d16a8cadc45fd738adc6427dfb234a0de65?context=repo  
**9.** Щоб отримати логи виконав команди:  
sudo docker run -it --name=django --rm -p 8000:8000 denysitis/labpy4:django
sudo docker run -it --rm --net=host -v $(pwd)/server.log:/app/server.log denysitis/labpy4:monitoring