document.addEventListener('DOMContentLoaded', function(){
    let deleteBtn = document.getElementById('id_delete_btn');
    let uploadBtn = document.getElementById('id_upload_btn');
    let fileInput = document.getElementById('note-image');
    
    uploadBtn.disabled = true;
    
    fileInput.addEventListener('change', function(){
        // Check if any files are selected
        if (fileInput.files.length > 0) {
          // Enable upload button
          uploadBtn.disabled = false;
        } else {
          // No files selected, disable upload button
          uploadBtn.disabled = true;
      }
    })
    

    deleteBtn.addEventListener('click', function(){
        deleteImages();
    })
})


// Function to delete selected images
function deleteImages() {
    var selectedImageIds = [];
    var checkboxes = document.querySelectorAll('input[name="image_ids"]:checked');
    checkboxes.forEach(function(checkbox) {
      selectedImageIds.push(checkbox.value);
    });

    if (selectedImageIds.length === 0) {
      alert("Please select images to delete.");
      return;
    }

    // Add selected image IDs to the form for submission
    var deleteForm = document.getElementById("deleteForm");
    selectedImageIds.forEach(function(imageId) {
      var input = document.createElement("input");
      input.setAttribute("type", "hidden");
      input.setAttribute("name", "selected_image_ids");
      input.setAttribute("value", imageId);
      deleteForm.appendChild(input);
    });

    // Submit the form
    deleteForm.submit();
}