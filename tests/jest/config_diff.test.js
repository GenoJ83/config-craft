const { diffConfigs } = require('../../js/config_diff');

describe('Config Diff', () => {
  it('detects added and removed properties', () => {
    const o = { port: 80, host: '0.0.0.0' };
    const n = { host: '0.0.0.0', ssl: true };
    const diff = diffConfigs(o, n);
    expect(diff.added).toEqual(['ssl']);
    expect(diff.removed).toEqual(['port']);
    expect(diff.common).toEqual(['host']);
  });
});
