import os
from flask import Flask, send_from_directory, Response

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=BASE_DIR)

def inject_global_redirect(html_content):
    """
    Doğru eklenti linkini bağlar, tıklanma sorunlarını çözmek için 
    tüm dinamik altyapıyı (assets/skins) yönlendirir ve kontrol panelini sunar.
    """
    
    # 1. Stil Tanımlamaları (Mor temalı yuvarlak buton ve panel tasarımı)
    panel_style = """
    <style>
        #cors-control-panel {
            position: fixed;
            bottom: 70px;
            right: 20px;
            z-index: 999999;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: rgba(45, 12, 54, 0.95);
            color: #fff;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
            width: 290px;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            font-size: 13px;
            border: 1px solid #8e44ad;
        }
        #cors-control-panel.collapsed {
            width: 45px;
            height: 45px;
            padding: 0;
            overflow: hidden;
            border-radius: 50%;
            background: #8e44ad;
            cursor: pointer;
            bottom: 70px;
        }
        #cors-toggle-btn {
            float: right;
            cursor: pointer;
            font-weight: bold;
            background: rgba(255,255,255,0.2);
            padding: 2px 7px;
            border-radius: 4px;
            font-size: 11px;
        }
        #cors-control-panel.collapsed #cors-toggle-btn {
            float: none;
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: transparent;
            font-size: 18px;
        }
        #cors-panel-content h4 { margin: 0 0 8px 0; color: #e1b12c; font-size: 14px; }
        #cors-panel-content p { margin: 0 0 10px 0; line-height: 1.4; color: #f5f5f5; }
        .cors-btn {
            display: block;
            background: #27ae60;
            color: white;
            text-decoration: none;
            padding: 8px 12px;
            border-radius: 6px;
            font-weight: bold;
            text-align: center;
            margin-top: 5px;
            transition: background 0.2s;
            border: none;
        }
        .cors-btn:hover { background: #2ecc71; }
    </style>
    """

    # 2. JavaScript Mantığı (Genişletilmiş İstek Yakalama ve Doğru Link)
    redirect_script = """
    <script>
    (function() {
        // --- 1. GENİŞLETİLMİŞ XHR PROXY (Tıklama ve Toolbar Sorunlarını Çözen Kısım) ---
        var proxiedOpen = window.XMLHttpRequest.prototype.open;
        window.XMLHttpRequest.prototype.open = function(method, url, async, user, pass) {
            
            // Sadece 'slides/' değil, butonların ve interaktif modüllerin çalışması için gereken yolları da yakala
            var targets = ['slides/', 'assets/', 'skins/', 'slideview/'];
            var shouldRedirect = targets.some(function(target) { return url.includes(target); });
            
            if (shouldRedirect) {
                if (!url.startsWith('http')) {
                    // Local urlyi temizle ve ana siteye bağla
                    var cleanUrl = url;
                    if (url.startsWith('/')) { cleanUrl = url.substring(1); }
                    
                    // Eğer istek o anki klasör yapısına göre alt dizinden atılıyorsa temizle
                    if (cleanUrl.includes('slideview/')) {
                        cleanUrl = cleanUrl.substring(cleanUrl.indexOf('slideview/'));
                    }
                    
                    url = "https://histologyguide.com/" + cleanUrl;
                }
                console.log("[Sistem Yönlendirmesi Aktif] ->", url);
            }
            return proxiedOpen.apply(this, [method, url, async, user, pass]);
        };

        // --- 2. KONTROL PANELİ VE DOĞRU EKLENTİ LİNKİ ---
        window.addEventListener('DOMContentLoaded', function() {
            var panel = document.createElement('div');
            panel.id = 'cors-control-panel';
            panel.className = 'collapsed'; 
            
            panel.innerHTML = `
                <div id="cors-toggle-btn">⚙️</div>
                <div id="cors-panel-content" style="display:none;">
                    <h4>🔬 Slayt Bağlantı Paneli</h4>
                    <p>Slayt işaretçilerinin ve interaktif butonların eksiksiz çalışması için tarayıcınızda tek seferlik CORS izni aktif olmalıdır.</p>
                    <p><strong>Eğer butonlar çalışmıyor veya slayt yüklenmediyse:</strong></p>
                    <a href="https://chromewebstore.google.com/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf" target="_blank" class="cors-btn">Eklentiyi Kur / Aç (Chrome)</a>
                    <div style="margin-top:8px; font-size:11px; color:#ccc; text-align:center;">Eklentiyi kurduktan sonra uzantı simgesine tıklayıp aktif (Yeşil) hale getirmeyi unutmayın.</div>
                </div>
            `;
            document.body.appendChild(panel);

            var toggleBtn = document.getElementById('cors-toggle-btn');
            var content = document.getElementById('cors-panel-content');

            function togglePanel() {
                if (panel.classList.contains('collapsed')) {
                    panel.classList.remove('collapsed');
                    toggleBtn.innerText = '✕';
                    setTimeout(() => { content.style.display = 'block'; }, 100);
                } else {
                    content.style.display = 'none';
                    panel.classList.add('collapsed');
                    toggleBtn.innerText = '⚙️';
                }
            }

            toggleBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                togglePanel();
            });
            
            panel.addEventListener('click', function() {
                if (panel.classList.contains('collapsed')) {
                    togglePanel();
                }
            });
        });
    })();
    </script>
    """
    
    # Payload'ı enjekte et
    payload = panel_style + redirect_script
    if "</head>" in html_content:
        return html_content.replace("</head>", payload + "</head>")
    return payload + html_content

@app.route('/')
def index():
    index_path = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8", errors="ignore") as f:
            return inject_global_redirect(f.read())
    return "index.html bulunamadı."

@app.route('/<path:filename>')
def serve_all(filename):
    file_path = os.path.join(BASE_DIR, filename)
    if filename.endswith('.html') and os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return Response(inject_global_redirect(f.read()), mimetype='text/html')
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    # Hem Render ortam değişkenlerini (PORT) dinler hem de yerel çakışmaları tamamen önler.
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)