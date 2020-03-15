$(document).ready(function() {
  var length = $(".content_1").children(".box").length;//Number of boxes
  var boxWidth = $(".bigbox").width() / 4;//Window width divided by 4 to get moving width
  var virtual = length * boxWidth;	//Critical point of switching
  var speed = 500;	//Moving speed, speed is recommended to be less than half of the interval.
  var time =4000;	//Interval time
  $(".box").width(boxWidth-3);

  var Item = $('#switcher'); //Elements to be moved
  Item.css({ position: 'relative' }); //Settin position
  var move = boxWidth + 'px'; //The range of movement is the width of a box.
  var leftCriticalPoint = "-" + virtual + "px"; //If there are n boxes, take the length of n boxes as the Critical jump point.

  var flag = true;//Click allow

  scrollContentStructure(length);

  function scrollContentStructure(length) {
    if(length < 4) {
      $('#switcher').width(boxWidth * (length + 4)); //Window width strip 4, complement 6 Murl; suppose lily 3, strip 7. Complement 3
      if(length != 0) {
        var content_1 = $(".content_1").html();
        for(var i = 0; i < 6 - length; i++) {
          $(".content_1").append(content_1); //At least 6 boxes, append to enough
        }
      }
    } else {
      $('#switcher').width(virtual * 2);
      $(".content_2").html($(".content_1").html()); //copy
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
    //Currently in animation state Clickable state judgment
    //Flag prevents event stack accumulating
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
        // console.log("right");
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
        // console.log("left ");
      }
    }
  });

})
