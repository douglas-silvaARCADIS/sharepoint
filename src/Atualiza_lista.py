import win32com.client
import time

#cria a conexão
xlapp = win32com.client.DispatchEx("Excel.Application")
wb = xlapp.Workbooks.Open('C:\\Users\\douglas.silva\\Videos\\teste1.xlsx')
wb.RefreshAll()
xlapp.CalculateUnitlAsyncQueriesDone()
time.sleep(5)
xlapp.DisplayAlerts = False
wb.Save()
wb.Close()
xlapp.quit()