import aiohttp
import asyncio
import re
import random
from urllib import parse
from typing import Union, List, Dict

from const import TOKEN_URL, TOKEN_HEADERS, TOKEN_PAYLOAD
from const import API_URL, API_HEADERS, API_PAAYLOAD

class NaverPapago():
    def __init__(self):
        self.token_url = TOKEN_URL
        self.token_headers = TOKEN_HEADERS
        self.token_payload = TOKEN_PAYLOAD

        self.api_url = API_URL
        self.api_headers = API_HEADERS
        self.api_payload = API_PAAYLOAD

        # 토큰 초기화
        self.token = None
        
        # 세션 생성
        self.session = aiohttp.ClientSession()

    
    """passportKey 획득 로직"""
    # 토큰 초기화
    async def _initialize_token(self) -> None:
        # 토큰을 생성
        self.token = await self._get_token()

    # 토큰 생성을 요청
    async def _get_token(self) -> str:
        # 토큰 요청
        async with self.session.get(self.token_url, headers=self.token_headers, params=self.token_payload) as response:
            response.raise_for_status()

            if response.status == 200:
                # 토큰 업데이트
                return self._token_update(await response.text())
            
            else:
                return None

    def _token_update(self, token:str) -> str:
        match = re.search('passportKey=([a-zA-Z0-9]+)', token)
        # parse.unquote는 URL 디코딩 함수입니다.
        return parse.unquote(match.group(1)) if match is not None else None    
    """passportKey 획득 로직"""



    """번역 API 요청 로직"""
    async def translate(self, texts:Union[str, List[str]], src_lang:str="ko", tar_lang:str="en") -> Dict: # type: ignore
        texts = [texts] if not isinstance(texts, list) else texts
        
        await self._initialize_token() if self.token is None else None
        
        for text in texts:
            async for translation in self._stream_translations(text=text, src_lang=src_lang, tar_lang=tar_lang):
                yield translation


    async def _stream_translations(self, text: str, src_lang: str, tar_lang: str) -> Dict: # type: ignore
        # 페이로드 업데이트
        self.api_payload["query"] = text
        self.api_payload["passportKey"] = self.token
        self.api_payload["srcLang"] = src_lang
        self.api_payload["tarLang"] = tar_lang

        max_length_text = 200
        async with self.session.get(self.api_url, headers=self.api_headers, params=self.api_payload) as response:
            if len(text) < max_length_text:
                if response.status == 200:
                    message_result = await response.json()
                    message_result = message_result["message"]["result"]
                    message_result["sourceText"] = self.api_payload["query"]

                    yield {
                        "srcLangType": message_result["srcLangType"],
                        "tarLangType": message_result["tarLangType"],
                        "translatedText": message_result["translatedText"],
                        "sourceText": message_result["sourceText"],
                    }

                    await asyncio.sleep(random.uniform(0.5, 3))
                
                else:
                    print(f"response status error: {response.status}")
                    await self._initialize_token()
                    await self._stream_translations(text=text, src_lang=src_lang, tar_lang=tar_lang)
            
            else:
                yield {
                    "sourceTextLengthError": f"{max_length_text} over ({len(text)})"
                }

    """번역 API 요청 로직"""

    # 세션 종료.
    async def close(self):
        await self.session.close()




async def main():
    api = NaverPapago()

    # 테스트 문장
    sentences = [
        "오늘은 날씨가 맑고 화창합니다.",
        "내일은 중요한 회의가 있어서 일찍 일어나야 해요.",
        "주말에 가족들과 함께 영화를 보러 갈 계획입니다.",
        "이번 여름 휴가는 제주도로 가기로 결정했어요.",
        "새로운 언어를 배우는 것은 항상 흥미롭고 도전적입니다.",
        "운동은 건강에 매우 중요하다고 생각합니다.",
        "친구와 함께 맛있는 저녁 식사를 했어요.",
    ]

    
    async for text in api.translate(texts=sentences, src_lang="ko", tar_lang="en"):
        print(text)

    await api.close()


if __name__ == "__main__":
    asyncio.run(main())