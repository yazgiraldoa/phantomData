function sheetFormValidator(phantom_csv, sheets_url) {
  if (sheets_url === "") {
    return "google_sheet_url cannot be empty";
  }
  if (phantom_csv === "") {
    return "phantom_csv cannot be empty";
  }

  return null;
}
