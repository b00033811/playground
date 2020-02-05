FROM python:3.5-stretch AS build-env
WORKDIR /usr/src/app
COPY requirements.txt test.py ./
RUN pip install --upgrade pip --upgrade setuptools && \
    pip install -r requirements.txt  && \
    pyinstaller test.py 
RUN echo "test app"
FROM gcr.io/distroless/python3
COPY --from=build-env /usr/src/app/dist /usr/src/app/dist
ENTRYPOINT ["/usr/src/app/dist/test/test"]
