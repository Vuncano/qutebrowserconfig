config.load_autoconfig(False)

c.url.searchengines = {
        'DEFAULT': 'https://google.com/search?hl=en&q={}'
}

c.url.start_pages = ['https://google.com/']

c.url.default_page = 'https://google.com/'

config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')

# c.colors.webpage.darkmode.algorithm = 'lightness-hsl'
# c.colors.webpage.darkmode.enabled = True

c.colors.webpage.preferred_color_scheme = 'dark'
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.contrast = 0.0
c.colors.webpage.darkmode.grayscale.all = False
c.colors.webpage.darkmode.grayscale.images = 0.0
c.colors.webpage.darkmode.policy.images = 'smart'
c.colors.webpage.darkmode.policy.page = 'smart'
c.colors.webpage.darkmode.threshold.background = 128
c.colors.webpage.darkmode.threshold.text = 128 
# c.colors.webpage.darkmode.enabled = True


c.fonts.hints = 'default_size default_family'

config.bind('M', 'hint links spawn mpv {hint-url}')

config.unbind('d')
config.bind('dd', 'tab-close')
