import { fade, slide, scale } from 'svelte/transition';
import type { TransitionConfig } from 'svelte/transition';

// Types for our animation configurations
interface AnimationParams {
  duration?: number;
  delay?: number;
}

// Header animations
export const headerTitle = (node: Element): TransitionConfig => 
  slide(node, { duration: 1000, delay: 300 });

export const headerUnderline = (node: Element): TransitionConfig => 
  slide(node, { duration: 800, delay: 800, axis: 'x' });

export const headerFadeOut = (node: Element): TransitionConfig => 
  fade(node, { duration: 200 });

// Nav menu animations
export const navMenuFade = (node: Element): TransitionConfig => 
  fade(node, { duration: 300 });

// Filler text animations
export const paragraphFade = (node: Element, { delay = 0 }: AnimationParams = {}): TransitionConfig => 
  fade(node, { duration: 400, delay });

export const lineFade = (node: Element, { delay = 0 }: AnimationParams = {}): TransitionConfig => 
  slide(node, { duration: 400, delay, axis: 'x' });

// Helper function for calculating staggered delays
export const getStaggeredDelay = (index: number, baseDelay: number = 50): number => 
  index * baseDelay; 