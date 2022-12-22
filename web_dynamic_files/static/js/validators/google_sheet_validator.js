function googleSheetValidator(googleSheetUrl) {
  if (googleSheetUrl === "") {
    return "google_sheet_url cannot be empty";
  }

  if (!googleSheetUrl.startsWith("https://docs.google.com/spreadsheets/")) {
    return "This is not a valid Google Sheets url";
  }
  return null;
}
