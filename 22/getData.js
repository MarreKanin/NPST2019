fetch("/8a2a8e12017977d9dbf0ed33e254e94e.txt", {
  headers: { "X-Access-Code": document.querySelector("input").value }
})
  .then(response => response.text())
  .then(text => (document.querySelector("#output").innerHTML = text))
  .then(fetch("/8a2a8e12017977d9dbf0ed33e254e94e.txt", {
    headers: { "X-Access-Code": document.querySelector("input").value }
  })
    .then(response => response.text())
    .then(text => (document.querySelector("#output").innerHTML = text))
    .then(response => (
      console.log(response))
    );
