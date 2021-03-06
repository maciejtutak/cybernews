import dill as pickle
from collection.models import Entry, Tag
from django.core.management.base import BaseCommand, CommandError

import logging


logger = logging.getLogger(__file__)

class Command(BaseCommand):
    help = 'Queries the DB for untagged entries and updates them.'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        labels = Tag.objects.all()

        # helper function for TFIDF Vectorizer
        def identity(arg):
            return arg

        logger.debug('Opening svc_model_pipeline.pickle!')
        with open('svc_model_pipeline.pickle', 'rb') as f:
            model_lsvc = pickle.load(f)
            logger.info('model loaded OK.')

            queryset = Entry.objects.all().filter(tagged=False)
            articles_to_classify = [entry.article.text for entry in queryset]

            if len(articles_to_classify) > 0:
                results = model_lsvc.predict(articles_to_classify)

                # x = [[1, 0, 0], [1, 1, 1], [0, 0, 1]]
                # a = ['a', 'b', 'c']
                #
                # result = [['a'], ['a', 'b', 'c'], ['c']]
                #
                # [[a[i] for i, j in enumerate(k) if j == 1] for k in x]

                tags = [[labels[i] for i, j in enumerate(k) if j == 1] for k in results]

                for i, entry in enumerate(queryset):
                    entry.tagged = True
                    for tag in tags[i]:
                        entry.tags.add(tag)
                    entry.save()
            else:
                print('There are no new articles.')
                logger.info('There are no new articles.')

            logger.info('classify completed.')


