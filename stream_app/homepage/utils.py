import requests,json

from requests.auth import HTTPBasicAuth
from stream_app import settings


class DataMixin():
    def get_user_context(self, **kwargs):
        context = kwargs
        context['title']='Категории - Lastream.online'
        context['output_url']=settings.OUTPUT_URL

        return context

    def get_stream_list(self):

        return requests.get(f"{settings.PROTOCOL}://ome:8081/v1/vhosts/default/apps/input/streams", 
                            auth=HTTPBasicAuth(settings.OME_API_TOKEN[0], settings.OME_API_TOKEN[1])).json()['response']    