$(document).ready(function() {
  // Function to add a new item to the list
  $("#add_item").click(function() {
    $("ul.my_list").append("<li>Item</li>");
  });

  // Function to remove the last item from the list
  $("#remove_item").click(function() {
    $("ul.my_list li:last-child").remove();
  });

  // Function to clear the entire list
  $("#clear_list").click(function() {
    $("ul.my_list").empty();
  });
});

