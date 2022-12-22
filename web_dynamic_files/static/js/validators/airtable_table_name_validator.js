function airtableTableNameValidator(airtable_table_name) {
  if (airtable_table_name === "") {
    return "airtable_table_name cannot be empty";
  }

  return null;
}
