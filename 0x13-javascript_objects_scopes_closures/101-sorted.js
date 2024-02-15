#!/usr/bin/node

const dict = require('./101-data').dict;

const occurrencesById = {};

for (const userID in dict)
{
	const occurrences = dict[userId];
	if (occurrences in occurrencesById)
	{
		occurrencesById[uccurrences].push(userId);
	}
	else
	{
		occurrencesById[occurrences] = [userId];
	}
}

console.log(occurencesById);
