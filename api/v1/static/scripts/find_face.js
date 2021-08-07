#!/usr/bin/nodejs

$("#btn").click(function () {
    let img1 = $(".preview_image_one").attr("src");

    $('#upload').append('<img id="subir">');

    $('#subir').attr('src=' + img1);
});