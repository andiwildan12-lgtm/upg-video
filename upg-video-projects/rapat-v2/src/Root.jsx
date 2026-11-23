import {Composition} from 'remotion';
import {Main} from './Main';
import {TOTAL} from './timeline.js';
export const Root = () => <Composition id="Main" component={Main} durationInFrames={Math.round(TOTAL * 30)} fps={30} width={1080} height={1920} />;
