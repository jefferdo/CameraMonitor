$id = (Get-PnpDevice -Class 'camera' -Status ok | Get-PnpDeviceProperty -KeyName "DEVPKEY_Device_PDOName").data
echo $id
