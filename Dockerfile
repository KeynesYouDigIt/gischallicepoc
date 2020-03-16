FROM lambci/lambda-base-2:build

COPY . /app

# WORKDIR /app
# RUN chmod +x wait-for-it.sh
# RUN ./wait-for-it.sh db:5432 

WORKDIR /app/postSomeGis

RUN pip install pipenv \
    && pipenv install --system

CMD [ "pipenv", "run", "setup"]