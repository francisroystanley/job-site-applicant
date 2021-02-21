const titlecase = (string) => {
  if (!string) return;
  return string.split(' ').map(function(string) {
    string = string.trim();
    return string.charAt(0).toUpperCase() + string.substr(1).toLowerCase();
  }).join(' ');
};

export default titlecase;
