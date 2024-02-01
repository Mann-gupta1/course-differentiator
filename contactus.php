<?php
$servername = "localhost"; 
$username = "root"; 
$password = "Guptaji@1234";
$database = "course_diffrentiator";


$conn = mysqli_connect($servername, $username, $password, $database);
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';
// Check connection
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  exit();
}

$Firstname = mysqli_real_escape_string($conn, $_POST["firstname"]);
$Lastname = mysqli_real_escape_string($conn, $_POST["lastname"]); 
$Email = mysqli_real_escape_string($conn, $_POST["email"]);
$Message = mysqli_real_escape_string($conn, $_POST["message"]); 

$sql = "INSERT INTO contactus(`firstname`, `lastname`, `email`, `message`) VALUES(?, ?, ?, ?)";
$stmt = mysqli_prepare($conn, $sql);
mysqli_stmt_bind_param($stmt, "ssss", $Firstname, $Lastname, $Email, $Message);
$result = mysqli_stmt_execute($stmt);

if ($result) {
  include 'main.html';
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
        $mail->Body    = 'Thanks for Contacting <b>Course Differentiator</b><br> your message <i>' . $Message .'</i> has been recevied. to our team';
        $mail->send();
        echo '<script>alert("Check Email");</script>';
    } catch (Exception $e) {
        echo "<script>alert('Email could not be sent. to $Email');</script>";
    }
  
  
} else {
  echo '<script>alert("Something went wrong");</script>';
}
mysqli_close($conn);


// $to="$Email";
// $subject ="Signup";
// $message="Greet from Course Differentiator ,Hello you has been signed up succesfully !!
// Thanks pro joining with us ";
// $header=" from : manngupta923@gmail.com";


    // ===========================================mail sent======================================
    //Create an instance; passing `true` enables exceptions

?>