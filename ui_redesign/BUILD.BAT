pyinstaller main.py ^
	-F ^
	--log-level=DEBUG ^
	--noconsole ^
	--name "hsapp" ^
	--add-data="./assets/imgs;./assets/imgs" ^
	--add-data="./assets/icons;./assets/icons" ^
	--noconfirm ^
	--icon="./assets/icons/HSAPP.ico" ^