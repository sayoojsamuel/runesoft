import logging

import azure.functions as func
import json

from .predict import predict_image_from_url

def main(req: func.HttpRequest) -> func.HttpResponse:
    image_url = req.params.get('img')

    if image_url:
        logging.info('Image URL received: ' + image_url)
        try:
            results = predict_image_from_url(image_url)
        except Exception as err:
            results = {"error":"Invalid URL or something else my lov: \n" + str(err) }
    else:
        logging.info('Coudnt fetch Image URL:')
        results = {"error":"Submit an image url with ?img="}

    headers = {
        "Content-type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }

    return func.HttpResponse(json.dumps(results), headers = headers)

"""
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
"""
