import os
from pathlib import Path

import joblib
from django.test import TestCase

from ai.models import ReplyAi


class AiTest(TestCase):
    model_file_path = os.path.join(Path(__file__).resolve().parent, 'ai/reply_default_model.pkl')
    model = joblib.load(model_file_path)
    prediction = model.predict(['안녕'])
    print(prediction)

    # 추가 fit
    # transformed_X_train = model.named_steps['count_vectorizer'].transform(['안녕'])
    # model.named_steps['multinomial_NB'].partial_fit(transformed_X_train, [0])
    # joblib.dump(model, model_file_path)
    #
    # ReplyAi.objects.create(comment='안녕', target=0)
