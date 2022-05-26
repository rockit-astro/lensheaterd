Name:      superwasp-lensheater-server
Version:   20220528
Release:   0
Url:       https://github.com/warwick-one-metre/lensheaterd
Summary:   Lens heater daemon for the SuperWASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-pyserial, python3-warwick-observatory-common
Requires:  python3-warwick-observatory-lensheater, superwasp-lensheater-data

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/lensheaterd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/lensheaterd@.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/lensheaterd
%defattr(0644,root,root,-)
%{_unitdir}/lensheaterd@.service

%changelog
