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
                    "Endpoint": "/kolZone/list/",
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
                    "Example Usage": "curl -X GET 'https://lita-user-data-id.vercel.app/api/kolZone/list/?gender=0&skillId=-1'"
                },
                "Player InSkills API": {
                    "Description": "Fetches player skills based on skillIds.",
                    "Endpoint": "/player/inskills/",
                    "Method": "GET",
                    "Query Parameters": {
                        "skillIds": {
                            "description": "Comma-separated list of skill IDs",
                            "options": {
                                "1": "Mobile Legends",
                                "20": "Teman Curhat",
                                "3": "PUBG",
                                "2": "Free Fire",
                                "167": "Honor of Kings",
                                "100": "Ludo King",
                                "139": "Eggy Party",
                                "90": "Stumble Guys",
                                "22": "Magic Chess",
                                "21": "Valorant",
                                "18": "COD: Mobile",
                                "69": "Genshin Impact",
                                "23": "Sausage Man",
                                "87": "AoV",
                                "10": "LOL: Wild Rift",
                                "65": "Dota 2",
                                "160": "Blood Strike",
                                "89": "Point Blank",
                                "60": "CS2",
                                "122": "Teman Nyanyi",
                                "102": " Black Desert Mobile",
                                "103": "Sky : Children of the light",
                                "159": "Sleep Call",
                                "109": "Supersus",
                                "113": "Let’s Get Rich"
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
                            "required": True
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
                            "required": True
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
                            "required": True
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
                            "required": True
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
                            "required": True
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
                            "required": True
                        },
                        "userId": {
                            "description": "User ID",
                            "required": True
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
                            "required": True
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
        return Response(data, status=status.HTTP_200_OK)

class SkillAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "status": "0",
            "msg": "",
            "data": [
                {
                    "id": "1",
                    "name": "Mobile Legends",
                    "title": "Mobile Legends",
                    "brickIcon": "https://data.lita.game/static/skill/skill_1_brick.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301923/in_mlbb_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/static/skill/skill_1_brick_mini.png",
                    "imageUrl": "https://data.lita.game/static/skill/skill_1.png?t=t",
                    "mainIconUrl": "https://data.lita.game/static/skill/home_icon/new_mlbb_home_icon.png",
                    "iconUrl": "https://data.lita.game/static/skill/square/sq_mlbb.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081556/in_mobile-legends_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/static/skill/skill_1_banner.png",
                    "type": "1",
                    "unit": "1"
                },
                {
                    "id": "20",
                    "name": "Teman Curhat",
                    "title": "Teman Curhat",
                    "brickIcon": "https://data.lita.game/static/skill/skill_20_brick.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_chat_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/static/skill/skill_20_brick_mini.png",
                    "imageUrl": "https://data.lita.game/static/skill/skill_20_icon.png",
                    "mainIconUrl": "https://data.lita.game/static/skill/home_icon/just_chatting.png",
                    "iconUrl": "https://data.lita.game/static/skill/square/sq_chat.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081557/in_chat_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/static/skill/skill_20_banner.png",
                    "type": "2",
                    "unit": "2"
                },
                {
                    "id": "3",
                    "name": "PUBG",
                    "title": "PUBG",
                    "brickIcon": "https://data.lita.game/static/skill/skill_3_brick.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_pubg_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/static/skill/skill_3_brick_mini.png",
                    "imageUrl": "https://data.lita.game/static/skill/skill_3.png?t=t",
                    "mainIconUrl": "https://data.lita.game/static/skill/home_icon/pubg.png",
                    "iconUrl": "https://data.lita.game/static/skill/square/sg_pubg.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081558/in_pubg_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/static/skill/skill_3_banner.png",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "2",
                    "name": "Free Fire",
                    "title": "Free Fire",
                    "brickIcon": "https://data.lita.game/static/skill/skill_2_brick.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_ff_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/static/skill/skill_2_brick_mini.png",
                    "imageUrl": "https://data.lita.game/static/skill/skill_2.png?t=t",
                    "mainIconUrl": "https://data.lita.game/static/skill/home_icon/ff.png",
                    "iconUrl": "https://data.lita.game/static/skill/square/sq_ff.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081559/in_free-fire_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/static/skill/skill_2_banner.png",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "167",
                    "name": "Honor of Kings",
                    "title": "Honor of Kings",
                    "brickIcon": "https://data.lita.game/mgr/skill/202406211438/in_honor-of-king_brick-icon.png?width=192&height=192",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202406211438/in_honor-of-king_brick-new-icon.png?width=192&height=192",
                    "brickMini": "https://data.lita.game/mgr/skill/202406211438/in_honor-of-king_brick-mini.png?width=160&height=160",
                    "imageUrl": "https://data.lita.game/mgr/skill/202406211438/in_honor-of-king_brick-icon.png?width=192&height=192",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202406211438/in_honor-of-king_main-icon.png?width=240&height=240",
                    "iconUrl": "https://data.lita.game/mgr/skill/202406211438/in_honor-of-king_brick-icon.png?width=192&height=192",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202406211438/in_honor-of-king_pc-image.png?width=273&height=345",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202406211438/in_honor-of-king_brick-icon.png?width=192&height=192",
                    "type": "1",
                    "unit": "1"
                },
                {
                    "id": "100",
                    "name": "Ludo King",
                    "title": "Ludo King",
                    "brickIcon": "https://data.lita.game/mgr/skill/202208231738/20220823174659.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_ludo_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202208231738/20220823174729.png",
                    "imageUrl": "https://data.lita.game/mgr/skill/202208231738/20220823174659.png",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202208231738/20220823174927.png",
                    "iconUrl": "https://data.lita.game/mgr/skill/202208261653/20220826165340.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081658/in_ludo-king_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202208231738/20220823174659.png",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "139",
                    "name": "Eggy Party",
                    "title": "Eggy Party",
                    "brickIcon": "https://data.lita.game/mgr/skill/202309291733/in_eggyparty_brick-icon.png?width=256&height=256",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_eggy_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202309291733/in_eggyparty_brick-mini.png?width=160&height=160",
                    "imageUrl": "https://data.lita.game/mgr/skill/202309291733/in_eggyparty_brick-icon.png?width=256&height=256",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202309291733/in_eggyparty_main-icon.png?width=320&height=320",
                    "iconUrl": "https://data.lita.game/mgr/skill/202309291733/in_eggyparty_brick-icon.png?width=256&height=256",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202309291733/in_eggyparty_pc-image.png?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202309291733/in_eggyparty_brick-icon.png?width=256&height=256",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "90",
                    "name": "Stumble Guys",
                    "title": "Stumble Guys",
                    "brickIcon": "https://data.lita.game/mgr/skill/202207291240/20220729134630.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_stumble_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202207291240/20220729134657.png",
                    "imageUrl": "https://data.lita.game/mgr/skill/202207291240/20220729134630.png",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202208011140/20220801114129.png",
                    "iconUrl": "https://data.lita.game/mgr/skill/202208261641/20220826164713.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081600/in_stumble-guys_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202207291240/20220729134630.png",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "22",
                    "name": "Magic Chess",
                    "title": "Magic Chess",
                    "brickIcon": "https://data.lita.game/static/skill/skill_22_brick.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_magicchess_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/static/skill/skill_22_brick_mini.png",
                    "imageUrl": "https://data.lita.game/mgr/skill/202306161530/20230616153023.png?width=142&height=142",
                    "mainIconUrl": "https://data.lita.game/static/skill/home_icon/magic_chess.png",
                    "iconUrl": "https://data.lita.game/static/skill/square/sg_magic_chess.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081600/in_magic-chess_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202306161530/20230616153029.png?width=142&height=142",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "21",
                    "name": "Valorant",
                    "title": "Valorant",
                    "brickIcon": "https://data.lita.game/static/skill/skill_21_brick.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_valorant_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/static/skill/skill_21_brick_mini.png",
                    "imageUrl": "https://data.lita.game/mgr/skill/202306161529/20230616152942.png?width=142&height=142",
                    "mainIconUrl": "https://data.lita.game/static/skill/home_icon/valorant.png",
                    "iconUrl": "https://data.lita.game/static/skill/square/sq_valorant.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081601/in_valorant_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202306161529/20230616152945.png?width=142&height=142",
                    "type": "1",
                    "unit": "1"
                },
                {
                    "id": "18",
                    "name": "COD: Mobile",
                    "title": "COD: Mobile",
                    "brickIcon": "https://data.lita.game/static/skill/skill_18_brick.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_cod_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/static/skill/skill_18_brick_mini.png",
                    "imageUrl": "https://data.lita.game/static/skill/skill_18.png?t=t",
                    "mainIconUrl": "https://data.lita.game/static/skill/home_icon/cod_mobile.png",
                    "iconUrl": "https://data.lita.game/static/skill/square/sq_cod.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081602/in_call-of-duty_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/static/skill/skill_18_banner.png",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "69",
                    "name": "Genshin Impact",
                    "title": "Genshin Impact",
                    "brickIcon": "https://data.lita.game/static/skill/skill_69_brick.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_genshin_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/static/skill/skill_69_brick_mini.png",
                    "imageUrl": "https://data.lita.game/static/skill/skill_69.png",
                    "mainIconUrl": "https://data.lita.game/static/skill/skill_69_main.png",
                    "iconUrl": "https://data.lita.game/static/skill/skill_69.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081602/in_genshin-impact_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "23",
                    "name": "Sausage Man",
                    "title": "Sausage Man",
                    "brickIcon": "https://data.lita.game/static/skill/skill_23_brick.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_sausage_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/static/skill/skill_23_brick_mini.png",
                    "imageUrl": "https://data.lita.game/mgr/skill/202306161530/20230616153110.png?width=142&height=142",
                    "mainIconUrl": "https://data.lita.game/static/skill/home_icon/sausage_man.png",
                    "iconUrl": "https://data.lita.game/static/skill/square/sq_sausage_man.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081603/in_sausage-man_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202306161530/20230616153113.png?width=142&height=142",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "87",
                    "name": "AoV",
                    "title": "AoV",
                    "brickIcon": "https://data.lita.game/mgr/skill/202207271928/20220728145028.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_aov_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202207271928/20220728145032.png",
                    "imageUrl": "https://data.lita.game/mgr/skill/202207271928/20220728145028.png",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202208011136/20220801113748.png",
                    "iconUrl": "https://data.lita.game/mgr/skill/202208261650/20220826165138.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081701/in_aov_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202207271928/20220728145028.png",
                    "type": "1",
                    "unit": "1"
                },
                {
                    "id": "10",
                    "name": "LOL: Wild Rift",
                    "title": "LOL: Wild Rift",
                    "brickIcon": "https://data.lita.game/static/skill/skill_10_brick.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_lol_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/static/skill/skill_10_brick_mini.png",
                    "imageUrl": "https://data.lita.game/static/skill/skill_10.png?t=t",
                    "mainIconUrl": "https://data.lita.game/static/skill/home_icon/lol_mobile.png",
                    "iconUrl": "https://data.lita.game/static/skill/square/sq_lolm.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081701/in_lol-wild-rift_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/static/skill/skill_10_banner.png",
                    "type": "1",
                    "unit": "1"
                },
                {
                    "id": "65",
                    "name": "Dota 2",
                    "title": "Dota 2",
                    "brickIcon": "https://data.lita.game/static/skill/skill_65_brick.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_dota_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/static/skill/skill_65_brick_mini.png",
                    "imageUrl": "https://data.lita.game/static/skill/skill_65.png",
                    "mainIconUrl": "https://data.lita.game/static/skill/skill_65_main.png",
                    "iconUrl": "https://data.lita.game/static/skill/skill_65.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081702/in_dota-two_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "160",
                    "name": "Blood Strike",
                    "title": "Blood Strike",
                    "brickIcon": "https://data.lita.game/mgr/skill/202404021903/in_blood-strike_brick-icon.png?width=192&height=192",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202404021903/in_blood-strike_brick-new-icon.png?width=240&height=240",
                    "brickMini": "https://data.lita.game/mgr/skill/202404021903/in_blood-strike_brick-mini.png?width=160&height=160",
                    "imageUrl": "https://data.lita.game/mgr/skill/202404021903/in_blood-strike_brick-icon.png?width=192&height=192",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202404021903/in_blood-strike_main-icon.png?width=240&height=240",
                    "iconUrl": "https://data.lita.game/mgr/skill/202404021903/in_blood-strike_brick-icon.png?width=192&height=192",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202404021903/in_blood-strike_pc-image.png?width=273&height=345",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202404021903/in_blood-strike_brick-icon.png?width=192&height=192",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "89",
                    "name": "Point Blank",
                    "title": "Point Blank",
                    "brickIcon": "https://data.lita.game/mgr/skill/202207281748/20220728174858.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_pointblank_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202207281748/20220728174901.png",
                    "imageUrl": "https://data.lita.game/mgr/skill/202207281748/20220728174858.png",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202208031010/20220803101053.png",
                    "iconUrl": "https://data.lita.game/mgr/skill/202208261651/20220826165304.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081703/in_point-blank_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202207281748/20220728174858.png",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "60",
                    "name": "CS2",
                    "title": "CS2",
                    "brickIcon": "https://data.lita.game/mgr/skill/202310071356/in_cstwo_brick-icon.png?width=256&height=256",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_cs_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202310071356/in_cstwo_brick-mini.png?width=160&height=160",
                    "imageUrl": "https://data.lita.game/mgr/skill/202310071356/in_cstwo_brick-icon.png?width=256&height=256",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202310071356/in_cstwo_main-icon.png?width=320&height=320",
                    "iconUrl": "https://data.lita.game/mgr/skill/202310071356/in_cstwo_brick-icon.png?width=256&height=256",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310071356/in_cstwo_pc-image.png?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202310071356/in_cstwo_brick-icon.png?width=256&height=256",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "122",
                    "name": "Teman Nyanyi",
                    "title": "Teman Nyanyi",
                    "brickIcon": "https://data.lita.game/mgr/skill/202303232145/20230323214604.png?width=142&height=142",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301944/in_teman_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202303232145/20230323214614.png?width=40&height=40",
                    "imageUrl": "https://data.lita.game/mgr/skill/202303232145/20230323214644.png?width=256&height=256",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202303232145/20230323214651.png?width=320&height=320",
                    "iconUrl": "https://data.lita.game/mgr/skill/202303232145/20230323214604.png?width=142&height=142",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081609/in_sing_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202303232145/20230323214604.png?width=142&height=142",
                    "type": "2",
                    "unit": "1"
                },
                {
                    "id": "102",
                    "name": " Black Desert Mobile",
                    "title": " Black Desert Mobile",
                    "brickIcon": "https://data.lita.game/mgr/skill/202208231857/20220823185904.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_blackdesert_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202208231857/20220823185921.png",
                    "imageUrl": "https://data.lita.game/mgr/skill/202208231857/20220823185904.png",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202208231857/20220823190016.png",
                    "iconUrl": "https://data.lita.game/mgr/skill/202208261654/20220826165413.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081703/in_black-desert-mobile_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202208231857/20220823185904.png",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "103",
                    "name": "Sky : Children of the light",
                    "title": "Sky : Children of the light",
                    "brickIcon": "https://data.lita.game/mgr/skill/202208231904/20220823190631.png",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_sky_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202208231904/20220823190719.png",
                    "imageUrl": "https://data.lita.game/mgr/skill/202208231904/20220823190631.png",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202208231904/20220823190811.png",
                    "iconUrl": "https://data.lita.game/mgr/skill/202208261654/20220826165453.png",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081704/in_sky_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202208231904/20220823190631.png",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "159",
                    "name": "Sleep Call",
                    "title": "Sleep Call",
                    "brickIcon": "https://data.lita.game/mgr/skill/202403141055/in_sleep-call_brick-icon.png?width=256&height=256",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202403141143/in_sleep-call_brick-new-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202403141055/in_sleep-call_brick-mini.png?width=40&height=40",
                    "imageUrl": "https://data.lita.game/mgr/skill/202403141055/in_sleep-call_brick-icon.png?width=256&height=256",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202403141055/in_sleep-call_main-icon.png?width=320&height=320",
                    "iconUrl": "https://data.lita.game/mgr/skill/202403141055/in_sleep-call_brick-icon.png?width=256&height=256",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202403141055/in_sleep-call_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202403141055/in_sleep-call_brick-icon.png?width=256&height=256",
                    "type": "2",
                    "unit": "2"
                },
                {
                    "id": "109",
                    "name": "Supersus",
                    "title": "Supersus",
                    "brickIcon": "https://data.lita.game/mgr/skill/202301111126/20230111112729.png?width=256&height=256",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_supersus_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202301111126/20230111112734.png?width=160&height=160",
                    "imageUrl": "https://data.lita.game/mgr/skill/202301111126/20230111112729.png?width=256&height=256",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202301111126/20230111112746.png?width=320&height=320",
                    "iconUrl": "https://data.lita.game/mgr/skill/202301111126/20230111112729.png?width=256&height=256",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081608/in_supersus_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202301111126/20230111112729.png?width=256&height=256",
                    "type": "1",
                    "unit": "2"
                },
                {
                    "id": "113",
                    "name": "Let’s Get Rich",
                    "title": "Let’s Get Rich",
                    "brickIcon": "https://data.lita.game/mgr/skill/202302131817/20230213181736.png?width=256&height=256",
                    "brickNewIcon": "https://data.lita.game/mgr/skill/202311301926/in_letsgetrich_brick-icon.png?width=160&height=160",
                    "brickMini": "https://data.lita.game/mgr/skill/202302131817/20230213181745.png?width=160&height=160",
                    "imageUrl": "https://data.lita.game/mgr/skill/202302131817/20230213181736.png?width=256&height=256",
                    "mainIconUrl": "https://data.lita.game/mgr/skill/202302131817/20230213181850.png?width=320&height=320",
                    "iconUrl": "https://data.lita.game/mgr/skill/202302131817/20230213181736.png?width=256&height=256",
                    "pcImageUrl": "https://data.lita.game/mgr/skill/202310081609/in_lets-get-rich_pc-image.jpeg?width=253&height=320",
                    "bannerUrl": "https://data.lita.game/mgr/skill/202302131817/20230213181736.png?width=256&height=256",
                    "type": "1",
                    "unit": "2"
                }
            ]
        }
        return Response(data, status=status.HTTP_200_OK)

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
        gender = request.query_params.get('gender', '2')
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
