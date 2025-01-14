import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class BaseAPIView(APIView):
    def get_base_headers(self):
        return {
            settings.APPPLAT_KEY: settings.APPPLAT_VALUE,
            settings.DNT_KEY: settings.DNT_VALUE,
            settings.L_APP_ID_KEY: settings.L_APP_ID_VALUE,
            settings.L_APP_PLATFORM_KEY: settings.L_APP_PLATFORM_VALUE,
            settings.L_LOCALE_KEY: settings.L_LOCALE_VALUE,
            settings.L_USER_LOCALE_KEY: settings.L_USER_LOCALE_VALUE,
            settings.ORIGIN_KEY: settings.ORIGIN_VALUE,
            settings.REFERER_KEY: settings.REFERER_VALUE,
        }

    def get_response(self, url, headers):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.text, status=response.status_code)

class JsonResponseView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "API Documentation": {
                "Author": "ridwaanhall",
                "Version": "1.0.0",
                "Last Update": "2025-01-14",
                "Skill API": {
                    "Description": "Fetches skill data.",
                    "Endpoint": "/skill/",
                    "Method": "GET",
                    "Example Usage": "curl -X GET https://lita-user-data-id.vercel.app/api/skill/"
                },
                "KolZone List API": {
                    "Description": "Fetches KolZone list based on gender and skillId.",
                    "Endpoint": "/kolzone/list/",
                    "Method": "GET",
                    "Query Parameters": {
                        "gender": {
                            "description": "Gender filter",
                            "options": {
                                "0": "all",
                                "1": "boy",
                                "2": "girl"
                            },
                            "default": "0"
                        },
                        "skillId": {
                            "description": "Skill ID filter",
                            "default": "-1"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/kolzone/list/?gender=0&skillId=-1'"
                },
                "Player InSkills API": {
                    "Description": "Fetches player skills based on skillIds.",
                    "Endpoint": "/player/inskills/",
                    "Method": "GET",
                    "Query Parameters": {
                        "skillIds": {
                            "description": "Comma-separated list of skill IDs",
                            "options": {
                                "1": "",
                                "20": "",
                                "3": "",
                                "2": "",
                                "167": "",
                                "100": "",
                                "139": "",
                                "90": "",
                                "22": "",
                                "21": "",
                                "18": "",
                                "69": "",
                                "23": "",
                                "87": "",
                                "10": "",
                                "65": "",
                                "160": "",
                                "89": "",
                                "60": "",
                                "122": "",
                                "102": "",
                                "103": "",
                                "159": "",
                                "109": "",
                                "113": ""
                            },
                            "default": "1,20,3,2,167,100,139,90,22,21,18,69,23,87,10,65,160,89,60,122,102,103,159,109,113"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/player/inskills/?skillIds=1,20'"
                },
                "Player Recommend Batch API": {
                    "Description": "Fetches recommended players in batches.",
                    "Endpoint": "/player/recommend/batch/",
                    "Method": "GET",
                    "Query Parameters": {
                        "page": {
                            "description": "Page number",
                            "default": "1"
                        },
                        "rows": {
                            "description": "Number of rows per page",
                            "default": "10"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/player/recommend/batch/?page=1&rows=10'"
                },
                "Skill Search Options API": {
                    "Description": "Fetches search options for skills.",
                    "Endpoint": "/skill/searchopts/",
                    "Method": "GET",
                    "Query Parameters": {
                        "skillId": {
                            "description": "Skill ID",
                            "default": "1"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/skill/searchopts/?skillId=1'"
                },
                "Player Inskill Batch API": {
                    "Description": "Fetches players based on multiple criteria.",
                    "Endpoint": "/player/inskill/batch/",
                    "Method": "GET",
                    "Query Parameters": {
                        "gender": {
                            "description": "Gender filter",
                            "options": {
                                "0": "all",
                                "1": "boy",
                                "2": "girl"
                            }
                        },
                        "levelIds": {
                            "description": "Comma-separated list of level IDs",
                            "default": ""
                        },
                        "newBie": {
                            "description": "Newbie filter",
                            "default": "0"
                        },
                        "order": {
                            "description": "Order",
                            "default": "",
                            "options": {
                                "desc": "descending",
                                "asc": "ascending"
                            }
                        },
                        "page": {
                            "description": "Page number",
                            "default": "1"
                        },
                        "positionIds": {
                            "description": "Comma-separated list of position IDs",
                            "default": ""
                        },
                        "rows": {
                            "description": "Number of rows per page",
                            "default": "30"
                        },
                        "skillId": {
                            "description": "Skill ID",
                            "default": "1"
                        },
                        "sort": {
                            "description": "Sort criteria",
                            "default": "",
                            "options": {
                                "auditTime": "audit time",
                                "avgStar": "average star",
                                "price": "price"
                            }
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/player/inskill/batch/?gender=0&levelIds=&newBie=0&order=&page=1&positionIds=&rows=30&skillId=1&sort='"
                },
                "Player Detail API": {
                    "Description": "Fetches player details based on player number.",
                    "Endpoint": "/player/detail/g3/",
                    "Method": "GET",
                    "Query Parameters": {
                        "no": {
                            "description": "Player number",
                            "required": "true"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/player/detail/g3/?no=12345'"
                },
                "Player Received Gift API": {
                    "Description": "Fetches received gifts for a player.",
                    "Endpoint": "/player/received/gift/",
                    "Method": "GET",
                    "Query Parameters": {
                        "id": {
                            "description": "Player ID",
                            "required": "true"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/player/received/gift/?id=12345'"
                },
                "Player Received Rank Gift API": {
                    "Description": "Fetches rank gifts received by a player.",
                    "Endpoint": "/player/received/rank/gift/",
                    "Method": "GET",
                    "Query Parameters": {
                        "id": {
                            "description": "Player ID",
                            "required": "true"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/player/received/rank/gift/?id=12345'"
                },
                "Player Received Rank Total API": {
                    "Description": "Fetches total rank received by a player.",
                    "Endpoint": "/player/received/rank/total/",
                    "Method": "GET",
                    "Query Parameters": {
                        "id": {
                            "description": "Player ID",
                            "required": "true"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/player/received/rank/total/?id=12345'"
                },
                "Player Received Rank Order API": {
                    "Description": "Fetches rank orders received by a player.",
                    "Endpoint": "/player/received/rank/order/",
                    "Method": "GET",
                    "Query Parameters": {
                        "id": {
                            "description": "Player ID",
                            "required": "true"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/player/received/rank/order/?id=12345'"
                },
                "Player Skill Comment API": {
                    "Description": "Fetches comments for a skill of a player.",
                    "Endpoint": "/player/skill/comment/",
                    "Method": "GET",
                    "Query Parameters": {
                        "skillId": {
                            "description": "Skill ID",
                            "required": "true"
                        },
                        "userId": {
                            "description": "User ID",
                            "required": "true"
                        },
                        "page": {
                            "description": "Page number",
                            "default": "1"
                        },
                        "rows": {
                            "description": "Number of rows per page",
                            "default": "5"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/player/skill/comment/?skillId=1&userId=12345&page=1&rows=5'"
                },
                "Moment User List API": {
                    "Description": "Fetches user moments based on authorId and momentId.",
                    "Endpoint": "/moment/user/list/",
                    "Method": "GET",
                    "Query Parameters": {
                        "authorId": {
                            "description": "Author ID",
                            "required": "true"
                        },
                        "momentId": {
                            "description": "Moment ID",
                            "default": "0"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/moment/user/list/?authorId=12345&momentId=0'"
                },
                "Moment HotSort List API": {
                    "Description": "Fetches hot sorted moments.",
                    "Endpoint": "/moment/hotsort/list/",
                    "Method": "GET",
                    "Query Parameters": {
                        "batchNo": {
                            "description": "Batch number",
                            "default": "0"
                        },
                        "nextIndex": {
                            "description": "Next index",
                            "default": "0"
                        }
                    },
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/moment/hotsort/list/?batchNo=0&nextIndex=0'"
                }
            }
        }
        return Response(data)

class SkillAPIView(BaseAPIView):
    def get(self, request):
        url = f"{settings.URL_MAIN}/skill"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "s6AfXg",
            settings.L_SIGN_KEY: "76404ba94cf004d",
            settings.L_TIMESTAMP_KEY: "1736764132212",
            settings.L_TRACE_ID_KEY: "2e8fe1584a586254eb30b6e93cf10e9e",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE,
        })
        return self.get_response(url, headers)

class KolZoneListAPIView(BaseAPIView):
    def get(self, request):
        gender = request.query_params.get('gender', '0')
        skillId = request.query_params.get('skillId', '-1')
        url = f"{settings.URL_BASIC}/kolZone/list?gender={gender}&skillId={skillId}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "PZP5Ve",
            settings.L_SIGN_KEY: "68d3df6426d7d1c",
            settings.L_TIMESTAMP_KEY: "1736764132997",
            settings.L_TRACE_ID_KEY: "da3ae4a0320db4eef3f26b810ce6559a",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE,
        })
        return self.get_response(url, headers)

class PlayerInSkillsAPIView(BaseAPIView):
    def get(self, request):
        skillIds = request.query_params.get('skillIds', '1,20,3,2,167,100,139,90,22,21,18,69,23,87,10,65,160,89,60,122,102,103,159,109,113')
        url = f"{settings.URL_MAIN}/player/inskills?skillIds={skillIds}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "A99qCY",
            settings.L_SIGN_KEY: "f2dcce56c1d53ea",
            settings.L_TIMESTAMP_KEY: "1736764133395",
            settings.L_TRACE_ID_KEY: "7ef34e5bc2e9662c49523f00d52bef72",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE,
        })
        return self.get_response(url, headers)

class PlayerRecommendBatchAPIView(BaseAPIView):
    def get(self, request):
        page = request.query_params.get('page', '1')
        rows = request.query_params.get('rows', '10')
        url = f"{settings.URL_MAIN}/player/recommend/batch?page={page}&rows={rows}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "5JC3TG",
            settings.L_SIGN_KEY: "a6b28c15dd2f6f0",
            settings.L_TIMESTAMP_KEY: "1736764133467",
            settings.L_TRACE_ID_KEY: "33846cc9280dd0564771d6ed8d6f694c",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE,
        })
        return self.get_response(url, headers)

class SkillSearchOptsAPIView(BaseAPIView):
    def get(self, request):
        skill_id = request.query_params.get('skillId', '1')
        url = f"{settings.URL_MAIN}/skill/searchopts?skillId={skill_id}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "skKvi7",
            settings.L_SIGN_KEY: "65825684a3661a3",
            settings.L_TIMESTAMP_KEY: "1736772658522",
            settings.L_TRACE_ID_KEY: "d4e776a7d8c5d315468fb4bd2e268cf4",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE_V2,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE_V2,
        })
        return self.get_response(url, headers)

class PlayerInskillBatchAPIView(BaseAPIView):
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

        url = f"{settings.URL_MAIN}/player/inskill/batch?gender={gender}&levelIds={level_ids}&newBie={newbie}&order={order}&page={page}&positionIds={position_ids}&rows={rows}&skillId={skill_id}&sort={sort}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "tckVJP",
            settings.L_SIGN_KEY: "ee21ddd29006d93",
            settings.L_TIMESTAMP_KEY: "1736772658522",
            settings.L_TRACE_ID_KEY: "5fc7d652e11a5d47fa7bf01846d6872e",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE_V2,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE_V2,
        })
        return self.get_response(url, headers)

class PlayerDetailAPIView(BaseAPIView):
    def get(self, request):
        player_no = request.query_params.get('no')
        
        if not player_no:
            return Response({'error': 'The "no" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f"{settings.URL_MAIN}/player/detail/g3?no={player_no}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "g5PcXV",
            settings.L_SIGN_KEY: "ef54f0d8c6dc953",
            settings.L_TIMESTAMP_KEY: "1736824456578",
            settings.L_TRACE_ID_KEY: "d1bddf50f05c8a1315750abd8783a8dc",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE_V3,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE_V3,
        })
        return self.get_response(url, headers)

class PlayerReceivedGiftAPIView(BaseAPIView):
    def get(self, request):
        player_id = request.query_params.get('id')
        
        if not player_id:
            return Response({'error': 'The "id" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f"{settings.URL_MAIN}/player/received/gift?id={player_id}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "qfPAWO",
            settings.L_SIGN_KEY: "55bbb61e3f23110",
            settings.L_TIMESTAMP_KEY: "1736824457586",
            settings.L_TRACE_ID_KEY: "2eef901980ee04c1ddb3b71d36ef6377",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE_V4,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE_V4,
        })
        return self.get_response(url, headers)

class PlayerReceivedRankGiftAPIView(BaseAPIView):
    def get(self, request):
        player_id = request.query_params.get('id')
        
        if not player_id:
            return Response({'error': 'The "id" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f"{settings.URL_MAIN}/player/received/rank/gift?id={player_id}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "6Serv9",
            settings.L_SIGN_KEY: "716d2ac70a158a7",
            settings.L_TIMESTAMP_KEY: "1736826174481",
            settings.L_TRACE_ID_KEY: "153213d7e144c8f933ef2c94d1667617",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE_V4,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE_V4,
        })
        return self.get_response(url, headers)

class PlayerReceivedRankTotalAPIView(BaseAPIView):
    def get(self, request):
        player_id = request.query_params.get('id')
        
        if not player_id:
            return Response({'error': 'The "id" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f"{settings.URL_MAIN}/player/received/rank/total?id={player_id}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "K3HO3X",
            settings.L_SIGN_KEY: "13ed7fff4f041bb",
            settings.L_TIMESTAMP_KEY: "1736824457587",
            settings.L_TRACE_ID_KEY: "2861f2c69b248d7a25616eddcc340beb",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE_V4,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE_V4,
        })
        return self.get_response(url, headers)

class PlayerReceivedRankOrderAPIView(BaseAPIView):
    def get(self, request):
        player_id = request.query_params.get('id')
        
        if not player_id:
            return Response({'error': 'The "id" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        url = f"{settings.URL_MAIN}/player/received/rank/order?id={player_id}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "EKBbCe",
            settings.L_SIGN_KEY: "2d2400f267608d6",
            settings.L_TIMESTAMP_KEY: "1736826512143",
            settings.L_TRACE_ID_KEY: "c42bae6df6183f5d70380f217d448419",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE_V4,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE_V4,
        })
        return self.get_response(url, headers)

class PlayerSkillCommentAPIView(BaseAPIView):
    def get(self, request):
        skill_id = request.query_params.get('skillId')
        user_id = request.query_params.get('userId')
        
        if not skill_id or not user_id:
            return Response({'error': 'The "skillId" and "userId" parameters are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        page = request.query_params.get('page', '1')
        rows = request.query_params.get('rows', '5')
        
        url = f"{settings.URL_MAIN}/player/skill/comment?skillId={skill_id}&userId={user_id}&page={page}&rows={rows}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "zRlBSH",
            settings.L_SIGN_KEY: "6d2b22a391a8946",
            settings.L_TIMESTAMP_KEY: "1736824457586",
            settings.L_TRACE_ID_KEY: "eb635dd2f5a2a2a3e9b2ffd09e2b8d34",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE_V4,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE_V4,
        })
        return self.get_response(url, headers)

class MomentUserListAPIView(BaseAPIView):
    def get(self, request):
        author_id = request.query_params.get('authorId')
        
        if not author_id:
            return Response({'error': 'The "authorId" parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        moment_id = request.query_params.get('momentId', '0')
        
        url = f"{settings.URL_MAIN}/moment/user/list?authorId={author_id}&momentId={moment_id}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "uc7zQD",
            settings.L_SIGN_KEY: "14981746a50abab",
            settings.L_TIMESTAMP_KEY: "1736825596428",
            settings.L_TRACE_ID_KEY: "242dfc1b2c70a4ed3fb2e31386475ec4",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE_V4,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE_V4,
        })
        return self.get_response(url, headers)

class MomentHotSortListAPIView(BaseAPIView):
    def get(self, request):
        batch_no = request.query_params.get('batchNo', '0')
        next_index = request.query_params.get('nextIndex', '0')
        
        url = f"{settings.URL_MAIN}/moment/hotsort/list?batchNo={batch_no}&nextIndex={next_index}"
        headers = self.get_base_headers()
        headers.update({
            settings.L_NONCE_KEY: "3s3HH9",
            settings.L_SIGN_KEY: "d43267c65f228f5",
            settings.L_TIMESTAMP_KEY: "1736828167855",
            settings.L_TRACE_ID_KEY: "1883084bbdd3f6e2d39d3f52109a6de3",
            settings.L_USER_TOKEN_KEY: settings.L_USER_TOKEN_VALUE_V4,
            settings.PROXYHEADER_KEY: settings.PROXYHEADER_VALUE_V4,
        })
        return self.get_response(url, headers)
