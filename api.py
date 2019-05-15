from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib

url = 'http://data.ex.co.kr/exopenapi/basicinfo/unitList'

queryParams = '?' + urlencode({quote_plus('serviceKey'): 'jx47RZYuJ02uCX32k0F2lGNTNDaeJ5duKCZrZwGN35dtEFOZhUbTym2166srj5fAf6ZvVonNqjMzIgS%2Bdx03dA%3D%3D',
                              quote_plus('type'): 'xml'
                             })

request = urllib.request.Request(url + unquote(queryParams))
print ('Your Request:\n' + url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print ('Your Request:\n'+url+queryParams)
print ("\nResult:")
print (response_body)
print ("\nDataType of Result Data:")
print (type(response_body))
filename = "mise.xml"
f = open(filename, "wb")
f.write(response_body)
f.close()