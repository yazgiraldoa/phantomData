function airTableValidator(
  phantom_csv,
  airtable_api_key,
  airtable_base_url,
  airtable_table_name
) {
  const phantomCsvResult = phantomCsvValidator(phantom_csv);
  if (phantomCsvResult !== null) {
    return phantomCsvResult;
  }

  const airtableApiKeyResult = airtableApiKeyValidator(airtable_api_key);
  if (airtableApiKeyResult !== null) {
    return airtableApiKeyResult;
  }

  const airtableBaseResult = airtableBaseUrlValidator(airtable_base_url);
  if (airtableBaseResult !== null) {
    return airtableBaseResult;
  }

  const airtableTableNameResult =
    airtableTableNameValidator(airtable_table_name);
  if (airtableTableNameResult !== null) {
    return airtableTableNameResult;
  }

  return null;
}
