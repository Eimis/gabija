'use strict';

var shoppingListController = function($rootScope, $scope) {

  var ctrl = this;
  //ctrl.model = ticTacModel;

  ctrl.$onInit = function() {
  };

};

angular
  .module('shoppinglist')
  .component('shoppingList', {
    templateUrl: 'static/shoppinglist/components/shoppinglist/shopping-list.html',
    controller: shoppingListController,
  });
