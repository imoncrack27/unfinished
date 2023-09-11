<template>
    <div class="flex h-screen">
        <div class="bg-[#087830] shadow-2xl border-r-4 text-white" :class="toggle ? 'w-1/3' : 'w-20'">
            <button class="pt-3 pb-1 px-2 " @click="toggle = !toggle" :class="toggle ? '' : 'border-b border-white'">
                <span class="hidden">menu</span>
                <i class="fa fa-bars h-10 w-16 text-3xl" :class="toggle ? 'hidden' : 'block'" aria-hidden="true"></i>
                <i class="fa fa-close h-10 w-16 text-3xl" :class="toggle ? 'block' : 'hidden'" aria-hidden="true"></i>

            </button>
            <div>
                <DashboardSideMenu class="bg-[#087830] h-screen w-full " :lists="lists" :hideText="hideText" />
            </div>
        </div>
        <div class="border text-center w-full ">
            dashboard
        </div>

    </div>
</template>

<script setup>

let toggle = ref(false)

const hideText = () => {
    if (toggle) {
        lists.value = false
    }
}
</script>

<style lang="scss" scoped></style>