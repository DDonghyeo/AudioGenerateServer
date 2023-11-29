# python build
FROM python:3.9

# 
# WORKDIR /code

# 
#COPY ./requirements.txt /code/requirements.txt

# install requirements 
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# 
#COPY ./app /code/app

# uvicorn run
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
