function airtableBaseUrlValidator(airtable_base_url) {
  if (airtable_base_url === "") {
    return "airtable_base_url cannot be empty";
  }

  if (!airtable_base_url.startsWith("https://airtable.com/app")) {
    return "This is not a valid Airtable url";
  }
  return null;
}
