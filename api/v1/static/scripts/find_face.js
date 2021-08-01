#!/usr/bin/nodejs

$("#btn").click(function() {
    img_one = document.getElementsByClassName("preview_image_one");
    img_two = document.getElementsByClassName("preview_image_two");

    src1 = img_one.getAttribute("src");
    src2 = img_two.getAttribute("src");

    console.log(src1);
    console.log(src2);
});