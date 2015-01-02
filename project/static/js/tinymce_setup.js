tinyMCE.init({

    mode: 'textareas',
    theme: 'advanced',
    skin: 'grappelli',

    accessibility_warnings: false,
    browsers: 'gecko,msie,safari,opera',
    dialog_type: 'window',
    editor_deselector: 'mceNoEditor',
    keep_styles: false,
    language: 'en',
    object_resizing: false,
    plugins: 'advlink,paste,media,grappelli',

    element_format: 'xhtml',
    fix_list_elements: true,
    forced_root_block: 'p',
    style_formats: [
        {title: 'Paragraph Small', block: 'p', classes: 'p_small'},
        {title: 'Paragraph ImageCaption', block: 'p', classes: 'p_caption'},
        {title: 'Clearfix', block: 'p', classes: 'clearfix'},
        {title: 'Code', block: 'p', classes: 'code'}
    ],
    verify_html: true,

    relative_urls: false,
    remove_script_host: true,

    width: 658,
    height: 300,
    indentation: '10px',

    content_css: "/static/css/otessier-tinymce.css",

    theme_advanced_toolbar_location: 'top',
    theme_advanced_toolbar_align: 'left',
    theme_advanced_statusbar_location: 'bottom',
    theme_advanced_buttons1: 'formatselect,styleselect,|,bold,italic,underline,|,bullist,numlist,blockquote,|,undo,redo,|,link,unlink,|,grappelli_adv',
    theme_advanced_buttons2: 'pasteword,template,media,charmap,|,code,|,table,cleanup,grappelli_documentstructure',
    theme_advanced_buttons3: '',
    theme_advanced_path: false,
    theme_advanced_blockformats: 'p,h1,h2,h3,h4,pre',
    theme_advanced_resizing: false,
    theme_advanced_resize_horizontal: false,
    theme_advanced_resizing_use_cookie: true,

    advlink_styles: 'Internal Link=internal;External Link=external',

    grappelli_adv_hidden: true,
    grappelli_show_documentstructure: 'on'
});

