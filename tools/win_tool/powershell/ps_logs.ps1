# This script gathers all the 
# TYPE System.Diagnostics.EventLogEntry#Windows Powershell/PowerShell/400
# It contains powershell commandlines

Get-EventLog -LogName 'Windows Powershell' | Export-CSV C:\Users\powershell-logs.csv
