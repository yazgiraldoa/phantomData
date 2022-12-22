function searchUrlValidator(search_url) {
  if (search_url === "") {
    return "search_url cannot be empty";
  }

  if (!search_url.startsWith("https://www.linkedin.com/sales/search/people?query=")
  ) {
    return "This is not a valid Search url";
  }
  return null;
}
