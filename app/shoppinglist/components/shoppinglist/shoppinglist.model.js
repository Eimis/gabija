angular.module('shoppinglist')
  .factory('shoppingListModel', function($http) {

    function submitData(scope, shopping_item) {

      var config = {
        headers: {'Accept': 'application/json'},
      };

      var data = {
        shopping_item: shopping_item,
      };

      return $http.post('/shopping/create', data, config)
        .then(function (response) {
          var added_item = angular.fromJson(response.data);
          return {
            shopping_item: added_item,
          };
        })
        .catch(function (response) {
        });
    }

    return {
      submitData: submitData,
    };
  });
