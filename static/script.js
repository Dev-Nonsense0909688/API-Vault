const password = document.getElementById("password");
const sig = document.getElementById("signal");

function success() {
  window.location.href = "/dashboard";
}

function fail() {
  password.style.borderColor = "var(--danger)";
  password.style.boxShadow = "0 0 0 .2rem rgba(239,68,68,.15)";
  sig.innerText = res.message || "Invalid password.";

  setTimeout(() => {
    sig.innerText = "";
    pass.style.borderColor = "";
    pass.style.boxShadow = "";
  }, 700);
}

async function login(event) {
  event.preventDefault();

  const req = await fetch("/api/v1/sessions/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      password: password.value,
    }),
  });

  const res = await req.json();

  if (res.success) success();
  else fail();
}
