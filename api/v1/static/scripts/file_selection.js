const input = document.querySelector("input");
const preview = document.querySelector(".preview");

input.addEventListener("change", updateImageDisplay);

function updateImageDisplay() {
  while (preview.firstChild) {
    preview.removeChild(preview.firstChild);
  }

  const file = input.files[0];
  console.log(file);
  const text = document.createElement("p");
  if (file.length === 0) {
    text.textContent = "No file currently selected for upload";
    preview.appendChild(text);
  } else {
    if (validFileType(file)) {
      text.textContent = `File name: ${file.name}`;
    } else {
      text.textContent = `File name ${file.name}: Not a valid file type. Update your selection.`;
    }
    preview.appendChild(text);
  }
}

const fileTypes = ["image/png", "image/jpeg"];

function validFileType(file) {
  return fileTypes.includes(file.type);
}


const input2 = document.querySelector("input");
const preview2 = document.querySelector(".preview2");

input2.addEventListener("change", updateImageDisplay);

function updateImageDisplay() {
  while (preview2.firstChild) {
    preview2.removeChild(preview2.firstChild);
  }

  const file2 = input2.files[0];
  const text = document.createElement("p");
  if (file2.length === 0) {
    text.textContent = "No file currently selected for upload";
    preview2.appendChild(text);
  } else {
    if (validFileType(file2)) {
      text.textContent = `File name: ${file2.name}`;
    } else {
      text.textContent = `File name ${file2.name}: Not a valid file type. Update your selection.`;
    }
    preview2.appendChild(text);
  }
}

const fileTypes2 = ["image/png", "image/jpeg"];

function validFileType(file2) {
  return fileTypes2.includes(file2.type);
}