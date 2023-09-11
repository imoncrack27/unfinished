<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()

function logout() {
 userStore.removeToken()
}
</script>

<template>
 <div>
  <DashboardMenuBar :logout="logout"/>
 </div>
</template>