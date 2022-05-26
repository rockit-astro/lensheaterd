Name:      superwasp-lensheater-data
Version:   20220528
Release:   0
Url:       https://github.com/warwick-one-metre/lensheaterd
Summary:   Lens heater configuration for the SuperWASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/lensheaterd/
%{__install} %{_sourcedir}/10-superwasp-lensheater.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/superwasp.json %{buildroot}%{_sysconfdir}/lensheaterd/

%files
%{_udevrulesdir}/10-superwasp-lensheater.rules
%{_sysconfdir}/lensheaterd/superwasp.json

%changelog
