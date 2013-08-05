var add20js = {
    init: function(anchorName) {
        var form_element = document.createElement('form');
        var anchor_element = document.getElementById(anchorName);

        if (!anchor_element) {
            if (console) { console.log('no anchor found'); }
            return false;
        }
        form_element.action = '#';
        form_element.id = 'add20form';

        var outputChild = document.createElement('div');
        form_element.appendChild(outputChild);

        var inputChild = document.createElement('input');
        inputChild.type = "text";
        form_element.appendChild(inputChild);

        var submitChild = document.createElement('input');
        submitChild.type = "submit";
        submitChild.value = "Add 20 to this";
        form_element.appendChild(submitChild)

        document.body.insertBefore(form_element, anchor_element);

        form_element.onsubmit = function() {
            while (outputChild.hasChildNodes()) {
                outputChild.removeChild(outputChild.lastChild);
            }
            var httpRequest;

            var addTo = parseInt(inputChild.value);

            if (window.XMLHttpRequest) {
                httpRequest = new XMLHttpRequest();
            } else {
                httpRequest = newActiveXObject("Microsoft.XMLHTTP");
            }

            httpRequest.onreadystatechange = function() {
                if (httpRequest.readyState === 4) {
                    if (httpRequest.status === 200){
                        var response_obj = JSON.parse(httpRequest.responseText);
                        outputChild.appendChild(document.createTextNode(response_obj['result']));
                    } else {
                        if (console) { console.log("AJAX request failed, status was " + httpRequest.status); }
                    }
                } else {
                    // some other ready state
                }
            };

            httpRequest.open('GET', '/add20json/' + addTo, true);
            httpRequest.send(null);
            return false;
        };


    }
}