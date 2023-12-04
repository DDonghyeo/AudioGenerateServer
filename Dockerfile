# python build
FROM python:3.9

# 
# WORKDIR /code

# 
#COPY ./requirements.txt /code/requirements.txt

RUN ls

# install requirements 
RUN pip install --no-cache-dir --upgrade git+https://github.com/suno-ai/bark.git

# 
#COPY ./app /code/app

# uvicorn run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
