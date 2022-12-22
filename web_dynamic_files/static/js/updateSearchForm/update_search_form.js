function updateSearchForm(event) {
  event.preventDefault();

  const sheet_url = document.getElementById("sheet_url").value;
  const search_url = document.getElementById("search_url").value;

  const validatorErrorMessage = updateSearchFormValidator(
    sheet_url,
    search_url
  );

  if (validatorErrorMessage !== null) {
    showErrorMessage(validatorErrorMessage);
    return;
  }

  fetch("/update_search_submission", {
    method: "POST",
    body: JSON.stringify({
      sheet_url,
      search_url,
    }),
    headers: { "Content-type": "application/json; charset=UTF-8" },
  })
    .then((response) => response.json())
    .then(({ status_code, detail }) => {
      if (status_code !== 200 || status_code !== 201) {
        showErrorMessage(detail);
      }
    })
    .catch((error) => {
      showErrorMessage("There is a wrong with your URLs");
    });
}
