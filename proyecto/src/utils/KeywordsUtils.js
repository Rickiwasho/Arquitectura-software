module.exports = {
    isInMessage: (message, keywords) => {
        return (keywords.filter(
            keyword => (message.split(/\W+/).length > 1)
                ? message.toLowerCase().includes(keyword) :
                message.toLowerCase() === keyword

        ).length ) > 0;
    },

    isAllInMessage: (message, keywords) => {
        return (keywords.filter(
            n => message.toLowerCase().includes(n)
        ).length ) == keywords.length;
    }
}