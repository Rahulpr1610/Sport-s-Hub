// new DataTable('#example');
new DataTable('#example', {
    autoWidth: false,
    columnDefs: [
        {
            targets: ['_all'],
            className: 'mdc-data-table__cell',
        },
    ],
});