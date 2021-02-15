module.exports = {
  babel: {
    loaderOptions: (babelLoaderOptions) => {
      const origBabelPresetCRAIndex = babelLoaderOptions.presets.findIndex(preset => preset[0].includes('babel-preset-react-app'));
      const origBabelPresetCRA = babelLoaderOptions.presets[origBabelPresetCRAIndex];
      babelLoaderOptions.presets[origBabelPresetCRAIndex] = (api, opts, env) => {
        const babelPresetCRAResult = require(origBabelPresetCRA[0])(api, origBabelPresetCRA[1], env);
        babelPresetCRAResult.presets.forEach(preset => {
          const isReactPreset = preset?.[1]?.runtime === 'automatic' && preset?.[1]?.development === true;
          if (isReactPreset) {
            preset[1].importSource = '@welldone-software/why-did-you-render';
          }
        });
        return babelPresetCRAResult;
      };
      return babelLoaderOptions;
    },
  }
};
