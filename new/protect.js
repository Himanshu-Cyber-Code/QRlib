document.write(unescape('%3Cstyle%3E%0A%20%20%20%20body%20%7B%0A%20%20%20%20%20%20%20%20-webkit-touch-callout%3A%20none%3B%0A%20%20%20%20%20%20%20%20-webkit-user-select%3A%20none%3B%0A%20%20%20%20%20%20%20%20-khtml-user-select%3A%20none%3B%0A%20%20%20%20%20%20%20%20-moz-user-select%3A%20none%3B%0A%20%20%20%20%20%20%20%20-ms-user-select%3A%20none%3B%0A%20%20%20%20%20%20%20%20user-select%3A%20none%3B%0A%20%20%20%20%7D%0A%3C%2Fstyle%3E%0A%3Cscript%3E%0A%20%20%20%20window.oncontextmenu%20%3D%20function%20%28%29%20%7B%0A%20%20%20%20%20%20%20%20return%20false%3B%0A%20%20%20%20%7D%0A%20%20%20%20%24%28document%29.keydown%28function%20%28event%29%20%7B%0A%20%20%20%20%20%20%20%20if%20%28event.keyCode%20%3D%3D%20123%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20false%3B%0A%20%20%20%20%20%20%20%20%7D%20else%20if%20%28%28event.ctrlKey%20%26%26%20event.shiftKey%20%26%26%20event.keyCode%20%3D%3D%2073%29%20%7C%7C%20%28event.ctrlKey%20%26%26%20event.shiftKey%20%26%26%20event.keyCode%20%3D%3D%2074%29%29%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20false%3B%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%29%3B%0A%3C%2Fscript%3E'));