<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user';

const userStore = useUserStore()
const router = useRouter()
let documents = ref()

onMounted(() => {
    if (!userStore.user.isAuthenticated) {
        router.push('/login')
    } else {
        getDocu()
    }
})

useSeoMeta({
    title: 'My documents',
    ogTitle: 'My documents',
    description: 'The description'
})

async function getDocu() {
    await $fetch('http://127.0.0.1:8000/api/v1/documents/my', {
        headers: {
            'Authorization': 'token ' + userStore.user.token,
            'Content-Type': 'application/json'
        },
    })
        .then(response => {
            documents.value = response
        })
        .catch(error => {
            console.log('error', error)
        })
}

function deleteDocument(id) {
    console.log('id', id)

    documents.value = documents.value.filter(document => document.id !== id)
}


</script>

<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">My Documents</h1>

        <div class="space-y-4">
            <Document v-for="document in documents" :key="document.id" :document="document" :my="true"
                v-on:deleteDocument="deleteDocument(id)" />





        </div>
    </div>
</template>
