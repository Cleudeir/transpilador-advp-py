import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 8041,
    host: '127.0.0.1',
    allowedHosts: ['pyadvpl.apps.tec.br'],
    proxy: {
      '/api': {
        target: 'http://localhost:8040',
        changeOrigin: true,
      },
    },
  },
})
