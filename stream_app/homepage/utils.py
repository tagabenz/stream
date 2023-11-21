import requests
import json

from stream_app import settings


class DataMixin():
    def get_user_context(self, **kwargs):
        context = kwargs
        context['title']='Категории - Lastream.online'
        context['output_url']=f"{settings.OME_LLHLS_STREAMING_HOST}/{settings.OME_APP_NAME}",

        return context

    def get_stream_list(self):

        return requests.get(settings.OME_API_GET_STREAMS,headers=settings.OME_API_AUTH_HEADER, timeout=0.3).json()['response']    