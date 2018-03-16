'use strict';

var shoppingListController = function($rootScope, $scope) {

  var ctrl = this;
  //ctrl.model = ticTacModel;

  ctrl.$onInit = function() {
  };

  //Initial scope values:
  ctrl.currentItem = null;
  ctrl.allItems = [];

  ctrl.addItem = function(addedItem) {
    if (addedItem) {
      ctrl.allItems.push(addedItem);
      ctrl.currentItem = null;
      console.log(ctrl.allItems);
    }
  };

};

angular
  .module('shoppinglist')
  .component('shoppingList', {
    templateUrl: 'static/shoppinglist/components/shoppinglist/shopping-list.html',
    controller: shoppingListController,
  });
