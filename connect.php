<?php
$servername = "localhost"; 
$username = "root"; 
$password = "Guptaji@1234";
$database = "course_diffrentiator";

$conn = mysqli_connect($servername, $username, $password, $database);

$Name = $_POST["name"];
$Username = $_POST["username"]; 
$Email = $_POST["email"];
$Password = $_POST["password"]; 
// ============================================mail function====================================================
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';


    //prompt function
    // function prompt($prompt_msg){
    //     echo("<script type='Number/javascript'> var answer = prompt('".$prompt_msg."'); </script>");

    //     $answer = "<script type='Number/javascript'> document.write(answer); </script>";
    //     return($answer);
    // }

    // //program
    // $prompt_msg = "Please type your name.";
    // $name = prompt($prompt_msg);

    // $output_msg = "Hello there ".$name."!";
    // echo($output_msg);

    // ===========================================mail sent======================================
    //Create an instance; passing `true` enables exceptions

$mail = new PHPMailer(true);

    try {
        //Server settings
        // $mail->SMTPDebug = SMTP::DEBUG_SERVER;                      //Enable verbose debug output
        $mail->isSMTP();                                            //Send using SMTP
        $mail->Host       = 'smtp.gmail.com';                     //Set the SMTP server to send through
        $mail->SMTPAuth   = true;                                   //Enable SMTP authentication
        $mail->Username   = 'manngupta923@gmail.com';                     //SMTP username
        $mail->Password   = 'alarkzbiokzunnki';                               //SMTP password
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;            //Enable implicit TLS encryption
        $mail->Port       = 465;                                    //TCP port to connect to; use 587 if you have set `SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS`
    
        //Recipients
        $mail->setFrom('manngupta923@gmail.com', 'Course Differentiator');
        $mail->addAddress($Email, $Username);     //Add a recipient
        
        //Content
        $mail->isHTML(true);                                  //Set email format to HTML
        $mail->Subject = 'Welcome to Course differentiator';
        $mail->Body    = 'Greeting  <br> Thanks for Joining with us <b>Course Differentiator</b>';
        $mail->send();
        echo '<script>alert("Check mail");</script>';
            $sql = "INSERT INTO signup(`Name`, `username`, `email`, `password`) VALUES('$Name', '$Username', '$Email', '$Password')";
            $result = mysqli_query($conn, $sql);
        if($result){
             include 'login.html';
        }

    } catch (Exception $e) {
        echo "<script>alert('Email could not be sent. to $Email');</script>";
    }
    
?>