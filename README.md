<div align="center">
<pre>
███╗   ███╗ █████╗ ██████╗ ██╗  ██╗███████╗████████╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝██╔════╝╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██╔████╔██║███████║██████╔╝█████╔╝ █████╗     ██║       ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝     ██║       ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗███████╗   ██║       ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                                
---------------------------------------------------
python cli program to check steam item market
</pre>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Static Badge](https://img.shields.io/badge/bs4-0.0.1-blue)
![Static Badge](https://img.shields.io/badge/requests-2.25.1-green)


</div>
Is the steam market interface too slow or ineficcient for you? Want something simpler? Try Steam Market Scraper -- A Python program that gives you market information watered down
<p align="center"><img src="https://github.com/gappro/Steam-market-scraper/assets/50177367/b3855bb2-56b2-4211-bf16-1081514a1b2f"></img></p>

## How to setup

```sh
python -m setup
```

## How to run

```sh
python -m src.main

Enter Steam market game url  <<Ex. https://steamcommunity.com/market/search?appid=322330#p>>
<Your Url>
Enter desired page number
<Your desired page number>
Enter 0 or 1 for price descendant or ascendant, alternatively 2 for none
<Your desired price order>
Turning to page <X>
<Y> Items displayed
<i>: <Item name> <Quantity> $<Value> USD | After tax: $<Value>
```

## How to test

```sh
python -m unittest tests.test_main.Testmain
```

<p align="center"><img src="https://github.com/gappro/Steam-market-scraper/assets/50177367/e866f922-5309-49e0-9462-77deac98bfe7"></img></p>

## Meta

Gabriel – gabrielv.gonz@gmail.com

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

[https://github.com/gappro](https://github.com/gappro)
