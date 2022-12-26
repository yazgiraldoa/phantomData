function target_popup(event) {
  event.preventDefault();

  let phantom_csv = document.getElementById("phantom_csv").value;
  let airtable_api_key = document.getElementById("airtable_api_key").value;
  let airtable_base_url = document.getElementById("airtable_base_url").value;
  let airtable_table_name = document.getElementById(
    "airtable_table_name"
  ).value;

  const data = {
    phantom_csv,
    airtable_api_key,
    airtable_base_url,
    airtable_table_name,
  };

  const validatorErrorMessage = airTableValidator(
    phantom_csv,
    airtable_api_key,
    airtable_base_url,
    airtable_table_name
  );

  if (validatorErrorMessage !== null) {
    showErrorMessage(validatorErrorMessage);
    return;
  }

  fetch("/airtable_submission", {
    method: "POST",
    body: JSON.stringify(data),
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
      showErrorMessage(
        "There is a wrong with your URLs, airtable name, or airtable api key"
      );
    });
}
