Name:      rockit-lensheater
Version:   %{_version}
Release:   1
Summary:   Lens heater controller
Url:       https://github.com/rockit-astro/lensheaterd
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/lensheaterd/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/lensheater %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/lensheaterd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/lensheaterd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/lensheater %{buildroot}/etc/bash_completion.d

%{__install} %{_sourcedir}/superwasp.json %{buildroot}%{_sysconfdir}/lensheaterd/
%{__install} %{_sourcedir}/10-superwasp-lensheater.rules %{buildroot}%{_udevrulesdir}

%package server
Summary:  Lens heater server
Group:    Unspecified
Requires: python3-rockit-lensheater python3-pyserial
%description server

%package client
Summary:  Lens heater client
Group:    Unspecified
Requires: python3-rockit-lensheater
%description client

%files server
%defattr(0755,root,root,-)
%{_bindir}/lensheaterd
%defattr(0644,root,root,-)
%{_unitdir}/lensheaterd@.service

%files client
%defattr(0755,root,root,-)
%{_bindir}/lensheater
/etc/bash_completion.d/lensheater

%package data-superwasp
Summary: Lens heater data for SuperWASP
Group:   Unspecified
%description data-superwasp

%files data-superwasp
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-superwasp-lensheater.rules
%{_sysconfdir}/lensheaterd/superwasp.json

%changelog
