'use strict';

var shoppingListController = function($rootScope, $scope, shoppingListModel) {

  var ctrl = this;
  ctrl.model = shoppingListModel;

  //Initial scope values:
  ctrl.currentItem = null;
  ctrl.allItems = [];
  ctrl.offlineMode = false;

  ctrl.$onInit = function() {
    ctrl.model.listData(ctrl).then(function(resp){
      ctrl.allItems = resp.items;
    });
  };

  ctrl.addItem = function(addedItem) {
    if (addedItem) {
      ctrl.currentItem = null;

      ctrl.model.submitData(ctrl, addedItem).then(function(resp){
        ctrl.allItems.push(resp.shopping_item);
      });
    }
  };

  ctrl.clearItems = function() {
    ctrl.model.clearData(ctrl).then(function(resp){
      if (resp.ok) {
        ctrl.model.listData(ctrl);
      }
    });
  };

  ctrl.updateItem = function(shopping_item) {
    ctrl.model.updateData(ctrl, shopping_item).then(function(resp){
      if (resp.ok) {
        //Reload data from backend:
        ctrl.model.listData(ctrl);
      }
    });
  };

  ctrl.changeOfflineMode = function(mode) {
    console.log(mode);
  }

};

angular
  .module('shoppinglist')
  .component('shoppingList', {
    templateUrl: 'static/shoppinglist/components/shoppinglist/shopping-list.html',
    controller: shoppingListController,
  });
