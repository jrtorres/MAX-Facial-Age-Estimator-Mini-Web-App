[![Build Status](https://travis-ci.org/CODAIT/MAX-Facial-Age-Estimator-Mini-Web-App.svg?branch=master)](https://travis-ci.org/CODAIT/MAX-Facial-Age-Estimator-Mini-Web-App)

# MAX Facial Age Estimator Mini Web App

A simple web app utilizing the [MAX Facial Age Estimator](https://github.com/IBM/MAX-Facial-Age-Estimator) model.

> Also try the [MAX Facial Age Estimator Web App](https://github.com/IBM/MAX-Facial-Age-Estimator-Web-App)
for a version that processes webcam video instead of uploaded images.

# Steps

## Run Locally

**Start the Model API**

1. [Deploy the Model](#deploy-the-model)
2. [Experiment with Model API (optional)](#experiment-with-model-api-optional)

**Build the Web App**

1. [Clone the repository](#clone-the-repository)
2. [Install dependencies](#install-dependencies)
3. [Start the server](#start-the-server)
4. [Configure ports (Optional)](#configure-ports-optional)

### Start the Model API

#### Deploy the Model

To run the docker image, which automatically starts the model serving API, run:

```
$ docker run -it -p 5000:5000 codait/max-facial-age-estimator
```

This will pull a pre-built image from Docker Hub (or use an existing image if already cached locally) and run it.
If you'd rather build and run the model locally, or deploy on a Kubernetes cluster, you can follow the steps in the
[model README](https://github.com/IBM/MAX-Facial-Age-Estimator#steps)

#### Experiment with Model API (optional)

The API server automatically generates an interactive Swagger documentation page.
Go to `http://localhost:5000` to load it. From there you can explore the API and also create test requests.

Use the `model/predict` endpoint to load a test file and get estimated ages and bounding boxes for the image from the API.

The [model assets folder](https://github.com/IBM/MAX-Facial-Age-Estimator/tree/master/assets)
contains one image you can use to test out the API, or you can use your own.

You can also test it on the command line, for example:

```
$ curl -F "image=@path/to/image.jpg" -X POST http://localhost:5000/model/predict
```

### Build the Web App

#### Clone the repository

Clone the web app repository locally. In a terminal, run the following command:

```
$ git clone https://github.com/CODAIT/MAX-Facial-Age-Estimator-Mini-Web-App.git
```

Change directory into the repository base folder:

```
$ cd MAX-Facial-Age-Estimator-Mini-Web-App
```

#### Install dependencies

Before running this web app you must install its dependencies:

```
$ pip install -r requirements.txt
```

#### Start the server

You then start the web app by running:

```
$ python app.py
```

You can then access the web app at: [`http://localhost:8000`](http://localhost:8000)

#### Configure ports (Optional)

If you want to use a different port or are running the model API at a different location you can change them with command-line options:

```
$ python app.py --port=[new port] --model=[endpoint url including protocol and port]
```

# Links

* [MAX Facial Age Estimator Web App](https://github.com/IBM/MAX-Facial-Age-Estimator-Web-App)
* [Model Asset eXchange (MAX)](https://developer.ibm.com/code/exchanges/models/)
* [Center for Open-Source Data & AI Technologies (CODAIT)](https://developer.ibm.com/code/open/centers/codait/)

# License

[Apache 2.0](LICENSE)
