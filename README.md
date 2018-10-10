[![Build Status](https://travis-ci.org/CODAIT/MAX-Workshop-Web-App.svg?branch=master)](https://travis-ci.org/CODAIT/MAX-Workshop-Web-App)

# IBM Model Asset Exchange Demo - Facial Age Estimator

One place for all open source deep learning models.

[![Model Asset Exchange](/doc/source/images/MAX.png)](https://developer.ibm.com/code/exchanges/models/)

## Workshop Goal

Create a web application using the [MAX Facial Age Estimator model](https://github.com/IBM/MAX-Facial-Age-Estimator)

## Workshop prerequisite

* [Install docker](https://docs.docker.com/install/)
* Install a code editor (Sublime text) or Python IDE (PyCharm)

## Workshop Takeaways

* Build a docker image of a MAX model.
* Deploy a deep learning model with a REST endpoint
* Run a web application using the model's REST API

# Steps

## Run Locally

#### Start the Model API

1. [Deploy the Model](#deploy-the-model)
2. [Experiment with Model API (optional)](#experiment-with-model-api-optional)

#### Build the Web App

1. [Clone the repository](#clone-the-repository)
2. [Install dependencies](#install-dependencies)
3. [Edit the code](#edit-the-code)
4. [Start the server](#start-the-server)


### Start the Model API

#### Deploy the Model

* Run the docker image to automatically start the model serving API

```
$ docker run -it -p 5000:5000 codait/max-facial-age-estimator
```

The above command will pull docker image from Docker Hub and run it. 

* To build the model locally,  run steps under 'Run Locally' from the [model Readme](https://github.com/IBM/MAX-Facial-Age-Estimator)

#### Experiment with Model API (optional)

The API server automatically generates an interactive Swagger documentation page. Go to ```http://localhost:5000``` to load it. From there you see the API with the test requests.

Use the ```model/predict``` endpoint to load a test file and get estimated ages and bounding boxes for the image from the API.

The [model assets folder](https://github.com/IBM/MAX-Facial-Age-Estimator/tree/master/assets) contains one image you can use to test out the API, or you can use your own.

You can also test it on the command line, for example:

```
$ curl -F "image=@path/to/image.jpg" -X POST http://localhost:5000/model/predict
```

## Build the Web App

#### Clone the repository

Clone the repo locally by running the following command:

```
$ git clone https://github.com/CODAIT/MAX-Workshop-Web-App.git
```

Change the directory 

```
$ cd MAX-Workshop-Web-App
```

#### Install dependencies

Run the following command:

```
$ pip install -r requirements.txt
```

#### Edit the code

* To send an input image from the server to the model API for prediction, complete the code below in [app.py](app.py)

```
result_age = requests.post('http://localhost:5000/model/predict', files=my_files, json={"key": "value"})
```

* Extract prediction

```
output_data = result_age.json()
result = output_data['predictions']
```

* Update Web UI with result

```
return render_template("index.html", image_name=output_name, people=ppl_count, avg=average_age)
```

#### Start the server

Run the following command to start the web app:

```
$ python app.py
```

Access the web app at ```http://localhost:8000```

NOTE: 

* The Facial Age Estimator endpoint must be available at ```http://localhost:5000``` for the web app to successfully start.

* 'Average Age' will be useful if there is more than one person in the picture. If there is only one person, average age will be the person's detected age.

![Desired Result](/doc/source/images/result.png)


# Links

1. [Model Asset Exchange](https://developer.ibm.com/code/exchanges/models/)
2. [Center for Open-Source Data and AI Technologies](https://developer.ibm.com/code/open/centers/codait/)
3. [MAX Announcement Blog](https://developer.ibm.com/code/2018/03/20/igniting-a-community-around-deep-learning-models-with-model-asset-exchange-max/)
4. [Artificial Intelligence Code Patterns](https://developer.ibm.com/code/technologies/artificial-intelligence/)
5. [Code Pattern Playlist](https://www.youtube.com/playlist?list=PLzUbsvIyrNfknNewObx5N7uGZ5FKH0Fde)
6. Mater the art of data science with IBM's [Watson Studio](https://dataplatform.cloud.ibm.com/)
7. [Deep Learning with Watson Studio](https://www.ibm.com/cloud/deep-learning)


# License

[Apache 2.0](LICENSE)
