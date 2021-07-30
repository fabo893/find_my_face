#!/usr/bin/nodejs

/*
const files = document.getElementById("img_one");
const previewContainer = document.getElementById("img_one_preview");
const previewImage = previewContainer.querySelector(".preview_image_one");
const previewText = previewContainer.querySelector(".preview_text_one");

$('#btn').on('click', function () {

    const file = this.files[0];

    $.ajax({
        type: 'POST',
        url: '/find',
        data: file,
        sucess: function() {
            if (file) {
                const reader = new FileReader();
                previewText.style.display = "none";
                previewImage.style.display = "block";
                reader.addEventListener("load", function () {
                  console.log(this);
                  previewImage.setAttribute("src", this.result);
                });
                reader.readAsDataURL(file);
            }
        },

    });

});
*/

$('#btn').on('click', function () {
    const img1 = document.querySelector(".preview_image_one");
    const img2 = document.querySelector(".preview_image_two");

    $.ajax({
        type: 'POST',
        url: '/find',
        data: { param: img1, param2: img2 },
        success: function () {
            console.log("Good")
        }
    });
});