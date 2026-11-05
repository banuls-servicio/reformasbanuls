#!/usr/bin/env python3
"""
Web Leads & SEO/AEO/GEO Architect CLI
--------------------------------------
Herramienta de automatización para auditar y reconstruir páginas web locales
a partir de fuentes de datos (Google Maps, Instagram, Web Antigua, Canva).
"""

import os
import sys
import re
import json
import argparse
import urllib.request

def fetch_url(url):
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"[!] Error al descargar {url}: {e}")
        return ""

def extract_nap_and_data(html_content):
    data = {
        "phones": list(set(re.findall(r'(\+?34\s?[6789]\d{2}[\s\.-]?\d{3}[\s\.-]?\d{3}|[6789]\d{2}[\s\.-]?\d{3}[\s\.-]?\d{3})', html_content))),
        "emails": list(set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', html_content))),
        "images": list(set(re.findall(r'(https?://[^\s"\'>]+\.(?:png|jpg|jpeg|webp|svg))', html_content)))
    }
    return data

def main():
    parser = argparse.ArgumentParser(description="Web Leads Re-engineering Agent")
    parser.add_argument("--name", required=True, help="Nombre del negocio (ej: 'Ventanas Bañuls')")
    parser.add_argument("--maps", help="URL de Google Maps")
    parser.add_argument("--site", help="URL del sitio web actual")
    parser.add_argument("--instagram", help="URL o handle de Instagram")
    parser.add_argument("--canva", help="URL de Canva site si existe")
    parser.add_argument("--output", default="output", help="Directorio de salida")
    
    args = parser.parse_args()
    print(f"[*] Iniciando Web Leads Architect para: {args.name}")
    os.makedirs(args.output, exist_ok=True)
    
    extracted_data = {"name": args.name, "sources": {}}
    if args.site:
        print(f"[*] Analizando sitio web actual: {args.site}")
        content = fetch_url(args.site)
        extracted_data["sources"]["site"] = extract_nap_and_data(content)
        
    if args.canva:
        print(f"[*] Analizando recursos de Canva: {args.canva}")
        content = fetch_url(args.canva)
        extracted_data["sources"]["canva"] = extract_nap_and_data(content)
        
    summary_path = os.path.join(args.output, "extracted_audit.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=2, ensure_ascii=False)
        
    print(f"[+] Auditoría de extracción guardada en {summary_path}")
    print("[+] Listo para generar estrategia SEO/AEO/GEO y frontend de alta conversión.")

if __name__ == "__main__":
    main()
