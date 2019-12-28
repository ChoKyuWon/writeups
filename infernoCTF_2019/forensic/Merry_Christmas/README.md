We get encrypted zip file, and the hint : ```Hint: What is mrT4ntr4's last name?```  
I google it, and password is ```Malhotra```.  
Then, flag.gif is come but it dose not readable by any gid reader.  
At first, I think password is wrong and tried many variable of ```Malhotra```.  
But I open the flag.gif in hex vewier, I can see the readable text, ```NETSCAPE 2.0```.  
I google it again, and this is extension of gif file.  
The hex value of file is like this:
```
41 41 41 41 41 61 53 04 69 00 E7 FB 00 32 00 00 AAAAAaS.i.çû.2..
38 00 02 3B 00 00 41 00 03 43 00 00 49 00 03 4D 8.;..A..C..I..M
00 00 56 00 00 50 02 00 60 00 00 5C 04 00 6A 00 ..V..P..`..\..j.
```
Replace ```41 41 41 41 41``` to ```47 49 46 38 39```, we can read the file. 
flag is ```infernoCTF{M3RRy_ChR1stmAs}```.