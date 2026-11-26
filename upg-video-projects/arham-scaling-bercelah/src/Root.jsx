import {Composition} from 'remotion';
import {Main} from './Main';
import {totalSec} from './timeline.js';

export const Root = () => (
	<Composition id="Main" component={Main} durationInFrames={Math.round(totalSec() * 30)} fps={30} width={1080} height={1920} />
);
