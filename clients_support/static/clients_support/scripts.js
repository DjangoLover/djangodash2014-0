$(function(){
    $(".dcs-plate").on("click", function(e){
        e.preventDefault();
        $(".dcs-form").show();
        $(".dcs-overlay").show();
    });
    $(".dcs-form_close").on("click", function(e){
        e.preventDefault();
        $(".dcs-form").hide();
        $(".dcs-overlay").hide();
    });
    $(".dcs-tickets_item").on("click", function(){
        $(this).toggleClass("dcs-tickets_item__active");
    });
});