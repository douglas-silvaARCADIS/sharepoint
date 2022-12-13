import requests
from shareplum import Office365
#from config import config

#Informações de configuração

username = ""
password = ""
path_name = 'https://arcadiso365.sharepoint.com'
site_name = "s"
link  = "https://arcadiso365.sharepoint.com/teams/BancodeLaudosBRU/Lists/Conexao_teste"

authcookie = Office365(path_name,username=username,password=password).GetCookies()
session = requests.Session()
session.cookies = authcookie


