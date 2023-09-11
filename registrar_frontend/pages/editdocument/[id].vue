<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user';

const userStore = useUserStore()
const router = useRouter()
const route = useRoute()

onMounted(() => {
    if (!userStore.user.isAuthenticated) {
        router.push('/login')

    }
})

const { data: document } = await useFetch('http://127.0.0.1:8000/api/v1/documents/' + route.params.id + '/')


let title = ref(document.value.title)
let description = ref(document.value.title)
let errors = ref([])

async function submitForm() {
    console.log('submitForm')

    errors.value = []

    if (title.value == '') { errors.value.push('The title field is missing') }
    if (description.value == '') { errors.value.push('The description field is missing') }

    if (errors.value.length == 0) {
        await $fetch('http://127.0.0.1:8000/api/v1/documents/' + route.params.id + '/edit/', {
            method: 'PUT',
            headers: {
                'Authorization': 'token ' + userStore.user.token,
                'Content-Type': 'application/json'
            },
            body: {
                category: document.value.category,
                title: title.value,
                description: description.value

            }
        })
            .then(response => {
                console.log('response', response)

                router.push({ path: '/mydocu' })
            })
            .catch(error => {
                if (error.response) {
                    for (const property in error.response._data) {
                        errors.value.push('${ property }: ${ error.response._data[property] }')
                    }
                    console.log(JSON.stringify(error.response))
                } else if (error.message) {
                    errors.value.push('Something went wrong. Please try again')

                    console.log(JSON.stringify(error))
                }
            })
    }
}
</script>

<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">Edit Document</h1>

        <form v-on:submit.prevent="submitForm" class="space-y-4">

            <div>
                <label>What kind of document do you want to request</label>
                <input v-model="title" type="text" class="w-full mt-2 p-4 rounded-xl bg-gray-100">
            </div>

            <div>
                <label>What do you want for the document for?</label>
                <textarea v-model="description" class="w-full mt-2 p-4 rounded-xl bg-gray-100"></textarea>

                <div v-if="errors.length" class="mb-6 py-4 px-6 bg-rose-400 text-white rounded-xl">

                    <p v-for="error in errors" v-bind:key="error">
                        {{ error }}
                    </p>
                </div>
            </div>
            <button class="py-4 px-6 bg-teal-700 text-white rounded-xl">Save changes</button>
        </form>
    </div>
</template>