FROM python:3.9.2-slim
# WORKDIR /code
# COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# COPY ./app /code/app
CMD ["uvicorn", "main:app" "--port", "8000", "--reload"]