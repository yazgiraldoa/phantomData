function updateSearchFormValidator(sheet_url, search_url) {
  const googleSheetResult = googleSheetValidator(sheet_url);
  if (googleSheetResult !== null) {
    return googleSheetResult;
  }

  const searchUrlResult = searchUrlValidator(search_url);
  if (searchUrlResult !== null) {
    return searchUrlResult;
  }

  return null;
}
