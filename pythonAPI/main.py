from ast import main
from distutils.log import debug
from flask import Flask , jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello"

@app.route("/top-headlines")
def hello():
    return jsonify ({
  "status": "ok",
  "totalResults": 70,
  "articles": [ { "source" :  {'id' : "101", 'name' : "The Times of India"}, 'author' : "Kshitij Anand",
      'title': "Stock Radar: This small-cap stock, taking support above 50-DMA, is a good short-term buy; here’s why - Economic Times",
      'description' : "The stock hit a 52-week high of Rs 398 on February 3, but failed to hold on to the momentum. It, however, bounced back after hitting a low of Rs 230 on July 12",
      'url' : "https://economictimes.indiatimes.com/markets/stocks/news/stock-radar-this-small-cap-stock-taking-support-above-50-dma-is-a-good-short-term-buy-heres-why/articleshow/94840563.cms",
      'urlToImage' : "https://img.etimg.com/thumb/msid-94865154,width-1070,height-580/photo.jpg",
      'publishedAt' : "2022-10-15T03:22:00Z",
      'content' : "SynopsisThe stock hit a 52-week high of Rs 398 on February 3, but failed to hold on to the momentum. It, however, bounced back after hitting a low of Rs 230 on July 12"},{
      "source": {
        "id": "102",
        "name": "Livemint"
      },
      "author": "Livemint",
      "title": "Adani Group 'not evaluating' proposal for acquiring Jaypee Cement | Mint - Mint",
      "description": "Reports earlier stated that the Gautam Adani-backed Group is in discussion to buy Jaypee Group's debt-laden cement business for approximately $606 million.",
      "url": "https://www.livemint.com/companies/news/adani-group-not-evaluating-proposal-for-acquiring-jaypee-cement-11665740025344.html",
      "urlToImage": "https://images.livemint.com/img/2022/10/14/600x338/adani-stock_1664863375771_1665740106940_1665740106940.jpg",
      "publishedAt": "2022-10-14T09:35:53Z",
      "content": "Adani Group on Friday said that they are not evaluating any proposal for acquiring Japyee Cement. Reports earlier stated that the Gautam Adani-backed Group is in discussion to buy Jaypee Group's debt… [+2258 chars]"
    },
    {
      "source": {
        "id": "103",
        "name": "Moneycontrol"
      },
      "author": "Moneycontrol News",
      "title": "India never had a stock market boom without a US recession, says Marcellus' Mukherjea - Moneycontrol",
      "description": "Assessing the prospects of IT stocks from a medium to long-term perspective, Saurabh Mukherjea said that companies like TCS, Infosys and HCL Tech have been performing well.",
      "url": "https://www.moneycontrol.com/news/business/markets/india-never-had-a-stock-market-boom-without-a-us-recession-says-marcellus-mukherjea-9329501.html",
      "urlToImage": "https://images.moneycontrol.com/static-mcnews/2022/02/Saurabh-Mukherjea-770x433.jpg",
      "publishedAt": "2022-10-14T09:11:06Z",
      "content": "A recession in the US has historically been a positive thing for India, according to Saurabh Mukherjea, founder of Marcellus Investment Managers.\r\nFirst, a US recession leads to a fall in crude oil p… [+1605 chars]"
    },
    {
      "source": {
        "id": "104",
        "name": "NDTV News"
      },
      "author": "Tinku",
      "title": "Watch: This ATM In Bangalore Delivers Fresh And Contactless Idlis In Minutes - NDTV",
      "description": "The machine is made by the startup Freshup Robotics, founded by Bengaluru-based entrepreneurs Sharan Hiremath and Suresh Chandrashekaran.",
      "url": "https://www.ndtv.com/india-news/watch-this-atm-in-bangalore-delivers-fresh-and-contactless-idlis-in-minutes-3430863",
      "urlToImage": "https://c.ndtvimg.com/2022-10/alvdvpco_mr-hiremath-got-the-idea-in-2016_625x300_14_October_22.jpg",
      "publishedAt": "2022-10-14T08:37:35Z",
      "content": "Mr Hiremath got the idea in 2016\r\nThere is no denying that idli is one of the most popular south Indian dishes. The light, soft and fluffy idlis are enough to keep you full for a long time. Dunk it i… [+1401 chars]"
    },
    {
      "source": {
        "id": "105",
        "name": "Moneycontrol"
      },
      "author": "Ashwin Mohan",
      "title": "NCLT approves Arcelor Mittal resolution plan for Uttam Galva - Moneycontrol",
      "description": "This is Arcelor Mittal’s third  purchase through the insolvency process in India after Essar Steel and Odisha Slurry Pipleine Infrastructure",
      "url": "https://www.moneycontrol.com/news/business/companies/nclt-approves-arcelor-mittal-resolution-plan-for-uttam-galva-9329511.html",
      "urlToImage": "https://images.moneycontrol.com/static-mcnews/2022/05/steel-770x433.jpg",
      "publishedAt": "2022-10-14T08:26:30Z",
      "content": "The National Company Law Appellate Tribunal (NCLT), Mumbai has approved the Rs 4,050-crore resolution plan submitted by an Indian arm of global steel behemoth Arcelor Mittal for debt-ridden Uttam Gal… [+1641 chars]"
    },
    {
      "source": {
        "id": "106",
        "name": "Livemint"
      },
      "author": "Livemint",
      "title": "Bonus shares issue, stock split decision to be taken by this company's board next week. Details here | Mint - Mint",
      "description": "A stock split increases the number of shares that are outstanding by issuing more shares to the current shareholders",
      "url": "https://www.livemint.com/market/stock-market-news/bonus-shares-issue-stock-split-decision-to-be-taken-by-maharashtra-seamless-s-board-next-week-11665734044005.html",
      "urlToImage": "https://images.livemint.com/img/2022/10/14/600x338/bonus_shares_1665734628277_1665734628424_1665734628424.jpg",
      "publishedAt": "2022-10-14T08:22:37Z",
      "content": "Maharashtra Seamless Ltd earlier this week informed that the company's board of directors will meet next week on Monday, 17th October, 2022 to consider the bonus issue of equity shares as well as sub… [+1733 chars]"
    },
    {
      "source": {
        "id": "107",
        "name": "Moneycontrol"
      },
      "author": "Moneycontrol News",
      "title": "Biggest rally coming in the second half of October, Nifty to touch 18,200 by Diwali: IIFL’s Sanjiv... - Moneycontrol",
      "description": "Veteran investor’s top Diwali pick is IndiGo, while he has identified JP Associates and BL Kashyap as turnaround stocks.",
      "url": "https://www.moneycontrol.com/news/business/markets/biggest-rally-coming-in-the-second-half-of-october-nifty-to-touch-18200-by-diwali-iifls-sanjiv-bhasin-9329001.html",
      "urlToImage": "https://images.moneycontrol.com/static-mcnews/2020/05/Sanjiv_Bhasin1280-770x433.jpg",
      "publishedAt": "2022-10-14T08:20:02Z",
      "content": "The second half of October will see the best bull rally ever and Nifty will hit 18,200 by Diwali, said IIFL Securities Director Sanjiv Bhasin. was talking to CNBC TV18.\r\nThe sheer pessimism o… [+3433 chars]"
    },
     {
      "source": {
        "id": "108",
        "name": "Analytics Insight"
      },
      "author": "Tinku",
      "title": "Bitcoin Price Prediction: Will BTC Head to US$30k or US$10k in 2022? - Analytics Insight",
      "description": "Tinku",
      "url": "https://www.analyticsinsight.net/bitcoin-price-prediction-will-btc-head-to-us30k-or-us10k-in-2022/",
      "urlToImage": "Tinku",
      "publishedAt": "2022-10-14T08:11:26Z",
      "content": "Tinku"
    },
    {
      "source": {
        "id": "109",
        "name": "YouTube"
      },
      "author": "Tinku",
      "title": "Elon Musk is under federal investigation over $44 billion Twitter deal | Latest World News | WION - WION",
      "description": "Elon Musk is being investigated by federal authorities over his conduct in his $44-billion takeover deal for Twitter. Lawyers representing Twitter said that ...",
      "url": "https://www.youtube.com/watch?v=H6UP2U9oI5I",
      "urlToImage": "https://i.ytimg.com/vi/H6UP2U9oI5I/maxresdefault.jpg",
      "publishedAt": "2022-10-14T07:59:27Z",
      "content": "Tinku"
    },
    {
      "source": {
        "id": "110",
        "name": "Moneycontrol"
      },
      "author": "Moneycontrol News",
      "title": "Shriram Group may bid for IDBI Bank in battle with Prem Watsa - Moneycontrol",
      "description": "Shriram was amongst 18 participants that attended virtual roadshows organised by the government in April to brief  suitors about the privatisation plan.",
      "url": "https://www.moneycontrol.com/news/business/shriram-group-may-bid-for-idbi-bank-in-battle-with-prem-watsa-9328621.html",
      "urlToImage": "https://images.moneycontrol.com/static-mcnews/2022/07/IDBI-770x433.png",
      "publishedAt": "2022-10-14T07:53:41Z",
      "content": "Shriram Group may submit an initial bid or expression of interest for state-owned lender IDBI Bank, The Economic Times said.\r\nThe Chennai-headquartered financier may float a separate holding company … [+1408 chars]",
    }]})

if __name__ == "__main__":
    app.run(debug = True)