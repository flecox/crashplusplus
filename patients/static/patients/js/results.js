
(function($) {

  function body_surface_area(weight, size, id) {
    var bsa = Math.sqrt((weight*size)/3600).toFixed(2);
    $(id + "body_surface_area").val(bsa);
  }

  function corporal_mass_index(weight, size, id) {
    var tmp = weight/Math.pow(size/100.0, 2);
    var cmi = tmp.toFixed(2);
    $(id + "corporal_mass_index").val(cmi);
  }

  function weight_changed() {
   var index = $(this).attr("id").split("-")[1];
   var id = "#id_medical_interviews-" + index + "-";
   var size = $(id + "size").val();
   var weight = $(this).val();
   if(weight && size) {
    body_surface_area(weight, size, id);
    corporal_mass_index(weight, size, id);
   }
  }

  function size_changed() {
    var index = $(this).attr("id").split("-")[1];
    var id = "#id_medical_interviews-" + index + "-";
    var weight = $(id + "weight").val();
    var size = $(this).val();
    if(weight && size) {
      body_surface_area(weight, size, id);
      corporal_mass_index(weight, size, id);
    }
  }

  function calculate() {
    var i = 0;
    for(i=0; i< $(".inline-related").length; i++) {
      var id = "#id_medical_interviews-" + i + "-";
      $(id + "weight").change(weight_changed);
      $(id + "size").change(size_changed);
    }
  }

  $(".add-row a").live("click", function() {
    calculate();
  });

  if($(".modal-container").length) {
    calculate();


    for(i=0; i< $(".inline-related").length; i++) {
      var id = "#id_medical_interviews-" + i + "-";
      $(id + "weight").trigger("change");
      $(id + "size").trigger("change");
    }

    $(".modal-container").easyModal();
    $(".close-modal").click(function() {
      $(".modal-container").trigger('closeModal');
    });
    $(".calculate-medic").live("click", function(e) {
      console.log("moo");
        e.preventDefault();
        console.log("mmm");

        var parent = $(this).parent().parent();

        var splitted = parent.attr("id").split("-");
        var index = splitted[splitted.length -1];


        var id = "id_medical_interviews-" + index + "-";

        var attr_list = ["performance_status", 'ldh', 'weight', 'size',
        'diatolic_blood_pressure', 'chemotherapy_scheme', 'can_use_phone',
        'can_walk', 'can_shop', 'can_cook', 'can_do_home_work',
        'can_do_manual_work', 'can_self_sanitize', 'taking_medication',
        'can_take_medication', 'can_manage_money', 'orientation_date',
        'orientation_place', 'record', 'atention_calculus', 'memory',
        'lenguage_names', 'lenguage_repeat', 'lenguage_indicate',
        'lenguage_obey', 'lenguage_write', 'lenguage_draw',
        'stopped_eating', 'lost_weight', 'movility', 'had_stress',
        'neorologic_issues'];

        var integers = ['ldh', 'diatolic_blood_pressure', 'size'];
        var floats =  ['weight'];
        var data ={};

        var i = 0;
        var can_send = true;

        for(i=0; i< attr_list.length; i++) {

          var attr = attr_list[i];
          var field = $("#"+ id + attr);
          var container = field.parent().parent();
          console.log($("#"+ id + attr));
          data[attr] = field.val();

          $(".errorlist", container).remove();
          if(!data[attr]) {

            container.prepend("<ul class='errorlist'><li>Este campo es obligatorio</li></ul>");
            can_send = false;

          } else if (integers.indexOf(attr) !== -1) {

            var intRegex = /^\d+$/;
            if(!intRegex.test(data[attr])) {
              container = field.parent().parent();
              container.prepend("<ul class='errorlist'><li>Ingrese un Numero</li></ul>");
              can_send = false;
            }

          } else if (floats.indexOf(attr) !== -1) {

            var floatRegex = /^[-+]?([0-9]*\.[0-9]+|[0-9]+)$/;
            if(!floatRegex.test(data[attr])) {
                container = field.parent().parent();
              container.prepend("<ul class='errorlist'><li>Ingrese un Numero Real</li></ul>");
                can_send = false;
            }
          }
        }


        if(can_send){

          $.ajax({
            url: '/admin/patients/results/',
            type: 'POST',
            async: false,
            data: data,
            success: function(result, e) {
              $(".modal-container .modal").html(result);
              $(".modal-container").trigger('openModal');
            }
          });

        } else {

          $("#fieldsetcollapser0", parent).text(gettext("Hide")).closest("fieldset").removeClass("collapsed").trigger("show.fieldset", [$("#fieldsetcollapser0", parent).attr("id")]);
          $("#fieldsetcollapser1", parent).text(gettext("Hide")).closest("fieldset").removeClass("collapsed").trigger("show.fieldset", [$("#fieldsetcollapser0", parent).attr("id")]);
          $("#fieldsetcollapser2", parent).text(gettext("Hide")).closest("fieldset").removeClass("collapsed").trigger("show.fieldset", [$("#fieldsetcollapser0", parent).attr("id")]);
          $(".modal-container .modal").html("Error en algunos campos");
          $(".modal-container").trigger('openModal');
        }
        return false;
    });
}
})(django.jQuery);