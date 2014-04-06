from trialshop import views
from django.conf.urls import patterns,url

urlpatterns=patterns('',

	url(r'^$',views.loginform.as_view(), name='login'),
		
	url(r'^signup$',views.signup.as_view(), name='signup'),
	url(r'^login_request/login$',views.loginform.as_view(), name='index'),
	url(r'^signup_request/login$',views.signup.as_view(), name='index'),
	url(r'^index$',views.IndexView.as_view(), name='index'),
	url(r'^category/(?P<category_id>\d+)/$',views.CategoryView.as_view(),name="category"),
	url(r'^desc/(?P<category_id>\d+)/$',views.DescView.as_view(),name="description"),
	url(r'^cart/(?P<cart_id>\d+)/$',views.AddToCart,name="cart"),
	url(r'^rmv/(?P<cart_id>\d+)/$',views.CartRemove,name="cartremove"),
	url(r'^cartbasket$',views.CartView.as_view(),name="basket"),
	# url(r'^form/(?P<cart_id>\d+)/$',views.cartform.as_view(), name='index'),
	url(r'^logout$',views.logout_view,name="login"),
	url(r'^login_request/$',views.login_request,name="login"),
	url(r'^signup_request/$',views.signup_request,name="signup"),
	url(r'^about/$',views.about.as_view(),name="basket"),
	
	# url(r'^f/$',views.user_auth(),name="form"),

	)
