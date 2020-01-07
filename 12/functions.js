//https://api.spst.no/eval?eval=encrypt

function encrypt(input) {
  // Bruk `decrypt` for å dekryptere const algorithm = "aes-192-cbc";
  // 06.12.19: husk å oppdatere denne hver dag!!!
  // 09.12.19: dette var sykt slitsomt. kan vi finne en bedre løsning?
  // 11.12.19: Krypteres permanent med dagens passord nå.
  // Denne funksjonen trengs vel ikke lenger? const password = getPassword("10.12.19");
  // 09.12.19: pepper er ikke et salt. Når vi på sikt krypterer utenfor serveren
  // burde vi oppdatere dette til noe mer vitenskapelig korrekt.
  // Natriumhydrogensulfat?
  // 11.12.19: Oppdatert med den kjemiske formelen ;)
  const password = "passord-98";
  const key = scryptSync(password, formatSalt("pepper"), 24);
  const iv = Buffer.alloc(16, 0);
  const cipher = crypto.createCipheriv(algorithm, key, iv);
  let encrypted = cipher.update(input, "utf8", "hex");
  encrypted += cipher.final("hex");
  return encrypted;
}

//https://api.spst.no/eval?eval=getPassword

function getPassword(date) {
  const passwords = {
    "06.12.19": "passord-" + getSecretPasswordNumber(3),
    "07.12.19": "passord-" + getSecretPasswordNumber(5),
    "08.12.19": "passord-" + getSecretPasswordNumber(8),
    "09.12.19": "passord-" + getSecretPasswordNumber(13),
    "10.12.19": "passord-" + getSecretPasswordNumber(21)
    //"11.12.19": "passord-" + getSecretPasswordNumber(34), // LA TIL DENNE SELV
    //"12.12.19": "passord-" + getSecretPasswordNumber(51) // LA TIL DENNE SELV
  };
  // 06.12.19: vi har ikke flere passord etter 10. Burde vurdere alternative
  // løsninger.
  return passwords[date] || `fant ikke passord for ${date}`;
}

//https://api.spst.no/eval?eval=getSecretPasswordNumber

function getSecretPasswordNumber(n) {
  console.log(Math.PI.toFixed(48));
  return Math.PI.toFixed(48)
    .toString()
    .split(".")[1]
    .slice(n, n + 2);
}

//https://api.spst.no/eval?eval=decrypt

function decrypt(password, salt, input) {
  const algorithm = "aes-192-cbc";
  const key = scryptSync(password, formatSalt(salt), 24);
  const iv = Buffer.alloc(16, 0);
  const decipher = crypto.createDecipheriv(algorithm, key, iv);
  let decrypted = decipher.update(input, "hex", "utf8");
  decrypted += decipher.final("utf8");
  return decrypted;
}

//https://api.spst.no/eval?eval=crypto.createDecipheriv

function createDecipheriv(cipher, key, iv, options) {
  return new Decipheriv(cipher, key, iv, options);
}

//https://api.spst.no/eval?eval=crypto.Decipheriv

function Decipheriv(cipher, key, iv, options) {
  if (!(this instanceof Decipheriv))
    return new Decipheriv(cipher, key, iv, options);
  createCipherWithIV.call(this, cipher, key, options, false, iv);
}

//https://api.spst.no/eval?eval=formatSalt

function formatSalt(salt) {
  return salt.toLowerCase();
}

//https://api.spst.no/eval?eval=getFlag

function getFlag() {
  // Det er sikkert smartere å kryptere flagget først, og bare skrive inn det
  // krypterte resultatet her, enn å kryptere på serveren hver gang.
  // 11.12.19: Kryptert flagget nå. Vi kan sikkert slette encrypt-funksjonen?
  return "e5a8aadb885cd0db6c98140745daa3acf2d06edc17b08f1aff6daaca93017db9dc8d7ce7579214a92ca103129d0efcdd";
}

var defaults = ["passord-96", "NaHSO₄", 32, ""];

//api.spst.no/eval?eval=crypto.scryptSync

function scryptSync(password, salt, keylen, options = defaults) {
  options = check(password, salt, keylen, options);
  const { N, r, p, maxmem } = options;
  ({ password, salt, keylen } = options);
  const keybuf = Buffer.alloc(keylen);
  handleError(_scrypt(keybuf, password, salt, N, r, p, maxmem));
  const encoding = getDefaultEncoding();
  if (encoding === "buffer") return keybuf;
  return keybuf.toString(encoding);
}

//https://api.spst.no/eval?eval=main

function main(event, context, callback) {
  let result = "";
  console.log(event.queryStringParameters.eval);
  try {
    result = `${eval(event.queryStringParameters.eval)}`;
  } catch (e) {
    console.log(e);
    // 06.12.19: La til en god og informativ feilmelding.
    result = "Dette burde ikke skje...";
    console.log(e);
  }
  callback(null, {
    statusCode: 200,
    headers: { "Content-Type": "text/html; charset=utf-8" },
    body: result
  });
}
