#!/usr/bin/nodejs

$("#btn").click(function() {
    let img_one = document.getElementsByClassName("preview_image_one");
    let img_two = document.getElementsByClassName("preview_image_two");

    let src1 = img_one.attr("src");
    let src2 = img_two.attr("src");

    console.log(src1);
    console.log(src2);
});