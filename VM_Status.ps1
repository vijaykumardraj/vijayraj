echo "Status of VM on each nodes"
$i=1
while( $i -le 13 )
{
    if( $i -le 9 )
    {
    echo "**argdchv0$i"
    echo "***********"
    get-vm -ComputerName argdchv0$i
    }
    else
    {
    echo "**argdchv$i"
    echo "***********"
    get-vm -ComputerName argdchv$i
    }
    $i++
}

