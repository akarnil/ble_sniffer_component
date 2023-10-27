#from https://docs.aws.amazon.com/greengrass/v2/developerguide/create-first-component.html


# To locally deploy this component in a dev environment, you need to first deloy the cli component
Go to https://awspoc.iotconnect.io/deployment/8
Give the deployment a name
firmware = cli
Target Type = Devices
Target = Your device name
Components: aws.greengrass.cli ticked, version 2.11.0

sudo /greengrass/v2/bin/greengrass-cli deployment create \
--recipeDir ./recipes \
--artifactDir ./artifacts \
--merge "com.afk.ble_sniffer=1.0.0"

sudo tail -f /greengrass/v2/logs/com.afk.ble_sniffer.log

sudo /greengrass/v2/bin/greengrass-cli component restart --names "com.afk.ble_sniffer"

# To remove
sudo /greengrass/v2/bin/greengrass-cli deployment create --remove="com.afk.ble_sniffer"



# Upload directions

1. Go to https://awspoc.iotconnect.io/greengrass-firmware/8

1. Click on `Components`

1. Upload each item inside artifacts/com.afk.ble_sniffer/1.0.0/ under the artifacts tab.

1. Open up the .json inside recipes/
Scroll to Artifacts and look at the URIs

1. Go back to the website, there should be an upload list to the right, preceeding each artifact there is a little icon that copies the URI link,
update the URI link for each artifact in the json.

1. ArtifactsOnce done, upload the recipe and click save.

# To create firmware for deployment

1. Go to https://awspoc.iotconnect.io/greengrass-firmware/8

1. Click on `Create Firmware`

1. Give it a name, select the correct template, and add the components you need (including the ble_sniffer you uploaded) and click save

# To deploy

1. Go to https://awspoc.iotconnect.io/deployment/8

1. Click on `Deployment`

1. Give it a name, select the firmware you created in the previous step, target type = devices and select the target to be the device you want.

1. Click Deploy

1. (You may need to restart the greengrass.service after the successful deployment for it to start working)

