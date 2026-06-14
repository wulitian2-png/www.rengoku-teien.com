$(document).ready(function(){
$.each(["music0","music1","sample"],function(){
　$("#"+this).jPlayer({
　　ready: (function(id){
　　　return function(){
　　　　$(this).jPlayer("setMedia", {
　　　　　mp3:"vocal/" + id + ".mp3",
			mid:"vocal/" + id + ".mid"
　　　　});
　　　};
　　})(this),
　swfPath: "js",
　supplied: "mp3",
　cssSelectorAncestor: "#"+this,
　wmode: "window"
　});
});});