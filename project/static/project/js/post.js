document.addEventListener('DOMContentLoaded', function(){
    let input = document.querySelector('#id_content');
    console.log('js');
    let para = document.querySelector('#display');

    // copying the url feature
    copyBtn = document.getElementById('id_copyBtn');
    uploadSelect = document.getElementById('uploads');

    copyBtn.disabled = true;
    uploadSelect.addEventListener('change', function(){
        copyBtn.disabled = false;
    })
    
    copyBtn.addEventListener('click', function(e){
        copyToClipboard(e);
    })

    copyBtn.addEventListener('click', function() {
        console.log('clicked!')
        copyBtn.innerHTML = '<i class="fas fa-check"></i>'; // Change icon to a checkmark

        // After a short delay (e.g., 1 second), revert back to the copy icon
        setTimeout(function() {
            copyBtn.innerHTML = '<i class="fas fa-copy"></i>'; // Change icon back to copy
        }, 1000);
    });

    // Use the footnote extension
    marked.use(markedFootnote());

    const renderer = new marked.Renderer();
    marked.setOptions({
        renderer: renderer,
        gfm: true,
        breaks: true,
        pedantic: false, // Set to true if you want to conform to the original markdown.pl as much as possible
    });

    // support for superscripts
    // by overriding the `text` method of the renderer
    // renderer.text = function(text) {
    //     // Check if the text contains a superscript pattern (^text^)
    //     text = text.replace(/\^([^\^]+)\^/g, '<sup>$1</sup>');

    //     // Call the original text method with modified text
    //     return marked.Renderer.prototype.text.call(this, text);
    // };

    input.addEventListener('input', function(e){
        // When you delete all the text, input.value becomes an empty string, which is considered falsy in JavaScript, so the display doesn't update.
        if (input.value != null){
            let htmlContent = marked(input.value);
            para.innerHTML = `${htmlContent}`;

            autoClose(input, e);

            applyStylesToMarkdown(para);

            // Trigger MathJax to process the updated content
            MathJax.Hub.Queue(["Typeset", MathJax.Hub, para]);

            autoCloseMath(input, e);
        }
    })
    
    //When User navigates to upload image url, store the form data in the local storage...
    const uploadImageUrl = document.getElementById('id_upload_image_url');
    uploadImageUrl.addEventListener('click', function(){
        console.log('clicked url')
        storeFormData();
    })


    // Delete the localStorage form content after user saves the post
    const saveBtn = document.getElementById('id_save_post_btn');
    saveBtn.addEventListener('click', function(){
        localStorage.removeItem('formData');
    })


    // Call populateForm function when the page loads
    window.onload = populateForm;
})



//-----------------------------------------------------------------------------------------------------------------------------//

// storing data before navigating to upload images...
// Function to store form data in local storage
function storeFormData() {
    console.log('storeformdata');
    // Retrieve form data
    const formData = {
        title: document.getElementById('id_title').value,
        content: document.getElementById('id_content').value
        // Add more fields as needed
    };
    
    // Store form data in local storage
    localStorage.setItem('formData', JSON.stringify(formData));
}


// Function to populate form fields with stored data
function populateForm() {
    console.log('functionCalled')
    // Retrieve stored form data
    const storedData = localStorage.getItem('formData');
    if (storedData) {
        const formData = JSON.parse(storedData);
        // Populate form fields with stored data
        document.getElementById('id_title').value = formData.title;
        document.getElementById('id_content').value = formData.content;
        // Populate more fields as needed
    
    }
}

//-----------------------------------------------------------------------------------------------------------------------------//


function copyToClipboard(e) {
    // Prevent the default form submission behavior
    e.preventDefault();
    
    var imageId = document.getElementById("uploads").value;
    if (!imageId) return;
    
    fetch(`get-temporary-image-url/${imageId}/`)
        .then(response => response.json())
        .then(data => {
            console.log(data.image_url)
            if (data.image_url) {
                navigator.clipboard.writeText(data.image_url);
                // alert("Temporary Image URL copied to clipboard!");
            } else {
                alert("Failed to fetch temporary image URL.");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert("Failed to fetch temporary image URL.");
        });
    return false;
}
    




function autoClose(input, event){
    let caretPos = input.selectionStart;
    console.log('pos: ',caretPos);
    
    let charhalf = input.value.charAt(caretPos-3)
    let char1 = input.value.charAt(caretPos-2);
    let char2 = input.value.charAt(caretPos-1);
    if (event.inputType === 'deleteContentBackward' && char2 === '>') {
        return;
    }

    if (((char2 === '>') && (char1 != ' ')) && !((char1 === 'r' && charhalf === 'b') || (char1 === 'r' && charhalf === 'h'))) {
        console.log('char:', char2);
        console.log('char 0.5: ', char1);
        // Find the opening '<' character before caretPos
        let openingBracketIndex = input.value.lastIndexOf('<', caretPos - 2);
        let charAfteropening = input.value.charAt(openingBracketIndex+1);
        let closingBracketIndex = input.value.lastIndexOf('>', caretPos);
        let ErrorTag = closingBracketIndex-1; // before openingBracketIndex + 1
        let charAtErrorTag = input.value.charAt(ErrorTag);
 
        let tagEnd = input.value.indexOf(' ', openingBracketIndex); // 'space' from char '<'...
        console.log('tagEnd:', tagEnd);
        console.log('char after opening:', charAfteropening);
        if (openingBracketIndex !== -1 && charAtErrorTag !== '/' && charAfteropening !== '>' && charAfteropening !== '!') {
            // Extract the tag name from the opening tag

            // if space character found after '>' char...
            if (tagEnd !== -1 && tagEnd > closingBracketIndex){
                console.log('errorTag:', ErrorTag);
                console.log('caretpost of >:', closingBracketIndex);
                let tagName = input.value.substring(openingBracketIndex + 1, closingBracketIndex).trim();
                console.log('tagname: ', tagName);

                // Insert the closing tag with the corresponding name
                let beforeCaret = input.value.substring(0, caretPos);
                let afterCaret = input.value.substring(caretPos);
                input.value = beforeCaret + `</${tagName}>` + afterCaret;

                // Set the caret position to where it was before the insertion
                input.selectionStart = input.selectionEnd = caretPos;
            }

            // if space is found after '<' and before '>'
            else if (tagEnd !== -1 && tagEnd < closingBracketIndex) {
                console.log('here!');
                console.log('errorTag:', ErrorTag);
                console.log('caretpost of >:', closingBracketIndex);
                let tagName = input.value.substring(openingBracketIndex + 1, tagEnd).trim();
                console.log('tagname: ', tagName);

                // Insert the closing tag with the corresponding name
                let beforeCaret = input.value.substring(0, caretPos);
                let afterCaret = input.value.substring(caretPos);
                input.value = beforeCaret + `</${tagName}>` + afterCaret;

                // Set the caret position to where it was before the insertion
                input.selectionStart = input.selectionEnd = caretPos;
            }

            // no space character found...
            else{
                let tagName = input.value.substring(openingBracketIndex + 1, caretPos - 1).trim();
                console.log('tagnameII: ', tagName);
                // Insert the closing tag with the corresponding name
                let beforeCaret = input.value.substring(0, caretPos);
                let afterCaret = input.value.substring(caretPos);
                input.value = beforeCaret + `</${tagName}>` + afterCaret;

                // Set the caret position to where it was before the insertion
                input.selectionStart = input.selectionEnd = caretPos;
            }
        }
    }
}

function autoCloseMath(input, event){
    let caretPos = input.selectionStart;
    let char1 = input.value.charAt(caretPos-1)
    let char2 = input.value.charAt(caretPos-2)

    if (event.inputType === 'deleteContentBackward' && char2 === '$') {
        return;
    }
    if (char1 === '$' && char2 === '$'){
        // Find the opening '$$' character before caretPos
        let openingDollarIndex = input.value.lastIndexOf('$$', caretPos - 2);
        // console.log('mathjax:',openingDollarIndex);

        if (openingDollarIndex !== -1) {
            // Insert the closing '$$' after the opening one
            let beforeCaret = input.value.substring(0, caretPos);
            let afterCaret = input.value.substring(caretPos);
            input.value = beforeCaret + '$$' + afterCaret;

            // Set the caret position after the closing '$$'
            input.selectionStart = input.selectionEnd = caretPos;
        }

    }
}

function applyStylesToMarkdown(para) {
    let codeBlocks = para.querySelectorAll('pre code, code');

    codeBlocks.forEach((codeBlock) => {
        codeBlock.classList.add('codeBlock');

        let copyButton = document.createElement('span');
        copyButton.innerHTML = '<i class="fas fa-copy"></i>';
        // copyButton.textContent = 'Copy';
        copyButton.className = 'copyButton';
        copyButton.style.marginLeft = '10px';

        codeBlock.parentNode.appendChild(copyButton);
    });
    // Initialize ClipboardJS after buttons are added
    const clipboard = new ClipboardJS('.copyButton', {
        text: function (trigger) {
            return trigger.parentNode.querySelector('code').innerText;
        }
    });

    // Optional: Display a tooltip when the copy operation is successful
    clipboard.on('success', function (e) {
        e.clearSelection();
        e.trigger.innerHTML = '<i class="fa-solid fa-check"></i>';
        setTimeout(function () {
            e.trigger.innerHTML = '<i class="fas fa-copy"></i>';
        }, 1000);
    });
}