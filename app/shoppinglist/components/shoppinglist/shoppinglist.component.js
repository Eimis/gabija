'use strict';

var shoppingListController = function($rootScope, $scope, shoppingListModel, localStorageService) {

  var ctrl = this;
  ctrl.model = shoppingListModel;

  //Initial scope values:
  ctrl.currentItem = null;
  ctrl.allItems = [];

  ctrl.$onInit = function() {
    var offlineMode = localStorageService.get('offlineMode');
    ctrl.offlineMode = offlineMode || false;  // can be null

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
        ctrl.model.listData(ctrl).then(function(resp){
          ctrl.allItems = resp.items;
        });
      }
    });
  };

  ctrl.updateItem = function(shopping_item) {
    ctrl.model.updateData(ctrl, shopping_item).then(function(resp){
      if (resp.ok) {
        ctrl.model.listData(ctrl).then(function(resp){
          ctrl.allItems = resp.items;
        });
      }
    });
  };

  ctrl.changeOfflineMode = function(offlineMode) {
    localStorageService.set('offlineMode', ctrl.offlineMode);

    //If mode is changed from online to offline, nothing needs to be done because
    //items are always saved into local storage anyway.
    //If we're going back to online mode, database has to be updated with new
    //items:
    if (!offlineMode) { // we're switching to online mode
      var current_items = localStorageService.get('allItems');

      ctrl.model.syncData(ctrl, current_items);
    }
  };

};

angular
  .module('shoppinglist')
  .component('shoppingList', {
    templateUrl: 'static/shoppinglist/components/shoppinglist/shopping-list.html',
    controller: shoppingListController,
  });
