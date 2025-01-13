from django.conf import settings

import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

URL_BASIC = settings.URL_BASIC
URL_MAIN = settings.URL_MAIN

APPPLAT_KEY = settings.APPPLAT_KEY
APPPLAT_VALUE = settings.APPPLAT_VALUE
DNT_KEY = settings.DNT_KEY
DNT_VALUE = settings.DNT_VALUE
L_APP_ID_KEY = settings.L_APP_ID_KEY
L_APP_ID_VALUE = settings.L_APP_ID_VALUE
L_APP_PLATFORM_KEY = settings.L_APP_PLATFORM_KEY
L_APP_PLATFORM_VALUE = settings.L_APP_PLATFORM_VALUE
L_LOCALE_KEY = settings.L_LOCALE_KEY
L_LOCALE_VALUE = settings.L_LOCALE_VALUE
L_NONCE_KEY = settings.L_NONCE_KEY
L_NONCE_VALUE = settings.L_NONCE_VALUE
L_SIGN_KEY = settings.L_SIGN_KEY
L_SIGN_VALUE = settings.L_SIGN_VALUE
L_TIMESTAMP_KEY = settings.L_TIMESTAMP_KEY
L_TIMESTAMP_VALUE = settings.L_TIMESTAMP_VALUE
L_TRACE_ID_KEY = settings.L_TRACE_ID_KEY
L_TRACE_ID_VALUE = settings.L_TRACE_ID_VALUE
L_USER_LOCALE_KEY = settings.L_USER_LOCALE_KEY
L_USER_LOCALE_VALUE = settings.L_USER_LOCALE_VALUE
L_USER_TOKEN_KEY = settings.L_USER_TOKEN_KEY
L_USER_TOKEN_VALUE = settings.L_USER_TOKEN_VALUE
L_USER_TOKEN_VALUE_V2 = settings.L_USER_TOKEN_VALUE_V2
ORIGIN_KEY = settings.ORIGIN_KEY
ORIGIN_VALUE = settings.ORIGIN_VALUE
PROXYHEADER_KEY = settings.PROXYHEADER_KEY
PROXYHEADER_VALUE = settings.PROXYHEADER_VALUE
PROXYHEADER_VALUE_V2 = settings.PROXYHEADER_VALUE_V2
REFERER_KEY = settings.REFERER_KEY
REFERER_VALUE = settings.REFERER_VALUE

class JsonResponseView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'code': 200,
            'message': 'hello from backend',
        }
        return Response(data)

class SkillAPIView(APIView):
    def get(self, request):
        url = f"{URL_MAIN}/skill"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            L_NONCE_KEY: L_NONCE_VALUE,
            L_SIGN_KEY: L_SIGN_VALUE,
            L_TIMESTAMP_KEY: L_TIMESTAMP_VALUE,
            L_TRACE_ID_KEY: L_TRACE_ID_VALUE,
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class KolZoneListAPIView(APIView):
    def get(self, request):
        gender = request.query_params.get('gender', '0')
        skillId = request.query_params.get('skillId', '-1')
        url = f"{URL_BASIC}/kolZone/list?gender={gender}&skillId={skillId}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "PZP5Ve",
            "l-sign": "68d3df6426d7d1c",
            "l-timestamp": "1736764132997",
            "l-trace-id": "da3ae4a0320db4eef3f26b810ce6559a",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class PlayerInSkillsAPIView(APIView):
    def get(self, request):
        skillIds = request.query_params.get('skillIds', '1,20,3,2,167,100,139,90,22,21,18,69,23,87,10,65,160,89,60,122,102,103,159,109,113')
        url = f"{URL_MAIN}/player/inskills?skillIds={skillIds}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "A99qCY",
            "l-sign": "f2dcce56c1d53ea",
            "l-timestamp": "1736764133395",
            "l-trace-id": "7ef34e5bc2e9662c49523f00d52bef72",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class PlayerRecommendBatchAPIView(APIView):
    def get(self, request):
        page = request.query_params.get('page', '1')
        rows = request.query_params.get('rows', '10')
        url = f"{URL_MAIN}/player/recommend/batch?page={page}&rows={rows}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "5JC3TG",
            "l-sign": "a6b28c15dd2f6f0",
            "l-timestamp": "1736764133467",
            "l-trace-id": "33846cc9280dd0564771d6ed8d6f694c",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class SkillSearchOptsAPIView(APIView):
    def get(self, request):
        skill_id = request.query_params.get('skillId', '1')
        url = f"{URL_MAIN}/skill/searchopts?skillId={skill_id}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "skKvi7",
            "l-sign": "65825684a3661a3",
            "l-timestamp": "1736772658522",
            "l-trace-id": "d4e776a7d8c5d315468fb4bd2e268cf4",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE_V2,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE_V2,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class PlayerInskillBatchAPIView(APIView):
    def get(self, request):
        gender = request.query_params.get('gender', '0')
        level_ids = request.query_params.get('levelIds', '') # (rank: /api/skill/searchopts) -> 829, etc.
        newbie = request.query_params.get('newBie', '0')
        order = request.query_params.get('order', '') # desc, asc
        page = request.query_params.get('page', '1')
        position_ids = request.query_params.get('positionIds', '') # (role: /api/skill/searchopts) -> 1, etc.
        rows = request.query_params.get('rows', '30')
        skill_id = request.query_params.get('skillId', '1')
        sort = request.query_params.get('sort', '') # auditTime, avgStar, price, 

        url = f"{URL_MAIN}/player/inskill/batch?gender={gender}&levelIds={level_ids}&newBie={newbie}&order={order}&page={page}&positionIds={position_ids}&rows={rows}&skillId={skill_id}&sort={sort}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "tckVJP",
            "l-sign": "ee21ddd29006d93",
            "l-timestamp": "1736772658522",
            "l-trace-id": "5fc7d652e11a5d47fa7bf01846d6872e",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE_V2,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE_V2,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class PlayerDetailAPIView(APIView):
    def get(self, request):
        player_no = request.query_params.get('no')
        
        if not player_no:
            return Response({'error': 'The "no" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f"https://h-api.lita.game/funbit/v2/player/detail/g3?no={player_no}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "YNjAz1",
            "l-sign": "f091b23e7748d85",
            "l-timestamp": "1736775379180",
            "l-trace-id": "cf80d2cd8e741a670f715608e6cc7e3a",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            "l-user-token": "DeHujIL76cSdXl+RD0+EDEAZEZu+gXhk5eBuXBzgxMe19nv8pngXjnhY1nVXyWaRo3JRYtXmgyLUfb3Sq15heAvy07uiB0GwtcgWeCoTg58=",
            ORIGIN_KEY: ORIGIN_VALUE,
            "proxyheader": "eyJjaGVjayI6IkIzQTc4RkREMzA2NDZBRUUzNzkwNDBDNDdFQUNFMENBIiwidGltZSI6MTczNjc3NTM2NjEzOSwidXNlckxvY2FsZSI6ImluLUlEIiwidmVyc2lvbiI6IjIuMCJ9",
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)
