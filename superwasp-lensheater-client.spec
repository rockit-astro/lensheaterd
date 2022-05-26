Name:      superwasp-lensheater-client
Version:   20220528
Release:   0
Url:       https://github.com/warwick-one-metre/lensheaterd
Summary:   Lens heater client for the SuperWASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-common, superwasp-lensheater-data

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/lensheater %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/lensheater %{buildroot}/etc/bash_completion.d/lensheater

%files
%defattr(0755,root,root,-)
%{_bindir}/lensheater
/etc/bash_completion.d/lensheater

%changelog
