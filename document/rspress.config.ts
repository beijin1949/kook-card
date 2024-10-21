import * as path from 'path';
import {defineConfig} from 'rspress/config';

export default defineConfig({
    root: path.join(__dirname, 'docs'),
    title: 'kook-card',
    description: '快速构建KMD卡片',
    icon: '/logo.png',
    logo: {
        light: '/logo.png',
        dark: '/logo.png',
    },
    logoText: "kook-card",
    globalStyles: path.join(__dirname, 'styles/tables.css'),
    themeConfig: {
        lastUpdated: true,
        searchPlaceholderText: '搜索文档...',
        searchNoResultsText: '没有找到你想要的东西',
        searchSuggestedQueryText: '建议尝试更换关键词搜索',
        socialLinks: [
            {icon: 'github', mode: 'link', content: 'https://github.com/beijin1949/kook-card'},
            {
                icon: {
                    svg: '<svg width="20px" height="20px" viewBox="0 0 250 245" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n' +
                        '    <g id="页面-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">\n' +
                        '        <g id="KOOK-特殊应用标志">\n' +
                        '            <polygon id="Fill-4974" fill="#000000" points="234.43 0 37.175 0 0 175.98 0 175.99 15.513 204.594 103.367 204.594 125 244.474 147.502 244.474 155.922 204.594 212.848 204.594 250 28.704"></polygon>\n' +
                        '            <polygon id="Fill-4975" fill="#FFFFFF" points="194.3951 22.4776 147.5461 22.4776 113.5271 61.3906 121.7471 22.4776 74.6321 22.4776 43.5301 169.7146 90.6451 169.7146 98.9911 130.2036 120.4221 169.7146 163.2931 169.7146 166.6911 153.6236 138.6351 101.8826 190.0511 43.0526"></polygon>\n' +
                        '        </g>\n' +
                        '    </g>\n' +
                        '</svg>'
                }, mode: 'link', content: 'https://github.com/beijin1949/kook-card'
            },
        ],
        enableContentAnimation: true,
        enableAppearanceAnimation: true,
        enableScrollToTop: true
    },
});
