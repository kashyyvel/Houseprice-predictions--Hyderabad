<?php

$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "usnm";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $username = $_POST["username"];
    $password = $_POST["password"];
    
    $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
    
    $result = $conn->query($sql);
    
    if ($result->num_rows > 0) {
        header("Location: welcome.php");
        exit();
    } else {
        $error = "Invalid username or password";
    }
}

?>
