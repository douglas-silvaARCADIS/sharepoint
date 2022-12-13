from shareplum import Site
from shareplum import Office365

authcookie = Office365('https://arcadiso365.sharepoint.com', username='douglas.silva@arcadislogos.com.br', password='Senha').GetCookies()
site = Site('https://arcadiso365.sharepoint.com/teams/BancodeLaudosBRU/Lists/', authcookie=authcookie)
sp_list = site.List('Conexao_teste')
data = sp_list.GetListItems('All Items', rowlimit=200)