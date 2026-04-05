<template>
    <router-link :to="{ name: 'tab', params: { id: 1 } }">Home</router-link> |
    <router-view></router-view>
</template>
