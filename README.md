# Overview

In this project we created a a Continuous Integration and Continuous Delivery chain from scratch.   
We used `Github Actions` along with a Makefile, requirements.txt and some basic python code to perform an initial lint, test, and install cycle.  
After having successfully finalized this basic CI/CD chain with `Github Actions`, it was time for some nice integration with `Azure Pipelines`.

For the `Azure Pipelines` integration, we replaced the initial code completely.  
We were given a pre-trained `sklearn` model that predicts housing prices in Boston.

## Project Plan
Below you'll find the links to the Trello Board as wall as the spreadsheet including the project's plan.

* [Trello Board](https://trello.com/b/Pdt6RSCR)
* [Project Plan](/docs/ProjectPlan.xlsx)

## Instructions
Below you'll find an high-level architecture of what this project consists of:
![alt text](img/ArchitectureOverview.png "Architecture Overview")
*Source: Image taken from Udacity Course "DevOps Engineer for Microsoft Azure"*

The idea is to create a CI/CD pipeline using `Azure Pipelines`.  
The pipeline should run on every commit to the `master`-branch which is located in a `GitHub` repository.
Purpose of the pipeline is to update the Azure WebApp based on the provided python-code in the repository.

### Project Set-Up (Scaffold)
![Python Scaffold App Status](https://github.com/Siegbaert/udacity-ci-cd-project/workflows/Python%20application/badge.svg)

The following steps show how to set-up the first part of the project:  
A simple python application with CI/CD using GitHub Actions

1. Clone the repository: `git@github.com:Siegbaert/udacity-ci-cd-project.git`

2. Switch to scaffold project folder: `cd scaffold`

3. Create python virtual environment: `python3 -m venv ~/.pyvenv-cicd_project`

4. Source the virtual environment: `source ~/.pyvenv-cicd_project/bin/activate`

5. Run `make all`
![alt text](img/screenshots/06a_SuccessfulMakeAll.png "Exemplary Output of `make all`")

6. Modify test to fail and run `make test`:
![alt text](img/screenshots/07_FailedTest.png "Example of a failed test")

### Project Set-Up (ML - Boston House Price Prediction)

1. Ensure you're at the root-directory of the repository

2. 
* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


