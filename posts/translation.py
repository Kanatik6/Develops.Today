from modeltranslation.translator import translator, TranslationOptions
from posts.models import Post

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body_text','author_name')

translator.register(Post, NewsTranslationOptions)
