<!DOCTYPE html>
<html>
<head>
    <title>PHP7 Hello World</title>
    <meta charset="utf-8" />
</head>
<body>
<h1>Hello World: apache/php</h1>
<?php
    $load = sys_getloadavg();
?>
    <ul>
        <li>Server time: <?php echo date("c") ?></li>
        <li>Server load: <?php echo $load[0]; ?></li>
    </ul>
</body>
</html>
