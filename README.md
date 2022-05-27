# run django

```base
cd djangonautic/
pip install -r req.txt
python manage.py runserver
```

admin account : ngounse
passwd : 123

## add filed database table

python manage.py makemigrations

## migrate database table

python manage.py migrate

## python shell

from articles.models import Article

```bash
## list
Article.objects.all()

article2 = Article()

article2.title = "Django Rules"
## save
article3.save()
```

## create app

python manage.py startapp "folder name"

## to make change in setting effect

```base
python manage.py collectstatic
```
