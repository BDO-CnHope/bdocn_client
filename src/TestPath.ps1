<#
 .Synopsis
  黑沙美服汉化文本工具
    .NOTES   Author: Sasulaw@CnHope
   DateLastModified: 20200314   资源均参考和来自于互联网
#>$font="prestringtable\font"$ads="ads"

# Test Path
function TestPath
{
$tsfont = Test-Path $font
if ( $tsfont -eq "True" )
{
Out-Null
}
else
{
mkdir -Force $font | Out-Null
}
$tsads = Test-Path $ads
if ( $tsads -eq "True" )
{
Out-Null
}
else
{
mkdir $ads | Out-Null
}
}