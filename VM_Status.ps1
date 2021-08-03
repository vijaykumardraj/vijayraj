#Invoke-Command -ComputerName PTYlkitb28 {get-vm | measure-vm }
#get-vm | Enable-VMResourceMetering
#get-vm -ComputerName PTYdchv13 | Measure-VM
echo "Status of VM on each nodes"
$i=1
while( $i -le 13 )
{
    if( $i -le 9 )
    {
    echo "**PTYdchv0$i"
    echo "***********"
    get-vm -ComputerName PTYdchv0$i
    }
    else
    {
    echo "**PTYdchv$i"
    echo "***********"
    get-vm -ComputerName PTYdchv$i
    }
    $i++
}

