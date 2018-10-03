## Generated by graphCompress tool automatically ##
## Compress configuration and fine tuning goal ##
compressConfig = {
  'res2a_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [36, 36]},
  'res2b_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [36, 36]},
  'res2c_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [36, 36]},
  'res3a_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [72, 72]},
  'res3b_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [72, 72]},
  'res3c_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [72, 72]},
  'res3d_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [72, 72]},
  'res4a_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [100, 100]},
  'res4b_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [100, 100]},
  'res4c_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [100, 100]},
  'res4d_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [100, 100]},
  'res4e_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [100, 100]},
  'res4f_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [108, 108]},
  'res5a_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [120, 120]},
  'res5b_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [140, 140]},
  'res5c_branch2b'  : {'algorithm': 'Tucker-2', 'rank': [160, 160]},
  'fc1000'  : {'algorithm': 'SVD', 'rank': [200]},
}
tuningGoal = [{'accuracy@5': 0.9118799941062927, 'accuracy@1': 0.7292400004982948}]

## Compress factor and layer factors of this config##
desiredCompressFactor = None
realCompressFactor = 1.49464527723
layerCompressFactor = {
  'res2a_branch2b'  : 2.26548672566,
  'res2b_branch2b'  : 2.26548672566,
  'res2c_branch2b'  : 2.26548672566,
  'res3a_branch2b'  : 2.26548672566,
  'res3b_branch2b'  : 2.26548672566,
  'res3c_branch2b'  : 2.26548672566,
  'res3d_branch2b'  : 2.26548672566,
  'res4a_branch2b'  : 4.17722379603,
  'res4b_branch2b'  : 4.17722379603,
  'res4c_branch2b'  : 4.17722379603,
  'res4d_branch2b'  : 4.17722379603,
  'res4e_branch2b'  : 4.17722379603,
  'res4f_branch2b'  : 3.68014375562,
  'res5a_branch2b'  : 9.34448669202,
  'res5b_branch2b'  : 7.37833375031,
  'res5c_branch2b'  : 5.98441558442,
  'fc1000'  : 3.35958005249,
}