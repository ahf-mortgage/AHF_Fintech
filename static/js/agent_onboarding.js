
const steps = document.querySelectorAll('.step-content');
const circles = document.querySelectorAll('.progress-circle');
const nextButtons = document.querySelectorAll('.btn-next');

let currentStep = 0;

nextButtons.forEach((button) => {
    button.addEventListener('click', () => {
        steps[currentStep].classList.remove('active');
        circles[currentStep].classList.remove('progress-active');
        circles[currentStep].classList.add('progress-completed');

        currentStep++;
        steps[currentStep].classList.add('active');
        circles[currentStep].classList.add('progress-active');
    });
});
