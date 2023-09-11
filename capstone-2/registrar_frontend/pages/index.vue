<script setup>

    const { data: documents } = await useFetch('http://127.0.0.1:8000/api/v1/documents/newest/')


</script>
<template>

    <div>
        <Header />
        <div class="py-20 px06 bg-cyan-500 text-center ">
            <h1 class="mb-12 text-5xl text-white">Registrar Operational System</h1>
            <NuxtLink to="/browse" class="inline-block py-4 px-8 bg-teal-900 text-white rounded-xl">Track document
            </NuxtLink>
        </div>

        <div class="py-10 px-6">
            <h2 class="mb-8 text-2xl text-center">Newest documents</h2>
            <div class="space-y-4">
                <document v-for="document in documents" v-bind:key="document.id" v-bind:document="document" />
            </div>
        </div>
        <Footer/>
    </div>
</template>

<style scoped>

</style>