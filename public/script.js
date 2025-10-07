let userData = null;

// Get DOM elements
const button = document.getElementById("generateButton");
const input = document.getElementById("imagePrompt");

// Dynamic base URL based on environment
function getBaseUrl() {
    if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') {
       
        return 'http://localhost:5001/my-project-for-first-firebase/us-central1';
    } else {
        
        return '';
    }
}


function showSignupModal() {
    document.getElementById("signupModal").style.display = "block";
}

function closeSignupModal() {
    document.getElementById("signupModal").style.display = "none";
    document.getElementById("signupForm").reset();
    document.getElementById("signupMessage").style.display = "none";
}

window.showSignupModal = showSignupModal;
window.closeSignupModal = closeSignupModal;

document.getElementById("signupForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const messageDiv = document.getElementById("signupMessage");
    
    try {
        const baseUrl = getBaseUrl();
        const url = baseUrl ? `${baseUrl}/register_this_user` : '/register_this_user';
        
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                data: {
                    username: username,
                    password: password
                }
            })
        });
        
        const result = await response.json();
        
        if (result.error) {
            throw new Error(result.error.message);
        }
        
        
        messageDiv.textContent = "Account created successfully! You can now generate images.";
        messageDiv.className = "success";
        messageDiv.style.display = "block";
        
        
        userData = { userId: result.result.uid };
        
        
        setTimeout(() => {
            closeSignupModal();
        }, 2000);
        
    } catch (error) {
       
        messageDiv.textContent = error.message || "Error creating account. Please try again.";
        messageDiv.className = "error";
        messageDiv.style.display = "block";
    }
});

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById("signupModal");
    if (event.target == modal) {
        closeSignupModal();
    }
}

window.addEventListener('DOMContentLoaded', () => {
    showSignupModal();
});


async function generateImage() {
    const prompt = input.value.trim();
    const style = document.getElementById("styleChoice").value;
    
    if (!prompt) {
        alert("Please enter something!");
        return;
    }
    
    if (!userData) {
        alert("Please sign up first!");
        showSignupModal();
        return;
    }

    try {
        const baseUrl = getBaseUrl();
        const url = baseUrl ? `${baseUrl}/create_fake_image_url` : '/create_fake_image_url';
        
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                data: {
                    uid: userData.userId,
                    imagePrompt: prompt,
                    style: style
                }
            })
        });

        const result = await response.json();
        
        if (result.error) {
            throw new Error(result.error.message);
        }

        const imageUrl = result.result.imageUrl;
        document.getElementById("fakeurl").textContent = imageUrl;
    } catch (error) {
        console.error("Error:", error);
        alert("Error generating image: " + (error.message || "Please try again."));
    }
}

window.generateImage = generateImage;
        
       