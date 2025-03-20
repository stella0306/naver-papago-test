import re
from urllib import parse

text = """
(function(){var startApplication=function(){var require=window.require.config({"context":"x4z","paths":{"Controller":"https://ssl.pstatic.net/sstatic/fe/sfe/translator/Controller_240305"}});define("jquery",[],function(){return jQuery;});require(["jquery","Controller"],function($,Controller){var htInit={"input":"ko","output":"en","text":""};new Controller({elRoot:$("#_au_translator"),sNMTTransApi:"https://m.search.naver.com/p/csearch/ocontent/util/nmtProxy.naver",sPassportKey:"39ccfc89e1200d9e952e50a11eaaf8810e56263c",sPinyinApi:"https://m.search.naver.com/p/csearch/ocontent/util/tlitProxy.naver",sTtsApi:"https://m.search.naver.com/p/csearch/ocontent/util/ttsProxy.naver?service=nco_translate&from=pc_search&speech_fmt=mp3&speed=0&passportKey=39ccfc89e1200d9e952e50a11eaaf8810e56263c",sHuriganaApi:"https://m.search.naver.com/p/csearch/ocontent/util/furiganaProxy.naver",sSmallTransUrl:"https://papago.naver.com?sk={=sSourceLang}&st={=sText}&tk={=sTargetLang}",sPapagoLinkURL:"https://papago.naver.com?sk={=sSourceLang}&st={=sText}&tk={=sTargetLang}",htInit:htInit,htLang:{"ko":{"class":"kor","class2":"","label":"한국어","speaker_id":"&speaker=mijin"},"en":{"class":"","class2":"","label":"영어","speaker_id":"&speaker=clara&speed=3"},"ja":{"class":"jpn","class2":"","label":"일본어","speaker_id":"&speaker=yuri"},"zh":{"class":"chn","class2":"spk","label":"중국어(간체)","speaker_id":"&speaker=meimei"},"fr":{"class":"","class2":"","label":"프랑스어","speaker_id":""},"es":{"class":"","class2":"","label":"스페인어","speaker_id":""},"pt":{"class":"","class2":"","label":"포르투갈어","speaker_id":""},"id":{"class":"","class2":"","label":"인도네시아어","speaker_id":""},"th":{"class":"thai","class2":"","label":"태국어","speaker_id":""},"cn":{"class":"chn","class2":"spk","label":"중국어(번체)","speaker_id":""},"ru":{"class":"","class2":"","label":"러시아어","speaker_id":""},"de":{"class":"","class2":"","label":"독일어","speaker_id":""},"vi":{"class":"","class2":"","label":"베트남어","speaker_id":""},"hi":{"class":"","class2":"","label":"힌디어","speaker_id":""},"it":{"class":"","class2":"","label":"이탈리아어","speaker_id":""},"ar":{"class":"arabic","class2":"","label":"아랍어","speaker_id":""}},htTranslatableMap:{"ko":["en","ja","zh","cn","es","fr","de","ru","it","vi","th","id","ar"],"en":["ko","ja","zh","cn","es","fr","de","ru","pt","it","vi","th","id","hi","ar"],"ja":["ko","en","zh","cn","es","fr","de","ru","it","vi","th","id","ar"],"zh":["ko","en","ja","cn","es","fr","de","ru","it","vi","th","id","ar"],"cn":["ko","en","ja","zh","es","fr","de","ru","it","vi","th","id","ar"],"es":["ko","en","ja","zh","cn","fr","de","ru","it","vi","th","id","ar"],"fr":["ko","en","ja","zh","cn","es","de","ru","it","vi","th","id","ar"],"de":["ko","en","ja","zh","cn","es","fr","ru","it","vi","th","id","ar"],"ru":["ko","en","ja","zh","cn","es","fr","de","it","vi","th","id","ar"],"pt":["en"],"it":["ko","en","ja","zh","cn","es","fr","de","ru","vi","th","id","ar"],"vi":["ko","en","ja","zh","cn","es","fr","de","ru","it","th","id","ar"],"th":["ko","en","ja","zh","cn","es","fr","de","ru","it","vi","id","ar"],"id":["ko","en","ja","zh","cn","es","fr","de","ru","it","vi","th","ar"],"hi":["en"],"ar":["ko","en","ja","zh","cn","es","fr","de","ru","vi","th","id"]},aSupportLang:["ko","en","ja","zh","cn","es","fr","de","ru","pt","it","vi","th","id","hi","ar"],aTtsSupportLang:["ko","en","ja","zh"],nExpandMinHeight:90,nExpandMaxHeight:276,nTextMaxLength:200,nTtsMaxByte:450,nInputDelay:150,nEnableUiDelay:250,nAutoTransDelay:0});});};var requirejs="https://ssl.pstatic.net/sstatic/au/module/requirejs/require-2.3.5.js";nhn.common.load_js(window.require?null:requirejs,startApplication,true,150);})();
"""

def _token_update(token):
    match = re.search('passportKey=([a-zA-Z0-9]+)', token)
    # parse.unquote는 URL 디코딩 함수입니다.
    return parse.unquote(match.group(1)) if match is not None else None    

print(_token_update(text))