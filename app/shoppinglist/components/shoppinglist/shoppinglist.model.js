angular.module('shoppinglist')
  .factory('shoppingListModel', function($http) {

    //a method to create new object instance:
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

    //a method to list all object instances:
    function listData(scope) {

      var config = {
        headers: {'Accept': 'application/json'},
      };

      return $http.get('/shopping/list', config)
        .then(function (response) {
          var items = angular.fromJson(response.data);

          scope.allItems = items;
          return {
            items: items,
          };
        })
        .catch(function (response) {
        });
    }

    //a method to clear all object instances:
    function clearData(scope) {

      var config = {
        headers: {'Accept': 'application/json'},
      };

      return $http.get('/shopping/clear', config)
        .then(function (response) {
          return response.data;
        })
        .catch(function (response) {
        });
    }

    return {
      submitData: submitData,
      listData: listData,
      clearData: clearData,
    };
  });
