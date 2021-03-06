module.exports = {
    moneyFormatter: (amount) => {
        const moneyFormatter = new Intl.NumberFormat('en_US', {
            style: 'currency',
            currency: 'USD'
        });
        return moneyFormatter.format(amount);
    },
    decimalFormatter: (amount) => {
        if((Math.abs(amount) > 999) && (Math.abs(amount) <= 999999)){
            return Math.sign(amount)*((Math.abs(amount)/1000).toFixed(1))+'k';

        }else if((Math.abs(amount)>999999) && (Math.abs(amount)<= 999999999)){
            return Math.sign(amount)*((Math.abs(amount)/1000000).toFixed(1))+ 'million'
        }
        else {
            return Math.sign(amount)*((Math.abs(amount)/1000000000).toFixed(1))+ 'billion'
        }
    }
}