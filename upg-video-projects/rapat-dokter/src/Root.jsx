import {Composition} from 'remotion';
import {Main} from './Main';
import {META} from './meta.js';
import {totalSec} from './timeline.js';

// META ditulis otomatis oleh scripts/prep_footage.py (resolusi & fps footage).
export const Root = () => (
	<Composition
		id="Main"
		component={Main}
		durationInFrames={Math.round(totalSec() * META.fps)}
		fps={META.fps}
		width={META.width}
		height={META.height}
	/>
);
