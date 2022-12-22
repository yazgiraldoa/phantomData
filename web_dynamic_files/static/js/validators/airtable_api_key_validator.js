function airtableApiKeyValidator(airtable_api_key) {
  if (airtable_api_key === "") {
    return "airtable_api_key cannot be empty";
  }

  if (!airtable_api_key.startsWith("key")) {
    return "This is not a valid Airtable api key";
  }
  return null;
}
