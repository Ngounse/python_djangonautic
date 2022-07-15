from articles.models import Article
import graphene
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article
        fields = ("id", "title", "slug", "body", "date", "thumb" )


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    all_articles = graphene.List(ArticleType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    article_by_title = graphene.Field(ArticleType, title=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

    def resolve_all_articles(root, info):
        return Article.objects.select_related("author").all()

    def resolve_article_by_title(root, info, title):
        try:
            return Article.objects.get(title=title)
        except Article.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)