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
    $input.on('keydown', function (e) {
      if (e.which !== 13) return;
      e.preventDefault();
      var params = new URLSearchParams(window.location.search);
      var value = $.trim($input.val());
      if (value) params.set('q', value);
      else params.delete('q');
      params.delete('page');
      var qs = params.toString();
      window.location.search = qs ? '?' + qs : '';
    });
  }

  $(function () {
    numberRows();
    bindSearch();
  });
})(window.jQuery);
