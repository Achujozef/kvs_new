/* Row numbering (continues across server-side pages) and server-side search. */
(function ($) {
  // Number rows of the listing table(s), offset by the current page.
  function numberRows() {
    var start = window.KVS_PAGE_START || 1;
    $('table[id^="table-id"]').each(function () {
      var $table = $(this);
      $table.find('thead tr').first().prepend('<th> ID </th>');
      var id = start;
      $table.find('tbody tr').each(function () {
        $(this).prepend('<td>' + id++ + '</td>');
      });
    });
  }

  // Search runs on the server so it covers every page, not just the visible one.
  function bindSearch() {
    var $input = $('#search_input_all');
    if (!$input.length) return;

    function run(clear) {
      var params = new URLSearchParams(window.location.search);
      var value = clear ? '' : $.trim($input.val());
      if (value) params.set('q', value);
      else params.delete('q');
      params.delete('page');
      var qs = params.toString();
      window.location.href = window.location.pathname + (qs ? '?' + qs : '');
    }

    var $go = $('<button type="button" class="btn btn-warning mt-2 me-2">Search</button>');
    $input.after($go);
    $go.on('click', function () { run(false); });
    if ($.trim($input.val())) {
      var $clear = $('<button type="button" class="btn btn-secondary mt-2">Clear</button>');
      $go.after($clear);
      $clear.on('click', function () { run(true); });
    }
    $input.on('keydown', function (e) {
      if (e.which !== 13) return;
      e.preventDefault();
      run(false);
    });
  }

  $(function () {
    numberRows();
    bindSearch();
  });
})(window.jQuery);
