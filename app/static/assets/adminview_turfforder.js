// new DataTable('#example');
new DataTable('#example');

const table = new DataTable('#example', {
    paging: false,
    scrollY: '200px'
});
 
document.querySelectorAll('a.toggle-vis').forEach((el) => {
    el.addEventListener('click', function (e) {
        e.preventDefault();
 
        let columnIdx = e.target.getAttribute('data-column');
        let column = table.column(columnIdx);
 
        // Toggle the visibility
        column.visible(!column.visible());
    });
});