sudo /greengrass/v2/bin/greengrass-cli deployment create \
--recipeDir ./recipes \
--artifactDir ./artifacts \
--merge "com.example.blscanner=1.0.0" \
&& sudo /greengrass/v2/bin/greengrass-cli component restart --names "com.example.blscanner"