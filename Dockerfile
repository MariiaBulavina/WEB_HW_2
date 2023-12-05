FROM python:3.12.0

ENV APP /bot_helper_dm

WORKDIR $APP

COPY . .

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install 

ENTRYPOINT [ "python3", "bot_helper_dm/bot.py"]