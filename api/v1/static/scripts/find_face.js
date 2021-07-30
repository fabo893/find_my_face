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

    $.ajax({
        type: 'POST',
        url: '/save',
        success: success
    });
});