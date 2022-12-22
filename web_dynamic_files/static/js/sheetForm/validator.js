function sheetFormValidator(phantom_csv, sheets_url) {
  const googleSheetResult = googleSheetValidator(sheets_url);
  if (googleSheetResult !== null) {
    return googleSheetResult;
  }

  const phantomCsvResult = phantomCsvValidator(phantom_csv);
  if (phantomCsvResult !== null) {
    return phantomCsvResult;
  }

  return null;
}
