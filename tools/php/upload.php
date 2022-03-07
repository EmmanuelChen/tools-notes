<?php
//$target_dir="/";
//$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);

if(isset($_POST["submit"])){
$name = $_FILES['file_upload']['name'];
//check for errors
    if($_FILES['file_upload']['error'] > 0) die('An error ocurred');
    
    //upload file
    if(!move_upload_file($_FILES['file_upload']['tmp_name']))
	die('Error uploading');

    die('File uploaded successfully.');    

}?>


<html>
   <body>

      <form action="" method="POST" enctype="multipart/form-data">
         <input type="file" name="image" />
         <input type="submit"/>
      </form>

   </body>
</html>
