#Invoke-Command -ComputerName PTYlkitb28 {get-vm | measure-vm }
#get-vm | Enable-VMResourceMetering
#get-vm -ComputerName PTYdchv13 | Measure-VM
try {write-host "in try"
throw {write-host "this in try after error caught"
write-host "try....."}
}
catch{ throw }

finally {
echo "Status of VM on each nodes"
$i=1
while( $i -le 13 )
{
    if( $i -le 9 )
    {
    echo "**PTYdchv0$i"
    echo "***********"
    #get-vm -ComputerName PTYdchv0$i
    }
    else
    {
    echo "**PTYdchv$i"
    echo "***********"
    #get-vm -ComputerName PTYdchv$i
    }
    $i++
}

}