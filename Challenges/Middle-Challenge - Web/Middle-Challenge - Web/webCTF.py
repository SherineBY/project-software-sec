import base64
import os
import webbrowser

FLAG = b"CTF{Web_CTF_Challenge}"

def rot13(data: bytes) -> bytes:
    result = []
    for c in data:
        if 65 <= c <= 90:  # 'A'-'Z'
            c = ((c - 65 + 13) % 26) + 65
        elif 97 <= c <= 122:  # 'a'-'z'
            c = ((c - 97 + 13) % 26) + 97
        result.append(c)
    return bytes(result)


rot_flag = rot13(FLAG)

b64_flag = base64.b64encode(rot_flag)

hex_flag = b64_flag.hex().encode()

xor_key = 0x5A

xor_flag = bytes([b ^ xor_key for b in hex_flag])

js_array = ",".join(str(b) for b in xor_flag)  # Comma-separated ASCII values

html_content = f"""<!DOCTYPE html>
<html>
<head>
<title>Web Challenge</title>
</head>
<body>
<h1>Welcome to the Web CTF Challenge</h1>
<p>Analyze the page source and the JavaScript code to find the hidden FLAG.</p>

<script>
var arr = [{js_array}];

function obscureProcess(a) {{
    var key = 0x5A;
    for (var i = 0; i < a.length; i++) {{
        a[i] = a[i] ^ key;
    }}
    return a;
}}

function toStringFromBytes(a) {{
    var s = '';
    for (var i = 0; i < a.length; i++) {{
        s += String.fromCharCode(a[i]);
    }}
    return s;
}}

function hexToBytes(hexstr) {{
    var bytes = [];
    for (var i = 0; i < hexstr.length; i += 2) {{
        bytes.push(parseInt(hexstr.substr(i, 2), 16));
    }}
    return bytes;
}}

function base64Decode(str) {{
    return atob(str);
}}

function rot13(str) {{
    return str.replace(/[a-zA-Z]/g, function(c) {{
        var code = c.charCodeAt(0);
        var base = (code >= 97) ? 97 : 65;
        return String.fromCharCode(((code - base + 13) % 26) + base);
    }});
}}
</script>
</body>
</html>
"""


html_file = "CTFchallenge.html"
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

webbrowser.open(f"file://{os.path.abspath(html_file)}")
