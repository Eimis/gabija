angular.module('shoppinglist')
  .factory('shoppingListModel', function($http, $q, localStorageService) {

    //a method to create new object instance:
    function submitData(scope, shopping_item) {

      if (scope.offlineMode) {  // ofline mode
        var deferred = $q.defer();

        //FIXME: timezone:
        var new_item = {'name': shopping_item, 'added_on': new Date()};

        deferred.resolve({'shopping_item': new_item});
        return deferred.promise;

      } else { // online mode
        var config = {
          headers: {'Accept': 'application/json'},
        };

        var data = {
          shopping_item: shopping_item,
        };

        return $http.post('/shopping/create', data, config)
          .then(function(response) {
            var added_item = angular.fromJson(response.data);
            return {
              shopping_item: added_item,
            };
          })
          .catch(function(response) {});
      }
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

      if (scope.offlineMode) { // ofline mode
        var deferred = $q.defer();

        localStorageService.set('allItems', []);

        deferred.resolve({'ok': true});
        return deferred.promise;

      } else { // online mode
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
    }

    //a method to update object instance:
    function updateData(scope, updated_item) {

      var config = {
        headers: {'Accept': 'application/json'},
      };

      var data = {
        updated_item: updated_item,
      };

      return $http.post('/shopping/update', data, config)
        .then(function (response) {
          var updated_item = angular.fromJson(response.data);
          return {
            updated_item: updated_item,
          };
        })
        .catch(function (response) {
        });
    }

    return {
      submitData: submitData,
      listData: listData,
      clearData: clearData,
      updateData: updateData,
    };
  });
