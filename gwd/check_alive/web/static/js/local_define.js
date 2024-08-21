
    function deleterow(){
	var rowSelected=$("#table").bootstrapTable('getSelections');
	//console.log(rowSelected);
	 if (rowSelected.length == 0) {
            alert('请选择要删除的记录');
            return;
        }
     if (confirm('确认删除选中的记录吗？')) {
            console.log(rowSelected);
            var ids = [];
            for (var i = 0; i < rowSelected.length; i++) {
                var id = rowSelected[i].id;
                ids.push(id);
                console.log(id);
            }
            console.log(ids);
            var idsStr = JSON.stringify(ids);
            $.ajax({
                type: "GET",
                url: "/bulk/delete?ids=" + encodeURIComponent(idsStr)
            })
            location.reload();
            return;
        }
    }

    function actionFormatter(value, row, index) {
            var id = index + 1;
            var result = "";
            result += '<a href="javascript:;" class="btn btn-xs btn-success" onclick=\"viewViewById(' + id + ')\" data-toggle="modal" data-target="#viewModal"  title="查看">';
            result += '<span class="fa fa-search" ></span></a>';
            result += '<a href="javascript:;" class="btn btn-xs btn-info" onclick=\"editViewById(' + id + ')\" data-toggle="modal" data-target="#editModal" title="编辑">';
            result += '<span class="fa fa-edit"></span></a>';
            result += '<a href="javascript:;" class="btn btn-xs btn-danger" onclick=\"deleteView(' + id + ')\"  title="删除">';
            result += '<span class="fa fa-trash"></span></a>';
            return result;
        }

    function viewViewById(id) {
        console.log(id);
        $.ajax({
        url: '/api/view/' + id,
        type: 'GET',
        success: showQuery,
        error: function (xhr, status, error) {
            alert(xhr.status);
        },
        dataType: 'json'
        });

     }

      function showQuery(data) {
         console.log(data);
        $('#modal_name').val(data.name);
        $('#modal_env').val(data.env);
        $('#modal_location').val(data.location);
        $('#modal_ip').val(data.ip);
        $('#modal_port').val(data.port);
        $('#modal_url').val(data.url);
        $('#modal_key').val(data.key);
        $('#modal_desc').val(data.desc);
        $('.form-control').attr('readonly', true);
        //$('#saveModal').hide();
        $('#modal-form').modal('show');
     }

     function editViewById(id) {
        console.log(id);
        $.ajax({
        url: '/api/edit/' + id,
        type: 'GET',
        success: editQuery,
        error: function (xhr, status, error) {
            alert(xhr.status);
        },
        dataType: 'json'
        });
     }

  function editQuery(data) {
         console.log(data);
         $('#edit_id').val(data.id);
        $('#edit_name').val(data.name);
        $('#edit_env').val(data.env);
        $('#edit_location').val(data.location);
        $('#edit_ip').val(data.ip);
        $('#edit_port').val(data.port);
        $('#edit_url').val(data.url);
        $('#edit_key').val(data.key);
        $('#edit_desc').val(data.desc);
        $('.form-control').attr('readonly', false);
        $('#edit-form').modal('show');
     }


    function deleteView(id) {
        $.ajax({
            url: '/api/delete?ids=' + encodeURIComponent(id),
            type: 'GET',
        });
        location.reload();
    }

    function exportData() {
        console.log('export');
        var rowSelected=$("#table").bootstrapTable('getSelections');
        if (rowSelected.length == 0) {
            confirm('确认导出所有记录吗？');
            var xhr = new XMLHttpRequest();
            xhr.open('GET', '/api/export?ids=', true);
            xhr.responseType = 'blob';
            xhr.onload = function () {
            if (this.status === 200) {
            var blob = new Blob([this.response], {type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'});
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = 'output.xlsx';
            link.click();
            }
        };
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send();
        return;
        }
        if (confirm('确认导出选中的记录吗？')) {
             var ids = [];
            for (var i = 0; i < rowSelected.length; i++) {
            var id = rowSelected[i].id;
            ids.push(id);
            }
        var idsStr = JSON.stringify(ids);
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/export?ids=' + encodeURIComponent(idsStr), true);
        xhr.responseType = 'blob';
        xhr.onload = function () {
        if (this.status === 200) {
            var blob = new Blob([this.response], {type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'});
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = 'output.xlsx';
            link.click();
            }
        };
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send();
        return;
        }
        };

    $('#table').on("check.bs.table", function (e, row) {
    var member = row.name;
    //console.log(member);
    });

    $('#table').on("uncheck.bs.table", function (e, row) {
    var member = row.name;
    //console.log(member);
    });

    $('#table').on('click-row.bs.table', function (e, row) {
    });

    $('#export').click(function () {
        exportData();
    });
