import requests, re
from app import dao, app

# proxies = {
#   'http': 'http://10.10.1.10:3128',
# }
#
# requests.get('http://example.org', proxies=proxies,timeout=None)
# with app.app_context():
#     print(dao.check_user_name('haiphan'))
#     dao.delete_order(11)
so_lau = "1"
txt = "11102"

# x = re.findall("^{solau}.*".format(solau=so_lau), txt)
# print(x)
print(txt.startswith(so_lau))
