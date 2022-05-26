# run django

```base
cd djangonautic/
pip install -r req.txt
python manage.py runserver
```

## create app

python manage.py startapp "folder name"

## add filed database table

python manage.py makemigrations

## migrate database table

python manage.py migrate

## shell

from articles.models import Article

```bash
## list
Article.objects.all()

article2 = Article()

article2.title = "Django Rules"
## save
article3.save()
```

## to make change in setting eff

```base
python manage.py collectstatic
```
