
import pickle
import sys

techacademy = "https://search.yahoo.co.jp/search?p="
with open('url.DAT', 'wb') as web:
  pickle.dump(techacademy , web)

techacademy1 = 1
with open('CONFIG.DAT', 'wb') as web1:
  pickle.dump(techacademy1 , web1)

sys.exit()