# IBM Model Asset Exchange Demo - Age Estimator

One place for all open source deep learning models.

Link to [Model Asset Exchange](https://developer.ibm.com/code/exchanges/models/)

## Workshop Goal

Create a web application using [MAX-Age Estimator mode](https://github.com/IBM/MAX-Facial-Age-Estimator)

## Workshop prerequisite

* Install docker
* Run the below command to install all the dependencies:

```
$ pip install -r requirement.txt

```

## Workshop Takeaways

* Build docker image of MAX model.
* Deploy a deep learning model with a REST endpoint
* Run a web application using the model's REST API

# Steps

## Run Locally

### Start the Model API

1. [Deploy the Model](#deploy-the-Model)
2. [Experiment with Model API](#Experiment-with-Model-API) (optional)

### Building the Web App

1. 





# Start the Model API

### Deploy the Model

* Run the docker image to automatically start the model serving API

```
docker run -it -p 5000:5000 codait/max-facial-age-estimator
```

The above command will pull docker image from Docker Hub and run it. 

* To build the model locally,  run steps under 'Run Locally' from the [model Readme](https://github.com/IBM/MAX-Facial-Age-Estimator)

### Experiment with Model API

The API server automatically generates an interactive Swagger documentation page. Go to ```http://localhost:5000``` to load it. From there you see the API with the test requests.

Use the ```model/predict``` endpoint to load a test file and get estimated ages and bounding boxes for the image from the API.

The [model assets folder](https://github.com/IBM/MAX-Facial-Age-Estimator/tree/master/assets) contains one image you can use to test out the API, or you can use your own.

You can also test it on the command line, for example:

```
curl -F "image=@path/to/tom_cruise.jpg" -X POST http://localhost:5000/model/predict
```




