# Operationalizing Machine Learning in Azure

## Overview

This is the second project from the Udacity Azure ML Nanodegree program. The project involved continuing working with the Bank Marketing dataset from Project 1. Azure was used to configure a cloud-based machine learning production model, deploy it, and consume it. In addition, the project also involved creating, publishing, and consuming a pipeline.

## Summary

The bankmarketing\_train.csv dataset was trained using AutoML modeling and the best model was deployed. The model was consumed using two methods – 1. Model Endpoint and 2. Pipeline Endpoint.

## Project Architecture

The image below showed the steps involved in performing this project. As I ended up using the lab provided by Udacity, I didn&#39;t have to perform the &quot;Authentication&quot; step, which is why this step is greyed out in the image. The two methods used to deploy and consume the model is also shown. In the &quot;Model Endpoint&quot; method, the best model is directly deployed to the Endpoint. Alternately, in the case of &quot;Pipeline Endpoint&quot; method, the training pipeline is published to the Endpoint. Pipelines provide a great way to automate the workflows. Registering and accessing dataset, Creating Experiment and Compute Clusters are done in both methods using different procedures as will be laid out in the later sections.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML1.jpg)

## Register Dataset

Bank marketing dataset is available under Registered Datasets (as shown in the image below) of the Azure Machine Learning tool for the &quot;Model Endpoint method&quot;, which uses GUI-based ML setup.The bankmarketing\_train.csv dataset contains various metrics about potential customers that could eventually be utilizing the services of the bank. The final objective of the project is to determine who is likely to end up becoming a customer based on the information available from the database.

The bankmarketing\_train.csv dataset can be accessed from the following link:

https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing\_train.csv


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML2.JPG)


In the case of &quot;Pipeline Endpoint&quot; method, the dataset is accessed using the following code:


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML3.jpg)


### Create Experiment

For the first method (Model Endpoint), a new Experiment with the name &quot;exp-automl&quot; is created using the GUI-based Automated ML setup. &quot;Minimum number of nodes&quot; is set to 1. Column &quot;y&quot; is chosen as the Target column.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML4.jpg)


&quot;Classification&quot; is chosen as the specific &quot;Task&quot; type. &quot;Training job time&quot; is set to 1 hr from the default 3 hrs for &quot;Exit Criterion&quot;. Max. concurrent iterations is set to 5.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML5.jpg)


For the &quot;Pipeline Endpoint&quot; method, the same experiment name is reused and specified using the SDK code.


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML6.jpg)


### Create a Compute Cluster

A new Compute Cluster named &quot;automl-cluster&quot; is created on the STANDARD\_DS12\_V2 machine.


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML7.jpg)


Similarly, for the &quot;Pipeline Endpoint&quot; method, the same cluster created from the previous method is used. The relevant code is shown in the image below.


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML8.jpg)


### Model Endpoint Method

In this section, the unique aspects of &quot;Model Endpoint&quot; method are discussed.

#### Automated ML

As explained in the previous sections, Automated ML method is performed using the GUI-based methodology. The Automated ML method automates all the aspects of Machine Learning and returns the best model.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML9.jpg)




#### Identify the Best Model

The &quot;VotingEnsemble&quot; model was chosen as the Best model with an Accuracy of 0.91775. The details of the Voting Ensemble method are discussed in the ReadME documentation of [https://github.com/Kbhamidipa3/udacityazure\_p1\_final].


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML10.jpg)


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML11.jpg)


The below image shows that the model does a decent job of predicting the outcome.


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML12.jpg)


#### Deploy the Best Model

The next step is to deploy the best model for consumption by the end user. For this, the best model is selected from the AutoML run and &quot;Deploy&quot; button highlighted in the following image is clicked.


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML13.jpg)


Azure Contained Instance (ACI) is chosen as the Compute Type as highlighted in the image below for generating Authentication Key. Authentication is enabled to avoid unauthorized access.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML14.jpg)


It takes a while for the process to complete. If everything is done correctly, the Deployment State should change to &quot;Healthy&quot; as shown in the image below.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML15.jpg)


A REST endpoint is created and authentication is enabled. However, &quot;Application Insights Enabled&quot; is by default set to &quot;false&quot;. This needs to be enabled so as to get some useful insights.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML16.jpg)


Before enabling the insights using logs.py, config.json files needs to be downloaded to the same folder where other files needed for this project are saved. JSON file helps to transmit data between applications.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML17.jpg)


The corresponding deployment name used in the &quot;Deploy&quot; step is set in the logs.py file. To enable the insights, service.update function is used and set to True in the file. The logs.py is then run in a GitBash like terminal.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML18.jpg)


Microsoft required authentication at this step.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML19.jpg)


Once the python code runs successfully, we can see that the &quot;Application Insights enabled&quot; is set to &quot;true&quot; as shown in the image below.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML20.jpg)


Primary and Secondary keys are generated as well as shown in the image below. And Primary Key will be used for authentication subsequently.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML21.jpg)



#### Consume Model Endpoints

The next step in the process is consuming the model endpoints. For this step, the json file listed under &quot;Swagger URI&quot; (highlighted in yellow in the image below) is downloaded to the swagger folder where &quot;serve.py&quot; and &quot;swagger.sh&quot; files are saved.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML22.jpg)


The next step is to ensure that the docker is installed on the computer. And serve.py is used to start a Python server on Port 8000.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML23.jpg)


When swagger.sh is run, Swagger container is run on port 80. Clicking on the &quot;petstore.swagger.io&quot; link in a browser at this point will run a generic one as shown below.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML24.jpg)


In order to run the deployed model, serve.py file is run on another terminal using &quot;python serve.py&quot;. At this point, the local host gets consumed by the serve.py file and the deployed automl model is now available as shown below:

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML25.jpg)


Interacting with the &quot;score&quot; next to POST shows the inputs that the model will take-in in order to make the prediction. We can see the inputs from the bank marketing database in the image below.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML26.jpg)


At this point, we need to ensure Apache Benchmark command-line tool is installed and available. Then the REST Endpoint and Primary key values retrieved from the Deploy model are used to update the endpoint.py file as shown in the two images below. The relevant inputs are updated in the endpoint.py as well.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML27.jpg)


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML28.jpg)


When the endpoint.py file is run, a data.json file is created in the same folder as the endpoint.py file.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML29.jpg)


The REST Endpoint and Primary key values also need to be updated in the benchmark.sh file as well as shown by the highlighted text in the image below.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML30.jpg)


Running the benchmark.sh file at this point provides a highly verbose output similar to what&#39;s shown in the following image. The things to pay attention to are:

The number of &quot;Failed Requests&quot;, which returned a value of zero. This indicates the model is running as expected.

The other important metrics are &quot;Requests per second&quot; and &quot;Time per request&quot;. The smaller numbers against these metrics show that the model is running well within the acceptable time.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML31.jpg)

Finally endpoint.py file is run succesfully with two input datasets in the terminal and the prediction is made as shown in the image below:

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML47.JPG)


### Pipeline Endpoint Method

The second method is deployment through the creation of pipeline endpoints. There are a few steps involved with this procedure as well. The entire SDK code written to implement the pipeline can be accessed from the &quot;aml-pipelines-with-automated-machine-learning-step.ipynb&quot; file saved to the github folder.

The model didn&#39;t run right away and gave errors due to an incompatibility with the newly updated SDK 1.19.0 version. In order to overcome this issue, the following code is run first. The code uninstalled the 1.19.0 version and installed the 1.18.0 version. This allowed the rest of the code to run without any issues.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML32.jpg)


#### Automated ML

The Automated ML is implemented using the SDK code below. Since the final objective is to make a yes or no kind of a prediction, the task is set to &quot;classification&quot;. All other settings of the code are discussed in the first project&#39;s ReadMe available at [https://github.com/Kbhamidipa3/udacityazure\_p1\_final].

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML33.jpg)


#### Create Pipeline and AutoML Step

PipelineData method is used to identify the desired outputs from a specified step as shown below.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML34.jpg)


The AutoML step is then created using the following code and the specified outputs are defined:

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML35.jpg)


Then the pipeline is defined, submitted using the experiment and run successfully as shown below:

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML36.jpg)


The pipeline run can be seen &quot;Running&quot; in the GUI as shown in the images below.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML37.jpg)


Once the run is completed, the following images can be seen in the GUI.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML38.jpg)


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML39.jpg)


#### Retrieve and Test the Best Model

Then the best model returned from the AutoML run is retrieved and tested using the code below. The confusion matrix shown at the end of the image is indicating that the model is performing well. More details about the confusion matrix can be found from the ReadMe available at [https://github.com/Kbhamidipa3/udacityazure\_p1\_final].

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML40.jpg)


![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML41.jpg)


#### Publish and Run from REST Endpoint

The final step involves Publishing and Running from the REST endpoint as shown below. Authentication is done before retrieving the Endpoint.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML42.jpg)


The REST url is then accessed and the pipeline run is submitted.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML43.jpg)


The GUI images look like the following.

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML44.jpg)


The Active Status and the REST Endpoints are also seen:

![GitHub Logo](https://github.com/Kbhamidipa3/-udacityazure_p2_final/blob/main/images/AML45.jpg)


# Documentation

In addition to this ReadMe documentation, the screencast of the full procedure from the Deploying part can be found at the following link:
