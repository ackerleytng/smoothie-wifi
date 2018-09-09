/*
 * Functions to get wifi APs
 */

const getWifiAps = function () {
  const params = {
    method: 'GET',
    headers: {
      "Content-Type": "application/json",
    },
  }
  return fetch('/wifi', params)
    .then(r => r.json())
}

const fracToFloat = function (s) {
  const parts = s.split("/")
  return parseFloat(parts[0]) / parseFloat(parts[1])
}

const sortByQuality = function (networks) {
  return networks.sort((a, b) => fracToFloat(b.Quality) - fracToFloat(a.Quality))
}

const formatNetwork = function (network) {
  return `${network.ESSID} - strength: (${network.Quality})`
}

const createOption = function (network) {
  const option = document.createElement('option')
  
  option.value = network.ESSID
  option.text = formatNetwork(network)

  return option
}

const updateSelect = function (networks) {
  const select = document.getElementById('ssid')
  networks.map(n => select.add(createOption(n)))
}

const updateSelectWithAps = function () {
  getWifiAps()
    .then(sortByQuality)
    .then(updateSelect)
}

/*
 * Spinner functions
 */

const spinner = '<i class="fas fa-spinner fa-spin"></i> '

const addSpinner = function (e) {
  e.innerHTML = spinner + e.innerHTML
}

const removeSpinner = function (e) {
  e.innerHTML = e.innerHTML.replace(spinner, '')
}

/*
 * Functions to apply settings
 */

const getWifiConfig = function () {
  const ssidSelect = document.getElementById('ssid')
  const pskInput = document.getElementById('password-field')
  
  const ssid = ssidSelect.options[ssidSelect.selectedIndex].value
  const psk = pskInput.value

  return {
    ssid: ssid,
    psk: psk
  }
}

const applySettingsRaw = function (data) {
  console.log(data)
  const params = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  }
  return fetch('/wifi', params)
    // TODO implement feedback for POST .then(r => r.json())
}

const applySettings = function () {
  const button = document.getElementById('apply-settings')

  addSpinner(button)

  applySettingsRaw(getWifiConfig())
    .then(r => removeSpinner(button))  
}

/*
 * Functions to remove settings
 */

const removeSettingsRaw = function () {
  const params = {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  }
  return fetch('/wifi', params)
    .then(r => r.json())
}

const removeSettings = function () {
  const button = document.getElementById('remove-settings')

  addSpinner(button)

  removeSettingsRaw()
    .then(r => removeSpinner(button))  
}

/*
 * "main"
 */

updateSelectWithAps()
