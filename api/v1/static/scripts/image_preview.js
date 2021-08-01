
// First picture upload
const files = document.getElementById("img_one");
const previewContainer = document.getElementById("img_one_preview");
const previewImage = previewContainer.querySelector(".preview_image_one");
const previewText = previewContainer.querySelector(".preview_text_one");

files.addEventListener("change", function () {
  const file = this.files[0];
  if (file) {
    const reader = new FileReader();
    previewText.style.display = "none";
    previewImage.style.display = "block";
    reader.addEventListener("load", function () {
      console.log(this);
      previewImage.setAttribute("src", this.result);
    });
    reader.readAsDataURL(file);
  } else {
    previewText.style.display = null;
    previewImage.style.display = null;
    previewImage.setAttribute("src", "");
  }
});


// Second picture upload
const files2 = document.getElementById("img_two");
const previewContainer2 = document.getElementById("img_two_preview");
const previewImage2 = previewContainer2.querySelector(".preview_image_two");
const previewText2 = previewContainer2.querySelector(".preview_text_two");

files2.addEventListener("change", function () {
  const file2 = this.files[0];
  if (file2) {
    const reader = new FileReader();
    previewText2.style.display = "none";
    previewImage2.style.display = "block";
    reader.addEventListener("load", function () {
      console.log(this);
      previewImage2.setAttribute("src", this.result);
    });
    reader.readAsDataURL(file2);
  } else {
    previewText2.style.display = null;
    previewImage2.style.display = null;
    previewImage2.setAttribute("src", "");
  }
});