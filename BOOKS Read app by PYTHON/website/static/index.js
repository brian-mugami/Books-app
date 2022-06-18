function deleteNote(bookid){
     fetch("/delete-note", {
     method:"POST",
     body: JSON.stringify({ bookid: bookid})
     }).then((_res) => {
     window.location.href="/mybooks";
     });
}