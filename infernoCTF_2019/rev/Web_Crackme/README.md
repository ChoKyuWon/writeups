In chrome developer tool, I can see it use WASM(WebAssembly.)  
The page's script is like this:
```js
const wabtCompiler = WabtModule();
async function loadText(url) {
    let response = await fetch(url, {cache: "no-cache"});
    let data = await response.text()
    return data;
}
    methods: {
        async selectExample(example) {
            const wat = await Promise.all(loadText(example + '/assembly.wat'));
            this.wat = wat;
            return 0;
        },
        async execute() {
			var key = document.getElementById('key').value;
			var stringFromKey = "";
			for (var i = 0; i < key.length; i++) {
  				stringFromKey+=key.charCodeAt(i).toString(16);
			}
            const parsedWat = wabtCompiler.parseWat("", this.wat);
            const buffer = parsedWat.toBinary({}).buffer;
            const wasmModule = await WebAssembly.compile(buffer);
            eval(this.js);
            return 0;
        }
    }
});
```
(it is just simplified version)  
It look get js and WASM in other url, so I capture the traffic by Fiddler4.  
I can see two request on ```/challenge/script.js``` and ```/challenge/assembly.wat```.  
In browser console, type this code:  
```js
async function loadText(url) {
    let response = await fetch(url, {cache: "no-cache"});
    let data = await response.text()
    return data;
}
const [wat, js] = await Promise.all([
                loadText('/challenge/assembly.wat'),
                loadText('/challenge/script.js'),
]);
```
and you can read wat and js.  
wasm code is like this:
```wasm
(module
  (memory 1)
  (func $myFunction1 (result i32)
    (i32.store
      (i32.const 0)
      (i32.const 0xd359beef) 
    )
    (i32.store
      (i32.const 3)
      (i32.const 0x5579) 
    )
	(i32.store
	  (i32.const 5)
	  (i32.const 0x66) 
	)
    (i32.load
      (i32.const 2)
    )
  )

  (func $myFunction2 (result i32)
    (i32.store
      (i32.const 0)
      (i32.const 0xc939ba2d) 
    )
    (i32.store
      (i32.const 3)
      (i32.const 0x7165) 
    )
	(i32.store16
	  (i32.const 4)
	  (i32.const 0x2D4D) 
	)
    (i32.load
      (i32.const 2)
    )
  )
  (export "myFunction1" (func $myFunction1))
  (export "myFunction2" (func $myFunction2))
)
```
Some value is hardcoded on wasm, and script.js compare the value and input.  
Analyze the wasm code is one way to know the value, but I use browser console.  
```js
const wabtCompiler = WabtModule();
async function loadText(url) {
    let response = await fetch(url, {cache: "no-cache"});
    let data = await response.text()
    return data;
}
const [wat, js] = await Promise.all([
                loadText('/challenge/assembly.wat'),
                loadText('/challenge/script.js'),
]);
const parsedWat = wabtCompiler.parseWat("", this.wat);
const buffer = parsedWat.toBinary({}).buffer;
const wasmModule = await WebAssembly.compile(buffer);
const wasmInstance = new WebAssembly.Instance(wasmModule, {});
const { myFunction1,myFunction2 } = wasmInstance.exports;

let res1 = myFunction1().toString(16);
let res2 = myFunction2().toString(16);
```
Now res1 + res2 is the value, ```665579592d4d6539```.  
To conver it to string, flag is ```infernoCTF{fUyY-Me9}```.