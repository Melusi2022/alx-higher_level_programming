#!/usr/bin/node
/**
 *   * adds a <li> element to a list when the user clicks on the tag DIV#add_item
 *     * use JQuery
 *       */
const $ = window.$;
$('DIV#add_item').click(function () {
	  $('UL.my_list').append('<li
