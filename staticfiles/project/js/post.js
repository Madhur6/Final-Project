document.addEventListener('DOMContentLoaded', function(){
    let input = document.querySelector('#id_content');
    console.log('js');
    let para = document.querySelector('#display');


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
    renderer.text = function(text) {
        // Check if the text contains a superscript pattern (^text^)
        text = text.replace(/\^([^\^]+)\^/g, '<sup>$1</sup>');

        // Call the original text method with modified text
        return marked.Renderer.prototype.text.call(this, text);
    };

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
})

function autoClose(input, event){
    let caretPos = input.selectionStart;
    // console.log('pos: ',caretPos);

    let char1 = input.value.charAt(caretPos-2);
    let char2 = input.value.charAt(caretPos-1);

    if (event.inputType === 'deleteContentBackward' && char2 === '>') {
        return;
    }

    if ((char2 === '>') && (char1 != ' ')){
        // console.log('char:', char2);
        // Find the opening '<' character before caretPos
        let openingBracketIndex = input.value.lastIndexOf('<', caretPos - 2);
        let ErrorTag = openingBracketIndex+1;
        let charAtErrorTag = input.value.charAt(ErrorTag);

        let tagEnd = input.value.indexOf(' ', openingBracketIndex);
        // console.log('tagEnd', tagEnd);
        if (openingBracketIndex !== -1 && charAtErrorTag !== '/') {
            // Extract the tag name from the opening tag
            if (tagEnd !== -1){
                // console.log('hey')
                let tagName = input.value.substring(openingBracketIndex + 1, tagEnd).trim();

                // Insert the closing tag with the corresponding name
                let beforeCaret = input.value.substring(0, caretPos);
                let afterCaret = input.value.substring(caretPos);
                input.value = beforeCaret + `</${tagName}>` + afterCaret;

                // Set the caret position to where it was before the insertion
                input.selectionStart = input.selectionEnd = caretPos;
                
            }else{
                let tagName = input.value.substring(openingBracketIndex + 1, caretPos - 1).trim();
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