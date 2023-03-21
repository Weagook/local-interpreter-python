function runCode() {
    const code = document.getElementById("codeInput").value;
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        const response = xhr.responseText;
        document.getElementById("output").textContent = response;
      }
    }
    
    xhr.open
    ("POST", "/run-python-code");
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.send(JSON.stringify({ code }));
    } 