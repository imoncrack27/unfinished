import { Title } from '../.nuxt/components';
<script setup>
import { useUserStore } from '@/stores/user';

const userStore = useUserStore()
const emit = defineEmits(['deleteDocument'])

const props = defineProps({
    my: {
        type: [Boolean]
    },
    document: {
        type: [Object]
    }
}
)

async function deleteDocument(id) {
    await $fetch('http://127.0.0.1:8000/api/v1/documents/' + id + '/delete/', {
        method: 'DELETE',
        headers: {
            'Authorization': 'token ' + userStore.user.token,
            'Content-Type': 'application/json'
        },
    })
        .then(response => {
            console.log('response', response)

            emit('deleteDocument', id)
        })
        .catch(error => {
            console.log(error)
        })
}
</script>

<template>
    <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
        <div>
            <h3 class="mb-2 text-xl font-semibold">{{ document.title }}</h3>
            <p class="text-gray-600">{{ document.company_name }}</p>


        </div>
        <div>
            <p class="mb-2">{{ document.position_location }}</p>
            <p>{{ document.position_status }}</p>
        </div>

        <div>
            <p>Date Requested {{ document.created_at_formatted }} </p>
        </div>

        <div class="space-x-4">
            <NuxtLink v-bind:to="'/browse/' + document.id" class="py-4 px-6 bg-teal-700 text-white rounded-xl">Details
            </NuxtLink>
            <NuxtLink v-bind:to="'/editdocument/' + document.id" class="py-4 px-6 bg-cyan-700 text-white rounded-xl"
                v-if="my">Edit</NuxtLink>
            <a @click="deleteDocument(document.id)" class="py-4 px-6 bg-rose-700 text-white rounded-xl" v-if="my">Delete</a>
        </div>
    </div>
</template>