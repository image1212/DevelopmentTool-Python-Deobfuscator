import base64, codecs
import sys
sys.path.append("code")
import code as i
code = (base64.b64decode(i.trust),'<string>','exec')
print(code[0].decode("utf-8"))