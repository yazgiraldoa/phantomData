function showErrorMessage(message) {
  Swal.fire({
    icon: "error",
    title: "Oops... This is Bad",
    text: message,
  }),
    "width=400,height=400,resizeable,scrollbars";
}

function showSuccessMessage(message) {
  Swal.fire({
    icon: "success",
    title: "Success!",
    text: message,
  }),
    "width=400,height=400,resizeable,scrollbars";
}
