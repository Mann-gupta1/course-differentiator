
<?php
$servername = "localhost"; 
$username = "root"; 
$password = "Guptaji@1234";
$database = "course_diffrentiator";

$conn = mysqli_connect($servername, $username, $password, $database);

$Email = $_POST["E-mail"];
$Password = $_POST["Pass-word"];

$sql = "SELECT `email`,`password`,`username` FROM signup";
$result = mysqli_query($conn, $sql);
if($_POST["log-in"]){
    if(mysqli_num_rows($result) > 0){
        $flag = 0;
        while($row = mysqli_fetch_assoc($result)) {
            if($row["email"] == $Email && $row["password"] == $Password){
                include 'main.html';
                
                $username = $row["username"]; 
                echo '<script>
                var x = document.getElementById("navlogin");
                x.innerHTML = "'.$username.'"; 
                x.style.color="white";
                var y = document.getElementById("profilename");
                y.innerHTML = "'.$username.'";
                var logo = document.createElement("img"); 
                logo.src = "avatar/avatar1.png"; 
                logo.width=40;
                logo.height=40;
                logo.style.display="inline-block";
                x.appendChild(logo); 
                x.onmouseenter = function (){showMenu();};
                x.onmouseleave = function (){hideMenu();};
                x.onclick = function (){showonclick();};
                var y = document.getElementById("hideable");
                y.onmouseleave = function (){hideMenu();};
                function showMenu() {
                    var div = document.getElementById("hideable");
                    div.style.display = "block";
                }
        
                function hideMenu() {
                    var div = document.getElementById("hideable");
                    div.style.display = "none";
                    x.onmouseleave = function (){hideMenu();};
                }
                function showonclick(){
                    x.onmouseleave = function (){};
                    var div = document.getElementById("hideable");
                    div.style.display = "block";
                }
                var centerLogin = document.getElementById("center-login");
                centerLogin.style.display = "none";
            </script>';
                echo '<script> alert("You are loggedin")</script>';
                $flag = 1;
                break;
            }
            // if($row["email"] != $Email && $row["password"] == $Password){
            //     echo '<script>alert("Email is not correct")</script>';
            //     include 'login.html';
            //     $flag = 0;
            // }
            // if($row["email"] == $Email && $row["password"] != $Password){
            //     echo '<script>alert("Password is not correct")</script>';
            //     include 'login.html';
            //     $flag = 0;
            // }
        }
        if($flag == 0){
            echo '<script>alert("Email or password is not correct")</script>';
            include 'login.html';
        }
        if($flag == 0){
            echo '<script>alert("Singup to continue")</script>';
            // include 'login.html';
        }
    }
    else{
        echo '<script>alert("Please Singup")</script>';
        include 'login.html/#container';
    }
}


?>
