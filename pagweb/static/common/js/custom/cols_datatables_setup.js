function setupColsDateRange(table, cols_title_date_range_filter, cols_date_range_filter) {
    cols_date_range_filter.each(function (colIdx) {
        $('<input type="text" placeholder="Desde: dd/MM/aaaa" class="form-control" style="width:80%;display:inline"/>').appendTo($(this))
            .on('keydown focusout', function (ev) {
                $(this).mask('00-00-0000');
                // se recrea solo si aprieta enter o la casilla se pone vacia (luego de ir borrando)
                if (ev.keyCode === 13 || (ev.type === "focusout" && this.last_query !== this.value)) {
                    var dateISOFormat = '';
                    if (this.value.length > 0) {
                        var dateValue = this.value.split('-');
                        if (dateValue.length === 3) {
                            dateISOFormat = (new Date(dateValue[2], dateValue[1] - 1, dateValue[0], 0, 0, 0, 0)).toISOString();
                        }
                    }

                    var pos = table.column(cols_title_date_range_filter[colIdx])[0][0];

                    if (table.data().settings()[0].ajax.data === undefined)
                        table.data().settings()[0].ajax.data = {};

                    table.data().settings()[0].ajax.data[table.settings().init().columns[pos].name + '_gt'] = dateISOFormat;
                    table.draw();

                    this.last_query = this.value;
                }
            }).on('click', function (e) {
            e.stopPropagation();
        });

        $('<br><input type="text" placeholder="Hasta: dd/MM/aaaa" class="form-control" style="width:80%;display:inline"/>').appendTo($(this))
            .on('keydown focusout', function (ev) {
                $(this).mask('00-00-0000');
                // se recrea solo si aprieta enter o la casilla se pone vacia (luego de ir borrando)
                if (ev.keyCode === 13 || (ev.type === "focusout" && this.last_query !== this.value)) {
                    var dateISOFormat = '';
                    if (this.value.length > 0) {
                        var dateValue = this.value.split('-');
                        if (dateValue.length === 3) {
                            dateISOFormat = (new Date(dateValue[2], dateValue[1] - 1, dateValue[0], 0, 0, 0, 0)).toISOString();
                        }
                    }

                    var pos = table.column(cols_title_date_range_filter[colIdx])[0][0];

                    if (table.data().settings()[0].ajax.data === undefined)
                        table.data().settings()[0].ajax.data = {};

                    table.data().settings()[0].ajax.data[table.settings().init().columns[pos].name + '_lt'] = dateISOFormat;
                    table.draw();

                    this.last_query = this.value;
                }
            }).on('click', function (e) {
            e.stopPropagation();
        });
    });
}


function setupColsTextInputSearch(table,cols_title_text_input_search,cols_text_input_search) {
    cols_text_input_search.each(function (colIdx) {

            $('<input type="text" placeholder="Buscar" class="form-control" style="width:80%;display:inline"/>').appendTo($(this)).on('keydown focusout', function (ev) {
                // se recrea solo si aprieta enter o la casilla se pone vacia (luego de ir borrando)

                if (ev.keyCode === 13 || (ev.type === "focusout" && this.last_query !== this.value)) {
                    //table.column(colIdx).search(this.value).draw();
                    table.column(cols_title_text_input_search[colIdx]).search(this.value.replace(/;/g, "|"), true, false).draw();

                    this.last_query = this.value;
                }
            }).on('click', function (e) {
                e.stopPropagation();
            });
        }
    );

}