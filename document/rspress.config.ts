import * as path from 'path';
import { defineConfig } from 'rspress/config';

export default defineConfig({
  root: path.join(__dirname, 'docs'),
  title: 'kook-card',
  description: '快速构建KMD卡片',
  icon: '/logo.png',
  logo: {
    light: '/logo.png',
    dark: '/logo.png',
  },
  themeConfig: {
    socialLinks: [
      { icon: 'github', mode: 'link', content: 'https://github.com/beijin1949/kook-card' },
    ],
  },
});
