import requests
import json
import datetime as dt
from twilio.rest import Client
import twilio.base.exceptions as tw

STOCK = "TSLA"
COMPANY_NAME = "tesla"
STOCK_API_KEY = "51GF9C3RYNKXCOUK"
STOCK_ENDPOINT = "http://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "7abc720571bd4f849d2a9d59f4237466"
SMS_account_sid = "AC799ca80647325c715a9cc65b4edc0f31"
SMS_auth_token = "bd8c418fe486fdd2d70c16b6c502b05b"
FROM = '+13608001587'
TO = '+989190911812'


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def fetch_stock_price():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }
    # access to this api is restricted in Iran
    # I have to hardcode data because it doesn't work
    # print(f"http://www.alphavantage.co/query?function={stock_params['function']}&symbol={stock_params['symbol']}&apikey={stock_params['apikey']}")
    # response = requests.get(STOCK_ENDPOINT, params=stock_params)
    # data = response.json()
    data = json.dumps(
        {
            "Meta Data": {
                "1. Information": "Daily Prices (open, high, low, close) and Volumes",
                "2. Symbol": "TSLA",
                "3. Last Refreshed": "2022-10-26",
                "4. Output Size": "Compact",
                "5. Time Zone": "US/Eastern"
            },
            "Time Series (Daily)": {
                "2022-10-26": {
                    "1. open": "219.4000",
                    "2. high": "230.6000",
                    "3. low": "218.2000",
                    "4. close": "224.6400",
                    "5. volume": "84709714"
                },
                "2022-10-25": {
                    "1. open": "210.1000",
                    "2. high": "224.3498",
                    "3. low": "210.0000",
                    "4. close": "222.4150",
                    "5. volume": "96507870"
                },
                "2022-10-24": {
                    "1. open": "205.8200",
                    "2. high": "213.5000",
                    "3. low": "198.5863",
                    "4. close": "211.2500",
                    "5. volume": "100446765"
                },
                "2022-10-21": {
                    "1. open": "206.4150",
                    "2. high": "214.6600",
                    "3. low": "203.8000",
                    "4. close": "214.4400",
                    "5. volume": "75713754"
                },
                "2022-10-20": {
                    "1. open": "208.2800",
                    "2. high": "215.5500",
                    "3. low": "202.0000",
                    "4. close": "207.2800",
                    "5. volume": "117798062"
                },
                "2022-10-19": {
                    "1. open": "219.8000",
                    "2. high": "222.9300",
                    "3. low": "217.7800",
                    "4. close": "222.0400",
                    "5. volume": "66571479"
                },
                "2022-10-18": {
                    "1. open": "229.5000",
                    "2. high": "229.8200",
                    "3. low": "217.2500",
                    "4. close": "220.1900",
                    "5. volume": "75891905"
                },
                "2022-10-17": {
                    "1. open": "210.0400",
                    "2. high": "221.8600",
                    "3. low": "209.4500",
                    "4. close": "219.3500",
                    "5. volume": "79428810"
                },
                "2022-10-14": {
                    "1. open": "224.0100",
                    "2. high": "226.2600",
                    "3. low": "204.1600",
                    "4. close": "204.9900",
                    "5. volume": "94124511"
                },
                "2022-10-13": {
                    "1. open": "208.3000",
                    "2. high": "222.9900",
                    "3. low": "206.2200",
                    "4. close": "221.7200",
                    "5. volume": "91483045"
                },
                "2022-10-12": {
                    "1. open": "215.3300",
                    "2. high": "219.2999",
                    "3. low": "211.5100",
                    "4. close": "217.2400",
                    "5. volume": "66860699"
                },
                "2022-10-11": {
                    "1. open": "220.9450",
                    "2. high": "225.7500",
                    "3. low": "215.0000",
                    "4. close": "216.5000",
                    "5. volume": "77013202"
                },
                "2022-10-10": {
                    "1. open": "223.9300",
                    "2. high": "226.9900",
                    "3. low": "218.3582",
                    "4. close": "222.9600",
                    "5. volume": "67925018"
                },
                "2022-10-07": {
                    "1. open": "233.9350",
                    "2. high": "234.5715",
                    "3. low": "222.0200",
                    "4. close": "223.0700",
                    "5. volume": "83916800"
                },
                "2022-10-06": {
                    "1. open": "239.4400",
                    "2. high": "244.5800",
                    "3. low": "235.3500",
                    "4. close": "238.1300",
                    "5. volume": "69298437"
                },
                "2022-10-05": {
                    "1. open": "245.0100",
                    "2. high": "246.6697",
                    "3. low": "233.2700",
                    "4. close": "240.8100",
                    "5. volume": "86982673"
                },
                "2022-10-04": {
                    "1. open": "250.5200",
                    "2. high": "257.5000",
                    "3. low": "242.0100",
                    "4. close": "249.4400",
                    "5. volume": "109578535"
                },
                "2022-10-03": {
                    "1. open": "254.5000",
                    "2. high": "255.1600",
                    "3. low": "241.0100",
                    "4. close": "242.4000",
                    "5. volume": "98363541"
                },
                "2022-09-30": {
                    "1. open": "266.1450",
                    "2. high": "275.5700",
                    "3. low": "262.4700",
                    "4. close": "265.2500",
                    "5. volume": "67726598"
                },
                "2022-09-29": {
                    "1. open": "282.7600",
                    "2. high": "283.6500",
                    "3. low": "265.7800",
                    "4. close": "268.2100",
                    "5. volume": "77620642"
                },
                "2022-09-28": {
                    "1. open": "283.0800",
                    "2. high": "289.0000",
                    "3. low": "277.5700",
                    "4. close": "287.8100",
                    "5. volume": "54664809"
                },
                "2022-09-27": {
                    "1. open": "283.8400",
                    "2. high": "288.6700",
                    "3. low": "277.5100",
                    "4. close": "282.9400",
                    "5. volume": "61925185"
                },
                "2022-09-26": {
                    "1. open": "271.8300",
                    "2. high": "284.0900",
                    "3. low": "270.3100",
                    "4. close": "276.0100",
                    "5. volume": "58076913"
                },
                "2022-09-23": {
                    "1. open": "283.0900",
                    "2. high": "284.5000",
                    "3. low": "272.8200",
                    "4. close": "275.3300",
                    "5. volume": "63748362"
                },
                "2022-09-22": {
                    "1. open": "299.8600",
                    "2. high": "301.2900",
                    "3. low": "285.8200",
                    "4. close": "288.5900",
                    "5. volume": "70107683"
                },
                "2022-09-21": {
                    "1. open": "308.2900",
                    "2. high": "313.8000",
                    "3. low": "300.6300",
                    "4. close": "300.8000",
                    "5. volume": "62555656"
                },
                "2022-09-20": {
                    "1. open": "306.9100",
                    "2. high": "313.3300",
                    "3. low": "305.5800",
                    "4. close": "308.7300",
                    "5. volume": "61642783"
                },
                "2022-09-19": {
                    "1. open": "300.0900",
                    "2. high": "309.8400",
                    "3. low": "297.8000",
                    "4. close": "309.0700",
                    "5. volume": "60231156"
                },
                "2022-09-16": {
                    "1. open": "299.6050",
                    "2. high": "303.7100",
                    "3. low": "295.6005",
                    "4. close": "303.3500",
                    "5. volume": "87087786"
                },
                "2022-09-15": {
                    "1. open": "301.8250",
                    "2. high": "309.1200",
                    "3. low": "300.7247",
                    "4. close": "303.7500",
                    "5. volume": "64795523"
                },
                "2022-09-14": {
                    "1. open": "292.2400",
                    "2. high": "306.0000",
                    "3. low": "291.6400",
                    "4. close": "302.6100",
                    "5. volume": "72628653"
                },
                "2022-09-13": {
                    "1. open": "292.9000",
                    "2. high": "297.3999",
                    "3. low": "290.4000",
                    "4. close": "292.1300",
                    "5. volume": "68229619"
                },
                "2022-09-12": {
                    "1. open": "300.7200",
                    "2. high": "305.4900",
                    "3. low": "300.4000",
                    "4. close": "304.4200",
                    "5. volume": "48674604"
                },
                "2022-09-09": {
                    "1. open": "291.6700",
                    "2. high": "299.8500",
                    "3. low": "291.2450",
                    "4. close": "299.6800",
                    "5. volume": "54470854"
                },
                "2022-09-08": {
                    "1. open": "281.3000",
                    "2. high": "289.5000",
                    "3. low": "279.7600",
                    "4. close": "289.2600",
                    "5. volume": "53713124"
                },
                "2022-09-07": {
                    "1. open": "273.1000",
                    "2. high": "283.8400",
                    "3. low": "272.2700",
                    "4. close": "283.7000",
                    "5. volume": "50028916"
                },
                "2022-09-06": {
                    "1. open": "272.6750",
                    "2. high": "275.9900",
                    "3. low": "265.7400",
                    "4. close": "274.4200",
                    "5. volume": "55605247"
                },
                "2022-09-02": {
                    "1. open": "281.0650",
                    "2. high": "282.3500",
                    "3. low": "269.0800",
                    "4. close": "270.2100",
                    "5. volume": "50890090"
                },
                "2022-09-01": {
                    "1. open": "272.5750",
                    "2. high": "277.5800",
                    "3. low": "266.1500",
                    "4. close": "277.1600",
                    "5. volume": "54287024"
                },
                "2022-08-31": {
                    "1. open": "280.6200",
                    "2. high": "281.2500",
                    "3. low": "271.8100",
                    "4. close": "275.6100",
                    "5. volume": "52107337"
                },
                "2022-08-30": {
                    "1. open": "287.8650",
                    "2. high": "288.4800",
                    "3. low": "272.6500",
                    "4. close": "277.7000",
                    "5. volume": "50541759"
                },
                "2022-08-29": {
                    "1. open": "282.8300",
                    "2. high": "287.7400",
                    "3. low": "280.7000",
                    "4. close": "284.8200",
                    "5. volume": "41548729"
                },
                "2022-08-26": {
                    "1. open": "297.4300",
                    "2. high": "302.0000",
                    "3. low": "287.4700",
                    "4. close": "288.0900",
                    "5. volume": "57163947"
                },
                "2022-08-25": {
                    "1. open": "302.3600",
                    "2. high": "302.9600",
                    "3. low": "291.6000",
                    "4. close": "296.0700",
                    "5. volume": "52827378"
                },
                "2022-08-24": {
                    "1. open": "892.6900",
                    "2. high": "910.9400",
                    "3. low": "889.5000",
                    "4. close": "891.2900",
                    "5. volume": "19086572"
                },
                "2022-08-23": {
                    "1. open": "874.3600",
                    "2. high": "896.4799",
                    "3. low": "863.7700",
                    "4. close": "889.3600",
                    "5. volume": "21328348"
                },
                "2022-08-22": {
                    "1. open": "875.7400",
                    "2. high": "877.2000",
                    "3. low": "858.8900",
                    "4. close": "869.7400",
                    "5. volume": "18614449"
                },
                "2022-08-19": {
                    "1. open": "897.0000",
                    "2. high": "901.0800",
                    "3. low": "877.5000",
                    "4. close": "890.0000",
                    "5. volume": "20465129"
                },
                "2022-08-18": {
                    "1. open": "918.0000",
                    "2. high": "919.5000",
                    "3. low": "905.5600",
                    "4. close": "908.6100",
                    "5. volume": "15833512"
                },
                "2022-08-17": {
                    "1. open": "910.1900",
                    "2. high": "928.9700",
                    "3. low": "900.1000",
                    "4. close": "911.9900",
                    "5. volume": "22921990"
                },
                "2022-08-16": {
                    "1. open": "935.0000",
                    "2. high": "944.0000",
                    "3. low": "908.6500",
                    "4. close": "919.6900",
                    "5. volume": "29378774"
                },
                "2022-08-15": {
                    "1. open": "905.3600",
                    "2. high": "939.4000",
                    "3. low": "903.6900",
                    "4. close": "927.9600",
                    "5. volume": "29786389"
                },
                "2022-08-12": {
                    "1. open": "868.2450",
                    "2. high": "900.4800",
                    "3. low": "855.1000",
                    "4. close": "900.0900",
                    "5. volume": "26552429"
                },
                "2022-08-11": {
                    "1. open": "889.5400",
                    "2. high": "894.7100",
                    "3. low": "857.5000",
                    "4. close": "859.8900",
                    "5. volume": "23385015"
                },
                "2022-08-10": {
                    "1. open": "891.2000",
                    "2. high": "892.5300",
                    "3. low": "850.1100",
                    "4. close": "883.0700",
                    "5. volume": "31639624"
                },
                "2022-08-09": {
                    "1. open": "870.8800",
                    "2. high": "877.1900",
                    "3. low": "838.0600",
                    "4. close": "850.0000",
                    "5. volume": "28748227"
                },
                "2022-08-08": {
                    "1. open": "885.0000",
                    "2. high": "915.6000",
                    "3. low": "867.2562",
                    "4. close": "871.2700",
                    "5. volume": "33121758"
                },
                "2022-08-05": {
                    "1. open": "908.0100",
                    "2. high": "913.8199",
                    "3. low": "856.6340",
                    "4. close": "864.5100",
                    "5. volume": "37724299"
                },
                "2022-08-04": {
                    "1. open": "933.0000",
                    "2. high": "940.8200",
                    "3. low": "915.0000",
                    "4. close": "925.9000",
                    "5. volume": "24085439"
                },
                "2022-08-03": {
                    "1. open": "915.0000",
                    "2. high": "928.6500",
                    "3. low": "903.4500",
                    "4. close": "922.1900",
                    "5. volume": "26697035"
                },
                "2022-08-02": {
                    "1. open": "882.0100",
                    "2. high": "923.5000",
                    "3. low": "878.0000",
                    "4. close": "901.7600",
                    "5. volume": "31859156"
                },
                "2022-08-01": {
                    "1. open": "903.8250",
                    "2. high": "935.6347",
                    "3. low": "885.0000",
                    "4. close": "891.8300",
                    "5. volume": "39014296"
                },
                "2022-07-29": {
                    "1. open": "842.1000",
                    "2. high": "894.9600",
                    "3. low": "837.3000",
                    "4. close": "891.4500",
                    "5. volume": "31770961"
                },
                "2022-07-28": {
                    "1. open": "840.2000",
                    "2. high": "849.9000",
                    "3. low": "818.4000",
                    "4. close": "842.7000",
                    "5. volume": "28240997"
                },
                "2022-07-27": {
                    "1. open": "791.4300",
                    "2. high": "827.7768",
                    "3. low": "785.3701",
                    "4. close": "824.4600",
                    "5. volume": "29369996"
                },
                "2022-07-26": {
                    "1. open": "799.5400",
                    "2. high": "801.9299",
                    "3. low": "768.7900",
                    "4. close": "776.5800",
                    "5. volume": "22273586"
                },
                "2022-07-25": {
                    "1. open": "816.6500",
                    "2. high": "822.4400",
                    "3. low": "802.2000",
                    "4. close": "805.3000",
                    "5. volume": "21357835"
                },
                "2022-07-22": {
                    "1. open": "828.6600",
                    "2. high": "842.3600",
                    "3. low": "812.1400",
                    "4. close": "816.7300",
                    "5. volume": "34490949"
                },
                "2022-07-21": {
                    "1. open": "765.3200",
                    "2. high": "819.8000",
                    "3. low": "764.6000",
                    "4. close": "815.1200",
                    "5. volume": "47344059"
                },
                "2022-07-20": {
                    "1. open": "740.3500",
                    "2. high": "751.9900",
                    "3. low": "730.4490",
                    "4. close": "742.5000",
                    "5. volume": "29621363"
                },
                "2022-07-19": {
                    "1. open": "735.0000",
                    "2. high": "741.4200",
                    "3. low": "710.9300",
                    "4. close": "736.5900",
                    "5. volume": "26963370"
                },
                "2022-07-18": {
                    "1. open": "734.8100",
                    "2. high": "751.5500",
                    "3. low": "718.8100",
                    "4. close": "721.6400",
                    "5. volume": "27512476"
                },
                "2022-07-15": {
                    "1. open": "720.0000",
                    "2. high": "730.8699",
                    "3. low": "710.6700",
                    "4. close": "720.2000",
                    "5. volume": "23227673"
                },
                "2022-07-14": {
                    "1. open": "704.6900",
                    "2. high": "715.9600",
                    "3. low": "688.0000",
                    "4. close": "714.9400",
                    "5. volume": "26185833"
                },
                "2022-07-13": {
                    "1. open": "676.5000",
                    "2. high": "726.1799",
                    "3. low": "675.1000",
                    "4. close": "711.1200",
                    "5. volume": "32651499"
                },
                "2022-07-12": {
                    "1. open": "710.5400",
                    "2. high": "719.3200",
                    "3. low": "685.1050",
                    "4. close": "699.2100",
                    "5. volume": "29310320"
                },
                "2022-07-11": {
                    "1. open": "756.3100",
                    "2. high": "759.1900",
                    "3. low": "700.8800",
                    "4. close": "703.0300",
                    "5. volume": "33169740"
                },
                "2022-07-08": {
                    "1. open": "727.0000",
                    "2. high": "764.9399",
                    "3. low": "723.4843",
                    "4. close": "752.2900",
                    "5. volume": "33951362"
                },
                "2022-07-07": {
                    "1. open": "701.7600",
                    "2. high": "736.0850",
                    "3. low": "696.6300",
                    "4. close": "733.6300",
                    "5. volume": "27310230"
                },
                "2022-07-06": {
                    "1. open": "692.3400",
                    "2. high": "703.6900",
                    "3. low": "681.5600",
                    "4. close": "695.2000",
                    "5. volume": "23951210"
                },
                "2022-07-05": {
                    "1. open": "669.0000",
                    "2. high": "699.4400",
                    "3. low": "648.5001",
                    "4. close": "699.2000",
                    "5. volume": "28259704"
                },
                "2022-07-01": {
                    "1. open": "681.0000",
                    "2. high": "690.6900",
                    "3. low": "666.3601",
                    "4. close": "681.7900",
                    "5. volume": "24820148"
                },
                "2022-06-30": {
                    "1. open": "673.5300",
                    "2. high": "688.3700",
                    "3. low": "656.5900",
                    "4. close": "673.4200",
                    "5. volume": "31533484"
                },
                "2022-06-29": {
                    "1. open": "691.5000",
                    "2. high": "693.5200",
                    "3. low": "666.8200",
                    "4. close": "685.4700",
                    "5. volume": "27632418"
                },
                "2022-06-28": {
                    "1. open": "733.4500",
                    "2. high": "749.9100",
                    "3. low": "697.0300",
                    "4. close": "697.9900",
                    "5. volume": "30222167"
                },
                "2022-06-27": {
                    "1. open": "748.1000",
                    "2. high": "756.2100",
                    "3. low": "727.6966",
                    "4. close": "734.7600",
                    "5. volume": "29726104"
                },
                "2022-06-24": {
                    "1. open": "712.4050",
                    "2. high": "738.2000",
                    "3. low": "708.2600",
                    "4. close": "737.1200",
                    "5. volume": "31923565"
                },
                "2022-06-23": {
                    "1. open": "713.7150",
                    "2. high": "717.9500",
                    "3. low": "685.9100",
                    "4. close": "705.2100",
                    "5. volume": "34734226"
                },
                "2022-06-22": {
                    "1. open": "703.5100",
                    "2. high": "740.5000",
                    "3. low": "701.4800",
                    "4. close": "708.2600",
                    "5. volume": "33842420"
                },
                "2022-06-21": {
                    "1. open": "673.8100",
                    "2. high": "730.7321",
                    "3. low": "673.0000",
                    "4. close": "711.1100",
                    "5. volume": "40930985"
                },
                "2022-06-17": {
                    "1. open": "640.3000",
                    "2. high": "662.9082",
                    "3. low": "639.5900",
                    "4. close": "650.2800",
                    "5. volume": "30880590"
                },
                "2022-06-16": {
                    "1. open": "668.2100",
                    "2. high": "675.5000",
                    "3. low": "626.0800",
                    "4. close": "639.3000",
                    "5. volume": "35796900"
                },
                "2022-06-15": {
                    "1. open": "662.7500",
                    "2. high": "706.9899",
                    "3. low": "654.4500",
                    "4. close": "699.0000",
                    "5. volume": "39710645"
                },
                "2022-06-14": {
                    "1. open": "654.8600",
                    "2. high": "678.9900",
                    "3. low": "635.2100",
                    "4. close": "662.6700",
                    "5. volume": "32662932"
                },
                "2022-06-13": {
                    "1. open": "669.5000",
                    "2. high": "679.9000",
                    "3. low": "644.0500",
                    "4. close": "647.2100",
                    "5. volume": "34255754"
                },
                "2022-06-10": {
                    "1. open": "705.4700",
                    "2. high": "718.5000",
                    "3. low": "683.7400",
                    "4. close": "696.6900",
                    "5. volume": "32696966"
                },
                "2022-06-09": {
                    "1. open": "748.0200",
                    "2. high": "766.6399",
                    "3. low": "717.9800",
                    "4. close": "719.1200",
                    "5. volume": "32163769"
                },
                "2022-06-08": {
                    "1. open": "720.2600",
                    "2. high": "749.8900",
                    "3. low": "717.5300",
                    "4. close": "725.6000",
                    "5. volume": "25403540"
                },
                "2022-06-07": {
                    "1. open": "702.0000",
                    "2. high": "719.9900",
                    "3. low": "690.2800",
                    "4. close": "716.6600",
                    "5. volume": "24269534"
                },
                "2022-06-06": {
                    "1. open": "733.0600",
                    "2. high": "734.6000",
                    "3. low": "703.0500",
                    "4. close": "714.8400",
                    "5. volume": "28068174"
                }
            }
        }
    )
    data = json.loads(data)

    yesterday_data = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y-%m-%d")
    day_before_yesterday_data = (dt.datetime.now() - dt.timedelta(days=2)).strftime("%Y-%m-%d")
    yesterday_closing_price = float(data['Time Series (Daily)'][yesterday_data]['4. close'])
    day_before_closing_price = float(data['Time Series (Daily)'][day_before_yesterday_data]['4. close'])
    difference = yesterday_closing_price - day_before_closing_price
    percent = round(difference / yesterday_closing_price * 100)
    return percent > 0, percent, difference > 0


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    today = dt.datetime.now().strftime("%Y-%m-%d")
    news_params = {
        "q": COMPANY_NAME,
        "from": today,
        "to": today,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }
    # print(f"https://newsapi.org/v2/everything?q={news_params['q']}&from={news_params['from']}&to={news_params['to']}&sortBy={news_params['sortBy']}&apiKey={news_params['apiKey']}")
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    data = response.json()['articles']
    three_articles = data[:3]
    return three_articles


def send_sms(article_list: list):
    client = Client(SMS_account_sid, SMS_auth_token)
    for article in article_list:
        try:
            message = client.messages.create(
                body=article,
                from_=FROM,
                to=TO)
        except:
            print(f"**{article}")


status, percent, going_up = fetch_stock_price()
if status:
    up_down = None
    if going_up:
        up_down = "🔺"
    else:
        up_down = "🔻"

    result = get_news()
    news_list = [f"{COMPANY_NAME}: {up_down} {percent}%\nHeadline: {article['title']},\nBrief: {article['description']}"
                 for article in result]
    send_sms(news_list)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
