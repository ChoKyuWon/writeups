In zip file, it contain 3 file with smali extend. It can easily convert to java bytecode.  
In ```MainActivity$1.smali```, I can find main logic of username and password.

```
.line 70
const-string v1, "m&m"

invoke-virtual {p1, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

move-result p1
```
we can find username on this code.  
  

Analyze bytecode, password is like this:
```java
array = ["84", "5", "2", "f8eb53473", "4", "2efb3d", "f", "82df"]
secret = String.join("a", array).replaceAll('8', '0');
if(String.compare(secret, md5(inputpassword)) == true){
    pass()
}
```
so secret hash is ```04a5a2af0eb53473a4a2efb3dafa02df```. I tried to decrypt it on (https://www.md5online.org/md5-decrypt.html) and (https://md5.gromweb.com/), but they also can't decrypt it during CTF on held. While I use ```hashcat```, CTF is over.  
After CTF, I use md5online.org again, and then I get a result. but md5.gromweb.com isn't work yet.  
Anyway, flag is :```infernoCTF{m&m:mockingbird78209}```