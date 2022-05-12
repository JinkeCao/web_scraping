# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from os import system, listdir
# from __future__ import unicode_literals
# import youtube_dl
from func_timeout import func_set_timeout, FunctionTimedOut
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlencode
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from json import load
# import bilili
# b = bilili()

@func_set_timeout(999)
def link2bso(link):
    # system(r'"C:\Program Files\Google\Chrome\Application\chrome.exe"  --remote-debugging-port=9458 --user-data-dir="C:\Users\jkcao\Videos\selenium"')
    # o = webdriver.chrome.options.Options()
    # o.add_experimental_option("excludeSwitches", ['enable-automation'])
    # o.add_experimental_option('useAutomationExtension', False)
    # o.add_argument('--start-maximized')
    # o.add_argument('--incognito')
    # o.add_argument('--disable-blink-features=AutomationControlled')
    # o.add_experimental_option("debuggerAddress","127.0.0.1:9458")
    # driver = webdriver.Chrome(
    #     r'C:\Users\jkcao\Downloads\chromedriver.exe'
    #     # , options = o
    #     )
    driver = webdriver.Firefox() 
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument"
        , {
            "source":"Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            }
        )   
    driver.implicitly_wait(9)
    try:
        driver.get(link)
        sleep(9)
        c = 0
        while True:
            height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            sleep(1)
            next_height = driver.execute_script(r'return  document.documentElement.scrollTop || window.pageYoffset || document.body.srcollTop')
            c += 1
            if c > 5: break
            elif height == next_height: break
        bso = BeautifulSoup(driver.page_source, 'html.parser')
        
        return bso
    except Exception as e:return str(e)
    else:driver.quit()
        

def timered_link2bso(link):
    try: bso = link2bso(link)
    except FunctionTimedOut: bso = BeautifulSoup('TimedOut', 'html.parser')
    except Exception as e:
        print(str(e))
        bso = BeautifulSoup(str(e), 'html.parser')
    return bso

@func_set_timeout(999)
def yg(url):
    # system(
    #     r'bilili --danmaku no -d C:\Users\jkcao\Videos\tmp' 
    #     + r' --playlist-type no -y ' 
    #     + r'https:'
    #     + url
    #     )
    system(
        r'you-get --no-caption -o C:\Users\jkcao\Videos\kuaishou\ “'
        + url
        + '"'
        )

def timered_yg(url):
    try: yg(url)
    except FunctionTimedOut: print('gibili timeout')
    except Exception as e: print(str(e))

@func_set_timeout(999)    
def cp(tmp, rp):
    with SSHClient() as ssh:
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(
            hostname='172.10.10.113'
            , port=22
            , username='root'
            , password='iflytek@2021'
            )
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(
                tmp
                ,recursive=True
                ,remote_path=rp
                )
def timered_cp(tmp, rp):
    try: cp(tmp, rp)
    except FunctionTimedOut: print('ubili timeout')
    except Exception as e: print(str(e))

d = {"author": "观世界", "links": ["https://www.douyin.com/video/7053357864458439944", "https://www.douyin.com/video/7052918260022381860", "https://www.douyin.com/video/7044499138251214111", "https://www.douyin.com/video/7058238728300432647", "https://www.douyin.com/video/7058233731013676318", "https://www.douyin.com/video/7058241340945042702", "https://www.douyin.com/video/7058225965138316581", "https://www.douyin.com/video/7058210419458002213", "https://www.douyin.com/video/7058203697637018887", "https://www.douyin.com/video/7053399820161043743", "https://www.douyin.com/video/7053724036848831774", "https://www.douyin.com/video/7053406630028905758", "https://www.douyin.com/video/7053391204473523470", "https://www.douyin.com/video/7053371179133963528", "https://www.douyin.com/video/7053352687571569934", "https://www.douyin.com/video/7053349082630262052", "https://www.douyin.com/video/7053286812898348318", "https://www.douyin.com/video/7053055902433217800", "https://www.douyin.com/video/7053053859828223239", "https://www.douyin.com/video/7053047463023775012", "https://www.douyin.com/video/7053031751601458440", "https://www.douyin.com/video/7053011187142839555", "https://www.douyin.com/video/7053000585729117477", "https://www.douyin.com/video/7052919765551025416", "https://www.douyin.com/video/7052904054745222414", "https://www.douyin.com/video/7052659069089303844", "https://www.douyin.com/video/7052651417743396129", "https://www.douyin.com/video/7052641422394117383", "https://www.douyin.com/video/7052595040186535199", "https://www.douyin.com/video/7052577227271195911", "https://www.douyin.com/video/7052572765559295240", "https://www.douyin.com/video/7052519043152055588", "https://www.douyin.com/video/7052501094861229319", "https://www.douyin.com/video/7052493391086505230", "https://www.douyin.com/video/7052324008863337759", "https://www.douyin.com/video/7052285277938683144", "https://www.douyin.com/video/7052282836627361032", "https://www.douyin.com/video/7052282494795664653", "https://www.douyin.com/video/7052234636809735438", "https://www.douyin.com/video/7052223847675809054", "https://www.douyin.com/video/7052153971288329485", "https://www.douyin.com/video/7052130049901727012", "https://www.douyin.com/video/7052119524451175694", "https://www.douyin.com/video/7051939174185700645", "https://www.douyin.com/video/7051916419629452581", "https://www.douyin.com/video/7051915298026409223", "https://www.douyin.com/video/7051911461009968415", "https://www.douyin.com/video/7051907055677967623", "https://www.douyin.com/video/7051906616509091086", "https://www.douyin.com/video/7051863521847463205", "https://www.douyin.com/video/7051851815708544263", "https://www.douyin.com/video/7051878563661794568", "https://www.douyin.com/video/7051876850909334814", "https://www.douyin.com/video/7051874823366053127", "https://www.douyin.com/video/7051869815463578917", "https://www.douyin.com/video/7051553257075772703", "https://www.douyin.com/video/7051537369933024542", "https://www.douyin.com/video/7051524482015513892", "https://www.douyin.com/video/7051509585093463327", "https://www.douyin.com/video/7051503379251563812", "https://www.douyin.com/video/7051459071722966280", "https://www.douyin.com/video/7051436666854149412", "https://www.douyin.com/video/7051430493887221005", "https://www.douyin.com/video/7051414614415904008", "https://www.douyin.com/video/7051383323364445453", "https://www.douyin.com/video/7051122601585888548", "https://www.douyin.com/video/7051118375400934663", "https://www.douyin.com/video/7050800882576821511", "https://www.douyin.com/video/7050791157982432548", "https://www.douyin.com/video/7050772903108906247", "https://www.douyin.com/video/7050767401176042782", "https://www.douyin.com/video/7050745226180168996", "https://www.douyin.com/video/7050668192523373861", "https://www.douyin.com/video/7050481750413217032", "https://www.douyin.com/video/7050433756313718052", "https://www.douyin.com/video/7050424053663878433", "https://www.douyin.com/video/7050402483738299684", "https://www.douyin.com/video/7050394418720836875", "https://www.douyin.com/video/7050296658134895883", "https://www.douyin.com/video/7050284945243163936", "https://www.douyin.com/video/7050276170427895043", "https://www.douyin.com/video/7050076229461871885", "https://www.douyin.com/video/7050059755410197790", "https://www.douyin.com/video/7050057313872366884", "https://www.douyin.com/video/7050027553771359525", "https://www.douyin.com/video/7049973306149080357", "https://www.douyin.com/video/7049943932951694605", "https://www.douyin.com/video/7049904173491522853", "https://www.douyin.com/video/7049696907475684639", "https://www.douyin.com/video/7049692272585231646", "https://www.douyin.com/video/7049687754157935908", "https://www.douyin.com/video/7049675173896670500", "https://www.douyin.com/video/7049616955514359054", "https://www.douyin.com/video/7049565850189286692", "https://www.douyin.com/video/7049557832789675300", "https://www.douyin.com/video/7049530579653528868", "https://www.douyin.com/video/7049323312891088164", "https://www.douyin.com/video/7049310335957814559", "https://www.douyin.com/video/7049309144934862116", "https://www.douyin.com/video/7049303205523557639", "https://www.douyin.com/video/7049292214274395429", "https://www.douyin.com/video/7049282023558532389", "https://www.douyin.com/video/7048617994460613924", "https://www.douyin.com/video/7048609856487492895", "https://www.douyin.com/video/7048601972265504008", "https://www.douyin.com/video/7048565210713427237", "https://www.douyin.com/video/7048221114731875591", "https://www.douyin.com/video/7048126048193547534", "https://www.douyin.com/video/7047796745698348302", "https://www.douyin.com/video/7047766509401214244", "https://www.douyin.com/video/7047749579101474084", "https://www.douyin.com/video/7047460040470580511", "https://www.douyin.com/video/7047452084806913287", "https://www.douyin.com/video/7047441049496587556", "https://www.douyin.com/video/7047406491900333325", "https://www.douyin.com/video/7047401466104974623", "https://www.douyin.com/video/7047161641275821326", "https://www.douyin.com/video/7047127033570135310", "https://www.douyin.com/video/7047098693547330830", "https://www.douyin.com/video/7047095935972773133", "https://www.douyin.com/video/7047093062664834312", "https://www.douyin.com/video/7047091422029253919", "https://www.douyin.com/video/7047079877022960927", "https://www.douyin.com/video/7047071949637405960", "https://www.douyin.com/video/7047054918699453726", "https://www.douyin.com/video/7046753911054568740", "https://www.douyin.com/video/7046744939589340424", "https://www.douyin.com/video/7046703139763883294", "https://www.douyin.com/video/7046696770587331848", "https://www.douyin.com/video/7046688188336786702", "https://www.douyin.com/video/7046604470679112972", "https://www.douyin.com/video/7046562197891337480", "https://www.douyin.com/video/7046367498287009061", "https://www.douyin.com/video/7046357402442140958", "https://www.douyin.com/video/7046350672974974238", "https://www.douyin.com/video/7046331951254424845", "https://www.douyin.com/video/7046327341869485342", "https://www.douyin.com/video/7046034946401570079", "https://www.douyin.com/video/7045544111448902920", "https://www.douyin.com/video/7045539310426262797", "https://www.douyin.com/video/7045457665836764423", "https://www.douyin.com/video/7045232535172910350", "https://www.douyin.com/video/7045089907219500325", "https://www.douyin.com/video/7044829231175470349", "https://www.douyin.com/video/7044388603639778568", "https://www.douyin.com/video/7044142946408467749", "https://www.douyin.com/video/7044000663814114567", "https://www.douyin.com/video/7043994097719184677", "https://www.douyin.com/video/7043772685784059149", "https://www.douyin.com/video/7043763910129765639", "https://www.douyin.com/video/7043740671320083743", "https://www.douyin.com/video/7043721788190215460", "https://www.douyin.com/video/7043702756380544264", "https://www.douyin.com/video/7043052746668281125", "https://www.douyin.com/video/7042952240365063460", "https://www.douyin.com/video/7042883060370541860", "https://www.douyin.com/video/7042658082475740423", "https://www.douyin.com/video/7042651836544814373", "https://www.douyin.com/video/7042642128521923877", "https://www.douyin.com/video/7042595715754872101", "https://www.douyin.com/video/7042491518912892168", "https://www.douyin.com/video/7042488217219763493", "https://www.douyin.com/video/7042485585142943012", "https://www.douyin.com/video/7042281290514664743", "https://www.douyin.com/video/7042266149295230215", "https://www.douyin.com/video/7042249494833990950", "https://www.douyin.com/video/7042247369416658215", "https://www.douyin.com/video/7042180662526283040", "https://www.douyin.com/video/7042138302413114663", "https://www.douyin.com/video/7041904831979654436", "https://www.douyin.com/video/7041894733198707976", "https://www.douyin.com/video/7041875418642763016", "https://www.douyin.com/video/7041760666843221284", "https://www.douyin.com/video/7041753516032970014", "https://www.douyin.com/video/7041548254302981412", "https://www.douyin.com/video/7041508857050320132", "https://www.douyin.com/video/7041499831134604558", "https://www.douyin.com/video/7041493788451278094", "https://www.douyin.com/video/7041384885503757576", "https://www.douyin.com/video/7041142369529498887", "https://www.douyin.com/video/7041114623352802574", "https://www.douyin.com/video/7041099723238935844", "https://www.douyin.com/video/7041025643550706957", "https://www.douyin.com/video/7040408211190451459", "https://www.douyin.com/video/7040714229955022110", "https://www.douyin.com/video/7040695837168504101", "https://www.douyin.com/video/7040408043422502177", "https://www.douyin.com/video/7040358354144775457", "https://www.douyin.com/video/7040355798525988134", "https://www.douyin.com/video/7040263847403343117", "https://www.douyin.com/video/7040262893073468702", "https://www.douyin.com/video/7040253609551891719", "https://www.douyin.com/video/7040053341283470599", "https://www.douyin.com/video/7040041675770662151", "https://www.douyin.com/video/7040040585138310430", "https://www.douyin.com/video/7040035179276127501", "https://www.douyin.com/video/7039724404800097539", "https://www.douyin.com/video/7039876034560363790", "https://www.douyin.com/video/7039688542527720736", "https://www.douyin.com/video/7039659514085346591", "https://www.douyin.com/video/7039650252185423116", "https://www.douyin.com/video/7039648261015194913", "https://www.douyin.com/video/7039632945396649254", "https://www.douyin.com/video/7039541788339637541", "https://www.douyin.com/video/7039302841810373896", "https://www.douyin.com/video/7039286400453201188", "https://www.douyin.com/video/7039273816488561956", "https://www.douyin.com/video/7039261770065775908", "https://www.douyin.com/video/7039259991085288735", "https://www.douyin.com/video/7039160572746812703", "https://www.douyin.com/video/7039145074600594724", "https://www.douyin.com/video/7038975878184946976", "https://www.douyin.com/video/7038928467265588493", "https://www.douyin.com/video/7038849124107636006", "https://www.douyin.com/video/7038802330082364686", "https://www.douyin.com/video/7038797485497699621", "https://www.douyin.com/video/7038796224807341342", "https://www.douyin.com/video/7038625518979239182", "https://www.douyin.com/video/7038519357953084680", "https://www.douyin.com/video/7038517649524968734", "https://www.douyin.com/video/7038512629853343007", "https://www.douyin.com/video/7038508947925536031", "https://www.douyin.com/video/7038477186613005599", "https://www.douyin.com/video/7038429312558681355", "https://www.douyin.com/video/7038418697777630467", "https://www.douyin.com/video/7038401247950507276", "https://www.douyin.com/video/7038198931225939208", "https://www.douyin.com/video/7038195202099580167", "https://www.douyin.com/video/7038170382603455758", "https://www.douyin.com/video/7038106267948207390", "https://www.douyin.com/video/7038099728243952903", "https://www.douyin.com/video/7037845800570948871", "https://www.douyin.com/video/7037802250785312008", "https://www.douyin.com/video/7037784049062235400", "https://www.douyin.com/video/7037749002678455566", "https://www.douyin.com/video/7037691269161749774", "https://www.douyin.com/video/7037665832993885477", "https://www.douyin.com/video/7037657108283706637", "https://www.douyin.com/video/7037494819811265823", "https://www.douyin.com/video/7037452180638502175", "https://www.douyin.com/video/7037450183407455518", "https://www.douyin.com/video/7037448998109662467", "https://www.douyin.com/video/7037438750510599428", "https://www.douyin.com/video/7037429610497264904", "https://www.douyin.com/video/7037426988310646053", "https://www.douyin.com/video/7037371012127673636", "https://www.douyin.com/video/7037303462505221389", "https://www.douyin.com/video/7037290945255066917", "https://www.douyin.com/video/7037274378983214367", "https://www.douyin.com/video/7037118773526088968", "https://www.douyin.com/video/7037075651102395662", "https://www.douyin.com/video/7037061817843191053", "https://www.douyin.com/video/7037057066661399821", "https://www.douyin.com/video/7037054208784289031", "https://www.douyin.com/video/7036915464487980302", "https://www.douyin.com/video/7036909318460984612", "https://www.douyin.com/video/7036706953959050507", "https://www.douyin.com/video/7036697171382619396", "https://www.douyin.com/video/7036676391986859301", "https://www.douyin.com/video/7036664139317579038", "https://www.douyin.com/video/7036662053448224013", "https://www.douyin.com/video/7036567351382396168", "https://www.douyin.com/video/7036563815189744933", "https://www.douyin.com/video/7036306258202332449", "https://www.douyin.com/video/7036284781985844483", "https://www.douyin.com/video/7036206617817271566", "https://www.douyin.com/video/7036192201835056420", "https://www.douyin.com/video/7036173205459012868", "https://www.douyin.com/video/7035966506076785928", "https://www.douyin.com/video/7035955019241295135", "https://www.douyin.com/video/7035950615993830693", "https://www.douyin.com/video/7035886611439111455", "https://www.douyin.com/video/7035881636931636493", "https://www.douyin.com/video/7035823379898780935", "https://www.douyin.com/video/7035514219168681254", "https://www.douyin.com/video/7035487262091644164", "https://www.douyin.com/video/7035448862542286091", "https://www.douyin.com/video/7035220004656221444", "https://www.douyin.com/video/7035217938147757323", "https://www.douyin.com/video/7035198129678994721", "https://www.douyin.com/video/7035168262384078094", "https://www.douyin.com/video/7035145889710722336", "https://www.douyin.com/video/7035136254974922016", "https://www.douyin.com/video/7035082533498850597", "https://www.douyin.com/video/7035071514659622177", "https://www.douyin.com/video/7035058891025026312", "https://www.douyin.com/video/7034844803120500004", "https://www.douyin.com/video/7034838082113326366", "https://www.douyin.com/video/7034820367470316807", "https://www.douyin.com/video/7034733787506298148", "https://www.douyin.com/video/7034698801348676895", "https://www.douyin.com/video/7034533559163538721", "https://www.douyin.com/video/7034478350710230309", "https://www.douyin.com/video/7034477168243658021", "https://www.douyin.com/video/7034469728890506510", "https://www.douyin.com/video/7034464142903840036", "https://www.douyin.com/video/7034462412220763428", "https://www.douyin.com/video/7034435663802010893", "https://www.douyin.com/video/7034314534965873933", "https://www.douyin.com/video/7034097283390016775", "https://www.douyin.com/video/7034093166525484302", "https://www.douyin.com/video/7034074069167279390", "https://www.douyin.com/video/7034029277922331936", "https://www.douyin.com/video/7034018291039374629", "https://www.douyin.com/video/7033988960837815589", "https://www.douyin.com/video/7033962094198361357", "https://www.douyin.com/video/7033733134889815304", "https://www.douyin.com/video/7033723550229957920", "https://www.douyin.com/video/7033673342628465927", "https://www.douyin.com/video/7033669938518723853", "https://www.douyin.com/video/7033698065039052068", "https://www.douyin.com/video/7033664799141530916", "https://www.douyin.com/video/7033676828145372452", "https://www.douyin.com/video/7033658402429619470", "https://www.douyin.com/video/7033648497429646630", "https://www.douyin.com/video/7033580936893631751", "https://www.douyin.com/video/7033337328617704742", "https://www.douyin.com/video/7033337097427701031", "https://www.douyin.com/video/7033337026447543564", "https://www.douyin.com/video/7033333398747893000", "https://www.douyin.com/video/7033298982155652360", "https://www.douyin.com/video/7033323570298113319", "https://www.douyin.com/video/7033301044079693059", "https://www.douyin.com/video/7033056749343018271", "https://www.douyin.com/video/7032624989601860877", "https://www.douyin.com/video/7032619682746223908", "https://www.douyin.com/video/7032627218270440717", "https://www.douyin.com/video/7032955124456656132", "https://www.douyin.com/video/7032618721067797790", "https://www.douyin.com/video/7032894615309028640", "https://www.douyin.com/video/7032607515955186952", "https://www.douyin.com/video/7032601030474878245", "https://www.douyin.com/video/7032600666551946532", "https://www.douyin.com/video/7032591573137362213", "https://www.douyin.com/video/7032590950216060197", "https://www.douyin.com/video/7032582092936449312", "https://www.douyin.com/video/7032509654651407648", "https://www.douyin.com/video/7032476423667404069", "https://www.douyin.com/video/7032472809502788877", "https://www.douyin.com/video/7032466375276793125", "https://www.douyin.com/video/7032460695551610143", "https://www.douyin.com/video/7032255377643146509", "https://www.douyin.com/video/7032252286487235877", "https://www.douyin.com/video/7032250946168147238", "https://www.douyin.com/video/7032240087282797862", "https://www.douyin.com/video/7032235991326919972", "https://www.douyin.com/video/7032178776951835942", "https://www.douyin.com/video/7032176073483816224", "https://www.douyin.com/video/7032174164739935525", "https://www.douyin.com/video/7032159690847014180", "https://www.douyin.com/video/7032142582759050527", "https://www.douyin.com/video/7032140767069998350", "https://www.douyin.com/video/7032089686432648459", "https://www.douyin.com/video/7032085623364259083", "https://www.douyin.com/video/7031881990479547651", "https://www.douyin.com/video/7031814531269627147", "https://www.douyin.com/video/7031812248477781252", "https://www.douyin.com/video/7031807078519835937", "https://www.douyin.com/video/7031803115280010499", "https://www.douyin.com/video/7031801802911698209", "https://www.douyin.com/video/7031766618749340940", "https://www.douyin.com/video/7031760699093224708", "https://www.douyin.com/video/7031752493814009091", "https://www.douyin.com/video/7031718065180101918", "https://www.douyin.com/video/7031513947786218790", "https://www.douyin.com/video/7031513738645638403", "https://www.douyin.com/video/7031508269403344140", "https://www.douyin.com/video/7031506381110906151", "https://www.douyin.com/video/7031478945971211523", "https://www.douyin.com/video/7031475216807202081", "https://www.douyin.com/video/7031474452093209859", "https://www.douyin.com/video/7031363221428702476", "https://www.douyin.com/video/7031133746405412099", "https://www.douyin.com/video/7031135538342055179", "https://www.douyin.com/video/7031134107321093380", "https://www.douyin.com/video/7031134053231365412", "https://www.douyin.com/video/7031129839520337184", "https://www.douyin.com/video/7031127949667585292", "https://www.douyin.com/video/7031115543486795040", "https://www.douyin.com/video/7031107959174319374", "https://www.douyin.com/video/7031075811138538783", "https://www.douyin.com/video/7031047061013318942", "https://www.douyin.com/video/7031020108512300318", "https://www.douyin.com/video/7031009590317698334", "https://www.douyin.com/video/7030743789882903820", "https://www.douyin.com/video/7030602425362877710", "https://www.douyin.com/video/7030732649253702920", "https://www.douyin.com/video/7030726193573793061", "https://www.douyin.com/video/7030723065118051621", "https://www.douyin.com/video/7030688755799346440", "https://www.douyin.com/video/7030679720949746982", "https://www.douyin.com/video/7030673954679328013", "https://www.douyin.com/video/7030603685847764260", "https://www.douyin.com/video/7030600549875715336", "https://www.douyin.com/video/7030365406661561603", "https://www.douyin.com/video/7030034484820987173", "https://www.douyin.com/video/7030035362042973476", "https://www.douyin.com/video/7030295750869273894", "https://www.douyin.com/video/7030022001054010660", "https://www.douyin.com/video/7030021873920380173", "https://www.douyin.com/video/7030029214870965511", "https://www.douyin.com/video/7030026960965242125", "https://www.douyin.com/video/7030023779409562910", "https://www.douyin.com/video/7029957142027390244", "https://www.douyin.com/video/7029954825320156453", "https://www.douyin.com/video/7029946251047144712", "https://www.douyin.com/video/7029944598906539271", "https://www.douyin.com/video/7029934383855324447", "https://www.douyin.com/video/7029914910687644941", "https://www.douyin.com/video/7029894504278756639", "https://www.douyin.com/video/7029885294535036196", "https://www.douyin.com/video/7029720210353442056", "https://www.douyin.com/video/7029717715526978823", "https://www.douyin.com/video/7029716941233261854", "https://www.douyin.com/video/7029654929270770981", "https://www.douyin.com/video/7029612039634996494", "https://www.douyin.com/video/7029574290815175943", "https://www.douyin.com/video/7029573978826083621", "https://www.douyin.com/video/7029593666830322981", "https://www.douyin.com/video/7029573763670805774", "https://www.douyin.com/video/7029607924225887518", "https://www.douyin.com/video/7029564910363331876", "https://www.douyin.com/video/7029542588680129800", "https://www.douyin.com/video/7029528345649876255", "https://www.douyin.com/video/7029487044380462350", "https://www.douyin.com/video/7029275142173822222", "https://www.douyin.com/video/7029274055958220062", "https://www.douyin.com/video/7029280090269715719", "https://www.douyin.com/video/7029273513202666789", "https://www.douyin.com/video/7029258788947496223", "https://www.douyin.com/video/7029258363183680775", "https://www.douyin.com/video/7029251203385019655", "https://www.douyin.com/video/7029247215935704328", "https://www.douyin.com/video/7029150226166467871", "https://www.douyin.com/video/7029146346632400165", "https://www.douyin.com/video/7029171598972259598", "https://www.douyin.com/video/7029163480401956133", "https://www.douyin.com/video/7029117400150773023", "https://www.douyin.com/video/7028958828943150349", "https://www.douyin.com/video/7028972070658657544", "https://www.douyin.com/video/7028956221667282212", "https://www.douyin.com/video/7028890012141849863", "https://www.douyin.com/video/7028890740117818638", "https://www.douyin.com/video/7028804926880927013", "https://www.douyin.com/video/7028833678935559461", "https://www.douyin.com/video/7028829116057079070", "https://www.douyin.com/video/7028846266637356319", "https://www.douyin.com/video/7028875382006811917", "https://www.douyin.com/video/7028799558901583140", "https://www.douyin.com/video/7028846019408416036", "https://www.douyin.com/video/7028826786716847390", "https://www.douyin.com/video/7028796304075623688", "https://www.douyin.com/video/7028748387361115422", "https://www.douyin.com/video/7028544818548706599", "https://www.douyin.com/video/7028536912830811429", "https://www.douyin.com/video/7028543852197711115", "https://www.douyin.com/video/7028538169935138084", "https://www.douyin.com/video/7028535222966701324", "https://www.douyin.com/video/7028528898270858528", "https://www.douyin.com/video/7028526464098192679", "https://www.douyin.com/video/7028503717699767588", "https://www.douyin.com/video/7028459372892228871", "https://www.douyin.com/video/7028457760748522782", "https://www.douyin.com/video/7028458744430284039", "https://www.douyin.com/video/7028386593656327454", "https://www.douyin.com/video/7028219874090487071", "https://www.douyin.com/video/7028163267340127501", "https://www.douyin.com/video/7028081492681100557", "https://www.douyin.com/video/7028078844233993508", "https://www.douyin.com/video/7028075997270445319", "https://www.douyin.com/video/7028117444283731230", "https://www.douyin.com/video/7028114097744940318", "https://www.douyin.com/video/7028096622307331358", "https://www.douyin.com/video/7028044535074671880", "https://www.douyin.com/video/7027811340387487012", "https://www.douyin.com/video/7027801590299987237", "https://www.douyin.com/video/7027751000324721928", "https://www.douyin.com/video/7027741130217377037", "https://www.douyin.com/video/7027670492928691464", "https://www.douyin.com/video/7027664253855321351", "https://www.douyin.com/video/7027434038763867405", "https://www.douyin.com/video/7027427903352638750", "https://www.douyin.com/video/7027418461424864519", "https://www.douyin.com/video/7027412070324882696", "https://www.douyin.com/video/7027380264405863683", "https://www.douyin.com/video/7027053659020070158", "https://www.douyin.com/video/7027045119471766797", "https://www.douyin.com/video/7026993157502012685", "https://www.douyin.com/video/7026987129091788046", "https://www.douyin.com/video/7027013995374628133", "https://www.douyin.com/video/7027010347848502535", "https://www.douyin.com/video/7027008531454856478", "https://www.douyin.com/video/7026980311422504206", "https://www.douyin.com/video/7026973569439583519", "https://www.douyin.com/video/7026929584067087623"]}
for i in d['links']:
    try:
        system(' '.join([
            r"C:/Users/jkcao/Downloads/lux_0.12.0_Windows_32-bit/lux.exe"
            ,'-n 1 -o'
            ,r"C:/Users/jkcao/Videos/douyin"
            ,i
            ]))
        sleep(19)
    except:
        continue
        # except: pass
        # s = 0
        # while r'.download' in ' '.join(listdir(r'C:\Users\jkcao\Videos\douyin')) or len(listdir(r'C:\Users\jkcao\Videos\douyin')) != 1:
        #         sleep(9)
        #         s += 1
        #         if s > 11: break
        # ld = listdir(r'C:\Users\jkcao\Videos\douyin')
        # try:
        #     timered_cp(
        #     tmp='C:\\Users\\jkcao\\Videos\\douyin\\' + ld[0]
        #     , rp = '/iflytek/jkcao/douyin/' + d['author']
        #     )
        #     sleep(9)
        # except: pass
        # while len(listdir(r'C:\Users\jkcao\Videos\douyin')) > 0:
        #     for d in ld:
        #         system(
        #             r'del /f /s /q "'
        #             + 'C:\\Users\\jkcao\\Videos\\douyin\\'
        #             + d
        #             + '"'
        #             )
        #         sleep(1)
    # for p in range(1,51):
    #     print(k, p)
    #     try:
    #         l = 'https://search.bilibili.com/all?' + urlencode({'keyword': k,'page': p})
    #         bso = timered_link2bso(l)
    #         sleep(9)
    #         if len(bso.find_all(class_='video-item matrix'))>0:
    #             for li in bso.find_all(class_='video-item matrix'):
    #                 try:
    #                     if r'http:' not in li.a['href'].split('?')[0]:
    #                         url = r'http:' + li.a['href'].split('?')[0]
    #                     else:
    #                         url = li.a['href'].split('?')[0]
    #                     try:
    #                         timered_gbili(url)
    #                         sleep(9)
    #                     except: pass
    #                     s = 0
    #                     while r'.download' in ' '.join(listdir(r'C:\Users\jkcao\Videos\tmp')) or len(listdir(r'C:\Users\jkcao\Videos\tmp')) != 1:
    #                         sleep(9)
    #                         s += 1
    #                         if s > 111: break
                        
    #                     ld = listdir(r'C:\Users\jkcao\Videos\tmp')
    #                     try:
    #                         timered_ubili(
    #                         tmp='C:\\Users\\jkcao\\Videos\\tmp\\' + ld[0]
    #                         , rp = '/iflytek/jkcao/bili/' + k
    #                         )
    #                         sleep(9)
    #                     except: pass
    #                     while len(listdir(r'C:\Users\jkcao\Videos\tmp')) > 0:
    #                         for d in ld:
    #                             system(
    #                                 r'del /f /s /q "'
    #                                 + 'C:\\Users\\jkcao\\Videos\\tmp\\'
    #                                 + d
    #                                 + '"'
    #                                 )
    #                             sleep(1)
    #                 except: continue
    #         else: break
    #     except Exception as e:
    #         print(str(e))
    #         continue
