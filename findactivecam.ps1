while ($true) {
    $value = .\Listdlls64.exe "svchost.exe" | findstr.exe "FrameServer"
    cls
    if ($value.length -ne 0) {
        echo "Active Camera Found"  
    }
    Start-Sleep -s 2
}
