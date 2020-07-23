 $(document).ready(function () {
  $("#select_dropdown").change(function () {
    var e = document.getElementById("select_dropdown");
    var value = e.options[e.selectedIndex].value;
    console.log(value)

    $.ajax({
      url: "{% url 'Unreadpost' %}",
      type: "post" #or "post", //
      data: value,
      headers: { "X-CSRFToken": "{{ csrf_token }}" }, // for csrf token
      success: function (data) {
        alert(data.result);
      },
    });
  });
});