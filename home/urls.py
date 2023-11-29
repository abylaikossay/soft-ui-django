from django.urls import path

from home.views import home, traders, consumer_existing_positions, \
    consumer_target_positions, provider_existing_positions

urlpatterns = [
    path('', home.index, name='index'),

    path('health/', home.health_check, name='health_check'),

    path('traders/', traders.index, name="traders_index"),
    path('traders/edit/<int:id>', traders.edit, name="traders_edit"),

    path('consumer_existing_positions/', consumer_existing_positions.index, name="consumer_existing_positions_index"),
    path('consumer_target_positions/', consumer_target_positions.index, name="consumer_target_positions_index"),
    path('provider_existing_positions/', provider_existing_positions.index, name="provider_existing_positions_index"),
]
