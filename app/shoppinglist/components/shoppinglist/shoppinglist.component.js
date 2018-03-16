'use strict';

var shoppingListController = function($rootScope, $scope, shoppingListModel) {

  var ctrl = this;
  ctrl.model = shoppingListModel;

  ctrl.$onInit = function() {
  };

  //Initial scope values:
  ctrl.currentItem = null;
  ctrl.allItems = [];

  ctrl.addItem = function(addedItem) {
    if (addedItem) {
      ctrl.currentItem = null;

      ctrl.model.submitData(ctrl, addedItem).then(function(resp){
        ctrl.allItems.push(resp.shopping_item);
      });
    }
  };

};

angular
  .module('shoppinglist')
  .component('shoppingList', {
    templateUrl: 'static/shoppinglist/components/shoppinglist/shopping-list.html',
    controller: shoppingListController,
  });
