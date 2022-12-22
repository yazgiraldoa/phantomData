function phantomCsvValidator(phantomCsvUrl) {
  if (phantomCsvUrl === "") {
    return "phantom_csv cannot be empty";
  }

  if (
    !phantomCsvUrl.includes("phantombooster") ||
    !phantomCsvUrl.endsWith("csv")
  ) {
    return "This is not a valid Phantom buster url";
  }
  return null;
}
