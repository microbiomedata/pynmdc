"""Test workflow automation using run-time API"""
import os
import sys
import json
import requests

def get_site_token(client_id, client_secret):
    """Get run-time API access_token using user name and password."""

    api_url = 'https://api-dev.microbiomedata.org/token'
    headers = {"accept": "application/json"}
    credential = {"username": "",
                  "grant_type": "client_credentials",
                  "client_id": client_id,
                  "client_secret": client_secret,
                  "scope": "",
                  "password": ""}
    response = requests.post(api_url, data=credential, headers=headers)

    if response.status_code == 200:
        return response.json()['access_token']
    return None

def get_user(token):
    """Get user name"""
    users_me_url = "https://api-dev.microbiomedata.org/users/me/"
    headers = {"Accept": "application/json",
               "Authorization" : f"Bearer {token}",
               "Connection": "keep-alive"}
    response = requests.get(users_me_url, headers=headers)
    return response

def get_v1_outputs(token, data):
    """ Get the v1 outputs.

    This requires authentication as a client not a user.

    It needs a name change, e.g. v1_workflow_output_ingest
    """
    api_url = "https://api-dev.microbiomedata.org/v1/outputs"
    headers = {"Accept": "application/json",
               "Authorization" : f"Bearer {token}",
               "Connection": "keep-alive"}
    response = requests.post(api_url, headers=headers, json=data)
    return response


def get_workflows(token):
    """List registered workflows"""
    workflow_url = "https://api-dev.microbiomedata.org/workflows"
    headers = {"Accept": "application/json",
               "Authorization": f"Bearer {token}",
               "Connection": "keep-alive"}
    response = requests.get(workflow_url, headers=headers)
    return response


def get_objects_by_id(token, obj_id):
    api_url = f"https://api-dev.microbiomedata.org/objects/{obj_id}"
    headers = {"Accept": "application/json",
               "Authorization" : f"Bearer {token}",
               "Connection": "keep-alive"}
    response = requests.get(api_url, headers=headers)
    return response

