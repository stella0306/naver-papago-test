
TOKEN_URL = "https://search.naver.com/search.naver"
TOKEN_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Priority": "u=0, i",
    "Referer": "https://www.naver.com/",
    "Sec-CH-UA": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "Sec-CH-UA-Arch": "x86",
    "Sec-CH-UA-Bitness": "64",
    "Sec-CH-UA-Form-Factors": "Desktop",
    "Sec-CH-UA-Full-Version-List": "\"Chromium\";v=\"134.0.6998.89\", \"Not:A-Brand\";v=\"24.0.0.0\", \"Google Chrome\";v=\"134.0.6998.89\"",
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Model": "\"\"",
    "Sec-CH-UA-Platform": "Windows",
    "Sec-CH-UA-Platform-Version": "10.0.0",
    "Sec-CH-UA-Wow64": "?0",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

TOKEN_PAYLOAD = {
    "where": "nexearch",
    "sm": "top_hty",
    "fbm": "0",
    "ie": "utf8",
    "query": "파파고",
}



API_URL = "https://m.search.naver.com/p/csearch/ocontent/util/nmtProxy.naver"
API_HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": TOKEN_URL,
    "Sec-CH-UA": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

API_PAAYLOAD = {
    "query": "",
    "passportKey": "",
    "srcLang": "",
    "tarLang":"",
}