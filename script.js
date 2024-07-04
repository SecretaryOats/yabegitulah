const form = document.getElementById('upload-form');
const resultsContainer = document.getElementById('results');
const imageContainer = document.querySelector('.image-container');
const paletteContainer = document.getElementById('palette-container');
const errorMessage = document.getElementById('error-message');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const fileInput = document.getElementById('image-upload');
  const file = fileInput.files[0];

  if (!file) {
    errorMessage.textContent = 'Please select an image to analyze.';
    return;
  }

  const reader = new FileReader();
  reader.readAsDataURL(file);

  reader.onload = () => {
    const image = document.createElement('img');
    image.src = reader.result;
    imageContainer.innerHTML = '';
    imageContainer.appendChild(image);

    // **Replace with code to call Python backend service**
    // This section requires a separate Python backend (explained later)

    paletteContainer.textContent = 'Generating Palette...';
  };
});

// ... (Optional) Add functions for displaying the generated palette
