# IBM Model Asset Exchange Demo - Age Estimator

One place for all open source deep learning models.

![Model Asset Exchange](docs/MAX.jpg)

## Workshop Goal

Create a web application using [MAX-Age Estimator mode](https://github.com/IBM/MAX-Facial-Age-Estimator)

## Workshop prerequisite

* [Install docker](https://docs.docker.com/install/)
* Install Code Editor (Sublime text) or Python IDE (PyCharm)

## Workshop Takeaways

* Build docker image of MAX model.
* Deploy a deep learning model with a REST endpoint
* Run a web application using the model's REST API

# Steps

## Run Locally

### Start the Model API

1. [Deploy the Model](#deploy-the-Model)
2. [Experiment with Model API](#Experiment-with-Model-API) (optional)

### Build the Web App

1. [Code check out](#Code-check-out)
2. [Install dependencies](#Install-dependencies)
3. [Code edit](#Code-edit)
4. [Running the server](#Running-the-server)


# Start the Model API

### Deploy the Model

* Run the docker image to automatically start the model serving API

```
docker run -it -p 5000:5000 codait/max-facial-age-estimator
```

The above command will pull docker image from Docker Hub and run it. 

* To build the model locally,  run steps under 'Run Locally' from the [model Readme](https://github.com/IBM/MAX-Facial-Age-Estimator)

### Experiment with Model API (optional)

The API server automatically generates an interactive Swagger documentation page. Go to ```http://localhost:5000``` to load it. From there you see the API with the test requests.

Use the ```model/predict``` endpoint to load a test file and get estimated ages and bounding boxes for the image from the API.

The [model assets folder](https://github.com/IBM/MAX-Facial-Age-Estimator/tree/master/assets) contains one image you can use to test out the API, or you can use your own.

You can also test it on the command line, for example:

```
curl -F "image=@path/to/tom_cruise.jpg" -X POST http://localhost:5000/model/predict
```

# Build Web App

### Code check out

Clone the repo locally by running the following command:

```
git clone https://github.com/SSaishruthi/Demo_app.git

```

Change the directory 

```
cd Demo_app
```

### Install dependencies

Run the below command.

```
pip install -r requirements.txt
```

### Code edit

* To send input image from server to model API for prediction, complete the below code in [app.py](app.py)

```
result_age = requests.post('http://localhost:5000/model/predict',files=my_files, json={"key": "value"})
```
* Extract prediction

```
output_data = result_age.json()
result = output_data['predictions']
```
* Update result to Web UI

```
return render_template("index.html", image_name=output_name, people= ppl_count, avg=average_age)
```

### Running the server

Run the below command to start the web app.

```
python app.py
```

Access web app at ```http://127.0.0.1:8000```

NOTE: The Facial Age Estimator endpoint must be available at ```http://localhost:5000``` for the web app to successfully start.


# Links

1. [Model Asset Exchange](https://developer.ibm.com/code/exchanges/models/)
2. [Center for Open-Source Data and AI Technologies](https://developer.ibm.com/code/open/centers/codait/)
3. [MAX Announcement Blog](https://developer.ibm.com/code/2018/03/20/igniting-a-community-around-deep-learning-models-with-model-asset-exchange-max/)
4. [Artificial Intelligence Code Patterns](https://developer.ibm.com/code/technologies/artificial-intelligence/)
5. [Code Pattern Playlist](https://www.youtube.com/playlist?list=PLzUbsvIyrNfknNewObx5N7uGZ5FKH0Fde)
6. Mater the art of data science with IBM's [Watson Studio](https://dataplatform.cloud.ibm.com/)
7. [Deep Learning with Watson Studio](https://www.ibm.com/cloud/deep-learning)


# License


