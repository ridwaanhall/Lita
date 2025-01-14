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
L_USER_TOKEN_VALUE_V3 = settings.L_USER_TOKEN_VALUE_V3
L_USER_TOKEN_VALUE_V4 = settings.L_USER_TOKEN_VALUE_V4
ORIGIN_KEY = settings.ORIGIN_KEY
ORIGIN_VALUE = settings.ORIGIN_VALUE
PROXYHEADER_KEY = settings.PROXYHEADER_KEY
PROXYHEADER_VALUE = settings.PROXYHEADER_VALUE
PROXYHEADER_VALUE_V2 = settings.PROXYHEADER_VALUE_V2
PROXYHEADER_VALUE_V3 = settings.PROXYHEADER_VALUE_V3
PROXYHEADER_VALUE_V4 = settings.PROXYHEADER_VALUE_V4
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
        
        url = f"{URL_MAIN}/player/detail/g3?no={player_no}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "g5PcXV",
            "l-sign": "ef54f0d8c6dc953",
            "l-timestamp": "1736824456578",
            "l-trace-id": "d1bddf50f05c8a1315750abd8783a8dc",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE_V3,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE_V3,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class PlayerReceivedGiftAPIView(APIView):
    def get(self, request):
        player_id = request.query_params.get('id')
        
        if not player_id:
            return Response({'error': 'The "id" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f"{URL_MAIN}/player/received/gift?id={player_id}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "qfPAWO",
            "l-sign": "55bbb61e3f23110",
            "l-timestamp": "1736824457586",
            "l-trace-id": "2eef901980ee04c1ddb3b71d36ef6377",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE_V4,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE_V4,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class PlayerReceivedRankGiftAPIView(APIView):
    def get(self, request):
        player_id = request.query_params.get('id')
        
        if not player_id:
            return Response({'error': 'The "id" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f"{URL_MAIN}/player/received/rank/gift?id={player_id}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "6Serv9",
            "l-sign": "716d2ac70a158a7",
            "l-timestamp": "1736826174481",
            "l-trace-id": "153213d7e144c8f933ef2c94d1667617",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE_V4,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE_V4,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class PlayerReceivedRankTotalAPIView(APIView):
    def get(self, request):
        player_id = request.query_params.get('id')
        
        if not player_id:
            return Response({'error': 'The "id" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f"{URL_MAIN}/player/received/rank/total?id={player_id}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "K3HO3X",
            "l-sign": "13ed7fff4f041bb",
            "l-timestamp": "1736824457587",
            "l-trace-id": "2861f2c69b248d7a25616eddcc340beb",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE_V4,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE_V4,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class PlayerReceivedRankOrderAPIView(APIView):
    def get(self, request):
        player_id = request.query_params.get('id')
        
        if not player_id:
            return Response({'error': 'The "id" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f"{URL_MAIN}/player/received/rank/order?id={player_id}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "EKBbCe",
            "l-sign": "2d2400f267608d6",
            "l-timestamp": "1736826512143",
            "l-trace-id": "c42bae6df6183f5d70380f217d448419",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE_V4,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE_V4,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class PlayerSkillCommentAPIView(APIView):
    def get(self, request):
        skill_id = request.query_params.get('skillId')
        user_id = request.query_params.get('userId')
        
        if not skill_id or not user_id:
            return Response({'error': 'The "skillId" and "userId" parameters are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        page = request.query_params.get('page', '1')
        rows = request.query_params.get('rows', '5')
        
        url = f"{URL_MAIN}/player/skill/comment?skillId={skill_id}&userId={user_id}&page={page}&rows={rows}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "zRlBSH",
            "l-sign": "6d2b22a391a8946",
            "l-timestamp": "1736824457586",
            "l-trace-id": "eb635dd2f5a2a2a3e9b2ffd09e2b8d34",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE_V4,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE_V4,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class MomentUserListAPIView(APIView):
    def get(self, request):
        author_id = request.query_params.get('authorId')
        
        if not author_id:
            return Response({'error': 'The "authorId" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        moment_id = request.query_params.get('momentId', '0')
        
        url = f"{URL_MAIN}/moment/user/list?authorId={author_id}&momentId={moment_id}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "uc7zQD",
            "l-sign": "14981746a50abab",
            "l-timestamp": "1736825596428",
            "l-trace-id": "242dfc1b2c70a4ed3fb2e31386475ec4",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE_V4,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE_V4,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class MomentHotSortListAPIView(APIView):
    def get(self, request):
        batch_no = request.query_params.get('batchNo', '0')
        next_index = request.query_params.get('nextIndex', '0')
        
        url = f"{URL_MAIN}/moment/hotsort/list?batchNo={batch_no}&nextIndex={next_index}"
        headers = {
            APPPLAT_KEY: APPPLAT_VALUE,
            DNT_KEY: DNT_VALUE,
            L_APP_ID_KEY: L_APP_ID_VALUE,
            L_APP_PLATFORM_KEY: L_APP_PLATFORM_VALUE,
            L_LOCALE_KEY: L_LOCALE_VALUE,
            "l-nonce": "3s3HH9",
            "l-sign": "d43267c65f228f5",
            "l-timestamp": "1736828167855",
            "l-trace-id": "1883084bbdd3f6e2d39d3f52109a6de3",
            L_USER_LOCALE_KEY: L_USER_LOCALE_VALUE,
            L_USER_TOKEN_KEY: L_USER_TOKEN_VALUE_V4,
            ORIGIN_KEY: ORIGIN_VALUE,
            PROXYHEADER_KEY: PROXYHEADER_VALUE_V4,
            REFERER_KEY: REFERER_VALUE,
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)
