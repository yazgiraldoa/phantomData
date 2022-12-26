function popup(event) {
  event.preventDefault();

  let phantom_csv = document.getElementById("phantom_csv").value;
  let sheets_url = document.getElementById("sheets_url").value;

  const validatorErrorMessage = sheetFormValidator(phantom_csv, sheets_url);

  if (validatorErrorMessage !== null) {
    showErrorMessage(validatorErrorMessage);
    return;
  }
  fetch("/sheet_submission", {
    method: "POST",
    body: JSON.stringify({ phantom_csv, sheets_url }),
    headers: { "Content-type": "application/json; charset=UTF-8" },
  })
    .then((response) => response.json())
    .then(({ status_code, detail }) => {
      if (status_code === 201) {
        showSuccessMessage("Task scheduled successfully");
      } else {
        showErrorMessage(detail);
      }
    })
    .catch((error) => {
      showErrorMessage("There is a wrong with your phantom_csv or sheets_url");
    });
}
