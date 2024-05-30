// Adding an LI element to list when thr tag is clicked

$('div#add_item').click(function () {
    let ele = '<li>Item</li>';
    $('ul.my_list').append(ele);
  });
