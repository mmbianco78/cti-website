# CLAUDE.md - Project Guidelines and Rules

## CRITICAL RULES - ALWAYS FOLLOW

### 1. ALWAYS CHECK YOUR OWN WORK
**NEVER claim something is fixed without verifying it yourself.**
- After making any change, use appropriate tools (curl, grep, browser screenshots) to verify the change worked
- Check the actual rendered output, not just the source code
- If dealing with visual elements (CSS, images, layouts), always check in a browser
- DO NOT tell the user something is "fixed" or "should work now" without confirmation

### 2. Lint and Type Check Commands
When completing any coding task:
- Run: `npm run lint` (if available)
- Run: `npm run typecheck` (if available)
- If these commands are not found, ask the user for the correct commands
- Write them to this CLAUDE.md file for future reference

## Project-Specific Information

### CTI Website (Clay Target Instruction)
- Framework: Astro
- CSS: Tailwind CSS + custom styles
- Images directory: `/public/assets/images/`
- Development server: `npm run dev`

### Known Issues and Solutions
1. **CSS Variables Issue**: Some CSS custom properties may not be defined, causing invisible text. Always use explicit hex colors when in doubt.
2. **Image Paths**: Always verify image paths exist before using them. Check both `/assets/images/` and `/public/assets/images/`
3. **Parallax Backgrounds**: Use `background-attachment: fixed` for desktop, `scroll` for mobile

## Development Best Practices
1. Always run development server in background: `npm run dev > /dev/null 2>&1 &`
2. Check for existing patterns before implementing new features
3. Maintain consistent code style with existing codebase
4. Never add emojis unless explicitly requested