#!/bin/bash

# Function app and storage account names must be unique.
storageName=runestorage
functionAppName=runeserverless
region=westeurope

# Create a resource group.
az group create --name runeResourceGroup --location $region

# Create an Azure storage account in the resource group.
az storage account create \
  --name $storageName \
  --location $region \
  --resource-group runeResourceGroup \
  --sku Standard_LRS

# Create a serverless function app in the resource group.
az functionapp create \
  --name $functionAppName \
  --storage-account $storageName \
  --consumption-plan-location $region \
  --resource-group runeResourceGroup \
  --functions-version 2 \
  --os-type Linux \
  --runtime python
