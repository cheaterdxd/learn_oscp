# information gathering

source: <http://e-learning.ptithcm.edu.vn/>  
ilias version: 5.4.20

error in:  
Fatal error: Allowed memory size of 536870912 bytes exhausted (tried to allocate 262144 bytes) in C:\xampp\htdocs\ILIAS-5.4.20\Services\UICore\classes\class.ilCtrl.php on line 675

Fatal error: Allowed memory size of 536870912 bytes exhausted (tried to allocate 262144 bytes) in C:\xampp\htdocs\ILIAS-5.4.20\libs\composer\vendor\composer\ClassLoader.php on line 321

## code understanding  

getcmd()  
Parameters:
    $cmd = $_get[cmd]  
    if $post[cmd] == post
        đâs  
