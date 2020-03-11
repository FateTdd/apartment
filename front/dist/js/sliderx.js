$(document).ready(function() {
  var length = $(".content_1").children(".box").length;
  var boxWidth = $(".bigbox").width() / 4;
  var virtual = length * boxWidth;
  var speed = 500;
  var time =4000;
  $(".box").width(boxWidth-3);

  var Item = $('#switcher');
  Item.css({ position: 'relative' });
  var move = boxWidth + 'px';
  var leftCriticalPoint = "-" + virtual + "px";

  var flag = true;

  scrollContentStructure(length);

  function scrollContentStructure(length) {
    if(length < 4) {
      $('#switcher').width(boxWidth * (length + 4));
      if(length != 0) {
        var content_1 = $(".content_1").html();
        for(var i = 0; i < 6 - length; i++) {
          $(".content_1").append(content_1);
        }
      }
    } else {
      $('#switcher').width(virtual * 2);
      $(".content_2").html($(".content_1").html());
    }
  }

  if(length != 0) {
    var callback = setInterval(moving, time);
  }

  function moving() {
    flag = false;
    if(Item[0].style.left == leftCriticalPoint) {
      Item[0].style.left = "0px";
    }
    Item.animate({ left: '-=' + move }, speed, function() {
      if(Item[0].style.left == leftCriticalPoint) {
        Item[0].style.left = "0px";
      }
    });
    flag = true;
  }

  $("li").click(function() {
    if(!Item.is(":animated") && flag) {
      var left = Item[0].style.left;
      clearInterval(callback);

      if($(this).index() == 1) {
        if(left == leftCriticalPoint) {
          Item[0].style.left = "0px";
        }
        Item.animate({ left: '-=' + move }, speed, function() {
          if(Item[0].style.left == leftCriticalPoint) {
            Item[0].style.left = "0px";
          }
          callback = setInterval(moving, time);
        });
        // console.log("右");
      } else if($(this).index() == 0) {
        if(isNaN(parseInt(left)) || left == "0px") {
          Item[0].style.left = leftCriticalPoint;
        }
        Item.animate({ left: '+=' + move }, speed, function() {
          if(Item[0].style.left == "0px") {
            Item[0].style.left = leftCriticalPoint;
          }
          callback = setInterval(moving, time);
        });

      }
    }
  });

})
