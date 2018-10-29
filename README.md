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
5. [Instructions for Docker (Optional)](#instructions-for-docker-optional)

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

#### Instructions for Docker (Optional)

To run the web app with Docker the containers running the web server and the REST endpoint need to share the same
network stack. This is done in the following steps:

Modify the command that runs the Facial Age Estimator REST endpoint to map an additional port in the container to a
port on the host machine. In the example below it is mapped to port `8000` on the host but other ports can also be used.

    docker run -it -p 5000:5000 -p 8000:8000 --name max-facial-age-estimator codait/max-facial-age-estimator

Build the web app image by running:

    docker build -t max-facial-age-estimator-mini-web-app .

Run the web app container using:

    docker run --net='container:max-facial-age-estimator' -it max-facial-age-estimator-mini-web-app

##### Using the Docker Hub Image

You can also deploy the web app with the latest docker image available on DockerHub by running:

    docker run --net='container:max-facial-age-estimator' -it codait/max-facial-age-estimator-mini-web-app

This will use the model docker container run above and can be run without cloning the web app repo locally.

## Deploy on Kubernetes

You can also deploy the model and web app on Kubernetes using the latest docker images on Docker Hub.

On your Kubernetes cluster, run the following commands:

    kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-Facial-Age-Estimator/master/max-facial-age-estimator.yaml
    kubectl apply -f https://raw.githubusercontent.com/CODAIT/MAX-Facial-Age-Estimator-Mini-Web-App/master/max-facial-age-estimator-mini-web-app.yaml

The web app will be available at port `8000` of your cluster.
The model will only be available internally, but can be accessed externally through the `NodePort`.

# Links

* [MAX Facial Age Estimator Web App](https://github.com/IBM/MAX-Facial-Age-Estimator-Web-App)
* [Model Asset eXchange (MAX)](https://developer.ibm.com/code/exchanges/models/)
* [Center for Open-Source Data & AI Technologies (CODAIT)](https://developer.ibm.com/code/open/centers/codait/)

# License

[Apache 2.0](LICENSE)
