import { NuxtLink } from '../.nuxt/components';
<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

function logout() {
    userStore.removeToken()
}
</script>

<template>
    <div>
        <nav class="p-6 flex items-center justify-between bg-dark bg-green-800">
            <NuxtLink to="/" class="text-cl text-white">La Salle University - Ozamis</NuxtLink>

            <div class="flex mt-6 md:mt-0 items-center space-x-4">
                <template v-if="userStore.user.isAuthenticated">

                    <NuxtLink to="/mydocu" class="py-4 px-6 bg-cyan-700 hover:bg-sky-100 text-white rounded-xl">
                        My Documents
                    </NuxtLink>
                    <NuxtLink to="/request" class="py-4 px-6 bg-cyan-500 hover:bg-sky-100 text-white rounded-xl">
                        Request a document
                    </NuxtLink>
                    <a v-on:click="logout" class="py-4 px-6 bg-rose-500 hover:bg-rose-100 text-white rounded-xl">
                        Log out
                    </a>
                </template>

                <template v-else>

                    <NuxtLink to="/login" class="py-4 px-6 bg-cyan-700 hover:bg-sky-100 text-white rounded-xl">
                        Login
                    </NuxtLink>

                    <NuxtLink to="/signup" class="py-4 px-6 bg-cyan-500 hover:bg-sky-100 text-white rounded-xl">Sign up
                    </NuxtLink>
                </template>
            </div>

        </nav>

        <slot />

        <footer class="p-6 flex-wrap items-center justify-around bg-green-900">

            <p class="text-gray-300 ">Copyright (c) 2023 - La Salle University - Ozamis</p>
            <P class="text-gray-300">La Salle St. Barangay Aguada Ozamis city, Misamis Occidental, Philippines</P>



        </footer>
    </div>
</template>