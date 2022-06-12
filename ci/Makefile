RDOCKER=registry.i.sumus.work
oCONTAINER ?= testgaus
iCONTAINER ?= front
iDOCKERFILE = Dockerfile

container:
	docker build -f ${iDOCKERFILE} -t ${iCONTAINER} . 

release:
	docker tag ${iCONTAINER} ${RDOCKER}/${oCONTAINER}/${iCONTAINER}:latest && \
	docker push ${RDOCKER}/${oCONTAINER}/${iCONTAINER}:latest