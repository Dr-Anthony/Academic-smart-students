const boxes = document.querySelectorAll(".welcome-box");
boxes.forEach(box => {
  box.addEventListener("mousemove", e => {
    const rect = box.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const rotateX = -(y - centerY) / 20;
    const rotateY = (x - centerX) / 20;
    box.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.05)`;
  });
  box.addEventListener("mouseleave", () => {
    box.style.transform = "rotateX(0deg) rotateY(0deg) scale(1)";
  });
});