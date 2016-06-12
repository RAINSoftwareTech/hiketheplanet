
   $('#mapModal').on('show.bs.modal', function (event) {
      var button = $(event.relatedTarget); // Button that triggered the modal
      var region = button.data('region'); // Extract info from data-* attributes
      var searchUrl = button.data('search-url');
      // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
      // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
      var modal = $(this);
      modal.find('.modal-title').text(region + ' Trailheads');
      askForPlots(region, searchUrl);
    });

    $('#mapModal').on('shown.bs.modal', function(){
        setTimeout(function() {
            map.invalidateSize();
       }, 1);
    });