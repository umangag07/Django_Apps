# Django

## Contain Django apps(you can use these in your projects with few changes that are specified) and full projects.

 
## Install
python and pip should be downloaded already.

```python
 pip install django
```
## For typing commands you can use any commmand shell or "Git bash".

# Basics
# Database used-"Postgresql" instead of default databse 'sqllite3'
## Install 

Database link- 
[PostgresqlDatabase](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
Pgadmin link-
[Pgadmin](https://www.pgadmin.org/download/pgadmin-4-windows/)
(For handling the database)
## Using the database
   <ul>
 <li> First create your databse by opening pgadmin after setup.</li>
     <ol>
      <li>name-your choice</li>
      <li>user-postgres</li>
      <li>Then click create.</li>
     </ol>
 <li> Changing the database in the django project(Go to your project folder and then in settings.py)</li>
 <li>For examle-</li>   
 
          DATABASES = {
               'default': {
                            'ENGINE': 'django.db.backends.postgresql',
                            'NAME':'ecom', #(your specified name will be here)
                            'USER':'postgres',
                            'PASSWORD':'12345', #(your specified password of databse (you created while installation of the database) will be here.) 
                            'HOST':'localhost'
                          }
                        }
     
     </ul>
   
