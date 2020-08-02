<script>

$(document).on('submit','#formSubmit',function(e){
    e.preventDefault();

    $.ajax({
        type:'POST',
        url:"{% url 'Coupon_to_create' %}",
        data:{
            'code':$('#code').val(),
            'startDate':$('#datepicker_from').val(),
            'endDate':$('#datepicker_to').val(),
            'profileChoices':$('#Profile_choices').val(),

            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
        },
        success:function(data){
        console.log("done")}

        });
        });
</script>

//THIS PAGE IS USED FOR added_to_coupon.html