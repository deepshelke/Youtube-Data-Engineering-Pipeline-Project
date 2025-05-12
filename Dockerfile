FROM public.ecr.aws/lambda/python:3.9

RUN pip install --upgrade pip && \
    pip install pandas pyarrow awswrangler

COPY app.py ${LAMBDA_TASK_ROOT}

CMD ["app.lambda_handler"]
