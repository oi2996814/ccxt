import os
import sys

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

# ----------------------------------------------------------------------------

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

# ----------------------------------------------------------------------------
import asyncio
import ccxt.async_support as ccxt  # noqa: E402


# AUTO-TRANSPILE #
async def example_1():
    my_ex = ccxt.kucoin()
    my_ex.proxy_url = 'https://cors-anywhere.herokuapp.com/'  # It prepends redirect url to requests, so requests leads to call url i.e.: https://cors-anywhere.herokuapp.com/?https://target_url.com . It might be useful for simple redirection or CORS bypassing purposes (Note, this will not work for websocket connections, but only for REST calls).
    print(await my_ex.fetch('https://api.ipify.org/'))

    await my_ex.close()

async def example_2():
    my_ex = ccxt.kucoin()
    # choose "httpProxy" or "httpsProxy" depending on your proxy url protocol
    my_ex.https_proxy = 'http://51.83.140.52:11230'  # It sets a real proxy for communication, so calls are made directly to url https://target_url.com , but tunneled through a proxy server (Note, this might work for websocket connections too).
    print(await my_ex.fetch('https://api.ipify.org/'))

    await my_ex.close()

async def example_3():
    my_ex = ccxt.kucoin()
    my_ex.socks_proxy = 'socks5://127.0.0.1:1080'  # It is for socks5 or socks5h proxy (Note, this might work for websocket connections too).
    print(await my_ex.fetch('https://api.ipify.org/'))


# Note, you can use your callback (instead of string value).
#
#     myEx.proxyUrl = mycallback;
#
#  or (JS/PHP)
#
#     myEx.proxyUrl = function (url, method, headers, body) { return 'xyz'; }
#
# Note, in php you can also pass a callback's string with a qualified namespace/class name, i.e. '\yourNamesPace\yourFunction'
    await my_ex.close()

asyncio.run(example_1())
