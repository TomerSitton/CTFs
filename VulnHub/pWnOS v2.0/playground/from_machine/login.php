HTTP/1.1 200 OK
Date: Sat, 15 May 2021 09:47:55 GMT
Server: Apache/2.2.17 (Ubuntu)
X-Powered-By: PHP/5.3.5-1ubuntu7
Vary: Accept-Encoding
Content-Length: 3102
Connection: close
Content-Type: text/html

<pre><?php # Script 16.8 - login.php
// This is the login page for the site.

require_once ('includes/config.inc.php'); 
$page_title = 'Login';
include ('includes/header.html');

if (get_magic_quotes_gpc()) {
        $in = array(&$_GET, &$_POST, &$_COOKIE);
        while (list($k,$v) = each($in)) {
                foreach ($v as $key => $val) {
                        if (!is_array($val)) {
                                $in[$k][$key] = stripslashes($val);
                                continue;
                        }
                        $in[] =& $in[$k][$key];
                }
        }
        unset($in);
}



    if(!empty($_POST)) {
        require_once (MYSQL);
		
		// Validate the email address:
		if (!empty($_POST['email'])) {
			$e = $_POST['email'];
		} else {
			$e = FALSE;
			echo '<p class="error">You forgot to enter your email address!</p>';
		}		
		
		// Validate the password:
		if (!empty($_POST['pass'])) {
			$p = $_POST['pass'];
		} else {
			$p = FALSE;
			echo '<p class="error">You forgot to enter your password!</p>';
		}
		
		if ($e && $p) { // If everything's OK.
		
			// Query the database:
			$q = "SELECT * FROM users WHERE email='".$_POST['email']."' AND pass='".SHA1($_POST['pass'])."' AND active IS NULL";		
			$r = mysqli_query ($dbc, $q) or trigger_error("Query: $q\n<br />MySQL Error: " . mysqli_error($dbc));
		
			//echo $q;
			//echo $r;

	/*

	*/

	if($row = mysqli_fetch_assoc($r)) {    
            echo '<h1>Welcome '.htmlentities($row['email']).'</h1><br/>';
            echo 'Logging in...<br/>';
       //     exit;

		//if($e == "admin@admin.com") {

		if (preg_match( "/admin@isints.com/", $e )) {
		echo 'WAF: SQL Injection Attack Detected. Details Logged. Denying Session. Goodbye!<br/>';
		
		}

		exit();
/*
		if (@mysqli_num_rows($r) == 1) { // A match was made.

			// Register the values & redirect:
			$_SESSION = mysqli_fetch_array ($r, MYSQLI_ASSOC); 
			mysqli_free_result($r);
			mysqli_close($dbc);
							
			$url = BASE_URL . 'index.php'; // Define the URL:
			ob_end_clean(); // Delete the buffer.
			header("Location: $url");
			exit(); // Quit the script.
				
		} else { // No match was made.
			echo '<p class="error">Either the email address and password entered do not match those on file or you have not yet activated your account.</p>';
		}
*/

        } else {
            $error = "Login Failed!<br/>\n";
        }

	} else { // If everything wasn't OK.
		echo '<p class="error">Please try again.</p>';
	}
	



	mysqli_close($dbc);

} // End of SUBMIT conditional.
?>

<h1>Login</h1>
<p>Your browser must allow cookies in order to log in.</p>
<form action="login.php" method="post">
	<fieldset>
	<p><b>Email Address:</b> <input type="text" name="email" size="20" maxlength="40" /></p>
	<p><b>Password:</b> <input type="password" name="pass" size="20" maxlength="20" /></p>
	<div align="center"><input type="submit" name="submit" value="Login" /></div>
	<input type="hidden" name="submitted" value="TRUE" />
	</fieldset>
</form>

<?php // Include the HTML footer.
include ('includes/footer.html');
?>
</pre>
