RDOCKER=registry.i.sumus.work
oCONTAINER ?= testgaus
iCONTAINER ?= front
iDOCKERFILE = Dockerfile

container:
	docker build -f ${iDOCKERFILE} -t ${iCONTAINER} . 

release:
	docker tag ${iCONTAINER} ${oCONTAINER}/${iCONTAINER}:latest && \
	docker push ${oCONTAINER}/${iCONTAINER}:latest