# MAX Facial Age Estimator Mini Web App

A simple web app utilizing the [MAX Facial Age Estimator](https://github.com/IBM/MAX-Facial-Age-Estimator) model. There are two components necessary to run this solution. One is the DL model which receives an image via APIs, then performs face detection/localization and age estimation. The second is the front end where a user submits an image to the model and displays the results of the model. 

> Also try the [MAX Facial Age Estimator Web App](https://github.com/IBM/MAX-Facial-Age-Estimator-Web-App)
for a version that processes webcam video instead of uploaded images.

1. [Running Locally with Docker](#running-locally-with-docker)
2. [Running Locally with Docker & Python](#running-locally-with-docker-and-python
)
3. [Running Remotely](#running-remotely)

## Running Locally with Docker

If you only have Docker installed, you can build & run both components of the solution as docker containers:

#### Start the Model API

1. To run the model docker image, which automatically starts the model serving API, run the command below. This will pull a pre-built image from Docker Hub (or use an existing image if already cached locally) and run it. If you'd rather build and run the model locally, or deploy on a Kubernetes cluster, you can follow the steps in the
[model README](https://github.com/IBM/MAX-Facial-Age-Estimator#steps). This command will map the port for the API server as well as the additional port needed for the web application created in the next section:

   ```bash
   docker run -it -p 5000:5000 -p 8000:8000 --name max-facial-age-estimator codait/max-facial-age-estimator
   ```

1. [Optional] The API server automatically generates an interactive Swagger documentation page. Go to `http://localhost:5000` to load it. From there you can explore the API and also create test requests. Use the `model/predict` endpoint to load a test file and get estimated ages and bounding boxes for the image from the API.

1. [Optional] You can also test the model API using curl. The [model assets folder](https://github.com/IBM/MAX-Facial-Age-Estimator/tree/master/assets) contains one image you can use to test out the API, or you can use your own.  You can also test it on the command line using curl as follows:

   ```
   curl -F "image=@path/to/image.jpg" -X POST http://localhost:5000/model/predict
   ```

#### Build the Web App

1. Clone the web app repository locally. In a terminal, run the following command:

   If you have git installed, run the folowing command:

   ```bash
   git clone https://github.com/jrtorres/MAX-Facial-Age-Estimator-Mini-Web-App.git
   ```

   If you do not have git installed, run the following command:

   ```bash
   docker run -ti --rm -v "$(pwd):/git" alpine/git clone https://github.com/jrtorres/MAX-Facial-Age-Estimator-Mini-Web-App.git
   ```

1. Change directory into the repository base folder:

   ```bash
   cd MAX-Facial-Age-Estimator-Mini-Web-App
   ```

1. Build the web app docker image by running:

   ```bash
   docker build -t max-facial-age-estimator-mini-web-app .
   ```

1. Run the web app container using:

   ```bash
   docker run --net='container:max-facial-age-estimator' -it max-facial-age-estimator-mini-web-app
   ```

1. Go to the web application using a web browser: http://localhost:8000


## Running Locally with Docker and Python

If you have Docker installed and Python, you can run the model as a docker container and the web application directly using python

#### Start the Model API

1. To run the modle docker image, which automatically starts the model serving API, run the command below:

   ```bash
   docker run -it -p 5000:5000 --name max-facial-age-estimator codait/max-facial-age-estimator
   ```

1. [Optional] The API server automatically generates an interactive Swagger documentation page. Go to `http://localhost:5000` to load it. From there you can explore the API and also create test requests. Use the `model/predict` endpoint to load a test file and get estimated ages and bounding boxes for the image from the API.

1. [Optional] You can also test the model API using curl. The [model assets folder](https://github.com/IBM/MAX-Facial-Age-Estimator/tree/master/assets) contains one image you can use to test out the API, or you can use your own.  You can also test it on the command line using curl as follows:

   ```bash
   curl -F "image=@path/to/image.jpg" -X POST http://localhost:5000/model/predict
   ```

#### Build the Web App

1. Clone the web app repository locally. In a terminal, run the following command:

   If you have git installed, run the folowing command:

   ```bash
   git clone https://github.com/jrtorres/MAX-Facial-Age-Estimator-Mini-Web-App.git
   ```

   If you do not have git installed, run the following command:

   ```bash
   docker run -ti --rm -v "$(pwd):/git" alpine/git clone https://github.com/jrtorres/MAX-Facial-Age-Estimator-Mini-Web-App.git
   ```

1. Change directory into the repository base folder:

   ```bash
   cd MAX-Facial-Age-Estimator-Mini-Web-App
   ```

1. Before running this web app you must install its dependencies (Note: You can also use virtual environments in python if you want to isolate these dependencies):

   ```bash
   pip install -r requirements.txt
   ```

1. You then start the web app by running:

   ```bash
   python app.py
   ```

1. Go to the web application using a web browser: http://localhost:8000


## Running Remotely

If you do not have docker or python installed locally. You can still run the solution remotely.  

#### Running on Play-with-Docker

1. Log into the play with docker environment - https://labs.play-with-docker.com/ (Note*: You will need docker ID to log into this environment).

1. Click the **`Add New Instance`** link on the left pane.

1. Start the age estimator model, which automatically starts the model serving API, by running the following command:

   ```bash
   docker run -d -p 5000:5000 -p 8000:8000 --name max-facial-age-estimator codait/max-facial-age-estimator
   ```

1. Clone the web app repository locally. In a terminal, run the following command:

   ```bash
   git clone https://github.com/jrtorres/MAX-Facial-Age-Estimator-Mini-Web-App.git
   ```

1. Change directory into the repository base folder:

   ```bash
   cd MAX-Facial-Age-Estimator-Mini-Web-App
   ```

1. Build the web app docker image by running:

   ```bash
   docker build -t max-facial-age-estimator-mini-web-app .
   ```

1. Run the web app container using:

   ```bash
   docker run --net='container:max-facial-age-estimator' -it max-facial-age-estimator-mini-web-app
   ```

1. Go to the web application using a web browser: http://localhost:8000


#### Deploy and Run on Kubernetes

You can also deploy the model and web app on Kubernetes using the latest docker images on Docker Hub. The web app will be available at port `8000` of your cluster.
The model will only be available internally, but can be accessed externally through the `NodePort`.

1. On your Kubernetes cluster, run the following commands:

   ```bash
   kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-Facial-Age-Estimator/master/max-facial-age-estimator.yaml
   ```

   ```bash
   kubectl apply -f https://raw.githubusercontent.com/CODAIT/MAX-Facial-Age-Estimator-Mini-Web-App/master/max-facial-age-estimator-mini-web-app.yaml
   ```

# Links

* [MAX Facial Age Estimator Web App](https://github.com/IBM/MAX-Facial-Age-Estimator-Web-App)
* [Model Asset eXchange (MAX)](https://developer.ibm.com/code/exchanges/models/)
* [Center for Open-Source Data & AI Technologies (CODAIT)](https://developer.ibm.com/code/open/centers/codait/)

# License

[Apache 2.0](LICENSE)
