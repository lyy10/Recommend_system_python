(function($) {
    $.fn.truncatable = function(options) {
        var defaults = {
            limit: 300,
            more: ' [see more...]',
            less: true,
            hideText: ' [see less]'
        };
        var options = $.extend(defaults, options);
        return this.each(function(num) {
            var stringLength = $(this).html().length;
            if (stringLength > defaults.limit) {
                var splitText = $(this).html().substr(defaults.limit);
                var splitPoint = splitText.substr(0, 1);
                var whiteSpace = new RegExp(/^\s+$/);
                for (var newLimit = defaults.limit; newLimit < stringLength; newLimit++) {
                    var newSplitText = $(this).html().substr(0, newLimit);
                    var newHiddenText = $(this).html().substr(newLimit);
                    var newSplitPoint = newSplitText.slice( - 1);
                    if (whiteSpace.test(newSplitPoint)) {
                        var hiddenText = '<span class="hiddenText_' + num + '" style="display:none">' + newHiddenText + '</span>';
                        var setNewLimit = (newLimit - 1);
                        var trunkLink = $('<a>').attr('class', 'more_' + num + '');
                        $(this).html($(this).html().substr(0, setNewLimit)).append('<a class="more_' + num + '" href="#" style="color: green">' + defaults.more + '<a/> ' + hiddenText);
                        $('a.more_' + num).bind('click',
                        function() {
                            $('span.hiddenText_' + num).show();
                            $('a.more_' + num).hide();
                            if (defaults.less == true) {
                                $('span.hiddenText_' + num).append('<a style="color: green" class="hide_' + num + '" href="" title="' + defaults.hideText + '">' + defaults.hideText + '</a>');
                                $('a.hide_' + num).bind('click',
                                function() {
                                    $('.hiddenText_' + num).hide();
                                    $('.more_' + num).show();
                                    $('.hide_' + num).empty();
                                    return false
                                })
                            }
                        });
                        newLimit = stringLength
                    }
                }
            }
        })
    }
})(jQuery);