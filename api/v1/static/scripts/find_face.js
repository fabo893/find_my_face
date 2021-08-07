#!/usr/bin/nodejs

$("#btn").click(function () {
    let img1 = $(".preview_image_one").attr("src");
    let img2 = $('.preview_image_two').attr('src');

    $.ajax({
        type: 'POST',
        url: '~/testing/printMatch.py' + img1 + img2,
        success: function (response) {
            console.log(response);
        }
    });
});