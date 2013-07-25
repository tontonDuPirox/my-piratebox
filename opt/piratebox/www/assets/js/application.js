function fnGetDomain(url) {
    return url.match(/:\/\/(.[^/]+)/)[1];
}

function reset() {
    self.document.psowrte.data.value = "";
    self.document.psowrte.data.focus();
}