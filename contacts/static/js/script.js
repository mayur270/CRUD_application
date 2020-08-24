// ############################ MODAL FUNCTION ###########################

$(function () {

  // ##### LOAD FORM FUNCTION #####

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#EmployeeModalForm").modal("show");
      },
      success: function (data) {
        $("#EmployeeModalForm .modal-content").html(data.employee_form);
      }
    });
  };

  // ##### SAVE FORM FUNCTION #####

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#EmployeeTable tbody").html(data.employee_list);
          $("#EmployeeModalForm").modal("hide");
        }
        else {
          $("#EmployeeModalForm .modal-content").html(data.employee_form);
        }
      }
    });
    return false;
  };

// ############### PUTTING IT ALL TOGETHER ####################

  // Create book
  $(".employee-create").click(loadForm);
  $("#EmployeeModalForm").on("submit", ".employee-create-form", saveForm);

  // Update book
  $("#EmployeeTable").on("click", ".employee-update", loadForm);
  $("#EmployeeModalForm").on("submit", ".employee-delete-form", saveForm);

  // Delete book
  $("#EmployeeTable").on("click", ".employee-delete", loadForm);
  $("#EmployeeModalForm").on("submit", ".employee-update-form", saveForm);

});
