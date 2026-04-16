function login() {
  const username = document.getElementById("username").value
  const senha = document.getElementById("senha").value
  const email = document.getElementById("email").value

  console.log("Username:", username)
  console.log("Senha:", senha)
  console.log("Email:", email)

  fetch("http://127.0.0.1:8000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ username, senha, email })
  })
  .then(res => res.json())
  .then(data => {
    if (data.user_id) {
      localStorage.setItem("usuario_id", data.user_id)
      window.location.href = "app.html"
    } else {
      alert("Login inválido")
    }
  })
}