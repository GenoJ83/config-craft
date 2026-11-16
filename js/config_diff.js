function diffConfigs(oldObj, newObj) {
  const oldKeys = Object.keys(oldObj || {});
  const newKeys = Object.keys(newObj || {});
  const added = newKeys.filter((k) => !oldKeys.includes(k));
  const removed = oldKeys.filter((k) => !newKeys.includes(k));
  const common = oldKeys.filter((k) => newKeys.includes(k));
  return { added, removed, common };
}
module.exports = { diffConfigs };
