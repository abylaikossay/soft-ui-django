from django.urls import path

from home.views import home, traders, consumer_existing_positions, \
    consumer_target_positions, provider_existing_positions

urlpatterns = [
    path('', home.index, name='index'),

    path('health/', home.health_check, name='health_check'),

    path('traders/', traders.index, name="traders_index"),
    path('traders/add', traders.add, name="traders_add"),
    path('traders/store', traders.store, name="traders_store"),
    path('traders/store-state', traders.store_state, name="store_consumer_state"),
    path('traders/edit/<int:id>', traders.edit, name="traders_edit"),
    path('traders/edit-state/<int:id>', traders.add_state, name="consumer_state_edit"),
    path('traders/update/<int:id>', traders.update, name="traders_update"),
    path('traders/update-state/<int:id>', traders.update_store, name="update_consumer_state"),
    path('traders/delete/<int:id>', traders.delete, name="traders_delete"),

    path('consumer_existing_positions/', consumer_existing_positions.index, name="consumer_existing_positions_index"),
    path('consumer_target_positions/', consumer_target_positions.index, name="consumer_target_positions_index"),
    path('provider_existing_positions/', provider_existing_positions.index, name="provider_existing_positions_index"),
    path('refresh_positions/<int:consumer_id>/', consumer_existing_positions.refresh_positions, name='refresh_positions'),

]
