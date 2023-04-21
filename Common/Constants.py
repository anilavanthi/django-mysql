
class Profiles:
    storeuser = 4
    salesuser = 6

class Note:
    welcome_subject_touser ="Welcome to Wheelsmart"
    welcome_body_touser ="Welcome to Wheelsmart. Last Login time: {0}."
    
   
class SMS:
    
    postfix ="\nFrom,\nWheelsmart."

    loginotp="Please used this OTP {otp} to Login your application By Wheelsmart.."

    welcome_touser ="Welcome to Wheelsmart. Your login details are as follows:\n\nUsername: {username}\nPassword: {password}"

    purchase_create_customer ="Dear {customername}\n Thank You for your Sale"
    sale_create_customer ="Dear {customername}\n Thank You for your Purchase "
    salequotation_create_customer ="Dear {customername}\n Thank You for asking SaleQuotation to this counter"
    purchasequotation_create_customer ="Dear {customername}\n Thank You for asking PurchaseQuotation to this counter"
    ovfquotation_create_customer ="Dear {customername}\n Thank You for asking OVFQuotation to this counter"
    enquiry_create_customer ="Dear {customername}\n Thank You for asking Enquiry for this counter"

    socketio_create_purchase =" Thank You for your Sale wheelsmart to this counter"
    socketio_create_sale =" Thank You for your Purchase wheelsmart to this counter"

       
class Email:
    
    postfix ="\nFrom,\nWheelsmart."

    welcome_subject_touser ="Welcome to Wheelsmart"
    welcome_body_touser ="Welcome to Wheelsmart. Please login to your account."


    