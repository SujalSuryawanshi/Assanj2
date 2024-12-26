from django.contrib import admin
from django.urls import path, include
from .views import Home,login_view, logout_view,send_friend_request, accept_friend_request, delete_friend_request,ListView,FollowStallerView,UnfollowStallerView,register,cat_view, resend_otp_view, staller_survey
from .views import EditPost,add_menu_item, delete_menu_item, edit_menu_item,future,add_foo_category,OfferView, NewOfferView, EditOfferView, delete_offer, like_rater, review_rater, rater_list, edit_profile,  pay_page_view
from . import views
from allauth.socialaccount.providers.google.views import oauth2_login
urlpatterns = [
    path("",Home.as_view(), name='home' ),
    path('register/', views.register, name='register'),
    path('verify-otp/<int:user_id>/', views.verify_otp, name='verify_otp'),
    path('resend-otp/<int:user_id>/', resend_otp_view, name='resend_otp'),
    path('accounts/login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path("place/<slug:name>/", ListView.as_view(), name="detail"),
    path('search', views.search , name='search'),
    path('search/', views.search_users, name='search_users'),
    
    path('send_request/', views.send_friend_request, name='send_friend_request'),
     path('accept_request/', views.accept_friend_request, name='accept_friend_request'),
    path('delete_request/', views.delete_friend_request, name='delete_friend_request'),
    path('per_del/', views.per_del_friend, name='per_del_friend'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/look/<str:username>/', views.user_profile, name='user_profile'),
    
    path('edit/<int:pk>',EditPost.as_view() , name='edit_info'),
    
    path('stallers/<str:name>/follow/', FollowStallerView.as_view(), name='follow_staller'),
    path('stallers/<str:name>/unfollow/', UnfollowStallerView.as_view(), name='unfollow_staller'),
    
    path('staller/<int:staller_id>/add_menu_item/', add_menu_item, name='add_menu_item'),
    path('delete-menu-item/<int:item_id>/', delete_menu_item, name='delete_menu_item'),
    
    path('edit-menu-item/<int:item_id>/', edit_menu_item, name='edit_menu_item'),
    path('add-foo-category/', add_foo_category, name='add_foo_category'),
    path('stall/<slug:name>/offers/', OfferView.as_view(), name='offers'),
    path('stall/<slug:staller_name>/new_offer/', NewOfferView.as_view(), name='new_offer'),
    path('offer/<int:offer_id>/edit/', EditOfferView.as_view(), name='edit_offer'),
    path('offer/<int:offer_id>/delete/', delete_offer, name='delete_offer'),
    
    path("future/", views.future, name="future"),
    path("category/<str:foo>/", views.cat_view, name="category"),
    path('rater/', views.rater_list, name='rater_list'),
    path('like/<int:rater_id>/', views.like_rater, name='like_rater'),
    path('review/<int:rater_id>/', views.review_rater, name='review_rater'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('liker/<int:staller_id>/', views.like_staller, name='like_staller'),
    path('staller/<int:staller_id>/survey/', staller_survey, name='staller_survey'),
    path("pay/<int:staller_id>/paypage", pay_page_view, name="pay"),
    # path("accounts/google/login/",views.google_login, name="google_login")
    path('accounts/google/direct-login/', oauth2_login, name='google_direct_login'),

    ##PAYMENTS##
     path('subscription/', views.subscription_page, name='subscription_page'),
    path('create_order/<str:plan_type>/', views.create_order, name='create_order'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failure/', views.payment_failure, name='payment_failure'),

    #stupid
     path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('refund-cancellation-policy/', views.refund_cancellation_policy, name='refund_cancellation_policy'),
    path('contact-us/', views.contact_page, name='contact_us'),

    ]
