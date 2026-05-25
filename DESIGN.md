---
name: Deep Tech Assurance
colors:
  surface: '#031713'
  surface-dim: '#031713'
  surface-bright: '#283d38'
  surface-container-lowest: '#00110e'
  surface-container-low: '#0a1f1b'
  surface-container: '#0e231f'
  surface-container-high: '#192e29'
  surface-container-highest: '#243934'
  on-surface: '#d0e8e0'
  on-surface-variant: '#d0c5b5'
  inverse-surface: '#d0e8e0'
  inverse-on-surface: '#20342f'
  outline: '#998f81'
  outline-variant: '#4d463a'
  surface-tint: '#e5c280'
  primary: '#ffe2af'
  on-primary: '#402d00'
  primary-container: '#e8c583'
  on-primary-container: '#6a511a'
  inverse-primary: '#755a23'
  secondary: '#a7cfc2'
  on-secondary: '#10362e'
  secondary-container: '#2b5046'
  on-secondary-container: '#99c1b5'
  tertiary: '#dfe5ff'
  on-tertiary: '#202f54'
  tertiary-container: '#bac9f6'
  on-tertiary-container: '#45547a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdea3'
  primary-fixed-dim: '#e5c280'
  on-primary-fixed: '#261900'
  on-primary-fixed-variant: '#5b430d'
  secondary-fixed: '#c3ebde'
  secondary-fixed-dim: '#a7cfc2'
  on-secondary-fixed: '#00201a'
  on-secondary-fixed-variant: '#294d44'
  tertiary-fixed: '#dae2ff'
  tertiary-fixed-dim: '#b7c6f2'
  on-tertiary-fixed: '#081a3d'
  on-tertiary-fixed-variant: '#37466b'
  background: '#031713'
  on-background: '#d0e8e0'
  surface-variant: '#243934'
  accent-cream: '#FBDDAF'
  pure-white: '#FFFFFF'
  surface-deep: '#022B23'
typography:
  display-lg:
    fontFamily: hankenGrotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: 80px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: hankenGrotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-xl:
    fontFamily: hankenGrotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: hankenGrotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  body-lg:
    fontFamily: hankenGrotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: hankenGrotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: hankenGrotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-desktop: 80px
  margin-mobile: 20px
  section-gap: 120px
---

## Brand & Style

This design system embodies a premium, high-stakes engineering aesthetic. It is tailored for a sophisticated technical audience that values precision, security, and elite-level quality assurance. 

The style is **Modern Corporate** with a **Minimalist** edge, utilizing a "Dark Mode" first approach to evoke a high-end developer environment. It relies on high-contrast typography, expansive whitespace to signal luxury and clarity, and subtle, smooth motion patterns that suggest a liquid-fast, modern interface. The visual narrative is one of deep-tech reliability—where engineering rigor meets refined, cutting-edge design.

## Colors

The palette is anchored by a deep, sophisticated forest-black (`#022B23` and `#011410`) which provides a luxurious, tech-forward canvas. The primary accent is a refined gold-tan (`#E8C583`), used strategically for calls to action and key highlights to break the dark aesthetic without appearing aggressive.

- **Backgrounds:** Use the near-black `#011410` for main page backgrounds and `#022B23` for elevated containers or sections.
- **Accents:** Use `#E8C583` for primary interactions. Use `#FBDDAF` for softer highlights or secondary visual interest.
- **Text:** High-contrast `#FFFFFF` for primary headings; use reduced opacity white (70-80%) for secondary body text to maintain a premium feel.

## Typography

The system utilizes **Hanken Grotesk** as a precise, modern alternative to Satoshi, maintaining a clean, geometric feel that balances technicality with approachability. 

- **Headlines:** Should be bold and impactful with slight negative letter-spacing to create a "locked-in" professional look.
- **Body Text:** Ample line-height is essential to maintain the "generous whitespace" philosophy, ensuring long-form technical content remains highly readable.
- **Labels:** Use uppercase for small labels and badges to inject a sense of utility and engineering rigor.

## Layout & Spacing

This design system follows a **Fixed Grid** approach for desktop to control line lengths and maintain a premium, editorial feel. 

- **Grid:** 12-column layout for desktop with 24px gutters.
- **Whitespace:** Emphasize vertical rhythm with large section gaps (`120px+`) to allow elements "room to breathe."
- **Reflow:** On mobile, margins shrink to 20px, and content stacks vertically. Text-heavy sections should maintain a maximum width of 720px even on large screens to preserve readability.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** rather than heavy shadows. The base layer is the darkest black, with interactive components or secondary cards sitting on a slightly lighter `#022B23` surface.

- **Borders:** Use low-contrast outlines (1px solid white at 10% opacity) to define shapes without breaking the dark-mode immersion.
- **Gradients:** Subtle radial gradients (from center-top) using the secondary color can be used to highlight specific sections of the page.
- **Shadows:** When necessary, use ultra-soft, large-radius shadows with 40% opacity of the `#011410` color to create a "floating" effect for modals.

## Shapes

The shape language is **Soft** but disciplined. Avoid overly round "bubbly" corners to maintain a professional engineering tone. 

- **Base Radius:** 0.25rem (4px) for small components like inputs and buttons.
- **Large Radius:** 0.75rem (12px) for cards and containers, providing a modern but structured frame for content.

## Components

- **Buttons:** Primary buttons use the `#E8C583` background with dark text. They should have a subtle scale-up transition on hover. Secondary buttons use a "Ghost" style with a 1px white-alpha border.
- **Inputs:** Dark backgrounds (`#022B23`) with a thin border that glows primary-gold on focus.
- **Cards:** Utilize a 1px border (`rgba(255,255,255,0.1)`) and a very subtle hover state that increases the background brightness slightly.
- **Chips/Badges:** Small, uppercase, with high letter-spacing. Use the accent-cream color at 10% opacity for the background and 100% opacity for the text.
- **Data Tables:** High-contrast headers with subtle row separators; the design should feel like a premium dashboard or code editor.