document.getElementById('ask').addEventListener('keydown', function(event) {
    // 检查按下的键是否是回车键
    if (event.key === 'Enter') {
      // 执行按钮点击事件
      Usercreatediv();
      Gptget();
    }
  });
function Usercreatediv(){
    var chatContainer = document.createElement("div");
    chatContainer.className = "media";

    // 创建媒体体部分
    var mediaBody = document.createElement("div");
    mediaBody.className = "media-body reverse";

    // 创建聊天消息1
    var chatMsg = document.createElement("div");
    chatMsg.className = "chat-msg";

    var askdata = document.getElementById("ask");
    var paragraph = document.createElement("p");
    if(askdata.value.trim() === ""){
        return ;
    }
    paragraph.textContent = askdata.value;

    chatMsg.appendChild(paragraph);

    mediaBody.appendChild(chatMsg);

    // 将媒体体部分添加到父容器
    chatContainer.appendChild(mediaBody);

    // 创建媒体图片部分
    var mediaImg = document.createElement("div");
    mediaImg.className = "media-img";

    // 创建图片
    var img = document.createElement("img");
    img.src = "assets/images/users/user-8.jpg";
    img.alt = "user";
    img.className = "rounded-circle thumb-md";

    // 将图片添加到媒体图片部分
    mediaImg.appendChild(img);

    // 将媒体图片部分添加到父容器
    chatContainer.appendChild(mediaImg);

    document.getElementById("container").appendChild(chatContainer);

    chatContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    // var scrollContainer = document.querySelector('.chat-body');
    // scrollContainer.scrollTop = scrollContainer.scrollHeight;
}
function Gptget(){
    var askdata = document.getElementById("ask");
    var temp = askdata.value
    if(askdata.value.trim() === ""){
        return ;
    }
    askdata.value=''
    askdata.focus();
    const ask = {
        userask : temp,
    }
    fetch('http://43.138.154.160:8081/url',{
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
        },
        body: JSON.stringify(ask),
    })
        .then(response=>response.json())
        .then(data=>{
            var gptcontainer = document.createElement("div");
            gptcontainer.className = "media";

            var mediaImg = document.createElement("div");
            mediaImg.className = "media-img";

            var img = document.createElement("img");
            img.src = "assets/images/users/user-4.jpg";
            img.alt = "user";
            img.className = "rounded-circle thumb-md";

            mediaImg.appendChild(img);

            gptcontainer.appendChild(mediaImg);

            var mediaBody = document.createElement("div");
            mediaBody.className = "media-body";

            var chatMsg = document.createElement("div");
            chatMsg.className = "chat-msg";
            var paragraph = document.createElement("p");
            paragraph.innerHTML = marked.parse(data.message);
            chatMsg.appendChild(paragraph);
            mediaBody.appendChild(chatMsg);

            gptcontainer.appendChild(mediaBody);

            document.getElementById("container").appendChild(gptcontainer);

            gptcontainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
        })
        .catch(error=>{
            console.error('Error:',error);
        })
}

$(document).ready(function() {
    // 给所有带有 clickable 类的 span 元素添加点击事件监听器
    $(".clickable").click(function() {
        // 获取 span 元素的 data-content 属性值，即要发送的内容
        var content = $(this).data("content");  
        // 发送内容到后端

        var chatContainer = document.createElement("div");
        chatContainer.className = "media";

        // 创建媒体体部分
        var mediaBody = document.createElement("div");
        mediaBody.className = "media-body reverse";

        // 创建聊天消息1
        var chatMsg = document.createElement("div");
        chatMsg.className = "chat-msg";

        var paragraph = document.createElement("p");
        paragraph.textContent = content;

        chatMsg.appendChild(paragraph);

        mediaBody.appendChild(chatMsg);

        // 将媒体体部分添加到父容器
        chatContainer.appendChild(mediaBody);

        // 创建媒体图片部分
        var mediaImg = document.createElement("div");
        mediaImg.className = "media-img";

        // 创建图片
        var img = document.createElement("img");
        img.src = "assets/images/users/user-8.jpg";
        img.alt = "user";
        img.className = "rounded-circle thumb-md";

        // 将图片添加到媒体图片部分
        mediaImg.appendChild(img);

        // 将媒体图片部分添加到父容器
        chatContainer.appendChild(mediaImg);

        document.getElementById("container").appendChild(chatContainer);

        chatContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
        const ask = {
            userask : content,
        }
        fetch('http://43.138.154.160:8081/url',{
            method : 'POST',
            headers : {
                'Content-Type' : 'application/json',
            },
            body: JSON.stringify(ask),
        })
            .then(response=>response.json())
            .then(data=>{
                var gptcontainer = document.createElement("div");
                gptcontainer.className = "media";
    
                var mediaImg = document.createElement("div");
                mediaImg.className = "media-img";
    
                var img = document.createElement("img");
                img.src = "assets/images/users/user-8.jpg";
                img.alt = "user";
                img.className = "rounded-circle thumb-md";
    
                mediaImg.appendChild(img);
    
                gptcontainer.appendChild(mediaImg);
    
                var mediaBody = document.createElement("div");
                mediaBody.className = "media-body";
    
                var chatMsg = document.createElement("div");
                chatMsg.className = "chat-msg";
                var paragraph = document.createElement("p");
                paragraph.innerHTML = marked.parse(data.message);
                chatMsg.appendChild(paragraph);
                mediaBody.appendChild(chatMsg);
    
                gptcontainer.appendChild(mediaBody);
    
                document.getElementById("container").appendChild(gptcontainer);
    
                gptcontainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
            })
            .catch(error=>{
                console.error('Error:',error);
            })
    });
});
