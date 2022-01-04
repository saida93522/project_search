const search_form = document.getElementById("searchForm");
const paginate_btn = document.querySelectorAll(".page-link");

// Ensure search form exists
if (search_form) {
  for (let i = 0; paginate_btn.length > i; i++) {
    paginate_btn[i].addEventListener("click", function (e) {
      e.preventDefault();

      //GET THE DATA ATTRIBUTE
      let page = this.dataset.page;
      console.log("PAGE: ", page);

      //ADD HIDDEN SEARCH INPUT TO FORM
      search_form.innerHTML += `<input value=${page} name="page" hidden/>`;

      //SUBMIT FORM
      search_form.submit();
    });
  }
}
