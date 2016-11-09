// /*
// Template Name: Penyler
// Author: <a href="http://www.os-templates.com/">OS Templates</a>
// Author URI: http://www.os-templates.com/
// Licence: Free to use under our free template licence terms
// Licence URI: http://www.os-templates.com/template-terms
// File: Mobile Menu JS

// Thanks to:
// "Convert a Menu to a Dropdown for Small Screens" from Chris Collier - http://css-tricks.com/convert-menu-to-dropdown/
// "Submenu's with a dash" Daryn St. Pierre - http://jsfiddle.net/bloqhead/Kq43X/
// */

// $('<form action="#"><select /></form>').appendTo(".menu-holder");$("<option />",{selected:"selected",value:"",text:"MENU"}).appendTo(".menu-holder select");$(".menu-holder a").each(function(){var e=$(this);if($(e).parents("ul ul ul").length>=1){$("<option />",{value:e.attr("href"),text:"- - - "+e.text()}).appendTo(".menu-holder select")}else if($(e).parents("ul ul").length>=1){$("<option />",{value:e.attr("href"),text:"- - "+e.text()}).appendTo(".menu-holder select")}else if($(e).parents("ul").length>=1){$("<option />",{value:e.attr("href"),text:""+e.text()}).appendTo(".menu-holder select")}else{$("<option />",{value:e.attr("href"),text:e.text()}).appendTo(".menu-holder select")}});$(".menu-holder select").change(function(){if($(this).find("option:selected").val()!=="#"){window.location=$(this).find("option:selected").val()}})