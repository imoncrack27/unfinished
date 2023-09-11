import { errors, category, title, description, userStore, router } from './request.vue';

export async function submitForm() {
console.log('submitForm');

errors.value = [];

if (category.value == '') { errors.value.push('You must select a category'); }
if (title.value == '') { errors.value.push('The title field is missing'); }
if (description.value == '') { errors.value.push('The description field is missing'); }

if (errors.value.length == 0) {
await $fetch('http://127.0.0.1:8000/api/v1/documents/request/', {
method: 'POST',
headers: {
'Authorization': 'token ' + userStore.user.token,
'Content-Type': 'application/json'
},
body: {
category: category.value,
title: title.value,
description: description.value
}
})
.then(response => {
console.log('response', response);

router.push({ path: '/mydocu' });
})
.catch(error => {
if (error.response) {
for (const property in error.response._data) {
errors.value.push('${ property }: ${ error.response._data[property] }');
}
console.log(JSON.stringify(error.response));
} else if (error.message) {
errors.value.push('Something went wrong. Please try again');

console.log(JSON.stringify(error));
}
});
}
}
