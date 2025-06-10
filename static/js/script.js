function zeigeInfo(stadt) {
    
    let urlStadt = stadt.toLowerCase().replace(/\s/g, '');

    const urlMap = {
        'bangkok': '/bangkok',
        'hua hin': '/huahin',
        'seka': '/seka',
        'pattaya': '/pattaya'
    };

    let url = urlMap[stadt.toLowerCase()] || '/';

     window.location.href = url;
}







    