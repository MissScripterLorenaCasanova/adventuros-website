<?php
include "../../UserManager/include.php";

$STH = $UMDB->prepare ("INSERT INTO game_tracking (ip, date, game_id ) VALUES (?, ?, ?)"); 
$STH->execute(array($_SERVER['REMOTE_ADDR'], date('Y-m-d H:i:s'), $_GET['image_id']));

header("Location: http://adventuros.evelend.com/images/main-menu-banner/spr_menu_image.png");