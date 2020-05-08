$(function() {
    $('#payment-form').submit(function() {
        var form = this;
        var card = {
            number: $('#id_credit_card_number').val(),
            expMonth: $('#id_expiry_month').val(),
            expYear: $('#id_expiry_year').val(),
            cvc: $('#id_cvv').val(),
        };
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            /*
             Added a conditional to ensure the cvv field is always 3 digits as stripe allows it be be authenticated
             when blank and when 3 or more digits.
             I Adapted this piece of code a fellow CI student pointed me to in the slack chat. Posted by user DaveL
             */
            if ($('#id_cvv')[0].value.length != 3) {
                showStripeErrors('Your cards cvv code is invalid');
            } else {
                $('#credit-card-errors').hide();
                $('#id_stripe_id').val(response.id);
            }

            //Prevent the credit card details from being submitted to our own server
            $('#id_credit_card_number').removeAttr('name');
            $('#id_cvv').removeAttr('name');
            $('#id_expiry_month').removeAttr('name');
            $('#id_expiry_year').removeAttr('name');

            form.submit();
        } else {
            $('#stripe-error-message').text(response.error.message);
            $('#credit-card-errors').show();
            $('#validate-card-btn').attr('disabled', false);
        }
    });
    return false;
    });
});