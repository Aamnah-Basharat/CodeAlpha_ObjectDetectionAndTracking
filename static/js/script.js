const video = document.getElementById("video-feed");
const startBtn = document.getElementById("start-btn");
const stopBtn = document.getElementById("stop-btn");
const cameraStatus = document.getElementById("camera-status");
const toast = document.getElementById("toast");

// video start
startBtn.addEventListener("click", async () => {
    await fetch("/start_camera");
    video.src = "/video_feed?" + new Date().getTime();
    cameraStatus.textContent = "Running";
    cameraStatus.style.color = "green";
    showToast("Camera Started");
    updateButtons(true);
});

// video stop
stopBtn.addEventListener("click", async () => {
    await fetch("/stop_camera");
    video.src = "";
    cameraStatus.textContent = "Stopped";
    cameraStatus.style.color = "red";
    showToast("Camera Stopped");
    updateButtons(false);
});

// toast function
function showToast(message) {
    toast.textContent = message;
    toast.classList.add("show");
    setTimeout(() => {
        toast.classList.remove("show");
    }, 2500);
}

function updateButtons(cameraRunning) {
    startBtn.disabled = cameraRunning;
    stopBtn.disabled = !cameraRunning;
}
updateButtons(false);

