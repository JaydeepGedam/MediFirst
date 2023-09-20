/**
* PHP Email Form Validation - v2.3
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/
!(function ($) {
  "use strict";

  $('form.contact-form').submit(function (e) {
    e.preventDefault();

    var f = $(this).find('.form-group'),
      ferror = false,
      emailExp = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;

    f.children('input').each(function () { // run all inputs

      var i = $(this); // current input
      var rule = i.attr('data-rule');

      if (rule !== undefined) {
        var ierror = false; // error flag for current input
        var pos = rule.indexOf(':', 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1, rule.length);
          rule = rule.substr(0, pos);
        } else {
          rule = rule.substr(pos + 1, rule.length);
        }

        switch (rule) {
          case 'required':
            if (i.val() === '') {
              ferror = ierror = true;
            }
            break;

          case 'minlen':
            if (i.val().length < parseInt(exp)) {
              ferror = ierror = true;
            }
            break;

          case 'email':
            if (!emailExp.test(i.val())) {
              ferror = ierror = true;
            }
            break;

          case 'checked':
            if (!i.is(':checked')) {
              ferror = ierror = true;
            }
            break;

          case 'regexp':
            exp = new RegExp(exp);
            if (!exp.test(i.val())) {
              ferror = ierror = true;
            }
            break;
        }
        i.next('.validate').html((ierror ? (i.attr('data-msg') !== undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
      }
    });
    f.children('textarea').each(function () { // run all inputs

      var i = $(this); // current input
      var rule = i.attr('data-rule');

      if (rule !== undefined) {
        var ierror = false; // error flag for current input
        var pos = rule.indexOf(':', 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1, rule.length);
          rule = rule.substr(0, pos);
        } else {
          rule = rule.substr(pos + 1, rule.length);
        }

        switch (rule) {
          case 'required':
            if (i.val() === '') {
              ferror = ierror = true;
            }
            break;

          case 'minlen':
            if (i.val().length < parseInt(exp)) {
              ferror = ierror = true;
            }
            break;
        }
        i.next('.validate').html((ierror ? (i.attr('data-msg') != undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
      }
    });
    if (ferror) return false;

    var this_form = $(this);
    var action = $(this).attr('action');

    if (!action) {
      this_form.find('.loading').slideUp();
      this_form.find('.error-message').slideDown().html('The form action property is not set!');
      return false;
    }

    this_form.find('.sent-message').slideUp();
    this_form.find('.error-message').slideUp();
    this_form.find('.loading').slideDown();

    if ($(this).data('recaptcha-site-key')) {
      var recaptcha_site_key = $(this).data('recaptcha-site-key');
      grecaptcha.ready(function () {
        grecaptcha.execute(recaptcha_site_key, { action: 'php_email_form_submit' }).then(function (token) {
          form_submit(this_form, action, this_form.serialize() + '&recaptcha-response=' + token);
        });
      });
    } else {
      form_submit(this_form, action, this_form.serialize());
    }

    return true;
  });

  function form_submit(this_form, action, data) {
    $.ajax({
      type: "POST",
      url: action,
      data: data,
      timeout: 40000
    }).done(function (data1) {
      if (data1.msg) {
        this_form.find('.loading').slideUp();
        this_form.find('.sent-message').slideDown();
        this_form.find("input:not(input[type=submit]), textarea").val('');
      }

    }).fail(function (data) {
      // console.log(data);
      var error_msg = "Form submission failed!<br>";
      if (!data.msg) {
        this_form.find('.loading').slideUp();
        this_form.find('.error-message').slideDown().html(error_msg);
      }
    });
  }

})(jQuery);



!(function ($) {
  "use strict";

  $('form.appointment-form').submit(function (e) {
    e.preventDefault();

    var f = $(this).find('.form-group'),
      ferror = false,
      emailExp = /^[^\s()<>@,;:\/]+@\w[\w\.-]+\.[a-z]{2,}$/i;

    f.children('input').each(function () { // run all inputs

      var i = $(this); // current input
      var rule = i.attr('data-rule');

      if (rule !== undefined) {
        var ierror = false; // error flag for current input
        var pos = rule.indexOf(':', 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1, rule.length);
          rule = rule.substr(0, pos);
        } else {
          rule = rule.substr(pos + 1, rule.length);
        }

        switch (rule) {
          case 'required':
            if (i.val() === '') {
              ferror = ierror = true;
            }
            break;

          case 'minlen':
            if (i.val().length < parseInt(exp)) {
              ferror = ierror = true;
            }
            break;

          case 'email':
            if (!emailExp.test(i.val())) {
              ferror = ierror = true;
            }
            break;

          case 'checked':
            if (!i.is(':checked')) {
              ferror = ierror = true;
            }
            break;

          case 'regexp':
            exp = new RegExp(exp);
            if (!exp.test(i.val())) {
              ferror = ierror = true;
            }
            break;
        }
        i.next('.validate').html((ierror ? (i.attr('data-msg') !== undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
      }
    });
    f.children('textarea').each(function () { // run all inputs

      var i = $(this); // current input
      var rule = i.attr('data-rule');

      if (rule !== undefined) {
        var ierror = false; // error flag for current input
        var pos = rule.indexOf(':', 0);
        if (pos >= 0) {
          var exp = rule.substr(pos + 1, rule.length);
          rule = rule.substr(0, pos);
        } else {
          rule = rule.substr(pos + 1, rule.length);
        }

        switch (rule) {
          case 'required':
            if (i.val() === '') {
              ferror = ierror = true;
            }
            break;

          case 'minlen':
            if (i.val().length < parseInt(exp)) {
              ferror = ierror = true;
            }
            break;
        }
        i.next('.validate').html((ierror ? (i.attr('data-msg') != undefined ? i.attr('data-msg') : 'wrong Input') : '')).show('blind');
      }
    });
    if (ferror) return false;

    var this_form = $(this);
    var action = $(this).attr('action');

    if (!action) {
      this_form.find('.loading').slideUp();
      this_form.find('.error-message').slideDown().html('The form action property is not set!');
      return false;
    }

    this_form.find('.sent-message').slideUp();
    this_form.find('.error-message').slideUp();
    this_form.find('.loading').slideDown();

    if ($(this).data('recaptcha-site-key')) {
      var recaptcha_site_key = $(this).data('recaptcha-site-key');
      grecaptcha.ready(function () {
        grecaptcha.execute(recaptcha_site_key, { action: 'php_email_form_submit' }).then(function (token) {
          form_submit(this_form, action, this_form.serialize() + '&recaptcha-response=' + token);
        });
      });
    } else {
      form_submit(this_form, action, this_form.serialize());
    }

    return true;
  });

  function form_submit(this_form, action, data) {
    $.ajax({
      type: "POST",
      url: action,
      data: data,
      timeout: 40000
    }).done(function (data) {
      console.log(data);
      if (data.msg) {
        this_form.find('.loading').slideUp();
        this_form.find('.sent-message').slideDown();

        var date = new Date();

        var day = date.getDate();
        var month = date.getMonth() + 1;
        var year = date.getFullYear();

        if (month < 10) month = "0" + month;
        if (day < 10) day = "0" + day;

        var today = year + "-" + month + "-" + day;

        this_form.find("input:not(input[type=submit]), textarea").val('');
        $('#tddate').val(today);
      }
      else {
        console.log(data);
        var error_msg = "Form submission failed! Please Login First or Check your form values<br>";
        if (!data.msg) {
          this_form.find('.loading').slideUp();
          this_form.find('.error-message').slideDown().html(error_msg);
        }
      }
    })

  }

})(jQuery);
