<#
 .Synopsis
  黑沙美服汉化文本工具:Download Function  . Reference
   https://stackoverflow.com/questions/21422364/is-there-any-way-to-monitor-the-progress-of-a-download-using-a-webclient-object
    .NOTES   Author: Sasulaw@CnHope
   DateLastModified: 20200314   资源均参考和来自于互联网
#>

function Download($url, $targetFile)
{
$uri = New-Object "System.Uri" "$url"
$request = [System.Net.HttpWebRequest]::Create($uri)
$request.set_Timeout(15000) #15 second timeout
$response = $request.GetResponse()
$totalLength = [System.Math]::Floor($response.get_ContentLength()/1024)
$responseStream = $response.GetResponseStream()
$targetStream = New-Object -TypeName System.IO.FileStream -ArgumentList $targetFile, Create
$buffer = new-object byte[] 10KB
$count = $responseStream.Read($buffer,0,$buffer.length)
$downloadedBytes = $count
while ($count -gt 0)
{
$targetStream.Write($buffer, 0, $count)
$count = $responseStream.Read($buffer,0,$buffer.length)
$downloadedBytes = $downloadedBytes + $count
Write-Progress -activity "Downloading file '$($url.split('/') | Select -Last 1)'" -status "Downloaded ($([System.Math]::Floor($downloadedBytes/1024))K of $($totalLength)K): " -PercentComplete ((([System.Math]::Floor($downloadedBytes/1024)) / $totalLength)  * 100)
}

Write-Progress -activity "Finished downloading file '$($url.split('/') | Select -Last 1)'"
$targetStream.Flush()
$targetStream.Close()
$targetStream.Dispose()
$responseStream.Dispose()
}