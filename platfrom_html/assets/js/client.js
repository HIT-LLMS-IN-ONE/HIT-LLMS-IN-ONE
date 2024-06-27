function generateRandomCodeFromLocalTime(length = 6
) {
    let randomCode = '';
    // 生成指定长度的随机数
    while (randomCode.length < length) {
        randomCode += Math.floor(Math.random() * 256); // 生成0到255之间的随机整数
    }
    // 截取指定长度的随机值
    randomCode = randomCode.slice(0, length);
    return randomCode;
}



async function createUser() {
    const username = document.getElementById('newUsername').value;
    const password = document.getElementById('newUserPassword').value;
    const password2 = document.getElementById('newUserPassword1').value;
    if(password!==password2){
        alert("两次输入的密码不一样")
    }
    else{
        const hash1 = CryptoJS.SHA256(username+password);
        const hash1Hex = hash1.toString(CryptoJS.enc.Hex);
    
        const response = await fetch('http://43.138.154.160:8081/create_user', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, hash1Hex })
        });
    
        if (response.ok) {
            alert('User created successfully.');
        } else {
            const data = await response.json();
            alert(data.error || 'Failed to create user.');
        }
    }
}

async function authenticateUser() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const authCode = generateRandomCodeFromLocalTime();
//    console.log(authCode)

    const hash1 = CryptoJS.SHA256(username+password);
    const hash1Hex = hash1.toString(CryptoJS.enc.Hex);
    const hash2 = CryptoJS.SHA256(hash1Hex+authCode);
    const hash2Hex = hash2.toString(CryptoJS.enc.Hex);


    const response = await fetch('http://43.138.154.160:8081/authenticate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, hash2Hex, auth_code: authCode })
    });

    if (response.ok) {
        const data = await response.json();
        //base64
        const encryptedAuthCode = data.encrypted_auth_code;

        var decryptedData = aesDecrypt(encryptedAuthCode, hash1Hex);

        var rawData = atob(decryptedData);

        var hexString = '';
        for (var i = 0; i < rawData.length; i++) {
            var hex = rawData.charCodeAt(i).toString(16);
            hexString += (hex.length === 2 ? hex : '0' + hex);
        }
//        console.log(hexString)
        var num1 = parseInt(hexString, 16);
        var num2 = parseInt(authCode, 16);
//        console.log(num1)
//        console.log(num2)
        if(num1==num2)
        {
            window.location.href = 'chatgpt.html?username=' + encodeURIComponent(username);
            var data_out = hash1Hex
            // 将后端返回的值转换为Blob对象
            // 创建一个URL对象，该URL指向Blob对象
            var blob = new Blob([data_out], { type: 'text/plain;charset=utf-8' });
            // 创建一个指向该Blob对象的URL
            var url = URL.createObjectURL(blob);

            // 创建一个新的a标签
            var link = document.createElement('a');
            link.href = url;

            // 设置下载文件的名称
            link.download = 'filename.txt';

            // 触发点击事件，开始下载文件
            document.body.appendChild(link);
            link.click();

            // 清理，移除创建的a标签和Blob URL
            document.body.removeChild(link);
            URL.revokeObjectURL(url);
        }
        else{
            alert('Wrong sever!');
        }

        //alert('Authentication successful. Auth code: ' + encryptedAuthCode);
    } else {
        alert('Authentication failed.');
    }
}

async function changePassword() {
    const username = document.getElementById('username_to').value;
    const oldPassword = document.getElementById('newPassword0').value;
    const newPassword = document.getElementById('newPassword1').value;

    if(oldPassword!=newPassword){
        alert("两次输入不一致");
    }
    else{
        const hash1 = CryptoJS.SHA256(username+newPassword);
        const hash1Hex = hash1.toString(CryptoJS.enc.Hex);
    
        const response = await fetch('http://43.138.154.160:8081/change_password', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, hash1Hex })
        });
    
        if (response.ok) {
            alert('Password changed successfully.');
            var data_out = hash1Hex
                // 将后端返回的值转换为Blob对象
                // 创建一个URL对象，该URL指向Blob对象
            var blob = new Blob([data_out], { type: 'text/plain;charset=utf-8' });
                // 创建一个指向该Blob对象的URL
            var url = URL.createObjectURL(blob);
    
                // 创建一个新的a标签
            var link = document.createElement('a');
            link.href = url;
    
                // 设置下载文件的名称
            link.download = 'filename.txt';
    
                // 触发点击事件，开始下载文件
            document.body.appendChild(link);
            link.click();
    
                // 清理，移除创建的a标签和Blob URL
            document.body.removeChild(link);
            URL.revokeObjectURL(url);
        } else {
            alert('Failed to change password.');
        }
    }
}



function aesDecrypt(encryptedData, keyHex) {
    // 将 Base64 编码的密文转换为 WordArray
    var ciphertext = CryptoJS.enc.Base64.parse(encryptedData);

    // 将十六进制密钥转换为 WordArray
    var key = CryptoJS.enc.Hex.parse(keyHex);

    // 使用 AES 解密
    var decrypted = CryptoJS.AES.decrypt({ ciphertext: ciphertext }, key, {
        mode: CryptoJS.mode.ECB, // ECB 模式
        padding: CryptoJS.pad.Pkcs7 // PKCS7 填充
    });

    // 返回解密后的字符串
    return decrypted.toString(CryptoJS.enc.Base64);
}


function aesEncrypt(plainText, keyHex) {
    // 将明文转换为 WordArray
    var plaintext = CryptoJS.enc.Utf8.parse(plainText);

    // 将十六进制密钥转换为 WordArray
    var key = CryptoJS.enc.Hex.parse(keyHex);

    // 使用 AES 加密
    var encrypted = CryptoJS.AES.encrypt(plaintext, key, {
        mode: CryptoJS.mode.ECB, // ECB 模式
        padding: CryptoJS.pad.Pkcs7 // PKCS7 填充
    });

    // 将密文转换为 Base64 字符串并返回
    return encrypted.ciphertext.toString(CryptoJS.enc.Base64);
}




