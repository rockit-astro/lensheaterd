RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

GIT_VERSION = $(shell git name-rev --name-only --tags --no-undefined HEAD 2>/dev/null || echo git-`git rev-parse --short HEAD`)
SERVER_VERSION = $(shell awk '/Version:/ { print $$2; }' superwasp-lensheater-server.spec)

all:
	mkdir -p build
	cp lensheaterd lensheaterd.bak
	awk '{sub("SOFTWARE_VERSION = .*$$","SOFTWARE_VERSION = \"$(SERVER_VERSION) ($(GIT_VERSION))\""); print $0}' lensheaterd.bak > lensheaterd
	${RPMBUILD} -ba superwasp-lensheater-server.spec
	${RPMBUILD} -ba superwasp-lensheater-client.spec
	${RPMBUILD} -ba superwasp-lensheater-data.spec
	${RPMBUILD} -ba python3-warwick-observatory-lensheater.spec

	mv build/noarch/*.rpm .
	rm -rf build
	mv lensheaterd.bak lensheaterd
